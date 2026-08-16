#!/usr/bin/env python3
"""Parse and validate Highwall's Markdown-first knowledge-object graph."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from pathlib import Path
from urllib.parse import unquote

from build_claim_index import build_index as build_claim_index_data
from consistency_common import parse_front_matter_data, scalar_text, split_markdown_row


GRAPH_RECORD_ROOTS = ("canon", "story", "design", "development", "references")
ENTITY_ID = re.compile(r"^entity-[a-z0-9]+(?:-[a-z0-9]+)*$")
RELATIONSHIP_ID = re.compile(r"^relationship-[a-z0-9]+(?:-[a-z0-9]+)*$")
KNOWLEDGE_CLAIM_ID = re.compile(r"^claim-[a-z0-9]+(?:-[a-z0-9]+)*$")
HISTORY_ID = re.compile(r"^history-[a-z0-9]+(?:-[a-z0-9]+)*$")
RELATIONSHIP_TYPE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
INTAKE_CLAIM_ID = re.compile(r"^CASE-[A-Z0-9-]+-C\d{3}$")

RELATIONSHIP_FIELDS = {
    "relationship_id",
    "relationship_type",
    "source",
    "target",
    "graph_status",
    "history_coverage",
    "supersedes",
    "superseded_by",
    "provenance",
}
KNOWLEDGE_CLAIM_FIELDS = {
    "claim_id",
    "content_id",
    "truth_kind",
    "authority_level",
    "lifecycle",
    "history_coverage",
    "about",
    "supersedes",
    "superseded_by",
    "provenance",
}
HISTORY_FIELDS = {
    "history_id",
    "sequence",
    "object_id",
    "change_type",
    "transition_sha256",
    "review_claims",
    "summary",
}
GRAPH_STATUSES = {"active", "superseded", "retired"}
CLAIM_LIFECYCLES = GRAPH_STATUSES
HISTORY_COVERAGE_VALUES = {"provenance-only", "prospective", "complete"}
AUTHORITY_LEVELS = {"established", "working", "unresolved", "non-canon"}
TRUTH_KINDS = {
    "objective",
    "in-world-belief",
    "historical-claim",
    "character-knowledge",
    "reader-reveal",
    "design",
    "administrative",
    "proposal",
    "question",
}
HISTORY_CHANGE_TYPES = {
    "graph-registered",
    "established",
    "metadata-changed",
    "moved",
    "claim-added",
    "claim-clarified",
    "relationship-added",
    "superseded",
    "retired",
}
REVIEW_AUTHORITIES = {
    "establish-canon",
    "working-canon",
    "establish-policy",
    "proposal-only",
    "classify",
}
REGISTRY_DIRECTIONS = {"directed", "symmetric"}
REGISTRY_AUTHORITY_EFFECTS = {"navigation-only", "semantic"}
REGISTRY_SELF_LINK_POLICIES = {"allowed", "forbidden"}
REGISTRY_PROVENANCE_POLICIES = {
    "navigation",
    "semantic-canon",
    "semantic-working",
    "administrative",
}
OBJECT_KINDS = {"entity", "relationship", "claim", "history", "intake-claim"}
ENTITY_GRAPH_METADATA_FIELDS = {
    "entity_id",
    "graph_status",
    "history_coverage",
    "supersedes",
    "superseded_by",
}
ENTITY_REGISTRATION_METADATA_FIELDS = {
    "entity_id",
    "graph_status",
    "history_coverage",
    "supersedes",
    "superseded_by",
}


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


def object_kind(object_id: str) -> str:
    if object_id.startswith("entity-"):
        return "entity"
    if object_id.startswith("relationship-"):
        return "relationship"
    if object_id.startswith("claim-"):
        return "claim"
    if object_id.startswith("history-"):
        return "history"
    if INTAKE_CLAIM_ID.fullmatch(object_id):
        return "intake-claim"
    return ""


def string_list(value: object, field: str, errors: list[str]) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        errors.append(f"{field} must be a list")
        return []
    result: list[str] = []
    for item in value:
        if isinstance(item, (dict, list)) or item is None:
            errors.append(f"{field} must contain only scalar values")
            continue
        result.append(scalar_text(item))
    return result


def normalize_provenance(
    value: object, errors: list[str]
) -> dict[str, list[str]]:
    """Normalize legacy review lists and schema-v2 provenance mappings."""
    if isinstance(value, list):
        return {
            "reviews": string_list(value, "provenance", errors),
            "review_claims": [],
        }
    if not isinstance(value, Mapping):
        if value is not None:
            errors.append("provenance must be a review list or mapping")
        return {"reviews": [], "review_claims": []}
    unknown = set(value) - {"reviews", "review_claims"}
    for field in sorted(unknown):
        errors.append(f"unsupported provenance field: {field}")
    return {
        "reviews": string_list(value.get("reviews"), "provenance.reviews", errors),
        "review_claims": string_list(
            value.get("review_claims"), "provenance.review_claims", errors
        ),
    }


def parse_relationships(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    """Parse relationship records from structured YAML front matter."""
    errors: list[str] = []
    try:
        metadata = parse_front_matter_data(path)
    except ValueError as error:
        return [], [str(error)]
    raw = metadata.get("relationships", [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        return [], ["relationships must be a list"]
    relationships: list[dict[str, object]] = []
    for index, value in enumerate(raw, start=1):
        if not isinstance(value, Mapping):
            errors.append(f"relationship entry {index} must be a mapping")
            continue
        unknown = set(value) - RELATIONSHIP_FIELDS
        for field in sorted(unknown):
            errors.append(f"unsupported relationship field: {field}")
        local_errors: list[str] = []
        relationship = {
            "relationship_id": scalar_text(value.get("relationship_id")),
            "relationship_type": scalar_text(value.get("relationship_type")),
            "source": scalar_text(value.get("source")),
            "target": scalar_text(value.get("target")),
            "graph_status": scalar_text(value.get("graph_status")),
            "history_coverage": scalar_text(value.get("history_coverage")),
            "supersedes": string_list(
                value.get("supersedes"), "relationship.supersedes", local_errors
            ),
            "superseded_by": string_list(
                value.get("superseded_by"), "relationship.superseded_by", local_errors
            ),
            "provenance": normalize_provenance(value.get("provenance"), local_errors),
        }
        errors.extend(local_errors)
        relationships.append(relationship)
    return relationships, errors


def parse_knowledge_claims(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    """Parse maintained knowledge claims from structured YAML front matter."""
    errors: list[str] = []
    try:
        metadata = parse_front_matter_data(path)
    except ValueError as error:
        return [], [str(error)]
    raw = metadata.get("claims", [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        return [], ["claims must be a list"]
    claims: list[dict[str, object]] = []
    for index, value in enumerate(raw, start=1):
        if not isinstance(value, Mapping):
            errors.append(f"claim entry {index} must be a mapping")
            continue
        unknown = set(value) - KNOWLEDGE_CLAIM_FIELDS
        for field in sorted(unknown):
            errors.append(f"unsupported knowledge claim field: {field}")
        local_errors: list[str] = []
        claim = {
            "claim_id": scalar_text(value.get("claim_id")),
            "content_id": scalar_text(value.get("content_id")),
            "truth_kind": scalar_text(value.get("truth_kind")),
            "authority_level": scalar_text(value.get("authority_level")),
            "lifecycle": scalar_text(value.get("lifecycle")),
            "history_coverage": scalar_text(value.get("history_coverage")),
            "about": string_list(value.get("about"), "claim.about", local_errors),
            "supersedes": string_list(
                value.get("supersedes"), "claim.supersedes", local_errors
            ),
            "superseded_by": string_list(
                value.get("superseded_by"), "claim.superseded_by", local_errors
            ),
            "provenance": normalize_provenance(value.get("provenance"), local_errors),
        }
        errors.extend(local_errors)
        claims.append(claim)
    return claims, errors


def parse_histories(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    """Parse append-only local history records from YAML front matter."""
    errors: list[str] = []
    try:
        metadata = parse_front_matter_data(path)
    except ValueError as error:
        return [], [str(error)]
    raw = metadata.get("history", [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        return [], ["history must be a list"]
    histories: list[dict[str, object]] = []
    for index, value in enumerate(raw, start=1):
        if not isinstance(value, Mapping):
            errors.append(f"history entry {index} must be a mapping")
            continue
        unknown = set(value) - HISTORY_FIELDS
        for field in sorted(unknown):
            errors.append(f"unsupported history field: {field}")
        local_errors: list[str] = []
        raw_sequence = value.get("sequence")
        try:
            sequence = int(scalar_text(raw_sequence))
        except ValueError:
            errors.append(f"history entry {index} sequence must be an integer")
            sequence = 0
        history = {
            "history_id": scalar_text(value.get("history_id")),
            "sequence": sequence,
            "object_id": scalar_text(value.get("object_id")),
            "change_type": scalar_text(value.get("change_type")),
            "transition_sha256": scalar_text(value.get("transition_sha256")),
            "review_claims": string_list(
                value.get("review_claims"), "history.review_claims", local_errors
            ),
            "summary": scalar_text(value.get("summary")),
        }
        errors.extend(local_errors)
        histories.append(history)
    return histories, errors


def parse_kind_set(value: str) -> set[str]:
    return {item.strip() for item in value.split(",") if item.strip()}


def relationship_type_registry(
    root: Path,
) -> tuple[dict[str, dict[str, object]], list[str]]:
    path = root / "references" / "relationship-types.md"
    errors: list[str] = []
    if not path.is_file():
        return {}, ["references/relationship-types.md: missing relationship type registry"]
    types: dict[str, dict[str, object]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = split_markdown_row(line)
        if len(cells) != 9 or not cells[0].startswith("`"):
            continue
        relationship_type = cells[0].strip("`")
        directionality = cells[1].strip("`")
        authority_effect = cells[2].strip("`")
        source_kinds = parse_kind_set(cells[3].replace("`", ""))
        target_kinds = parse_kind_set(cells[4].replace("`", ""))
        self_link = cells[5].strip("`")
        inverse = cells[6].strip("`")
        provenance_policy = cells[7].strip("`")
        if not RELATIONSHIP_TYPE.fullmatch(relationship_type):
            errors.append(f"references/relationship-types.md: invalid type {relationship_type!r}")
            continue
        if relationship_type in types:
            errors.append(
                f"references/relationship-types.md: duplicate type {relationship_type}"
            )
            continue
        if directionality not in REGISTRY_DIRECTIONS:
            errors.append(
                f"references/relationship-types.md: invalid directionality {directionality!r}"
            )
        if authority_effect not in REGISTRY_AUTHORITY_EFFECTS:
            errors.append(
                f"references/relationship-types.md: invalid authority effect {authority_effect!r}"
            )
        if not source_kinds or not source_kinds <= OBJECT_KINDS:
            errors.append(
                f"references/relationship-types.md: invalid source kinds {sorted(source_kinds)}"
            )
        if not target_kinds or not target_kinds <= OBJECT_KINDS:
            errors.append(
                f"references/relationship-types.md: invalid target kinds {sorted(target_kinds)}"
            )
        if self_link not in REGISTRY_SELF_LINK_POLICIES:
            errors.append(
                f"references/relationship-types.md: invalid self-link policy {self_link!r}"
            )
        if inverse != "none" and not RELATIONSHIP_TYPE.fullmatch(inverse):
            errors.append(
                f"references/relationship-types.md: invalid inverse {inverse!r}"
            )
        if provenance_policy not in REGISTRY_PROVENANCE_POLICIES:
            errors.append(
                "references/relationship-types.md: invalid provenance policy "
                f"{provenance_policy!r}"
            )
        if authority_effect == "semantic" and provenance_policy not in {
            "semantic-canon",
            "semantic-working",
        }:
            errors.append(
                "references/relationship-types.md: semantic relationship "
                f"{relationship_type} requires semantic provenance policy"
            )
        if authority_effect == "navigation-only" and provenance_policy != "navigation":
            errors.append(
                "references/relationship-types.md: navigation-only relationship "
                f"{relationship_type} requires navigation provenance policy"
            )
        definition = cells[8].strip()
        if not definition:
            errors.append(
                f"references/relationship-types.md: {relationship_type} has an empty definition"
            )
        types[relationship_type] = {
            "relationship_type": relationship_type,
            "directionality": directionality,
            "authority_effect": authority_effect,
            "source_kinds": sorted(source_kinds),
            "target_kinds": sorted(target_kinds),
            "self_link": self_link,
            "inverse": inverse,
            "provenance_policy": provenance_policy,
            "definition": definition,
        }
    if not types:
        errors.append("references/relationship-types.md: no controlled types found")
    for relationship_type, record in types.items():
        inverse = str(record["inverse"])
        if inverse != "none" and inverse not in types:
            errors.append(
                f"references/relationship-types.md: {relationship_type} has missing inverse {inverse}"
            )
        if record["directionality"] == "symmetric" and inverse != relationship_type:
            errors.append(
                f"references/relationship-types.md: symmetric {relationship_type} must be its own inverse"
            )
        if record["directionality"] == "symmetric" and (
            record["source_kinds"] != record["target_kinds"]
        ):
            errors.append(
                f"references/relationship-types.md: symmetric {relationship_type} "
                "must permit the same source and target kinds"
            )
        if inverse == "none" or inverse not in types:
            continue
        inverse_record = types[inverse]
        if inverse_record["inverse"] != relationship_type:
            errors.append(
                f"references/relationship-types.md: {relationship_type} inverse is not "
                f"reciprocal from {inverse}"
            )
        if inverse_record["directionality"] != record["directionality"]:
            errors.append(
                f"references/relationship-types.md: {relationship_type} and {inverse} "
                "have incompatible directionality"
            )
        if (
            record["source_kinds"] != inverse_record["target_kinds"]
            or record["target_kinds"] != inverse_record["source_kinds"]
        ):
            errors.append(
                f"references/relationship-types.md: {relationship_type} and {inverse} "
                "have incompatible inverse endpoint kinds"
            )
        if record["authority_effect"] != inverse_record["authority_effect"]:
            errors.append(
                f"references/relationship-types.md: {relationship_type} and {inverse} "
                "have incompatible authority effects"
            )
        if record["provenance_policy"] != inverse_record["provenance_policy"]:
            errors.append(
                f"references/relationship-types.md: {relationship_type} and {inverse} "
                "have incompatible provenance policies"
            )
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


CLAIM_MARKER_LINE = re.compile(
    r"<!-- claim:(claim-[a-z0-9]+(?:-[a-z0-9]+)*):(start|end) -->[ \t]*(?:\n)?"
)
CLAIM_BOUNDARY_LINE = re.compile(
    r"(?m)^<!-- claim:claim-[a-z0-9]+(?:-[a-z0-9]+)*:(?:start|end) -->[ \t]*\n?"
)


def parse_claim_passages(
    metadata: Mapping[str, object], path: Path
) -> tuple[dict[str, str], str, list[str]]:
    """Bind declared maintained claims to non-overlapping exact body passages."""
    body = markdown_body(path)
    errors: list[str] = []
    markers: list[tuple[int, int, str, str]] = []
    offset = 0
    for line_number, line in enumerate(body.splitlines(keepends=True), start=1):
        match = CLAIM_MARKER_LINE.fullmatch(line)
        if "<!-- claim:" in line and match is None:
            errors.append(f"malformed claim boundary on body line {line_number}")
        elif match is not None:
            markers.append((offset, offset + len(line), match.group(1), match.group(2)))
        offset += len(line)

    open_marker: tuple[int, int, str] | None = None
    seen: set[str] = set()
    passages: dict[str, str] = {}
    spans: list[tuple[int, int, str]] = []
    for start, end, claim_id, marker_kind in markers:
        if marker_kind == "start":
            if open_marker is not None:
                errors.append(
                    f"nested claim boundary {claim_id} inside {open_marker[2]}"
                )
                continue
            if claim_id in seen:
                errors.append(f"duplicate claim boundary for {claim_id}")
            open_marker = (start, end, claim_id)
            continue
        if open_marker is None:
            errors.append(f"claim boundary {claim_id} has an end marker before its start")
            continue
        open_start, content_start, open_id = open_marker
        open_marker = None
        if claim_id != open_id:
            errors.append(
                f"claim boundary {open_id} closes with mismatched end marker {claim_id}"
            )
            continue
        content = body[content_start:start].strip("\n")
        if not content.strip():
            errors.append(f"claim boundary {claim_id} has an empty bounded passage")
            continue
        if claim_id in passages:
            errors.append(f"duplicate claim boundary for {claim_id}")
            continue
        seen.add(claim_id)
        passages[claim_id] = content
        spans.append((open_start, end, claim_id))
    if open_marker is not None:
        errors.append(f"claim boundary {open_marker[2]} has no end marker")

    declared: list[str] = []
    raw_claims = metadata.get("claims", [])
    if isinstance(raw_claims, list):
        for value in raw_claims:
            if isinstance(value, Mapping):
                content_id = scalar_text(value.get("content_id"))
                if content_id:
                    declared.append(content_id)
    for claim_id in sorted(set(declared)):
        if claim_id not in passages:
            errors.append(f"declared claim {claim_id} has no matching claim boundary")
    for claim_id in sorted(passages):
        if claim_id not in declared:
            errors.append(f"undeclared claim boundary {claim_id}")
    if len(declared) != len(set(declared)):
        errors.append("duplicate declared claim content_id")

    if errors:
        return passages, body, errors
    residual: list[str] = []
    cursor = 0
    for start, end, claim_id in sorted(spans):
        residual.append(body[cursor:start])
        residual.append(f"<!-- maintained-claim:{claim_id} -->\n")
        cursor = end
    residual.append(body[cursor:])
    return passages, "".join(residual), []


def claim_content(path: Path, content_id: str) -> tuple[str, str | None]:
    """Return a structurally bound maintained-claim passage."""
    try:
        metadata = parse_front_matter_data(path)
    except ValueError as error:
        return "", str(error)
    passages, _, errors = parse_claim_passages(metadata, path)
    if errors:
        relevant = [error for error in errors if content_id in error]
        return "", "; ".join(relevant or errors)
    if content_id not in passages:
        return "", "must have exactly one matching start and end marker"
    return passages[content_id], None


def stable_state_hash(value: object) -> str:
    """Hash a JSON-normalized object state without generated location data."""
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def stable_transition_hash(
    *,
    kind: str,
    object_id: str,
    before_state_sha256: str,
    after_state_sha256: str,
    before_path: str,
    after_path: str,
    actions: list[str],
) -> str:
    """Bind a history event to one complete canonical object transition."""
    return stable_state_hash(
        {
            "transition_schema": 1,
            "kind": kind,
            "object_id": object_id,
            "before_state_sha256": before_state_sha256,
            "after_state_sha256": after_state_sha256,
            "before_path": before_path,
            "after_path": after_path,
            "actions": sorted(actions),
        }
    )


def markdown_body(path: Path) -> str:
    """Return normalized Markdown after YAML front matter."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\n") != "---":
        return text
    for index, line in enumerate(lines[1:], start=1):
        if line.rstrip("\n") == "---":
            return "".join(lines[index + 1 :])
    return text


