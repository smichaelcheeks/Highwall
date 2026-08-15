---
title: Storm Marshal Hydrology Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-storm-marshal-hydrology-graph-migration-s01.md"
case_id: CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - storm-marshal
  - highwall-region-hydrology
  - graph-migration
  - related-navigation
domains:
  - administration
  - government
  - places
search_terms:
  - related-to
  - entity-storm-marshal
  - entity-highwall-region-hydrology
  - flood
authoritative_targets:
  - canon/government/storm-marshal.md
  - canon/places/highwall-region-hydrology.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-highwall-hub-graph-migration-s01-review.md
  - 2026-08-15-civic-governance-graph-migration-s01-review.md
  - 2026-08-15-regional-environment-graph-migration-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Storm Marshal Hydrology Graph Migration Review

## Review scope

- **Submission:** [Storm Marshal Hydrology Graph Migration](../../intake/submissions/2026-08-15-storm-marshal-hydrology-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to applying the already
  established incremental graph-migration policy
- **Review objective:** Migrate the remaining resolvable canon-to-canon
  navigation link without changing lore, authority, legacy navigation,
  existing provenance, or relationship semantics.

## Audit baseline evaluation

- **Lore review:** `false`; the batch may only promote maintained generic
  `related` navigation into the controlled navigation-only `related-to` type.
- **Graph baseline:** `69fa52f3935c4de428ea9993c82c1b2d1e78b4f4`, the
  merged Highwall-hub migration from PR #38.
- **Current inventory:** 19 entities, 49 explicit relationships, and 2
  unmigrated legacy link rows.
- **Batch boundary:** Two entities, one unique symmetric relationship pair,
  and one legacy link row maintained from Storm Marshal toward Hydrology of
  the Highwall Region.
- **Targeted context:** Generated before authoritative mutation across both
  entities and the government, places, and flood-response neighborhood. It
  confirmed Storm Marshal's one-way legacy Hydrology link, the founding
  emergency-office and regional-hydrology claims, later institutional-learning
  clarification, and the prior regional Tier 3 flood boundaries.
- **Tier 3 assessment:** No lore facts, semantic relationship vocabulary,
  taxonomy, ownership, paths, aliases, flood behavior, hydrology, emergency
  authority, or government may change. This is a structural-equivalence
  migration, not a new lore baseline.

## Files inspected

The graph policy and controlled relationship registry; generated graph and
claim indexes; prior graph-migration cases; both proposed entity records and
their current `related`, relationship, and provenance metadata; repository
validation and graph-generation tooling; the remaining migration inventory;
the founding hydrology and civic-government reviews; the later government
clarification; the regional Tier 3 audit; and the canon-change log. Targeted
context exposed no contradiction or dependency requiring a wider mutation
boundary.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION-S01-C001 | Build the identified Storm Marshal hydrology graph-migration round. | administrative | `explicit` | None | Storm Marshal already maintains a generic `related` link to the Hydrology record; PRs #33–#38 establish and demonstrate bounded incremental migration. | `link-only` | Storm Marshal and the generated graph index | One controlled symmetric relationship preserves the existing generic navigation without asserting a stronger hydrologic, emergency-response, governmental, geographic, or causal fact. |
| CASE-2026-08-15-STORM-MARSHAL-HYDROLOGY-GRAPH-MIGRATION-S01-C002 | Preserve lore, provenance, the legacy link, and the story exclusion. | administrative | `source-authority` | None | The established graph policy and accepted referenced scope prohibit semantic strengthening. | `no-change` | All non-relationship canon content and the unresolved story inventory row | Explicit non-change boundaries prevent navigation migration from altering hydrology or government claims or treating the story record as a graph entity. |

## Planned relationship batch

The batch contains one existing generic navigation pair:

1. Storm Marshal—Hydrology of the Highwall Region

Implementation will create one addressable `related-to` object on the Storm
Marshal record, which already maintains the legacy link, preserve that link,
and point relationship provenance to this review.

## Explicit exclusions

- The unresolved story link from Regional Imperial Structure
- Assigning an entity ID or relationship metadata to the story-reveal record
- New controlled relationship types or inference of flood causation,
  emergency authority, institutional dependency, geography, location,
  ownership, chronology, or any other domain semantics
- Canon prose, status, canon level, aliases, tags, existing `related` links,
  and existing cumulative provenance

## Expected repository effects

- Add one controlled relationship object to the Storm Marshal record.
- Regenerate `knowledge-graph.json`, increasing explicit relationships from 49
  to 50 and reducing unmigrated legacy rows from 2 to 1.
- Regenerate the claim index for this review's two claims.
- Validate the relationship ID, controlled type, endpoints, provenance,
  deterministic index freshness, and semantic equivalence.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `canon/government/storm-marshal.md` | Add its existing Hydrology pair as an addressable `related-to` object. | C001 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 19 entities, 50 relationships, and 1 unmigrated link. | C001-C002 |
| Submission, review, and claim index | Preserve the instruction, reviewed boundary, dispositions, and generated claim navigation. | C001-C002 |

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| `canon/places/highwall-region-hydrology.md` | The pair is owned once on Storm Marshal, which already maintains the legacy link; duplicating it would create a duplicate graph relationship. | C001-C002 |
| Canon prose and existing front-matter fields | Status, canon level, aliases, tags, legacy `related`, and cumulative provenance remain unchanged. | C002 |
| The remaining inventory row | The unresolved story link lacks an entity endpoint and remains outside this batch. | C002 |
| Relationship-type registry and graph policy | No vocabulary or governance change was authorized or required. | C002 |

## Exceptions created

None. The unresolved story link remains visible in the generated migration
inventory because this navigation-equivalent batch does not establish a story
entity or reinterpret narrative information.

## Verification plan

- [x] Targeted context confirms the batch boundary before canon edits.
- [x] Exactly one unique relationship ID is added.
- [x] The relationship uses navigation-only `related-to`.
- [x] Both endpoints resolve and relationship provenance points to this review.
- [x] Existing canon prose and metadata remain otherwise unchanged.
- [x] The generated graph reports 19 entities, 50 relationships, and 1
  unmigrated legacy link.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 198 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 19 entities, 50
  relationships, and 1 unmigrated legacy link.
- `python scripts/build_claim_index.py --check`: current at 417 claims.
- `git diff --check`: passed.
- The complete canon diff contains only the reviewed relationship object; no
  narrative or pre-existing metadata line changed.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit and require both GitHub
  checks. Merge still requires a distinct author instruction.

## Amendments

None.
