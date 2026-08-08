#!/usr/bin/env python3
"""Build or verify the non-authoritative index of reviewed claims."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from consistency_common import ROOT, parse_claim_rows, parse_front_matter


EXCEPTIONAL_DISPOSITIONS = {"conflict", "defer", "retire"}
EXCEPTIONAL_RECORD_ROOTS = {
    "defer": {"open-questions", "proposals"},
    "conflict": {"contradictions"},
    "retire": {"retired"},
}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def exception_records(
    root: Path, review: Path, target: str, disposition: str
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    development_root = root / "development"
    for href in MARKDOWN_LINK.findall(target):
        path = (review.parent / href.partition("#")[0]).resolve()
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError as error:
            raise ValueError(f"Exception target escapes repository: {review}: {href}") from error
        if not path.is_file():
            raise ValueError(f"Missing exception record: {review}: {href}")
        try:
            relative_parts = path.relative_to(development_root).parts
        except ValueError as error:
            raise ValueError(
                f"Wrong exception record type for {disposition}: {relative}"
            ) from error
        if not relative_parts or relative_parts[0] not in EXCEPTIONAL_RECORD_ROOTS[disposition]:
            allowed = ", ".join(sorted(EXCEPTIONAL_RECORD_ROOTS[disposition]))
            raise ValueError(
                f"Wrong exception record type for {disposition}: {relative}; expected {allowed}"
            )
        metadata, _ = parse_front_matter(path)
        status = metadata.get("status", "")
        if not status:
            raise ValueError(f"Exception record has no status: {relative}")
        records.append({"path": relative, "status": status})
    return records


def build_index(root: Path = ROOT) -> dict[str, object]:
    root = root.resolve()
    claims: list[dict[str, object]] = []
    review_root = root / "development" / "intake-reviews"
    claim_sources: dict[str, Path] = {}
    for path in sorted(review_root.glob("*.md")):
        if path.name == "README.md":
            continue
        metadata, lists = parse_front_matter(path)
        for claim in parse_claim_rows(path):
            disposition = str(claim["disposition"])
            records = (
                exception_records(root, path, str(claim["target"]), disposition)
                if disposition in EXCEPTIONAL_DISPOSITIONS
                else []
            )
            if disposition in EXCEPTIONAL_DISPOSITIONS and not records:
                raise ValueError(
                    f"Exceptional claim has no linked development record: {claim['claim_id']}"
                )
            claims.append(
                {
                    **claim,
                    "exception_records": records,
                    "superseded_by": [],
                    "case_id": metadata.get("case_id", ""),
                    "submission_id": metadata.get("submission_id", ""),
                    "review_authority": metadata.get("authority", ""),
                    "review": path.relative_to(root).as_posix(),
                    "submission": metadata.get("submission", ""),
                    "subjects": lists.get("subjects", []),
                    "domains": lists.get("domains", []),
                    "authoritative_targets": lists.get("authoritative_targets", []),
                }
            )
            claim_id = str(claim["claim_id"])
            if claim_id in claim_sources:
                raise ValueError(
                    f"Duplicate claim ID {claim_id}: "
                    f"{claim_sources[claim_id].relative_to(root)} and {path.relative_to(root)}"
                )
            claim_sources[claim_id] = path
    claims_by_id = {str(claim["claim_id"]): claim for claim in claims}
    for claim in claims:
        for earlier_id in claim["supersedes"]:
            if earlier_id not in claims_by_id:
                raise ValueError(
                    f"Claim {claim['claim_id']} supersedes missing claim {earlier_id}"
                )
            claims_by_id[earlier_id]["superseded_by"].append(claim["claim_id"])
    for claim in claims:
        claim["superseded_by"].sort()
    claims.sort(key=lambda item: str(item["claim_id"]))
    return {
        "schema_version": 3,
        "authority": "navigation-only",
        "generated_from": "development/intake-reviews/*.md",
        "claims": claims,
    }


def render(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the tracked index is stale")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    root = args.root.resolve()
    output = root / "development" / "indexes" / "claim-index.json"
    data = build_index(root)
    expected = render(data)
    if args.check:
        actual = output.read_text(encoding="utf-8") if output.exists() else ""
        if actual != expected:
            print("Claim index is stale; run: python scripts/build_claim_index.py", file=sys.stderr)
            return 1
        print("Claim index is current.")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(expected, encoding="utf-8")
    print(f"Wrote {output.relative_to(root)} with {len(data['claims'])} claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
