#!/usr/bin/env python3
"""Shared parsers for Highwall consistency tooling."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAIM_ROW = re.compile(r"^\|\s*(CASE-.*-C\d{3})\s*\|")


def parse_front_matter(path: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}, {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, {}
    scalars: dict[str, str] = {}
    lists: dict[str, list[str]] = {}
    current_list: str | None = None
    for line in lines[1:end]:
        item = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if item and current_list:
            lists[current_list].append(item.group(1).strip().strip('"'))
            continue
        field = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if not field:
            current_list = None
            continue
        key = field.group(1)
        value = (field.group(2) or "").strip().strip('"')
        scalars[key] = value
        if value:
            current_list = None
        else:
            lists[key] = []
            current_list = key
    return scalars, lists


def parse_claim_rows(path: Path) -> list[dict[str, str]]:
    claims: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not CLAIM_ROW.match(line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            continue
        claims.append(
            {
                "claim_id": cells[0],
                "summary": cells[1],
                "classification": cells[2].strip("`"),
                "authority_basis": cells[3].strip("`"),
                "disposition": cells[6].strip("`"),
                "target": cells[7],
            }
        )
    return claims
