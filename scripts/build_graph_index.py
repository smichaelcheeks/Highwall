#!/usr/bin/env python3
"""Build or verify the Markdown-first entity/relationship graph index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from consistency_common import ROOT
from graph_common import GraphValidationError, build_graph_data


def render(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the tracked index is stale")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    root = args.root.resolve()
    output = root / "development" / "indexes" / "knowledge-graph.json"
    try:
        data = build_graph_data(root)
    except GraphValidationError as error:
        for message in error.errors:
            print(message, file=sys.stderr)
        return 1
    expected = render(data)
    if args.check:
        actual = output.read_text(encoding="utf-8") if output.exists() else ""
        if actual != expected:
            print(
                "Knowledge graph index is stale; run: python scripts/build_graph_index.py",
                file=sys.stderr,
            )
            return 1
        print("Knowledge graph index is current.")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(expected, encoding="utf-8")
    print(
        f"Wrote {output.relative_to(root)} with {len(data['entities'])} entities, "
        f"{len(data['relationships'])} relationships, "
        f"{len(data['knowledge_claims'])} maintained claims, "
        f"{len(data['histories'])} history events, and "
        f"{len(data['unmigrated_related_links'])} unmigrated related links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
