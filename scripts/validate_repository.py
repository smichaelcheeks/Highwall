#!/usr/bin/env python3
"""Validate structural invariants for the Highwall knowledge repository."""

from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from urllib.parse import unquote

from consistency_common import (
    CLAIM_COLUMN_COUNT,
    parse_front_matter_data,
    scalar_text,
    split_markdown_row,
)
from graph_common import GraphValidationError, build_graph_data, collect_object_snapshots


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_REQUIRED = {
    "title",
    "type",
    "status",
    "canon_level",
    "aliases",
    "tags",
    "entity_id",
    "related",
    "relationships",
    "provenance",
}
CANON_STATUSES = {"draft", "review", "active", "deprecated"}
CANON_LEVELS = {"established", "working", "unresolved"}
REVIEW_STATUSES = {
    "in-progress",
    "awaiting-confirmation",
    "awaiting-decision",
    "complete",
    "blocked",
}
DISPOSITIONS = {
    "create",
    "update",
    "no-change",
    "link-only",
    "defer",
    "conflict",
    "retire",
    "out-of-scope",
}
TRANSMISSION_STATUSES = {"complete"}
COMPLETION_BASES = {"end-marker", "explicit-confirmation", "complete-attachment"}
END_OF_PATCH_MARKER = "<!-- END OF PATCH -->"
LEGACY_END_OF_STITCH_MARKER = "<!-- END OF STITCH -->"
LEGACY_END_OF_SEED_MARKER = "<!-- END OF SEED -->"
END_MARKERS = (
    END_OF_PATCH_MARKER,
    LEGACY_END_OF_STITCH_MARKER,
    LEGACY_END_OF_SEED_MARKER,
)
IMPACT_FIELDS = {"subjects", "domains", "search_terms", "authoritative_targets"}
LORE_REVIEW_VALUES = {"true", "false"}
LORE_AUTHORITIES = {"establish-canon", "working-canon"}
AUDIT_SCALAR_FIELDS = {
    "semantic_audit_baseline",
    "audit_git_range",
    "incremental_context_generated",
    "consistency_tier_required",
    "consistency_tier_performed",
    "tier_three_trigger_active",
    "completed_canon_cases_since_tier_three",
}
AUDIT_LIST_FIELDS = {
    "prior_audited_relationships",
    "audit_results_carried_forward",
    "audit_results_revalidated",
    "audit_results_invalidated",
    "audit_results_widened",
    "tier_three_triggers",
}
INCREMENTAL_CONTEXT_STATES = {"yes", "no", "pending"}
CONSISTENCY_TIERS = {"tier-2", "tier-3"}
PERFORMED_CONSISTENCY_TIERS = CONSISTENCY_TIERS | {"pending"}
TRIGGER_STATES = {"yes", "no", "pending"}
TIER_3_TRIGGERS = {
    "ten-completed-canon-cases",
    "tagged-canon-snapshot",
    "sustained-story-drafting",
    "major-regional-change",
    "major-chronological-change",
    "major-political-change",
    "major-taxonomy-change",
    "major-ownership-change",
    "major-path-change",
    "major-alias-change",
    "three-or-more-semantic-domains",
    "repeated-unexpected-dependencies",
    "missing-baseline",
    "incomplete-baseline",
    "unreliable-baseline",
}
FULL_COMMIT = re.compile(r"^[0-9a-f]{40}$")
GIT_RANGE = re.compile(r"^([0-9a-f]{40})\.\.([0-9a-f]{40})$")
CONSISTENCY_DOMAINS = {
    "administration",
    "characters",
    "culture",
    "design",
    "economy",
    "government",
    "history",
    "institutions",
    "law",
    "organizations",
    "places",
    "religion",
    "story",
    "technology",
    "terminology",
}
SUBJECT_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DEVELOPMENT_DISPOSITIONS = {"defer", "conflict", "retire"}
DEVELOPMENT_DISPOSITION_ROOTS = {
    "defer": {"open-questions", "proposals"},
    "conflict": {"contradictions"},
    "retire": {"retired"},
}
CASE_ID = re.compile(r"^CASE-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+$")
SUBMISSION_ID = re.compile(r"^(CASE-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+)-(S|A)\d{2}$")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


