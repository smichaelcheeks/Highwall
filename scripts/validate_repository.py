#!/usr/bin/env python3
"""Validate structural invariants for the Highwall knowledge repository."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from consistency_common import CLAIM_COLUMN_COUNT, parse_inline_list, split_markdown_row


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_REQUIRED = {
    "title",
    "type",
    "status",
    "canon_level",
    "aliases",
    "tags",
    "related",
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
END_OF_SEED_MARKER = "<!-- END OF SEED -->"
IMPACT_FIELDS = {"subjects", "domains", "search_terms", "authoritative_targets"}
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
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            return None
        try:
            end = lines.index("---", 1)
        except ValueError:
            return None
        values: dict[str, str] = {}
        for line in lines[1:end]:
            match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
            if match:
                values[match.group(1)] = (match.group(2) or "").strip().strip('"')
        return values

    @staticmethod
    def parse_front_matter_lists(path: Path) -> dict[str, list[str]]:
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            return {}
        try:
            end = lines.index("---", 1)
        except ValueError:
            return {}
        values: dict[str, list[str]] = {}
        current: str | None = None
        for line in lines[1:end]:
            item = re.match(r"^\s+-\s+(.+?)\s*$", line)
            if item and current:
                values[current].append(item.group(1).strip().strip('"'))
                continue
            field = re.match(r"^([a-z_]+):\s*$", line)
            if field:
                current = field.group(1)
                values[current] = []
            else:
                inline = re.match(r"^([a-z_]+):\s*(\[.*\])\s*$", line)
                if inline:
                    parsed = parse_inline_list(inline.group(2))
                    if parsed is not None:
                        values[inline.group(1)] = parsed
                current = None
        return values

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
        list_fields = {"aliases", "tags", "related", "provenance"}
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

    def validate_transmission_completeness(self, path: Path, metadata: dict[str, str]) -> None:
        status = metadata.get("transmission_status")
        basis = metadata.get("completion_basis")
        if status not in TRANSMISSION_STATUSES:
            self.error(path, f"invalid or missing transmission_status: {status!r}")
        if basis not in COMPLETION_BASES:
            self.error(path, f"invalid or missing completion_basis: {basis!r}")
        if basis == "end-marker" and END_OF_SEED_MARKER not in path.read_text(encoding="utf-8"):
            self.error(path, f"completion_basis 'end-marker' requires {END_OF_SEED_MARKER}")

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
        self.validate_intake()
        self.validate_submission_immutability()
        if self.errors:
            print("Repository validation failed:", file=sys.stderr)
            for error in self.errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print(
            f"Repository validation passed: {len(self.markdown_files)} Markdown files; "
            "links, canon metadata, intake completeness, records, and immutability are valid."
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
