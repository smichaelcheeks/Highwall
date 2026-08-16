#!/usr/bin/env python3
"""Parse and validate Highwall's Markdown-first knowledge-object graph."""

from __future__ import annotations

import hashlib
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
OBJECT_KINDS = {"entity", "relationship", "claim"}


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
        if len(cells) != 8 or not cells[0].startswith("`"):
            continue
        relationship_type = cells[0].strip("`")
        directionality = cells[1].strip("`")
        authority_effect = cells[2].strip("`")
        source_kinds = parse_kind_set(cells[3].replace("`", ""))
        target_kinds = parse_kind_set(cells[4].replace("`", ""))
        self_link = cells[5].strip("`")
        inverse = cells[6].strip("`")
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
        types[relationship_type] = {
            "relationship_type": relationship_type,
            "directionality": directionality,
            "authority_effect": authority_effect,
            "source_kinds": sorted(source_kinds),
            "target_kinds": sorted(target_kinds),
            "self_link": self_link,
            "inverse": inverse,
            "definition": cells[7],
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


def claim_content(path: Path, content_id: str) -> tuple[str, str | None]:
    """Return normalized bounded claim content and an error, if any."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    start = f"<!-- claim:{content_id}:start -->"
    end = f"<!-- claim:{content_id}:end -->"
    if text.count(start) != 1 or text.count(end) != 1:
        return "", "must have exactly one matching start and end marker"
    start_index = text.index(start) + len(start)
    end_index = text.index(end)
    if end_index <= start_index:
        return "", "has an end marker before its start marker"
    content = text[start_index:end_index].strip("\n")
    if not content.strip():
        return "", "has an empty bounded passage"
    return content, None


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
                entities[entity_id] = {
                    "entity_id": entity_id,
                    "path": relative,
                    "graph_status": scalar_text(metadata.get("graph_status")),
                    "history_coverage": scalar_text(metadata.get("history_coverage")),
                }
            parsed_relationships, _ = parse_relationships(path)
            for relationship in parsed_relationships:
                relationship_id = str(relationship["relationship_id"])
                if relationship_id:
                    relationships[relationship_id] = {
                        **relationship,
                        "authoritative_record": relative,
                    }
            parsed_claims, _ = parse_knowledge_claims(path)
            for claim in parsed_claims:
                claim_id = str(claim["claim_id"])
                if claim_id:
                    claims[claim_id] = {**claim, "authoritative_record": relative}
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


def build_graph_data(root: Path) -> dict[str, object]:
    """Build unified knowledge-object navigation data or raise all errors."""
    root = root.resolve()
    relationship_types, errors = relationship_type_registry(root)
    submissions, reviews, intake_claims = build_review_objects(root, errors)
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
        errors.extend(f"{relative}: {error}" for error in relationship_errors)
        errors.extend(f"{relative}: {error}" for error in claim_errors)
        errors.extend(f"{relative}: {error}" for error in history_errors)

        entity_id = scalar_text(metadata.get("entity_id"))
        if not entity_id:
            if parsed_relationships or parsed_claims or parsed_histories:
                errors.append(f"{relative}: knowledge metadata requires entity_id")
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
        graph_status = scalar_text(metadata.get("graph_status"))
        if graph_status and graph_status not in GRAPH_STATUSES:
            errors.append(f"{relative}: invalid graph_status {graph_status!r}")
        history_coverage = scalar_text(metadata.get("history_coverage"))
        if graph_status and history_coverage not in HISTORY_COVERAGE_VALUES:
            errors.append(
                f"{relative}: schema-v2 entity has invalid history_coverage "
                f"{history_coverage!r}"
            )
        aliases = string_list(metadata.get("aliases", []), "aliases", errors)
        related = string_list(metadata.get("related", []), "related", errors)
        provenance = string_list(metadata.get("provenance", []), "provenance", errors)
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

    known_endpoints = set(entity_sources) | set(relationship_sources) | set(claim_sources)
    known_sources = {**entity_sources, **relationship_sources, **claim_sources}

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
            owner_entity = path_to_entity.get(owner.resolve())
            if registry["directionality"] == "directed":
                if owner_entity and owner_entity != source:
                    errors.append(f"{label} owner entity does not match source")
            elif owner_entity and owner_entity not in {source, target}:
                errors.append(f"{label} owner entity is not a symmetric endpoint")
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
        )

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
        history_by_object.setdefault(object_id, []).append(history)

    for object_id, object_histories in history_by_object.items():
        sequences = sorted(int(item["sequence"]) for item in object_histories)
        expected = list(range(1, len(sequences) + 1))
        if sequences != expected:
            errors.append(
                f"{known_sources.get(object_id, root).relative_to(root).as_posix()}: "
                f"history for {object_id} has non-contiguous sequences {sequences}"
            )

    for collection in (relationships, knowledge_claims):
        by_id = {
            str(item.get("relationship_id") or item.get("claim_id")): item
            for item in collection
        }
        for object_id, item in by_id.items():
            lifecycle = str(item.get("graph_status") or item.get("lifecycle"))
            supersedes = list(item["supersedes"])
            superseded_by = list(item["superseded_by"])
            for earlier in supersedes:
                if earlier not in by_id:
                    errors.append(f"{object_id} supersedes missing object {earlier}")
                elif object_id not in by_id[earlier]["superseded_by"]:
                    errors.append(f"{object_id} supersession lacks reverse link from {earlier}")
            for later in superseded_by:
                if later not in by_id:
                    errors.append(f"{object_id} has missing superseded_by object {later}")
                elif object_id not in by_id[later]["supersedes"]:
                    errors.append(f"{object_id} superseded_by lacks reverse link from {later}")
            if lifecycle == "superseded" and not superseded_by:
                errors.append(f"{object_id} is superseded without a replacement")

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
    intake_claim_registry = {
        str(item["claim_id"]): str(item["review"]) for item in intake_claims
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
        "intake_claims": intake_claim_registry,
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
            "intake_claims_without_knowledge_claim_reference": sorted(
                str(item["claim_id"])
                for item in intake_claims
                if str(item["claim_id"]) not in referenced_intake_claims
            ),
        },
        "unmigrated_related_links": unmigrated,
    }