def entity_state(metadata: Mapping[str, object], path: Path) -> dict[str, object]:
    """Return entity-owned state, excluding nested graph objects and histories."""
    owned_metadata = {
        str(key): value
        for key, value in metadata.items()
        if key not in {"relationships", "claims", "history"}
    }
    _, body, _ = parse_claim_passages(metadata, path)
    return {"metadata": owned_metadata, "body": body}


def entity_state_components(
    metadata: Mapping[str, object], path: Path
) -> tuple[dict[str, object], dict[str, object]]:
    """Separate lore-facing entity state from graph-administrative state."""
    state = entity_state(metadata, path)
    owned_metadata = state["metadata"]
    assert isinstance(owned_metadata, dict)
    content_metadata = {
        key: value
        for key, value in owned_metadata.items()
        if key not in ENTITY_GRAPH_METADATA_FIELDS
    }
    graph_metadata = {
        key: value
        for key, value in owned_metadata.items()
        if key in {"entity_id", "history_coverage"}
    }
    return (
        {"metadata": content_metadata, "body": state["body"]},
        graph_metadata,
    )


def collect_record_readable_snapshots(root: Path) -> dict[str, str]:
    """Hash readable record state so first-time registration cannot hide edits."""
    root = root.resolve()
    snapshots: dict[str, str] = {}
    for directory in GRAPH_RECORD_ROOTS:
        record_root = root / directory
        if not record_root.is_dir():
            continue
        for path in sorted(record_root.rglob("*.md")):
            try:
                metadata = parse_front_matter_data(path)
            except ValueError:
                continue
            if not metadata:
                continue
            content_state, _ = entity_state_components(metadata, path)
            readable_metadata = content_state.get("metadata", {})
            if isinstance(readable_metadata, dict):
                content_state["metadata"] = {
                    key: value
                    for key, value in readable_metadata.items()
                    if key not in ENTITY_REGISTRATION_METADATA_FIELDS
                }
            _, _, claim_errors = parse_claim_passages(metadata, path)
            body = markdown_body(path)
            if not claim_errors:
                body = CLAIM_BOUNDARY_LINE.sub("", body)
            content_state["body"] = body
            snapshots[path.relative_to(root).as_posix()] = stable_state_hash(
                content_state
            )
    return snapshots


