#!/usr/bin/env python3
"""Build deterministic, navigation-only audit context between Git commits."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

from consistency_common import ROOT, parse_inline_list


INDEX_PATH = "development/indexes/claim-index.json"
CATEGORY_ORDER = (
    "canon",
    "story",
    "design",
    "intake",
    "review",
    "development",
    "reference",
    "template",
    "script",
    "test",
    "workflow",
    "other",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
MISSING = object()


class AuditContextError(RuntimeError):
    """Raised when Git state cannot support a reliable comparison."""


def git(root: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "Git command failed"
        raise AuditContextError(detail)
    return result.stdout


def normalize_path(path: str) -> str:
    """Normalize Git or Windows-style repository paths to POSIX form."""
    normalized = posixpath.normpath(path.replace("\\", "/"))
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized.lstrip("/")


def classify_path(path: str) -> str:
    normalized = normalize_path(path)
    if normalized.startswith("development/intake-reviews/"):
        return "review"
    prefixes = {
        "canon/": "canon",
        "story/": "story",
        "design/": "design",
        "intake/": "intake",
        "development/": "development",
        "references/": "reference",
        "templates/": "template",
        "scripts/": "script",
        "tests/": "test",
        ".github/workflows/": "workflow",
    }
    for prefix, category in prefixes.items():
        if normalized.startswith(prefix):
            return category
    return "other"


def resolve_commit(root: Path, ref: str, label: str) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        detail = result.stderr.strip() or "unknown revision"
        raise AuditContextError(f"Cannot resolve {label} commit {ref!r}: {detail}")
    return result.stdout.strip()


def ensure_repository(root: Path, baseline: str, head: str) -> None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        raise AuditContextError("Repository structure is insufficient: not a Git repository")
    actual_root = Path(result.stdout.strip()).resolve()
    if actual_root != root.resolve():
        raise AuditContextError(
            "Repository structure is insufficient: --root must be the Git worktree root"
        )
    for commit in (baseline, head):
        probe = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}:development/intake-reviews"],
            cwd=root,
            check=False,
            capture_output=True,
        )
        if probe.returncode:
            raise AuditContextError(
                "Repository structure is insufficient for a reliable comparison: "
                f"development/intake-reviews is missing at {commit}"
            )


def ensure_ancestor(root: Path, baseline: str, head: str) -> None:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", baseline, head],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode == 1:
        raise AuditContextError(
            f"Baseline {baseline} is not an ancestor of head {head}; perform a fresh review"
        )
    if result.returncode:
        raise AuditContextError("Git could not verify the baseline ancestry relationship")


def ensure_clean_head(root: Path, head_ref: str, resolved_head: str) -> None:
    explicit_object_id = re.fullmatch(r"[0-9a-fA-F]{7,40}", head_ref) is not None
    current_head = git(root, "rev-parse", "HEAD").strip()
    if explicit_object_id or resolved_head != current_head:
        return
    status = git(root, "status", "--porcelain", "--untracked-files=all")
    if status.strip():
        raise AuditContextError(
            "Working tree is not clean; comparing to HEAD would silently omit "
            "uncommitted changes"
        )


def read_blob(root: Path, commit: str, path: str, *, required: bool = False) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{commit}:{normalize_path(path)}"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="strict",
    )
    if result.returncode:
        if required:
            raise AuditContextError(
                f"Required historical data cannot be read at {commit}:{normalize_path(path)}"
            )
        return None
    return result.stdout


def load_index(root: Path, commit: str) -> dict[str, dict[str, Any]]:
    text = read_blob(root, commit, INDEX_PATH, required=True)
    try:
        data = json.loads(text or "")
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise AuditContextError(
            f"Required historical claim index is unreadable at {commit}:{INDEX_PATH}: {error}"
        ) from error
    claims = data.get("claims") if isinstance(data, dict) else None
    if not isinstance(data, dict) or data.get("authority") != "navigation-only":
        raise AuditContextError(
            f"Required historical claim index is not navigation-only at {commit}:{INDEX_PATH}"
        )
    if not isinstance(claims, list):
        raise AuditContextError(
            f"Required historical claim index has no claims list at {commit}:{INDEX_PATH}"
        )
    by_id: dict[str, dict[str, Any]] = {}
    for claim in claims:
        if not isinstance(claim, dict) or not isinstance(claim.get("claim_id"), str):
            raise AuditContextError(
                f"Required historical claim index contains an invalid claim at {commit}"
            )
        claim_id = claim["claim_id"]
        if claim_id in by_id:
            raise AuditContextError(
                f"Required historical claim index contains duplicate claim ID {claim_id}"
            )
        by_id[claim_id] = claim
    return by_id


def parse_front_matter_text(text: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, {}
    scalars: dict[str, str] = {}
    lists: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines[1:end]:
        item = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if item and current:
            lists[current].append(item.group(1).strip().strip('"'))
            continue
        field = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if not field:
            current = None
            continue
        key = field.group(1)
        value = (field.group(2) or "").strip().strip('"')
        scalars[key] = value
        inline = parse_inline_list(value)
        if inline is not None:
            lists[key] = inline
            current = None
        elif value:
            current = None
        else:
            lists[key] = []
            current = key
    return scalars, lists


def changed_paths(root: Path, baseline: str, head: str) -> list[dict[str, str]]:
    output = git(root, "diff", "--name-status", "--find-renames", baseline, head, "--")
    changes: list[dict[str, str]] = []
    for line in output.splitlines():
        cells = line.split("\t")
        if len(cells) < 2:
            continue
        status = cells[0]
        if status.startswith(("R", "C")) and len(cells) >= 3:
            changes.append(
                {
                    "status": status,
                    "old_path": normalize_path(cells[1]),
                    "path": normalize_path(cells[2]),
                }
            )
        else:
            changes.append({"status": status, "path": normalize_path(cells[1])})
    return sorted(changes, key=lambda item: (item["path"], item["status"]))


def display_value(value: Any) -> str:
    if value is MISSING:
        return "<missing>"
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def claim_differences(
    baseline_claims: dict[str, dict[str, Any]], head_claims: dict[str, dict[str, Any]]
) -> tuple[list[str], list[str], dict[str, list[tuple[str, Any, Any]]], list[str]]:
    baseline_ids = set(baseline_claims)
    head_ids = set(head_claims)
    added = sorted(head_ids - baseline_ids)
    removed = sorted(baseline_ids - head_ids)
    changed: dict[str, list[tuple[str, Any, Any]]] = {}
    unchanged: list[str] = []
    for claim_id in sorted(baseline_ids & head_ids):
        before = baseline_claims[claim_id]
        after = head_claims[claim_id]
        fields = sorted((set(before) | set(after)) - {"claim_id"})
        differences = []
        for field in fields:
            before_value = before[field] if field in before else MISSING
            after_value = after[field] if field in after else MISSING
            if before_value != after_value:
                differences.append((field, before_value, after_value))
        if differences:
            changed[claim_id] = differences
        else:
            unchanged.append(claim_id)
    return added, removed, changed, unchanged


def format_field_change(field: str, before: Any, after: Any) -> str:
    if before is MISSING or after is MISSING:
        return f"{field}: {display_value(before)} -> {display_value(after)}"
    if field in {"supersedes", "superseded_by"}:
        before_set = set(before or [])
        after_set = set(after or [])
        added = sorted(after_set - before_set)
        removed = sorted(before_set - after_set)
        parts = []
        if added:
            parts.append(f"added {display_value(added)}")
        if removed:
            parts.append(f"removed {display_value(removed)}")
        if not parts:
            parts.append(
                f"order changed {display_value(before)} -> {display_value(after)}"
            )
        return f"{field}: " + "; ".join(parts)
    if field == "exception_records":
        before_status = {
            item.get("path", ""): item.get("status", "") for item in (before or [])
        }
        after_status = {
            item.get("path", ""): item.get("status", "") for item in (after or [])
        }
        if before_status == after_status and before != after:
            return (
                "exception_records: "
                f"{display_value(before)} -> {display_value(after)}"
            )
        return (
            "exceptional-record status: "
            f"{display_value(before_status)} -> {display_value(after_status)}"
        )
    return f"{field}: {display_value(before)} -> {display_value(after)}"


def review_manifests(
    root: Path, baseline: str, head: str, changes: list[dict[str, str]]
) -> list[dict[str, Any]]:
    manifests: list[dict[str, Any]] = []
    for change in changes:
        path = change["path"]
        old_path = change.get("old_path", path)
        if classify_path(path) != "review" and classify_path(old_path) != "review":
            continue
        text = read_blob(root, head, path) or read_blob(root, baseline, old_path)
        if text is None:
            continue
        scalars, lists = parse_front_matter_text(text)
        manifests.append(
            {
                "path": path,
                "subjects": sorted(lists.get("subjects", [])),
                "domains": sorted(lists.get("domains", [])),
                "search_terms": sorted(lists.get("search_terms", [])),
                "authoritative_targets": sorted(lists.get("authoritative_targets", [])),
                "authority": scalars.get("authority", ""),
            }
        )
    return sorted(manifests, key=lambda item: item["path"])


def canon_metadata_changes(
    root: Path, baseline: str, head: str, changes: list[dict[str, str]]
) -> list[tuple[str, list[tuple[str, Any, Any]]]]:
    result: list[tuple[str, list[tuple[str, Any, Any]]]] = []
    fields = ("status", "canon_level", "aliases", "related", "provenance")
    for change in changes:
        path = change["path"]
        old_path = change.get("old_path", path)
        if classify_path(path) != "canon" and classify_path(old_path) != "canon":
            continue
        before_text = read_blob(root, baseline, old_path)
        after_text = read_blob(root, head, path)
        before_scalars, before_lists = parse_front_matter_text(before_text or "")
        after_scalars, after_lists = parse_front_matter_text(after_text or "")
        differences: list[tuple[str, Any, Any]] = []
        for field in fields:
            before: Any = before_lists.get(field, before_scalars.get(field))
            after: Any = after_lists.get(field, after_scalars.get(field))
            if before != after:
                differences.append((field, before, after))
        result.append((path, differences))
    return result


def tree_paths(root: Path, commit: str, suffix: str | None = None) -> list[str]:
    paths = [normalize_path(item) for item in git(root, "ls-tree", "-r", "--name-only", commit).splitlines()]
    if suffix:
        paths = [path for path in paths if path.endswith(suffix)]
    return sorted(paths)


def resolve_link(source: str, href: str) -> str | None:
    target = href.strip().strip("<>").partition("#")[0]
    if not target or URL_SCHEME.match(target) or target.startswith("//"):
        return None
    return normalize_path(posixpath.join(str(PurePosixPath(source).parent), target))


def backlinks(
    root: Path, head: str, targets: set[str], changed: set[str]
) -> list[tuple[str, str, bool]]:
    if not targets:
        return []
    results: set[tuple[str, str, bool]] = set()
    for source in tree_paths(root, head, ".md"):
        text = read_blob(root, head, source)
        if text is None:
            continue
        for href in MARKDOWN_LINK.findall(text):
            target = resolve_link(source, href)
            if target in targets:
                results.add((source, target, source not in changed))
    return sorted(results)


def targeted_claims(
    claims: dict[str, dict[str, Any]], manifests: list[dict[str, Any]], targets: set[str]
) -> tuple[dict[str, list[str]], list[dict[str, Any]]]:
    criteria = {
        "subjects": sorted({item for manifest in manifests for item in manifest["subjects"]}),
        "domains": sorted({item for manifest in manifests for item in manifest["domains"]}),
        "terms": sorted({item for manifest in manifests for item in manifest["search_terms"]}),
        "targets": sorted(targets),
    }
    matches: list[dict[str, Any]] = []
    for claim in claims.values():
        haystack = " ".join(
            [
                str(claim.get("summary", "")),
                str(claim.get("target", "")),
                " ".join(claim.get("subjects", [])),
                " ".join(claim.get("domains", [])),
                " ".join(claim.get("authoritative_targets", [])),
            ]
        ).lower()
        if (
            any(item in claim.get("subjects", []) for item in criteria["subjects"])
            or any(item in claim.get("domains", []) for item in criteria["domains"])
            or any(item.lower() in haystack for item in criteria["terms"])
            or any(item.lower() in haystack for item in criteria["targets"])
        ):
            matches.append(claim)
    return criteria, sorted(matches, key=lambda item: item["claim_id"])


def build_report(root: Path, baseline_ref: str, head_ref: str) -> str:
    root = root.resolve()
    baseline = resolve_commit(root, baseline_ref, "baseline")
    head = resolve_commit(root, head_ref, "head")
    ensure_repository(root, baseline, head)
    ensure_ancestor(root, baseline, head)
    ensure_clean_head(root, head_ref, head)

    changes = changed_paths(root, baseline, head)
    baseline_claims = load_index(root, baseline)
    head_claims = load_index(root, head)
    added, removed, changed_claims, unchanged = claim_differences(
        baseline_claims, head_claims
    )
    manifests = review_manifests(root, baseline, head, changes)
    metadata = canon_metadata_changes(root, baseline, head, changes)
    changed_set = {item["path"] for item in changes}
    targets = {
        normalize_path(target)
        for manifest in manifests
        for target in manifest["authoritative_targets"]
    }
    targets.update(item["path"] for item in changes if classify_path(item["path"]) == "canon")
    linked = backlinks(root, head, targets, changed_set)
    criteria, context_claims = targeted_claims(head_claims, manifests, targets)

    lines = [
        "# Incremental Audit Context",
        "",
        "> Navigation-only change context. This report does not establish canon coherence,",
        "> authorize a claim retirement, or replace semantic review or the linked reviews.",
        "",
        "## Git baseline",
        "",
        f"- **Requested baseline:** `{baseline_ref}`",
        f"- **Resolved baseline:** `{baseline}`",
        f"- **Requested head:** `{head_ref}`",
        f"- **Resolved head:** `{head}`",
        "- **Baseline is ancestor of head:** Yes",
        f"- **Git range examined:** `{baseline}..{head}`",
        "",
        "## Changed paths by repository domain",
        "",
    ]
    grouped = {category: [] for category in CATEGORY_ORDER}
    for change in changes:
        grouped[classify_path(change["path"])].append(change)
    for category in CATEGORY_ORDER:
        lines.extend([f"### {category.title()}", ""])
        if not grouped[category]:
            lines.append("- None.")
        for change in grouped[category]:
            if "old_path" in change:
                lines.append(
                    f"- `{change['status']}` `{change['old_path']}` -> `{change['path']}`"
                )
            else:
                lines.append(f"- `{change['status']}` `{change['path']}`")
        lines.append("")

    lines.extend(["## Claim-index comparison", ""])
    lines.append(f"- **Added claims:** {len(added)}")
    lines.append(f"- **Removed claims:** {len(removed)}")
    lines.append(f"- **Changed claims:** {len(changed_claims)}")
    lines.append(f"- **Unchanged claims:** {len(unchanged)}")
    lines.extend(["", "### Added claims", ""])
    if added:
        for claim_id in added:
            claim = head_claims[claim_id]
            lines.append(
                f"- `{claim_id}` — {claim.get('summary', '')} "
                f"(authority: `{claim.get('review_authority', '')}`; "
                f"disposition: `{claim.get('disposition', '')}`)"
            )
    else:
        lines.append("- None.")
    lines.extend(["", "### Removed claims", ""])
    if removed:
        for claim_id in removed:
            claim = baseline_claims[claim_id]
            lines.append(
                f"- `{claim_id}` — {claim.get('summary', '')}; historical difference only. "
                "Semantic review is required before any retirement conclusion."
            )
    else:
        lines.append("- None.")
    lines.extend(["", "### Changed indexed fields", ""])
    if changed_claims:
        for claim_id, differences in changed_claims.items():
            lines.append(f"- `{claim_id}`")
            for field, before, after in differences:
                lines.append(f"  - {format_field_change(field, before, after)}")
    else:
        lines.append("- None.")
    lines.extend(
        [
            "",
            "### Unchanged claims",
            "",
            f"- {len(unchanged)} stable claim IDs have identical indexed fields at both commits.",
            "- Identical indexed fields are not evidence that every semantic dependency is unchanged.",
            "",
            "## Changed review impact manifests",
            "",
        ]
    )
    if manifests:
        for manifest in manifests:
            lines.append(f"### `{manifest['path']}`")
            lines.append("")
            lines.append(f"- **Review authority:** `{manifest['authority'] or 'Not recorded'}`")
            for label, key in (
                ("Subjects", "subjects"),
                ("Domains", "domains"),
                ("Terms", "search_terms"),
                ("Authoritative targets", "authoritative_targets"),
            ):
                values = manifest[key]
                lines.append(f"- **{label}:** {', '.join(f'`{item}`' for item in values) or 'None recorded'}")
            lines.append("")
    else:
        lines.append("- No changed intake review supplied an impact manifest.")
        lines.append("- Impact manifests assist interpretation but are not exhaustive and do not replace the Git diff.")
        lines.append("")

    lines.extend(["## Changed canon metadata", ""])
    if metadata:
        for path, differences in metadata:
            lines.append(f"### `{path}`")
            lines.append("")
            if differences:
                for field, before, after in differences:
                    lines.append(
                        f"- **{field}:** {display_value(before)} -> {display_value(after)}"
                    )
            else:
                lines.append("- No tracked status, authority-level, alias, relation, or provenance field changed.")
            lines.append("- Substantive body changes still require semantic review.")
            lines.append("")
    else:
        lines.append("- No canon files changed.")
        lines.append("")

    lines.extend(["## Relevant backlinks", ""])
    if linked:
        for source, target, source_unchanged in linked:
            qualifier = "; source file unchanged" if source_unchanged else ""
            lines.append(f"- `{source}` -> `{target}`{qualifier}")
    else:
        lines.append("- None discovered for the changed canon and declared authoritative targets.")
    lines.extend(["", "## Current targeted context", ""])
    for label, key in (
        ("Subjects", "subjects"),
        ("Domains", "domains"),
        ("Terms", "terms"),
        ("Targets", "targets"),
    ):
        lines.append(f"- **{label}:** {', '.join(f'`{item}`' for item in criteria[key]) or 'None'}")
    lines.extend(["", "### Relevant current indexed claims", ""])
    if context_claims:
        for claim in context_claims:
            lines.append(
                f"- `{claim['claim_id']}` — {claim.get('summary', '')} "
                f"(authority: `{claim.get('review_authority', '')}`; "
                f"disposition: `{claim.get('disposition', '')}`)"
            )
    else:
        lines.append("- None discovered from the recorded criteria.")

    lines.extend(
        [
            "",
            "## Dependency warning and limitations",
            "",
            "- Semantic dependencies may extend beyond directly changed files and beyond declared impact manifests.",
            "- An unchanged file can be invalidated by a changed dependency; a changed file does not invalidate every relationship involving it.",
            "- Git history is authoritative for changed paths. Impact manifests and the canon change log only assist interpretation.",
            "- Claim-index and generated context fields are navigation-only. Linked reviews and authority-bearing records remain authoritative.",
            "- Added, removed, or changed claim rows describe historical differences; they do not authorize promotion, retirement, correction, or supersession.",
            "- Meaning, contradiction, authority, ownership, narrative-boundary, and carry-forward judgments require semantic review.",
            "- Missing, ambiguous, or unauditable baseline evidence requires fresh review rather than guessed reuse.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="Prior audited commit or ref")
    parser.add_argument("--head", default="HEAD", help="New commit or ref (default: HEAD)")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        report = build_report(args.root, args.baseline, args.head)
    except (AuditContextError, UnicodeError) as error:
        print(f"Incremental audit context failed: {error}", file=sys.stderr)
        return 2
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
