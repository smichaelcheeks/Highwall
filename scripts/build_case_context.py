#!/usr/bin/env python3
"""Build a targeted consistency context report for an intake case."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from consistency_common import ROOT


INDEX = ROOT / "development" / "indexes" / "claim-index.json"
SEARCH_ROOTS = ("canon", "story", "design", "development")


def normalize(values: list[str]) -> list[str]:
    return sorted({value.strip().lower() for value in values if value.strip()})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", action="append", default=[])
    parser.add_argument("--domain", action="append", default=[])
    parser.add_argument("--term", action="append", default=[])
    parser.add_argument("--target", action="append", default=[])
    parser.add_argument("--max-results", type=int, default=50)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    subjects = normalize(args.subject)
    domains = normalize(args.domain)
    terms = normalize(args.term + [subject.replace("-", " ") for subject in subjects])
    targets = normalize(args.target)
    if not any((subjects, domains, terms, targets)):
        parser.error("provide at least one --subject, --domain, --term, or --target")

    index = json.loads(INDEX.read_text(encoding="utf-8"))
    matched_claims: list[dict[str, object]] = []
    for claim in index["claims"]:
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
            any(subject in claim.get("subjects", []) for subject in subjects)
            or any(domain in claim.get("domains", []) for domain in domains)
            or any(term in haystack for term in terms)
            or any(target in haystack for target in targets)
        ):
            matched_claims.append(claim)

    file_scores: list[tuple[int, str]] = []
    needles = terms + subjects + domains + [Path(target).name.lower() for target in targets]
    for root_name in SEARCH_ROOTS:
        for path in sorted((ROOT / root_name).rglob("*.md")):
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8").lower()
            score = sum(text.count(needle) for needle in needles if needle)
            if relative.lower() in targets:
                score += 1000
            if score:
                file_scores.append((score, relative))
    file_scores.sort(key=lambda item: (-item[0], item[1]))

    lines = [
        "# Targeted Case Context",
        "",
        "> Generated navigation context. This report is not canon evidence.",
        "",
        "## Criteria",
        "",
        f"- **Subjects:** {', '.join(subjects) or 'None'}",
        f"- **Domains:** {', '.join(domains) or 'None'}",
        f"- **Terms:** {', '.join(terms) or 'None'}",
        f"- **Targets:** {', '.join(targets) or 'None'}",
        "",
        "## Relevant files and backlinks",
        "",
    ]
    for score, relative in file_scores[: args.max_results]:
        lines.append(f"- `{relative}` (score {score})")
    if not file_scores:
        lines.append("- None found.")
    lines.extend(["", "## Indexed claims", ""])
    for claim in matched_claims[: args.max_results]:
        lines.append(
            f"- `{claim['claim_id']}` — {claim['summary']} "
            f"(`{claim['disposition']}`; `{claim['review']}`)"
        )
    if not matched_claims:
        lines.append("- None found.")
    report = "\n".join(lines) + "\n"
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