def collect_object_snapshots(root: Path) -> dict[str, dict[str, dict[str, object]]]:
    """Collect graph object state without applying current-registry validation."""
    root = root.resolve()
    entities: dict[str, dict[str, object]] = {}
    relationships: dict[str, dict[str, object]] = {}
    claims: dict[str, dict[str, object]] = {}
    histories: dict[str, dict[str, object]] = {}
    for directory in GRAPH_RECORD_ROOTS:
        record_root = root / directory
        if not record_root.is_dir():
            continue
        for path in sorted(record_root.rglob("*.md")):
            try:
                metadata = parse_front_matter_data(path)
            except ValueError:
                continue
            relative = path.relative_to(root).as_posix()
            entity_id = scalar_text(metadata.get("entity_id"))
            if entity_id:
                state = entity_state(metadata, path)
                content_state, graph_metadata = entity_state_components(metadata, path)
                entities[entity_id] = {
                    "entity_id": entity_id,
                    "path": relative,
                    "record_type": scalar_text(metadata.get("type")),
                    "canon_level": scalar_text(metadata.get("canon_level")),
                    "graph_status": scalar_text(metadata.get("graph_status")),
                    "history_coverage": scalar_text(metadata.get("history_coverage")),
                    "supersedes": string_list(
                        metadata.get("supersedes"), "entity.supersedes", []
                    ),
                    "superseded_by": string_list(
                        metadata.get("superseded_by"), "entity.superseded_by", []
                    ),
                    "state_sha256": stable_state_hash(state),
                    "content_state_sha256": stable_state_hash(content_state),
                    "graph_metadata_sha256": stable_state_hash(graph_metadata),
                    "supersession_sha256": stable_state_hash(
                        {
                            "supersedes": string_list(
                                metadata.get("supersedes"), "entity.supersedes", []
                            ),
                            "superseded_by": string_list(
                                metadata.get("superseded_by"),
                                "entity.superseded_by",
                                [],
                            ),
                        }
                    ),
                }
            parsed_relationships, _ = parse_relationships(path)
            for relationship in parsed_relationships:
                relationship_id = str(relationship["relationship_id"])
                if relationship_id:
                    non_lifecycle = {
                        key: value
                        for key, value in relationship.items()
                        if key not in {"graph_status", "supersedes", "superseded_by"}
                    }
                    relationships[relationship_id] = {
                        **relationship,
                        "state_sha256": stable_state_hash(relationship),
                        "non_lifecycle_sha256": stable_state_hash(non_lifecycle),
                        "supersession_sha256": stable_state_hash(
                            {
                                "supersedes": relationship["supersedes"],
                                "superseded_by": relationship["superseded_by"],
                            }
                        ),
                        "authoritative_record": relative,
                    }
            parsed_claims, _ = parse_knowledge_claims(path)
            for claim in parsed_claims:
                claim_id = str(claim["claim_id"])
                if claim_id:
                    content, content_error = claim_content(path, str(claim["content_id"]))
                    content_hash = (
                        ""
                        if content_error
                        else hashlib.sha256(content.encode("utf-8")).hexdigest()
                    )
                    claim_state = {**claim, "content_sha256": content_hash}
                    non_lifecycle_metadata = {
                        key: value
                        for key, value in claim.items()
                        if key not in {"lifecycle", "supersedes", "superseded_by"}
                    }
                    claims[claim_id] = {
                        **claim_state,
                        "state_sha256": stable_state_hash(claim_state),
                        "non_lifecycle_metadata_sha256": stable_state_hash(
                            non_lifecycle_metadata
                        ),
                        "supersession_sha256": stable_state_hash(
                            {
                                "supersedes": claim["supersedes"],
                                "superseded_by": claim["superseded_by"],
                            }
                        ),
                        "authoritative_record": relative,
                    }
            parsed_histories, _ = parse_histories(path)
            for history in parsed_histories:
                history_id = str(history["history_id"])
                if history_id:
                    histories[history_id] = {
                        **history,
                        "authoritative_record": relative,
                    }
    return {
        "entities": entities,
        "relationships": relationships,
        "claims": claims,
        "histories": histories,
    }


