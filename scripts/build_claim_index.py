#!/usr/bin/env python3
"""Build or verify the non-authoritative index of reviewed claims."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from consistency_common import ROOT, parse_claim_rows, parse_front_matter


OUTPUT = ROOT / "development" / "indexes" / "claim-index.json"


def build_index() -> dict[str, object]:
    claims: list[dict[str, object]] = []
    review_root = ROOT / "development" / "intake-reviews"
    for path in sorted(review_root.glob("*.md")):
        if path.name == "README.md":
            continue
        metadata, lists = parse_front_matter(path)
        for claim in parse_claim_rows(path):
            claims.append(
                {
                    **claim,
                    "case_id": metadata.get("case_id", ""),
                    "submission_id": metadata.get("submission_id", ""),
                    "review_authority": metadata.get("authority", ""),
                    "review": path.relative_to(ROOT).as_posix(),
                    "submission": metadata.get("submission", ""),
                    "subjects": lists.get("subjects", []),
                    "domains": lists.get("domains", []),
                    "authoritative_targets": lists.get("authoritative_targets", []),
                }
            )
    claims.sort(key=lambda item: str(item["claim_id"]))
    return {
        "schema_version": 2,
        "authority": "navigation-only",
        "generated_from": "development/intake-reviews/*.md",
        "claims": claims,
    }


def render(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the tracked index is stale")
    args = parser.parse_args()
    expected = render(build_index())
    if args.check:
        actual = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if actual != expected:
            print("Claim index is stale; run: python scripts/build_claim_index.py", file=sys.stderr)
            return 1
        print("Claim index is current.")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(build_index()['claims'])} claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
