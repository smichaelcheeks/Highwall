#!/usr/bin/env python3
"""Shared parsers for Highwall consistency tooling."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAIM_ROW = re.compile(r"^\|\s*(CASE-.*-C\d{3})\s*\|")
CLAIM_ID = re.compile(r"CASE-[A-Z0-9-]+-C\d{3}")
CLAIM_COLUMN_COUNT = 9


def parse_inline_list(value: str) -> list[str] | None:
    """Parse the simple inline-list form used by repository front matter."""
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [item.strip().strip("\"'") for item in inner.split(",")]


def split_markdown_row(line: str) -> list[str]:
    """Split a pipe-delimited Markdown row while preserving escaped pipes."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for character in stripped:
        if escaped:
            current.append(character)
            escaped = False
        elif character == "\\":
            current.append(character)
            escaped = True
        elif character == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
    cells.append("".join(current).strip())
    return cells


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
        inline_list = parse_inline_list(value)
        if inline_list is not None:
            lists[key] = inline_list
            current_list = None
        elif value:
            current_list = None
        else:
            lists[key] = []
            current_list = key
    return scalars, lists


def parse_claim_rows(path: Path) -> list[dict[str, object]]:
    claims: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not CLAIM_ROW.match(line):
            continue
        cells = split_markdown_row(line)
        if len(cells) != CLAIM_COLUMN_COUNT:
            continue
        claims.append(
            {
                "claim_id": cells[0],
                "summary": cells[1],
                "classification": cells[2].strip("`"),
                "authority_basis": cells[3].strip("`"),
                "supersedes": CLAIM_ID.findall(cells[4]),
                "disposition": cells[6].strip("`"),
                "target": cells[7],
            }
        )
    return claims
