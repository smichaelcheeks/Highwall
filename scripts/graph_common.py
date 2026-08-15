#!/usr/bin/env python3
"""Parse and validate Highwall's Markdown-first entity/relationship graph."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from consistency_common import parse_front_matter, split_markdown_row


GRAPH_RECORD_ROOTS = ("canon", "story", "design", "development", "references")
ENTITY_ID = re.compile(r"^entity-[a-z0-9]+(?:-[a-z0-9]+)*$")
RELATIONSHIP_ID = re.compile(r"^relationship-[a-z0-9]+(?:-[a-z0-9]+)*$")
RELATIONSHIP_TYPE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOP_LEVEL_FIELD = re.compile(r"^[a-z_][a-z0-9_]*:")
RELATIONSHIP_START = re.compile(r"^  - relationship_id:\s*(.*?)\s*$")
RELATIONSHIP_FIELD = re.compile(r"^    ([a-z_]+):\s*(.*?)\s*$")
PROVENANCE_ITEM = re.compile(r"^      -\s+(.+?)\s*$")
RELATIONSHIP_FIELDS = {"relationship_type", "source", "target", "provenance"}


class GraphValidationError(ValueError):
    """Raised when graph records cannot produce a structurally valid index."""

    def __init__(self, errors: list[str]) -> None:
        self.errors = errors
        super().__init__("; ".join(errors))


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def front_matter_lines(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return []
    try:
        end = lines.index("---", 1)
    except ValueError:
        return []
    return lines[1:end]


def parse_relationships(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    """Parse the controlled nested relationship list from Markdown front matter."""
    lines = front_matter_lines(path)
    errors: list[str] = []
    header_index: int | None = None
    inline_value = ""
    for index, line in enumerate(lines):
        match = re.match(r"^relationships:\s*(.*?)\s*$", line)
        if match:
            header_index = index
            inline_value = match.group(1)
            break
    if header_index is None:
        return [], errors
    if inline_value:
        if inline_value != "[]":
            errors.append("relationships must be [] or a structured list")
        return [], errors

    block: list[str] = []
    for line in lines[header_index + 1 :]:
        if TOP_LEVEL_FIELD.match(line):
            break
        block.append(line)

    relationships: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    in_provenance = False
    seen_fields: set[str] = set()
    for line in block:
        if not line.strip():
            continue
        start = RELATIONSHIP_START.match(line)
        if start:
            if current is not None:
                relationships.append(current)
            current = {"relationship_id": unquote(start.group(1)), "provenance": []}
            in_provenance = False
            seen_fields = set()
            continue
        if current is None:
            errors.append(f"malformed relationships entry: {line.strip()}")
            continue
        provenance_item = PROVENANCE_ITEM.match(line)
        if provenance_item and in_provenance:
            provenance = current["provenance"]
            assert isinstance(provenance, list)
            provenance.append(unquote(provenance_item.group(1)))
            continue
        field = RELATIONSHIP_FIELD.match(line)
        if field:
            key = field.group(1)
            value = unquote(field.group(2))
            if key not in RELATIONSHIP_FIELDS:
                errors.append(f"unsupported relationship field: {key}")
                continue
            if key in seen_fields:
                errors.append(f"duplicate relationship field: {key}")
                continue
            seen_fields.add(key)
            if key == "provenance":
                if value and value != "[]":
                    errors.append("relationship provenance must be a block list")
                current["provenance"] = []
                in_provenance = not value
            else:
                current[key] = value
                in_provenance = False
            continue
        errors.append(f"malformed relationship field: {line.strip()}")
    if current is not None:
        relationships.append(current)
    return relationships, errors


def relationship_type_registry(root: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    path = root / "references" / "relationship-types.md"
    errors: list[str] = []
    if not path.is_file():
        return {}, ["references/relationship-types.md: missing relationship type registry"]
    types: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = split_markdown_row(line)
        if len(cells) != 4 or not cells[0].startswith("`"):
            continue
        relationship_type = cells[0].strip("`")
        if not RELATIONSHIP_TYPE.fullmatch(relationship_type):
            errors.append(f"references/relationship-types.md: invalid type {relationship_type!r}")
            continue
        if relationship_type in types:
            errors.append(
                f"references/relationship-types.md: duplicate type {relationship_type}"
            )
            continue
        types[relationship_type] = {
            "relationship_type": relationship_type,
            "directionality": cells[1],
            "authority_effect": cells[2],
            "definition": cells[3],
        }
    if not types:
        errors.append("references/relationship-types.md: no controlled types found")
    return types, errors


def resolve_repository_pointer(root: Path, owner: Path, pointer: str) -> Path | None:
    value = unquote(pointer).partition("#")[0]
    if not value or "://" in value or value.startswith("mailto:"):
        return None
    resolved = (owner.parent / unquote(value)).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None
    return resolved


def build_graph_data(root: Path) -> dict[str, object]:
    """Build graph navigation data or raise with every structural error found."""
    root = root.resolve()
    relationship_types, errors = relationship_type_registry(root)
    entities: list[dict[str, object]] = []
    relationships: list[dict[str, object]] = []
    entity_sources: dict[str, Path] = {}
    relationship_sources: dict[str, Path] = {}
    path_to_entity: dict[Path, str] = {}
    entity_related: list[tuple[Path, str, list[str]]] = []

    paths: list[Path] = []
    for directory in GRAPH_RECORD_ROOTS:
        record_root = root / directory
        if record_root.is_dir():
            paths.extend(record_root.rglob("*.md"))

    for path in sorted(set(paths)):
        metadata, lists = parse_front_matter(path)
        entity_id = metadata.get("entity_id", "")
        parsed_relationships, parse_errors = parse_relationships(path)
        relative = path.relative_to(root).as_posix()
        errors.extend(f"{relative}: {error}" for error in parse_errors)
        if not entity_id:
            if parsed_relationships:
                errors.append(f"{relative}: relationships require entity_id")
            continue
        if not ENTITY_ID.fullmatch(entity_id):
            errors.append(f"{relative}: invalid entity_id {entity_id!r}")
            continue
        if entity_id in entity_sources:
            errors.append(
                f"{relative}: duplicate entity_id {entity_id}; first used by "
                f"{entity_sources[entity_id].relative_to(root).as_posix()}"
            )
            continue
        entity_sources[entity_id] = path
        path_to_entity[path.resolve()] = entity_id
        entity = {
            "entity_id": entity_id,
            "path": relative,
            "title": metadata.get("title", ""),
            "record_type": metadata.get("type", ""),
            "status": metadata.get("status", ""),
            "canon_level": metadata.get("canon_level", ""),
            "aliases": lists.get("aliases", []),
            "provenance": lists.get("provenance", []),
        }
        entities.append(entity)
        entity_related.append((path, entity_id, lists.get("related", [])))

        for relationship in parsed_relationships:
            relationship_id = str(relationship.get("relationship_id", ""))
            if not RELATIONSHIP_ID.fullmatch(relationship_id):
                errors.append(f"{relative}: invalid relationship_id {relationship_id!r}")
                continue
            if relationship_id in relationship_sources:
                errors.append(
                    f"{relative}: duplicate relationship_id {relationship_id}; first used by "
                    f"{relationship_sources[relationship_id].relative_to(root).as_posix()}"
                )
                continue
            relationship_sources[relationship_id] = path
            normalized = {
                "relationship_id": relationship_id,
                "relationship_type": str(relationship.get("relationship_type", "")),
                "source": str(relationship.get("source", "")),
                "target": str(relationship.get("target", "")),
                "provenance": list(relationship.get("provenance", [])),
                "authoritative_record": relative,
            }
            relationships.append(normalized)

    known_endpoints = set(entity_sources) | set(relationship_sources)
    for relationship in relationships:
        relationship_id = str(relationship["relationship_id"])
        owner = relationship_sources[relationship_id]
        relative = owner.relative_to(root).as_posix()
        relationship_type = str(relationship["relationship_type"])
        if relationship_type not in relationship_types:
            errors.append(
                f"{relative}: relationship {relationship_id} uses uncontrolled type "
                f"{relationship_type!r}"
            )
        for endpoint_name in ("source", "target"):
            endpoint = str(relationship[endpoint_name])
            if endpoint not in known_endpoints:
                errors.append(
                    f"{relative}: relationship {relationship_id} has unresolved "
                    f"{endpoint_name} {endpoint!r}"
                )
        provenance = relationship["provenance"]
        assert isinstance(provenance, list)
        if not provenance:
            errors.append(f"{relative}: relationship {relationship_id} has no provenance")
        for pointer in provenance:
            resolved = resolve_repository_pointer(root, owner, str(pointer))
            if resolved is None or not resolved.is_file():
                errors.append(
                    f"{relative}: relationship {relationship_id} has invalid provenance "
                    f"{pointer!r}"
                )

    explicit_related_pairs = {
        frozenset((str(item["source"]), str(item["target"])))
        for item in relationships
        if item["relationship_type"] == "related-to"
        and str(item["source"]).startswith("entity-")
        and str(item["target"]).startswith("entity-")
    }
    unmigrated: list[dict[str, str]] = []
    for path, source_entity, related_links in entity_related:
        for related_link in related_links:
            target_path = resolve_repository_pointer(root, path, related_link)
            target_entity = path_to_entity.get(target_path) if target_path else None
            if target_entity and frozenset((source_entity, target_entity)) in explicit_related_pairs:
                continue
            unmigrated.append(
                {
                    "source_entity_id": source_entity,
                    "source_path": path.relative_to(root).as_posix(),
                    "legacy_target": unquote(related_link),
                    "target_entity_id": target_entity or "",
                }
            )

    if errors:
        raise GraphValidationError(sorted(errors))
    entities.sort(key=lambda item: str(item["entity_id"]))
    relationships.sort(key=lambda item: str(item["relationship_id"]))
    unmigrated.sort(
        key=lambda item: (item["source_entity_id"], item["legacy_target"])
    )
    return {
        "schema_version": 1,
        "authority": "navigation-only",
        "generated_from": "Markdown records with explicit graph metadata",
        "relationship_types": [relationship_types[key] for key in sorted(relationship_types)],
        "entities": entities,
        "relationships": relationships,
        "unmigrated_related_links": unmigrated,
    }