def build_review_objects(
    root: Path, errors: list[str]
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    """Build submission, review, and immutable intake-claim projections."""
    submissions: list[dict[str, object]] = []
    for path in sorted((root / "intake" / "submissions").glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            metadata = parse_front_matter_data(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(root).as_posix()}: {error}")
            continue
        submission_id = scalar_text(metadata.get("submission_id"))
        if submission_id:
            submissions.append(
                {
                    "submission_id": submission_id,
                    "case_id": scalar_text(metadata.get("case_id")),
                    "record_type": scalar_text(metadata.get("type")),
                    "authority": scalar_text(metadata.get("authority")),
                    "path": path.relative_to(root).as_posix(),
                }
            )

    reviews: list[dict[str, object]] = []
    for path in sorted((root / "development" / "intake-reviews").glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            metadata = parse_front_matter_data(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(root).as_posix()}: {error}")
            continue
        reviews.append(
            {
                "submission_id": scalar_text(metadata.get("submission_id")),
                "case_id": scalar_text(metadata.get("case_id")),
                "status": scalar_text(metadata.get("status")),
                "authority": scalar_text(metadata.get("authority")),
                "path": path.relative_to(root).as_posix(),
            }
        )

    try:
        intake_claims = list(build_claim_index_data(root)["claims"])
    except ValueError as error:
        errors.append(f"claim index: {error}")
        intake_claims = []
    submissions.sort(key=lambda item: str(item["submission_id"]))
    reviews.sort(key=lambda item: (str(item["submission_id"]), str(item["path"])))
    return submissions, reviews, intake_claims


def build_development_objects(
    root: Path, intake_claims: list[dict[str, object]], errors: list[str]
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, str]]]:
    """Project decisions, exception records, and review-owned evidence references."""

    def records(directory: str, expected_types: set[str]) -> list[dict[str, object]]:
        projected: list[dict[str, object]] = []
        record_root = root / "development" / directory
        if not record_root.is_dir():
            return projected
        for path in sorted(record_root.glob("*.md")):
            if path.name == "README.md":
                continue
            try:
                metadata = parse_front_matter_data(path)
            except ValueError as error:
                errors.append(f"{path.relative_to(root).as_posix()}: {error}")
                continue
            record_type = scalar_text(metadata.get("type"))
            if record_type not in expected_types:
                errors.append(
                    f"{path.relative_to(root).as_posix()}: invalid projected record type "
                    f"{record_type!r}"
                )
            related_errors: list[str] = []
            projected.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "record_type": record_type,
                    "title": scalar_text(metadata.get("title")),
                    "status": scalar_text(metadata.get("status")),
                    "related": string_list(
                        metadata.get("related"), "related", related_errors
                    ),
                }
            )
            errors.extend(
                f"{path.relative_to(root).as_posix()}: {error}"
                for error in related_errors
            )
        return projected

    decisions = records("decisions", {"decision"})
    exceptions: list[dict[str, object]] = []
    for directory, expected in (
        ("open-questions", {"open-question"}),
        ("contradictions", {"contradiction"}),
        ("proposals", {"proposal"}),
        ("retired", {"retired"}),
    ):
        exceptions.extend(records(directory, expected))
    exceptions.sort(key=lambda item: str(item["path"]))

    evidence_references = [
        {
            "claim_id": str(claim["claim_id"]),
            "review": str(claim["review"]),
            "evidence": str(claim["existing_authority_or_evidence"]),
        }
        for claim in intake_claims
        if str(claim.get("existing_authority_or_evidence", "")).strip()
    ]
    evidence_references.sort(key=lambda item: item["claim_id"])
    return decisions, exceptions, evidence_references


