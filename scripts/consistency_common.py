#!/usr/bin/env python3
"""Shared parsers for Highwall consistency tooling."""

from __future__ import annotations

import re
from collections.abc import Mapping
from datetime import date, datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CLAIM_ROW = re.compile(r"^\|\s*(CASE-.*-C\d{3})\s*\|")
CLAIM_ID = re.compile(r"CASE-[A-Z0-9-]+-C\d{3}")
CLAIM_COLUMN_COUNT = 9


class FrontMatterLoader(yaml.SafeLoader):
    """Safe YAML loader with YAML 1.2-style true/false booleans."""


FrontMatterLoader.yaml_implicit_resolvers = {
    key: list(value) for key, value in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
for resolver_key, resolvers in list(FrontMatterLoader.yaml_implicit_resolvers.items()):
    FrontMatterLoader.yaml_implicit_resolvers[resolver_key] = [
        resolver
        for resolver in resolvers
        if resolver[0]
        not in {
            "tag:yaml.org,2002:bool",
            "tag:yaml.org,2002:float",
            "tag:yaml.org,2002:int",
            "tag:yaml.org,2002:null",
            "tag:yaml.org,2002:timestamp",
        }
    ]
FrontMatterLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|false)$", re.IGNORECASE),
    list("tTfF"),
)


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


def parse_front_matter_data(path: Path) -> dict[str, object]:
    """Parse a Markdown record's YAML front matter into native values."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    try:
        parsed = yaml.load("\n".join(lines[1:end]), Loader=FrontMatterLoader)
    except yaml.YAMLError as error:
        raise ValueError(f"invalid YAML front matter: {error}") from error
    if parsed is None:
        return {}
    if not isinstance(parsed, Mapping):
        raise ValueError("YAML front matter must be a mapping")
    return {str(key): value for key, value in parsed.items()}


def scalar_text(value: object) -> str:
    """Normalize a parsed YAML scalar for legacy string-oriented callers."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def parse_front_matter(path: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Return backward-compatible scalar and scalar-list front-matter views."""
    try:
        data = parse_front_matter_data(path)
    except ValueError:
        return {}, {}
    scalars: dict[str, str] = {}
    lists: dict[str, list[str]] = {}
    for key, value in data.items():
        if value is None or value == "":
            scalars[key] = ""
            lists[key] = []
        elif isinstance(value, list):
            if all(not isinstance(item, (dict, list)) for item in value):
                lists[key] = [scalar_text(item) for item in value]
            scalars[key] = "" if value else "[]"
        elif isinstance(value, dict):
            scalars[key] = ""
        else:
            scalars[key] = scalar_text(value)
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
                "existing_authority_or_evidence": cells[5],
                "disposition": cells[6].strip("`"),
                "target": cells[7],
            }
        )
    return claims