class Validator:
    def __init__(self, base_ref: str | None, root: Path = ROOT) -> None:
        self.base_ref = base_ref
        self.root = root.resolve()
        self.errors: list[str] = []
        self.markdown_files = sorted(self.root.rglob("*.md"))
        self.anchor_cache: dict[Path, set[str]] = {}

    def error(self, path: Path | str, message: str) -> None:
        display = path.relative_to(self.root) if isinstance(path, Path) else path
        self.errors.append(f"{display}: {message}")

    @staticmethod
    def parse_front_matter(path: Path) -> dict[str, str] | None:
        try:
            data = parse_front_matter_data(path)
        except ValueError:
            return None
        if not data:
            return None
        return {
            key: "" if isinstance(value, (dict, list)) else scalar_text(value)
            for key, value in data.items()
        }

    @staticmethod
    def parse_front_matter_lists(path: Path) -> dict[str, list[str]]:
        try:
            data = parse_front_matter_data(path)
        except ValueError:
            return {}
        return {
            key: [scalar_text(item) for item in value]
            for key, value in data.items()
            if isinstance(value, list)
        } | {key: [] for key, value in data.items() if value is None or value == ""}

    @staticmethod
    def slugify(heading: str) -> str:
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"[`*_~]", "", heading).strip().lower()
        heading = re.sub(r"[^\w\- ]", "", heading)
        return re.sub(r"[\s-]+", "-", heading).strip("-")

    def anchors_for(self, path: Path) -> set[str]:
        if path in self.anchor_cache:
            return self.anchor_cache[path]
        anchors: set[str] = set()
        counts: dict[str, int] = {}
        fenced = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if fenced or line.startswith(">"):
                continue
            match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
            if not match:
                continue
            base = self.slugify(match.group(1))
            count = counts.get(base, 0)
            counts[base] = count + 1
            anchors.add(base if count == 0 else f"{base}-{count}")
        self.anchor_cache[path] = anchors
        return anchors

    def validate_links(self) -> None:
        for path in self.markdown_files:
            text = path.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK.findall(text):
                target = raw_target.strip().strip("<>")
                if "TODO" in target or re.match(r"^(https?://|mailto:)", target):
                    continue
                file_part, separator, anchor = target.partition("#")
                file_part = file_part.replace("\\", "/")
                target_path = path if not file_part else (path.parent / unquote(file_part)).resolve()
                try:
                    target_path.relative_to(self.root)
                except ValueError:
                    self.error(path, f"link escapes repository: {raw_target}")
                    continue
                if not target_path.exists():
                    self.error(path, f"missing link target: {raw_target}")
                    continue
                if separator and anchor and target_path.is_file() and target_path.suffix.lower() == ".md":
                    if unquote(anchor).lower() not in self.anchors_for(target_path):
                        self.error(path, f"missing heading anchor: {raw_target}")

    def validate_canon_front_matter(self) -> None:
        list_fields = {"aliases", "tags", "related", "relationships", "provenance"}
        for path in sorted((self.root / "canon").rglob("*.md")):
            if path.name == "README.md":
                continue
            metadata = self.parse_front_matter(path)
            if metadata is None:
                self.error(path, "canon page lacks valid YAML front matter delimiters")
                continue
            missing = FRONT_MATTER_REQUIRED - metadata.keys()
            if missing:
                self.error(path, f"missing front matter fields: {', '.join(sorted(missing))}")
            if metadata.get("status") not in CANON_STATUSES:
                self.error(path, f"invalid canon status: {metadata.get('status')!r}")
            if metadata.get("canon_level") not in CANON_LEVELS:
                self.error(path, f"invalid canon level: {metadata.get('canon_level')!r}")
            parsed_lists = self.parse_front_matter_lists(path)
            for field in sorted(list_fields & metadata.keys()):
                if field not in parsed_lists:
                    self.error(path, f"front matter field must be a list: {field}")

    def validate_graph(self) -> None:
        try:
            graph = build_graph_data(self.root)
        except GraphValidationError as error:
            self.errors.extend(error.errors)
            return
        if self.base_ref:
            self.validate_graph_evolution(graph)

    def changed_paths(self) -> set[str]:
        if not self.base_ref:
            return set()
        result = subprocess.run(
            ["git", "diff", "--name-only", self.base_ref, "--"],
            cwd=self.root,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = result.stderr.strip() or "Git could not compare the requested ref"
            self.error("graph", f"invalid comparison ref {self.base_ref!r}: {detail}")
            return set()
        return {line.replace("\\", "/") for line in result.stdout.splitlines() if line}

    def validate_graph_evolution(self, graph: dict[str, object]) -> None:
        """Enforce durable identity and append-only graph evolution against Git."""
        if not self.base_ref:
            return
        archive = subprocess.run(
            ["git", "archive", "--format=tar", self.base_ref],
            cwd=self.root,
            check=False,
            capture_output=True,
        )
        if archive.returncode != 0:
            detail = archive.stderr.decode("utf-8", errors="replace").strip()
            self.error(
                "graph",
                f"could not read graph baseline {self.base_ref!r}: {detail or 'git archive failed'}",
            )
            return
        with tempfile.TemporaryDirectory(prefix="highwall-graph-base-") as directory:
            baseline_root = Path(directory)
            try:
                with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tar:
                    tar.extractall(baseline_root, filter="data")
            except (tarfile.TarError, OSError) as error:
                self.error("graph", f"could not extract graph baseline: {error}")
                return
            baseline = collect_object_snapshots(baseline_root)

        current = collect_object_snapshots(self.root)
        current_histories_by_object: dict[str, list[dict[str, object]]] = {}
        for item in current["histories"].values():
            current_histories_by_object.setdefault(str(item["object_id"]), []).append(item)

        for kind in ("entities", "relationships", "claims"):
            for object_id in sorted(baseline[kind]):
                if object_id not in current[kind]:
                    self.error(
                        baseline[kind][object_id]["path"]
                        if kind == "entities"
                        else baseline[kind][object_id]["authoritative_record"],
                        f"published {kind[:-1]} {object_id} was removed instead of retained as a tombstone",
                    )

        for relationship_id, earlier in baseline["relationships"].items():
            later = current["relationships"].get(relationship_id)
            if later is None:
                continue
            for field in ("relationship_type", "source", "target"):
                if earlier[field] != later[field]:
                    self.error(
                        str(later["authoritative_record"]),
                        f"published relationship {relationship_id} changed immutable {field}",
                    )

        for entity_id, earlier in baseline["entities"].items():
            later = current["entities"].get(entity_id)
            if later is not None and earlier["record_type"] != later["record_type"]:
                self.error(
                    str(later["path"]),
                    f"published entity {entity_id} changed immutable record_type",
                )

        for claim_id, earlier in baseline["claims"].items():
            later = current["claims"].get(claim_id)
            if later is None:
                continue
            for field in ("truth_kind", "about"):
                if earlier[field] != later[field]:
                    self.error(
                        str(later["authoritative_record"]),
                        f"published claim {claim_id} changed immutable {field}",
                    )

        for history_id, earlier in baseline["histories"].items():
            later = current["histories"].get(history_id)
            if later is None:
                self.error(
                    str(earlier["authoritative_record"]),
                    f"published history event {history_id} was removed",
                )
            elif {
                key: value for key, value in earlier.items() if key != "authoritative_record"
            } != {
                key: value for key, value in later.items() if key != "authoritative_record"
            }:
                self.error(
                    str(later["authoritative_record"]),
                    f"published history event {history_id} was rewritten",
                )

        inventory = graph["migration_inventory"]
        missing_status = set(inventory["entities_without_graph_status"]) | set(
            inventory["relationships_without_graph_status"]
        )
        missing_history_coverage = set(
            inventory["entities_without_history_coverage"]
        ) | set(inventory["relationships_without_history_coverage"])
        baseline_history_ids = set(baseline["histories"])

        def appended_histories(object_id: str) -> list[dict[str, object]]:
            return [
                event
                for event in current_histories_by_object.get(object_id, [])
                if str(event["history_id"]) not in baseline_history_ids
            ]

        def require_change_event(
            *,
            kind: str,
            object_id: str,
            item: dict[str, object],
            earlier: dict[str, object] | None,
            path_field: str,
        ) -> bool:
            path = str(item[path_field])
            state_changed = earlier is None or item["state_sha256"] != earlier["state_sha256"]
            moved = earlier is not None and path != str(earlier[path_field])
            if not state_changed and not moved:
                return False
            events = appended_histories(object_id)
            if not events:
                self.error(
                    path,
                    f"new or changed {kind} {object_id} did not append local history",
                )
                return True
            required_event_types: list[tuple[str, set[str]]] = []
            if earlier is None:
                initial_types = {
                    "entity": {"graph-registered", "established"},
                    "relationship": {"graph-registered", "relationship-added"},
                    "claim": {"graph-registered", "claim-added", "established"},
                }[kind]
                required_event_types.append(("initial publication", initial_types))
            event_types = {str(event["change_type"]) for event in events}
            if moved:
                required_event_types.append(("owner-path move", {"moved"}))
            lifecycle_field = "lifecycle" if kind == "claim" else "graph_status"
            lifecycle = str(item.get(lifecycle_field, ""))
            prior_lifecycle = str(earlier.get(lifecycle_field, "")) if earlier else ""
            if earlier is not None and not prior_lifecycle and lifecycle:
                required_event_types.append(("schema-v2 registration", {"graph-registered"}))
            elif lifecycle != prior_lifecycle and lifecycle in {"superseded", "retired"}:
                required_event_types.append((f"{lifecycle} lifecycle transition", {lifecycle}))
            if (
                kind == "claim"
                and earlier is not None
                and item.get("content_sha256") != earlier.get("content_sha256")
            ):
                required_event_types.append(("bounded claim-content change", {"claim-clarified"}))
            if state_changed and not required_event_types:
                required_event_types.append(("object-state change", {"metadata-changed"}))
            for reason, expected in required_event_types:
                if event_types.isdisjoint(expected):
                    self.error(
                        path,
                        f"new history for changed {kind} {object_id} has no compatible "
                        f"change_type for {reason}; expected one of {sorted(expected)}",
                    )
            return True

        for entity_id, item in current["entities"].items():
            earlier = baseline["entities"].get(entity_id)
            requires_v2 = require_change_event(
                kind="entity",
                object_id=entity_id,
                item=item,
                earlier=earlier,
                path_field="path",
            )
            if not requires_v2:
                continue
            try:
                entity_metadata = parse_front_matter_data(self.root / str(item["path"]))
            except ValueError:
                entity_metadata = {}
            if entity_id in missing_status:
                self.error(str(item["path"]), f"changed entity {entity_id} lacks graph_status")
            if entity_id in missing_history_coverage:
                self.error(
                    str(item["path"]),
                    f"changed entity {entity_id} lacks history_coverage",
                )
            for field in ("claims", "history", "supersedes", "superseded_by"):
                if field not in entity_metadata:
                    self.error(
                        str(item["path"]),
                        f"changed entity {entity_id} lacks schema-v2 {field} field",
                    )

        for kind, lifecycle_field in (("relationship", "graph_status"), ("claim", "lifecycle")):
            collection = f"{kind}s"
            for object_id, item in current[collection].items():
                earlier = baseline[collection].get(object_id)
                requires_v2 = require_change_event(
                    kind=kind,
                    object_id=object_id,
                    item=item,
                    earlier=earlier,
                    path_field="authoritative_record",
                )
                if requires_v2 and not item.get(lifecycle_field):
                    self.error(
                        str(item["authoritative_record"]),
                        f"new or changed {kind} {object_id} lacks {lifecycle_field}",
                    )

    def validate_intake(self) -> None:
        submissions: dict[str, Path] = {}
        submission_dir = self.root / "intake" / "submissions"
        for path in sorted(submission_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            metadata = self.parse_front_matter(path)
            if metadata is None:
                self.error(path, "submission lacks valid front matter")
                continue
            case_id = metadata.get("case_id", "")
            submission_id = metadata.get("submission_id", "")
            if not CASE_ID.fullmatch(case_id):
                self.error(path, f"invalid case_id: {case_id!r}")
            match = SUBMISSION_ID.fullmatch(submission_id)
            if not match or match.group(1) != case_id:
                self.error(path, f"submission_id does not belong to case: {submission_id!r}")
            if submission_id in submissions:
                self.error(path, f"duplicate submission_id also used by {submissions[submission_id].relative_to(self.root)}")
            submissions[submission_id] = path
            if self.is_new_submission(path):
                self.validate_transmission_completeness(path, metadata)

        reviewed: dict[str, Path] = {}
        review_dir = self.root / "development" / "intake-reviews"
        claim_owners: dict[str, Path] = {}
        for path in sorted(review_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            metadata = self.parse_front_matter(path)
            if metadata is None:
                self.error(path, "review lacks valid front matter")
                continue
            submission_id = metadata.get("submission_id", "")
            if submission_id not in submissions:
                self.error(path, f"review references unknown submission_id: {submission_id!r}")
            if submission_id in reviewed:
                self.error(path, f"duplicate review for {submission_id}")
            reviewed[submission_id] = path
            if metadata.get("case_id") != submission_id.rsplit("-", 1)[0]:
                self.error(path, "review case_id does not match submission_id")
            if metadata.get("status") not in REVIEW_STATUSES:
                self.error(path, f"invalid review status: {metadata.get('status')!r}")
            if self.is_new_path(path):
                self.validate_impact_manifest(path)
                self.validate_lore_review(path, metadata)
            for claim_id in self.validate_review_claims(path, submission_id):
                if claim_id in claim_owners:
                    self.error(
                        path,
                        "duplicate claim ID also used by "
                        f"{claim_owners[claim_id].relative_to(self.root)}: {claim_id}",
                    )
                else:
                    claim_owners[claim_id] = path

        for submission_id, path in submissions.items():
            if submission_id not in reviewed:
                self.error(path, f"no intake review found for {submission_id}")

    def is_new_path(self, path: Path) -> bool:
        if not self.base_ref:
            metadata = self.parse_front_matter(path) or {}
            return bool(
                {"transmission_status", "completion_basis"} & metadata.keys()
                or IMPACT_FIELDS & self.parse_front_matter_lists(path).keys()
            )
        relative_path = path.relative_to(self.root).as_posix()
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{self.base_ref}:{relative_path}"],
            cwd=self.root,
            check=False,
            capture_output=True,
            text=True,
        )
        return result.returncode != 0

    def is_new_submission(self, path: Path) -> bool:
        return self.is_new_path(path)

    def validate_impact_manifest(self, path: Path) -> None:
        lists = self.parse_front_matter_lists(path)
        missing = IMPACT_FIELDS - lists.keys()
        if missing:
            self.error(path, f"missing impact manifest fields: {', '.join(sorted(missing))}")
            return
        for field in IMPACT_FIELDS:
            if not lists[field]:
                self.error(path, f"impact manifest field must not be empty: {field}")
        for subject in lists["subjects"]:
            if not SUBJECT_ID.fullmatch(subject):
                self.error(path, f"invalid subject ID: {subject!r}")
        for domain in lists["domains"]:
            if domain not in CONSISTENCY_DOMAINS:
                self.error(path, f"invalid consistency domain: {domain!r}")
        for target in lists["authoritative_targets"]:
            target_path = (self.root / target.replace("\\", "/")).resolve()
            try:
                target_path.relative_to(self.root)
            except ValueError:
                self.error(path, f"authoritative target escapes repository: {target}")
                continue
            if not target_path.exists():
                self.error(path, f"missing authoritative target: {target}")

    def validate_lore_review(self, path: Path, metadata: dict[str, str]) -> None:
        lore_review = metadata.get("lore_review")
        if lore_review not in LORE_REVIEW_VALUES:
            self.error(path, f"invalid or missing lore_review: {lore_review!r}")
            return
        if metadata.get("authority") in LORE_AUTHORITIES and lore_review != "true":
            self.error(
                path,
                f"authority {metadata.get('authority')!r} requires lore_review: true",
            )
        if lore_review != "true":
            return

        missing_scalars = {
            field for field in AUDIT_SCALAR_FIELDS if not metadata.get(field)
        }
        if missing_scalars:
            self.error(
                path,
                "missing audit baseline fields: " + ", ".join(sorted(missing_scalars)),
            )

        lists = self.parse_front_matter_lists(path)
        missing_lists = AUDIT_LIST_FIELDS - lists.keys()
        if missing_lists:
            self.error(
                path,
                "missing audit baseline list fields: " + ", ".join(sorted(missing_lists)),
            )

        baseline = metadata.get("semantic_audit_baseline", "")
        git_range = metadata.get("audit_git_range", "")
        if baseline != "none" and not FULL_COMMIT.fullmatch(baseline):
            self.error(
                path,
                "semantic_audit_baseline must be a full commit hash or 'none'",
            )
        if baseline == "none":
            if git_range and git_range != "fresh-tier-3-required":
                self.error(
                    path,
                    "a missing semantic baseline requires audit_git_range: fresh-tier-3-required",
                )
        elif baseline:
            match = GIT_RANGE.fullmatch(git_range)
            if not match:
                self.error(path, "audit_git_range must contain two full commit hashes")
            elif match.group(1) != baseline:
                self.error(path, "audit_git_range must start at semantic_audit_baseline")

        context_state = metadata.get("incremental_context_generated")
        if context_state not in INCREMENTAL_CONTEXT_STATES:
            self.error(path, f"invalid incremental_context_generated: {context_state!r}")
        tier_required = metadata.get("consistency_tier_required")
        if tier_required not in CONSISTENCY_TIERS:
            self.error(path, f"invalid consistency_tier_required: {tier_required!r}")
        tier_performed = metadata.get("consistency_tier_performed")
        if tier_performed not in PERFORMED_CONSISTENCY_TIERS:
            self.error(path, f"invalid consistency_tier_performed: {tier_performed!r}")
        trigger_active = metadata.get("tier_three_trigger_active")
        if trigger_active not in TRIGGER_STATES:
            self.error(path, f"invalid tier_three_trigger_active: {trigger_active!r}")

        count_text = metadata.get("completed_canon_cases_since_tier_three", "")
        count: int | None = None
        if count_text.isdigit():
            count = int(count_text)
        elif count_text not in {"unknown", "pending"}:
            self.error(
                path,
                "completed_canon_cases_since_tier_three must be a nonnegative integer, "
                "'unknown', or 'pending'",
            )

        triggers = lists.get("tier_three_triggers", [])
        invalid_triggers = sorted(set(triggers) - TIER_3_TRIGGERS)
        if invalid_triggers:
            self.error(path, f"invalid Tier 3 triggers: {', '.join(invalid_triggers)}")
        if trigger_active == "yes" and not triggers:
            self.error(
                path,
                "tier_three_trigger_active is yes but tier_three_triggers is empty",
            )
        if trigger_active == "no" and triggers:
            self.error(
                path,
                "tier_three_trigger_active is no but tier_three_triggers is not empty",
            )

        required_triggers: set[str] = set()
        if baseline == "none":
            required_triggers.add("missing-baseline")
        if count is not None and count >= 10:
            required_triggers.add("ten-completed-canon-cases")
        if count_text == "unknown":
            required_triggers.add("unreliable-baseline")
        if len(lists.get("domains", [])) >= 3:
            required_triggers.add("three-or-more-semantic-domains")
        missing_triggers = sorted(required_triggers - set(triggers))
        if missing_triggers:
            self.error(
                path,
                "deterministic Tier 3 triggers are missing: "
                + ", ".join(missing_triggers),
            )
        if required_triggers and trigger_active != "yes":
            self.error(
                path,
                "deterministic Tier 3 trigger requires tier_three_trigger_active: yes",
            )
        if trigger_active == "yes" and tier_required != "tier-3":
            self.error(path, "active Tier 3 trigger requires consistency_tier_required: tier-3")

        prior_relationships = lists.get("prior_audited_relationships", [])
        audit_results = [
            result
            for field in AUDIT_LIST_FIELDS
            if field.startswith("audit_results_")
            for result in lists.get(field, [])
        ]
        missing_results = sorted(set(prior_relationships) - set(audit_results))
        unknown_results = sorted(set(audit_results) - set(prior_relationships))
        duplicate_results = sorted(
            result for result in set(audit_results) if audit_results.count(result) > 1
        )
        if missing_results:
            self.error(
                path,
                "prior audited relationships lack recorded results: "
                + ", ".join(missing_results),
            )
        if unknown_results:
            self.error(
                path,
                "audit results name unconsidered relationships: "
                + ", ".join(unknown_results),
            )
        if duplicate_results:
            self.error(
                path,
                "audit relationships have multiple results: "
                + ", ".join(duplicate_results),
            )

        if metadata.get("status") == "complete":
            pending = [
                field
                for field in (
                    "incremental_context_generated",
                    "consistency_tier_performed",
                    "tier_three_trigger_active",
                    "completed_canon_cases_since_tier_three",
                )
                if metadata.get(field) == "pending"
            ]
            if pending:
                self.error(
                    path,
                    "complete lore review has pending audit fields: "
                    + ", ".join(pending),
                )
            if tier_required == "tier-3" and tier_performed != "tier-3":
                self.error(
                    path,
                    "complete lore review requiring Tier 3 must record "
                    "consistency_tier_performed: tier-3",
                )
            if tier_required == "tier-2" and tier_performed not in CONSISTENCY_TIERS:
                self.error(path, "complete lore review must record the tier performed")

    def validate_transmission_completeness(self, path: Path, metadata: dict[str, str]) -> None:
        status = metadata.get("transmission_status")
        basis = metadata.get("completion_basis")
        if status not in TRANSMISSION_STATUSES:
            self.error(path, f"invalid or missing transmission_status: {status!r}")
        if basis not in COMPLETION_BASES:
            self.error(path, f"invalid or missing completion_basis: {basis!r}")
        if basis == "end-marker":
            body = path.read_text(encoding="utf-8")
            if not any(marker in body for marker in END_MARKERS):
                recognized = " or ".join(END_MARKERS)
                self.error(
                    path,
                    f"completion_basis 'end-marker' requires {recognized}",
                )

    def validate_review_claims(self, path: Path, submission_id: str) -> set[str]:
        seen: set[str] = set()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not re.match(r"^\|\s*CASE-.*-C\d{3}\s*\|", line):
                continue
            cells = split_markdown_row(line)
            if len(cells) != CLAIM_COLUMN_COUNT:
                self.error(
                    path,
                    f"line {line_number}: expected {CLAIM_COLUMN_COUNT} claim columns, found {len(cells)}",
                )
                continue
            claim_id = cells[0]
            if not claim_id.startswith(f"{submission_id}-C"):
                self.error(path, f"line {line_number}: claim ID does not belong to review submission")
            if claim_id in seen:
                self.error(path, f"line {line_number}: duplicate claim ID {claim_id}")
            seen.add(claim_id)
            dispositions = [value for value in DISPOSITIONS if f"`{value}`" in line]
            if len(dispositions) != 1:
                self.error(path, f"line {line_number}: expected one controlled disposition")
                continue
            if dispositions[0] in DEVELOPMENT_DISPOSITIONS:
                targets = MARKDOWN_LINK.findall(line)
                valid_target = False
                for target in targets:
                    target_path = (path.parent / target.partition("#")[0]).resolve()
                    development_root = self.root / "development"
                    if not target_path.exists() or development_root not in target_path.parents:
                        continue
                    relative_parts = target_path.relative_to(development_root).parts
                    if (
                        relative_parts
                        and relative_parts[0]
                        in DEVELOPMENT_DISPOSITION_ROOTS[dispositions[0]]
                    ):
                        valid_target = True
                if not valid_target:
                    allowed = ", ".join(
                        sorted(DEVELOPMENT_DISPOSITION_ROOTS[dispositions[0]])
                    )
                    self.error(
                        path,
                        f"line {line_number}: {dispositions[0]} must link to a "
                        f"development record under {allowed}",
                    )
        if not seen:
            self.error(path, "review contains no claim decision rows")
        return seen

    def validate_submission_immutability(self) -> None:
        if not self.base_ref:
            return
        result = subprocess.run(
            [
                "git",
                "diff",
                "--name-status",
                "--diff-filter=MDR",
                self.base_ref,
                "--",
                "intake/submissions",
            ],
            cwd=self.root,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = result.stderr.strip() or "Git could not compare the requested ref"
            self.error("intake/submissions", f"invalid comparison ref {self.base_ref!r}: {detail}")
            return
        for line in result.stdout.splitlines():
            paths = line.split("\t")[1:]
            protected = [item for item in paths if Path(item).name != "README.md"]
            if protected:
                self.error("intake/submissions", f"merged submissions are immutable: {line}")

    def run(self) -> int:
        self.validate_links()
        self.validate_canon_front_matter()
        self.validate_graph()
        self.validate_intake()
        self.validate_submission_immutability()
        if self.errors:
            print("Repository validation failed:", file=sys.stderr)
            for error in self.errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print(
            f"Repository validation passed: {len(self.markdown_files)} Markdown files; "
            "links, canon metadata, graph structure, intake completeness, records, and "
            "immutability are valid."
        )
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", help="Base commit/ref used to enforce merged submission immutability")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    return Validator(args.base_ref, args.root).run()


if __name__ == "__main__":
    raise SystemExit(main())