def validate_review_provenance(
    *,
    root: Path,
    owner: Path,
    label: str,
    provenance: dict[str, list[str]],
    reviews_by_path: dict[Path, dict[str, object]],
    intake_claims_by_id: dict[str, dict[str, object]],
    errors: list[str],
    require_review_claims: bool,
    object_id: str,
    allowed_authorities: set[str],
    allowed_dispositions: set[str],
) -> None:
    reviews = provenance["reviews"]
    review_claims = provenance["review_claims"]
    if not reviews:
        errors.append(f"{label} has no provenance reviews")
    resolved_reviews: set[Path] = set()
    for pointer in reviews:
        resolved = resolve_repository_pointer(root, owner, pointer)
        if resolved is None or resolved not in reviews_by_path:
            errors.append(f"{label} has invalid provenance review {pointer!r}")
            continue
        resolved_reviews.add(resolved)
        review = reviews_by_path[resolved]
        if review["status"] != "complete":
            errors.append(f"{label} cites incomplete provenance review {pointer!r}")
        if review["authority"] not in REVIEW_AUTHORITIES:
            errors.append(f"{label} cites review with invalid authority {pointer!r}")
    if require_review_claims and not review_claims:
        errors.append(f"{label} has no exact review-claim provenance")
    for claim_id in review_claims:
        if not INTAKE_CLAIM_ID.fullmatch(claim_id):
            errors.append(f"{label} has malformed review claim {claim_id!r}")
            continue
        claim = intake_claims_by_id.get(claim_id)
        if claim is None:
            errors.append(f"{label} cites missing review claim {claim_id}")
            continue
        review_path = (root / str(claim["review"])).resolve()
        if review_path not in resolved_reviews:
            errors.append(
                f"{label} review claim {claim_id} is not owned by a listed provenance review"
            )
        review = reviews_by_path.get(review_path)
        if review and review["status"] != "complete":
            errors.append(f"{label} cites review claim {claim_id} from an incomplete review")
        if not require_review_claims:
            continue
        review_authority = str(claim.get("review_authority", ""))
        if review_authority not in allowed_authorities:
            errors.append(
                f"{label} review claim {claim_id} has unauthorized review authority "
                f"{review_authority!r}"
            )
        disposition = str(claim.get("disposition", ""))
        if disposition not in allowed_dispositions:
            errors.append(
                f"{label} review claim {claim_id} has non-authorizing disposition "
                f"{disposition!r}"
            )
        if not target_names_object(claim.get("target", ""), object_id):
            errors.append(
                f"{label} review claim {claim_id} target does not name {object_id}"
            )


def relationship_provenance_authorities(policy: str) -> set[str]:
    return {
        "navigation": {"establish-policy", "establish-canon", "working-canon"},
        "semantic-canon": {"establish-canon"},
        "semantic-working": {"establish-canon", "working-canon"},
        "administrative": {"establish-policy"},
    }.get(policy, set())


def entity_content_authorities(entity: Mapping[str, object]) -> set[str]:
    """Return authorities permitted to change an entity's readable content."""
    path = str(entity.get("path", ""))
    canon_level = str(entity.get("canon_level", ""))
    if path.startswith("canon/") or path.startswith("story/"):
        if canon_level == "established":
            return {"establish-canon"}
        return {"establish-canon", "working-canon"}
    if path.startswith("design/"):
        return {"establish-policy", "proposal-only", "classify"}
    return {"establish-policy"}


def claim_provenance_authorities(claim: Mapping[str, object]) -> set[str]:
    truth_kind = str(claim.get("truth_kind", ""))
    authority_level = str(claim.get("authority_level", ""))
    if truth_kind in {"design", "administrative"}:
        return {"establish-policy"}
    if truth_kind in {"proposal", "question"}:
        return {"proposal-only", "classify", "establish-policy"}
    if authority_level == "established":
        return {"establish-canon"}
    if authority_level == "working":
        return {"establish-canon", "working-canon"}
    return {"establish-canon", "working-canon", "classify"}


def claim_provenance_dispositions(claim: Mapping[str, object]) -> set[str]:
    lifecycle = str(claim.get("lifecycle", ""))
    if str(claim.get("truth_kind", "")) in {"proposal", "question"}:
        allowed = {"create", "update", "defer"}
    else:
        allowed = {"create", "update"}
    if lifecycle in {"superseded", "retired"}:
        allowed.add("retire")
    return allowed


def relationship_provenance_dispositions(
    relationship: Mapping[str, object], policy: str
) -> set[str]:
    allowed = {"create", "update"}
    if policy == "navigation":
        allowed.add("link-only")
    if str(relationship.get("graph_status", "")) in {"superseded", "retired"}:
        allowed.add("retire")
    return allowed


def history_dispositions(
    change_type: str,
    *,
    object_kind_name: str,
    proposal_or_question: bool = False,
    navigation_relationship: bool = False,
) -> set[str]:
    """Return review dispositions that authorize a specific event action."""
    if change_type == "graph-registered":
        allowed = {"create", "update"}
        if object_kind_name == "relationship" and navigation_relationship:
            allowed.add("link-only")
        return allowed
    if change_type == "established":
        return {"create"}
    if change_type in {"metadata-changed", "moved", "claim-clarified"}:
        allowed = {"update"}
        if proposal_or_question and change_type == "claim-clarified":
            allowed.add("defer")
        return allowed
    if change_type == "claim-added":
        return {"create", "defer"} if proposal_or_question else {"create"}
    if change_type == "relationship-added":
        return (
            {"create", "link-only"}
            if navigation_relationship
            else {"create"}
        )
    if change_type == "superseded":
        return {"update", "retire"}
    if change_type == "retired":
        return {"retire"}
    return set()


def target_names_object(target: object, object_id: str) -> bool:
    return bool(
        re.search(
            rf"(?<![A-Za-z0-9-]){re.escape(object_id)}(?![A-Za-z0-9-])",
            str(target),
        )
    )


def build_graph_data(root: Path) -> dict[str, object]:
    """Build unified knowledge-object navigation data or raise all errors."""
    root = root.resolve()
    relationship_types, errors = relationship_type_registry(root)
    submissions, reviews, intake_claims = build_review_objects(root, errors)
    decisions, exceptions, evidence_references = build_development_objects(
        root, intake_claims, errors
    )
    reviews_by_path = {
        (root / str(review["path"])).resolve(): review for review in reviews
    }
    intake_claims_by_id = {
        str(claim["claim_id"]): claim for claim in intake_claims
    }

    entities: list[dict[str, object]] = []
    relationships: list[dict[str, object]] = []
    knowledge_claims: list[dict[str, object]] = []
    histories: list[dict[str, object]] = []
    entity_sources: dict[str, Path] = {}
    relationship_sources: dict[str, Path] = {}
    claim_sources: dict[str, Path] = {}
    history_sources: dict[str, Path] = {}
    path_to_entity: dict[Path, str] = {}
    entity_related: list[tuple[Path, str, list[str]]] = []

    paths: list[Path] = []
    for directory in GRAPH_RECORD_ROOTS:
        record_root = root / directory
        if record_root.is_dir():
            paths.extend(record_root.rglob("*.md"))

    for path in sorted(set(paths)):
        relative = path.relative_to(root).as_posix()
        try:
            metadata = parse_front_matter_data(path)
        except ValueError as error:
            errors.append(f"{relative}: {error}")
            continue
        parsed_relationships, relationship_errors = parse_relationships(path)
        parsed_claims, claim_errors = parse_knowledge_claims(path)
        parsed_histories, history_errors = parse_histories(path)
        boundary_errors: list[str] = []
        if scalar_text(metadata.get("entity_id")) or "claims" in metadata:
            _, _, boundary_errors = parse_claim_passages(metadata, path)
        errors.extend(f"{relative}: {error}" for error in relationship_errors)
        errors.extend(f"{relative}: {error}" for error in claim_errors)
        errors.extend(f"{relative}: {error}" for error in history_errors)
        errors.extend(f"{relative}: {error}" for error in boundary_errors)

        entity_id = scalar_text(metadata.get("entity_id"))
        if entity_id:
            if not ENTITY_ID.fullmatch(entity_id):
                errors.append(f"{relative}: invalid entity_id {entity_id!r}")
            elif entity_id in entity_sources:
                errors.append(
                    f"{relative}: duplicate entity_id {entity_id}; first used by "
                    f"{entity_sources[entity_id].relative_to(root).as_posix()}"
                )
            else:
                entity_sources[entity_id] = path
                path_to_entity[path.resolve()] = entity_id
                graph_status = scalar_text(metadata.get("graph_status"))
                if graph_status and graph_status not in GRAPH_STATUSES:
                    errors.append(f"{relative}: invalid graph_status {graph_status!r}")
                history_coverage = scalar_text(metadata.get("history_coverage"))
                if graph_status and history_coverage not in HISTORY_COVERAGE_VALUES:
                    errors.append(
                        f"{relative}: schema-v2 entity has invalid history_coverage "
                        f"{history_coverage!r}"
                    )
                if graph_status:
                    for field in ("claims", "history", "supersedes", "superseded_by"):
                        if field not in metadata:
                            errors.append(
                                f"{relative}: schema-v2 entity lacks {field} field"
                            )
                aliases = string_list(metadata.get("aliases", []), "aliases", errors)
                related = string_list(metadata.get("related", []), "related", errors)
                provenance = string_list(
                    metadata.get("provenance", []), "provenance", errors
                )
                supersedes = string_list(
                    metadata.get("supersedes"), "entity.supersedes", errors
                )
                superseded_by = string_list(
                    metadata.get("superseded_by"), "entity.superseded_by", errors
                )
                entities.append(
                    {
                        "entity_id": entity_id,
                        "path": relative,
                        "title": scalar_text(metadata.get("title")),
                        "record_type": scalar_text(metadata.get("type")),
                        "status": scalar_text(metadata.get("status")),
                        "canon_level": scalar_text(metadata.get("canon_level")),
                        "graph_status": graph_status,
                        "history_coverage": history_coverage,
                        "supersedes": supersedes,
                        "superseded_by": superseded_by,
                        "aliases": aliases,
                        "provenance": provenance,
                    }
                )
                entity_related.append((path, entity_id, related))

        for relationship in parsed_relationships:
            relationship_id = str(relationship["relationship_id"])
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
            relationships.append({**relationship, "authoritative_record": relative})

        for claim in parsed_claims:
            claim_id = str(claim["claim_id"])
            if not KNOWLEDGE_CLAIM_ID.fullmatch(claim_id):
                errors.append(f"{relative}: invalid knowledge claim_id {claim_id!r}")
                continue
            if claim_id in claim_sources:
                errors.append(
                    f"{relative}: duplicate knowledge claim_id {claim_id}; first used by "
                    f"{claim_sources[claim_id].relative_to(root).as_posix()}"
                )
                continue
            claim_sources[claim_id] = path
            content, content_error = claim_content(path, str(claim["content_id"]))
            if content_error:
                errors.append(f"{relative}: claim {claim_id} {content_error}")
                content_hash = ""
            else:
                content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
            knowledge_claims.append(
                {
                    **claim,
                    "content_sha256": content_hash,
                    "authoritative_record": relative,
                }
            )

        for history in parsed_histories:
            history_id = str(history["history_id"])
            if not HISTORY_ID.fullmatch(history_id):
                errors.append(f"{relative}: invalid history_id {history_id!r}")
                continue
            if history_id in history_sources:
                errors.append(
                    f"{relative}: duplicate history_id {history_id}; first used by "
                    f"{history_sources[history_id].relative_to(root).as_posix()}"
                )
                continue
            history_sources[history_id] = path
            histories.append({**history, "authoritative_record": relative})

    intake_claim_sources = {
        claim_id: root / str(claim["review"])
        for claim_id, claim in intake_claims_by_id.items()
    }
    known_endpoints = (
        set(entity_sources)
        | set(relationship_sources)
        | set(claim_sources)
        | set(history_sources)
        | set(intake_claim_sources)
    )
    known_sources = {
        **entity_sources,
        **relationship_sources,
        **claim_sources,
        **history_sources,
        **intake_claim_sources,
    }

    symmetric_pairs: dict[tuple[str, frozenset[str]], str] = {}
    for relationship in relationships:
        relationship_id = str(relationship["relationship_id"])
        owner = relationship_sources[relationship_id]
        relative = owner.relative_to(root).as_posix()
        label = f"{relative}: relationship {relationship_id}"
        relationship_type = str(relationship["relationship_type"])
        registry = relationship_types.get(relationship_type)
        if registry is None:
            errors.append(f"{label} uses uncontrolled type {relationship_type!r}")
        source = str(relationship["source"])
        target = str(relationship["target"])
        for endpoint_name, endpoint in (("source", source), ("target", target)):
            if endpoint not in known_endpoints:
                errors.append(f"{label} has unresolved {endpoint_name} {endpoint!r}")
        if registry is not None:
            source_kind = object_kind(source)
            target_kind = object_kind(target)
            if source_kind not in registry["source_kinds"]:
                errors.append(f"{label} disallows source kind {source_kind!r}")
            if target_kind not in registry["target_kinds"]:
                errors.append(f"{label} disallows target kind {target_kind!r}")
            if source == target and registry["self_link"] == "forbidden":
                errors.append(f"{label} is a forbidden self-link")
            source_owner = known_sources.get(source)
            target_owner = known_sources.get(target)
            if registry["directionality"] == "directed":
                if source_owner is not None and owner.resolve() != source_owner.resolve():
                    errors.append(
                        f"{label} is not stored on its source object's authoritative record"
                    )
            elif (
                source_owner is not None
                and target_owner is not None
                and owner.resolve()
                not in {source_owner.resolve(), target_owner.resolve()}
            ):
                errors.append(
                    f"{label} is not stored on a symmetric endpoint's authoritative record"
                )
            if registry["directionality"] == "symmetric":
                key = (relationship_type, frozenset((source, target)))
                prior = symmetric_pairs.get(key)
                if prior:
                    errors.append(f"{label} duplicates symmetric pair owned by {prior}")
                else:
                    symmetric_pairs[key] = relationship_id
        graph_status = str(relationship["graph_status"])
        if graph_status and graph_status not in GRAPH_STATUSES:
            errors.append(f"{label} has invalid graph_status {graph_status!r}")
        if graph_status and relationship["history_coverage"] not in HISTORY_COVERAGE_VALUES:
            errors.append(
                f"{label} has invalid history_coverage {relationship['history_coverage']!r}"
            )
        validate_review_provenance(
            root=root,
            owner=owner,
            label=label,
            provenance=relationship["provenance"],
            reviews_by_path=reviews_by_path,
            intake_claims_by_id=intake_claims_by_id,
            errors=errors,
            require_review_claims=bool(graph_status),
            object_id=relationship_id,
            allowed_authorities=relationship_provenance_authorities(
                str(registry["provenance_policy"]) if registry else ""
            ),
            allowed_dispositions=relationship_provenance_dispositions(
                relationship,
                str(registry["provenance_policy"]) if registry else "",
            ),
        )

    for claim in knowledge_claims:
        claim_id = str(claim["claim_id"])
        owner = claim_sources[claim_id]
        relative = owner.relative_to(root).as_posix()
        label = f"{relative}: claim {claim_id}"
        if str(claim["content_id"]) != claim_id:
            errors.append(f"{label} content_id must equal claim_id")
        if claim["truth_kind"] not in TRUTH_KINDS:
            errors.append(f"{label} has invalid truth_kind {claim['truth_kind']!r}")
        if claim["authority_level"] not in AUTHORITY_LEVELS:
            errors.append(
                f"{label} has invalid authority_level {claim['authority_level']!r}"
            )
        if claim["lifecycle"] not in CLAIM_LIFECYCLES:
            errors.append(f"{label} has invalid lifecycle {claim['lifecycle']!r}")
        if claim["history_coverage"] not in HISTORY_COVERAGE_VALUES:
            errors.append(
                f"{label} has invalid history_coverage {claim['history_coverage']!r}"
            )
        if not claim["about"]:
            errors.append(f"{label} has no about objects")
        for about in claim["about"]:
            if about not in known_endpoints:
                errors.append(f"{label} has unresolved about object {about!r}")
        validate_review_provenance(
            root=root,
            owner=owner,
            label=label,
            provenance=claim["provenance"],
            reviews_by_path=reviews_by_path,
            intake_claims_by_id=intake_claims_by_id,
            errors=errors,
            require_review_claims=True,
            object_id=claim_id,
            allowed_authorities=claim_provenance_authorities(claim),
            allowed_dispositions=claim_provenance_dispositions(claim),
        )

    knowledge_claims_by_id = {
        str(item["claim_id"]): item for item in knowledge_claims
    }
    entities_by_id = {str(item["entity_id"]): item for item in entities}
    relationships_by_id = {
        str(item["relationship_id"]): item for item in relationships
    }
    history_by_object: dict[str, list[dict[str, object]]] = {}
    for history in histories:
        history_id = str(history["history_id"])
        owner = history_sources[history_id]
        relative = owner.relative_to(root).as_posix()
        label = f"{relative}: history {history_id}"
        object_id = str(history["object_id"])
        if object_id not in known_sources:
            errors.append(f"{label} has unresolved object_id {object_id!r}")
        elif known_sources[object_id].resolve() != owner.resolve():
            errors.append(f"{label} is not stored on its object's authoritative record")
        if history["change_type"] not in HISTORY_CHANGE_TYPES:
            errors.append(f"{label} has invalid change_type {history['change_type']!r}")
        transition_sha256 = str(history["transition_sha256"])
        if transition_sha256 and not re.fullmatch(r"[0-9a-f]{64}", transition_sha256):
            errors.append(f"{label} has invalid transition_sha256")
        if not str(history["summary"]).strip():
            errors.append(f"{label} has an empty summary")
        review_claims = history["review_claims"]
        if not review_claims:
            errors.append(f"{label} has no review claims")
        for review_claim in review_claims:
            claim = intake_claims_by_id.get(review_claim)
            if claim is None:
                errors.append(f"{label} cites missing review claim {review_claim}")
                continue
            review_path = (root / str(claim["review"])).resolve()
            review = reviews_by_path.get(review_path)
            if review and review["status"] != "complete":
                errors.append(f"{label} cites review claim from an incomplete review")
            review_authority = str(claim.get("review_authority", ""))
            object_kind_name = object_kind(object_id)
            maintained_claim = knowledge_claims_by_id.get(object_id)
            proposal_or_question = bool(
                maintained_claim
                and maintained_claim["truth_kind"] in {"proposal", "question"}
            )
            if history["change_type"] == "moved":
                allowed_history_authorities = {
                    "establish-policy",
                    "establish-canon",
                    "working-canon",
                }
                navigation_relationship = False
            elif object_kind_name == "relationship":
                relationship = relationships_by_id.get(object_id, {})
                registry = relationship_types.get(
                    str(relationship.get("relationship_type", "")), {}
                )
                allowed_history_authorities = relationship_provenance_authorities(
                    str(registry.get("provenance_policy", ""))
                )
                navigation_relationship = (
                    str(registry.get("provenance_policy", "")) == "navigation"
                )
            elif object_kind_name == "claim" and maintained_claim:
                allowed_history_authorities = claim_provenance_authorities(
                    maintained_claim
                )
                navigation_relationship = False
            elif object_kind_name == "entity":
                entity = entities_by_id.get(object_id, {})
                if history["change_type"] in {"graph-registered", "moved"}:
                    allowed_history_authorities = {
                        "establish-policy",
                        "establish-canon",
                        "working-canon",
                    }
                elif history["change_type"] == "metadata-changed":
                    allowed_history_authorities = entity_content_authorities(entity) | {
                        "establish-policy"
                    }
                else:
                    allowed_history_authorities = entity_content_authorities(entity)
                navigation_relationship = False
            else:
                allowed_history_authorities = {"establish-policy"}
                navigation_relationship = False
            if review_authority not in allowed_history_authorities:
                errors.append(
                    f"{label} cites review claim with unauthorized authority "
                    f"{review_authority!r}; expected one of "
                    f"{sorted(allowed_history_authorities)}"
                )
            disposition = str(claim.get("disposition", ""))
            allowed_history_dispositions = history_dispositions(
                str(history["change_type"]),
                object_kind_name=object_kind_name,
                proposal_or_question=proposal_or_question,
                navigation_relationship=navigation_relationship,
            )
            if disposition not in allowed_history_dispositions:
                errors.append(
                    f"{label} cites disposition {disposition!r} incompatible with "
                    f"{history['change_type']!r}; expected one of "
                    f"{sorted(allowed_history_dispositions)}"
                )
            if not target_names_object(claim.get("target", ""), object_id):
                errors.append(
                    f"{label} review claim {review_claim} target does not name "
                    f"{object_id}"
                )
        history_by_object.setdefault(object_id, []).append(history)

    for object_id, object_histories in history_by_object.items():
        sequences = sorted(int(item["sequence"]) for item in object_histories)
        expected = list(range(1, len(sequences) + 1))
        if sequences != expected:
            errors.append(
                f"{known_sources.get(object_id, root).relative_to(root).as_posix()}: "
                f"history for {object_id} has non-contiguous sequences {sequences}"
            )

    for entity in entities:
        entity_id = str(entity["entity_id"])
        if entity["graph_status"] and entity_id not in history_by_object:
            errors.append(f"{entity['path']}: schema-v2 entity {entity_id} has no local history")
    for relationship in relationships:
        relationship_id = str(relationship["relationship_id"])
        if relationship["graph_status"] and relationship_id not in history_by_object:
            errors.append(
                f"{relationship['authoritative_record']}: schema-v2 relationship "
                f"{relationship_id} has no local history"
            )
    for claim in knowledge_claims:
        claim_id = str(claim["claim_id"])
        if claim_id not in history_by_object:
            errors.append(
                f"{claim['authoritative_record']}: maintained claim {claim_id} has no local history"
            )

    lifecycle_collections = (
        (entities, "entity_id", "graph_status"),
        (relationships, "relationship_id", "graph_status"),
        (knowledge_claims, "claim_id", "lifecycle"),
    )
    for collection, id_field, lifecycle_field in lifecycle_collections:
        by_id = {str(item[id_field]): item for item in collection}
        supersession_edges: dict[str, list[str]] = {}
        for object_id, item in by_id.items():
            lifecycle = str(item.get(lifecycle_field, ""))
            supersedes = list(item["supersedes"])
            superseded_by = list(item["superseded_by"])
            supersession_edges[object_id] = supersedes
            if len(supersedes) != len(set(supersedes)):
                errors.append(f"{object_id} contains duplicate supersedes links")
            if len(superseded_by) != len(set(superseded_by)):
                errors.append(f"{object_id} contains duplicate superseded_by links")
            if object_id in supersedes or object_id in superseded_by:
                errors.append(f"{object_id} cannot supersede itself")
            if lifecycle in {"active", "retired"} and superseded_by:
                errors.append(
                    f"{object_id} is {lifecycle} but has superseded_by replacements"
                )
            if lifecycle == "superseded" and not superseded_by:
                errors.append(f"{object_id} is superseded without a replacement")
            for earlier in supersedes:
                if earlier not in by_id:
                    errors.append(f"{object_id} supersedes missing object {earlier}")
                    continue
                if object_id not in by_id[earlier]["superseded_by"]:
                    errors.append(f"{object_id} supersession lacks reverse link from {earlier}")
                earlier_lifecycle = str(by_id[earlier].get(lifecycle_field, ""))
                if earlier_lifecycle and earlier_lifecycle != "superseded":
                    errors.append(
                        f"{object_id} supersedes {earlier} but its lifecycle is "
                        f"{earlier_lifecycle!r}"
                    )
            for later in superseded_by:
                if later not in by_id:
                    errors.append(f"{object_id} has missing superseded_by object {later}")
                    continue
                if object_id not in by_id[later]["supersedes"]:
                    errors.append(f"{object_id} superseded_by lacks reverse link from {later}")
                later_lifecycle = str(by_id[later].get(lifecycle_field, ""))
                if later_lifecycle == "retired":
                    errors.append(f"{object_id} has retired replacement {later}")

        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(object_id: str) -> None:
            if object_id in visiting:
                errors.append(f"{object_id} participates in a supersession cycle")
                return
            if object_id in visited:
                return
            visiting.add(object_id)
            for earlier in supersession_edges.get(object_id, []):
                if earlier in by_id:
                    visit(earlier)
            visiting.remove(object_id)
            visited.add(object_id)

        for object_id in sorted(by_id):
            visit(object_id)

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
        raise GraphValidationError(sorted(set(errors)))

    entities.sort(key=lambda item: str(item["entity_id"]))
    relationships.sort(key=lambda item: str(item["relationship_id"]))
    knowledge_claims.sort(key=lambda item: str(item["claim_id"]))
    histories.sort(key=lambda item: str(item["history_id"]))
    unmigrated.sort(key=lambda item: (item["source_entity_id"], item["legacy_target"]))
    referenced_intake_claims = {
        claim_id
        for claim in knowledge_claims
        for claim_id in claim["provenance"]["review_claims"]
    }
    return {
        "schema_version": 2,
        "authority": "navigation-only",
        "generated_from": "Markdown records with explicit knowledge-object metadata",
        "relationship_types": [
            relationship_types[key] for key in sorted(relationship_types)
        ],
        "entities": entities,
        "relationships": relationships,
        "knowledge_claims": knowledge_claims,
        "histories": histories,
        "submissions": submissions,
        "reviews": reviews,
        "intake_claims": intake_claims,
        "decisions": decisions,
        "exceptions": exceptions,
        "evidence_references": evidence_references,
        "migration_inventory": {
            "entities_without_graph_status": sorted(
                str(item["entity_id"]) for item in entities if not item["graph_status"]
            ),
            "entities_without_history": sorted(
                str(item["entity_id"])
                for item in entities
                if str(item["entity_id"]) not in history_by_object
            ),
            "entities_without_history_coverage": sorted(
                str(item["entity_id"])
                for item in entities
                if not item["history_coverage"]
            ),
            "relationships_without_graph_status": sorted(
                str(item["relationship_id"])
                for item in relationships
                if not item["graph_status"]
            ),
            "relationships_without_history": sorted(
                str(item["relationship_id"])
                for item in relationships
                if str(item["relationship_id"]) not in history_by_object
            ),
            "relationships_without_history_coverage": sorted(
                str(item["relationship_id"])
                for item in relationships
                if not item["history_coverage"]
            ),
            "relationships_without_review_claim_provenance": sorted(
                str(item["relationship_id"])
                for item in relationships
                if not item["provenance"]["review_claims"]
            ),
            "knowledge_claims_without_history": sorted(
                str(item["claim_id"])
                for item in knowledge_claims
                if str(item["claim_id"]) not in history_by_object
            ),
            "knowledge_claims_without_history_coverage": sorted(
                str(item["claim_id"])
                for item in knowledge_claims
                if not item["history_coverage"]
            ),
            "intake_claims_without_knowledge_claim_reference": sorted(
                str(item["claim_id"])
                for item in intake_claims
                if str(item["claim_id"]) not in referenced_intake_claims
            ),
        },
        "unmigrated_related_links": unmigrated,
    }
