---
title: Regional Imperial Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-regional-imperial-graph-migration-s01.md"
case_id: CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - regional-imperial-structure
  - graph-migration
  - related-navigation
domains:
  - administration
  - government
  - economy
  - places
search_terms:
  - related-to
  - entity-highwall-civic-government
  - entity-regional-imperial-structure
  - entity-regional-trade-system
  - entity-upriver-highlands
authoritative_targets:
  - canon/government/highwall-civic-government.md
  - canon/government/regional-imperial-structure.md
  - canon/economy/regional-trade-system.md
  - canon/places/upriver-highlands.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-regional-trade-graph-migration-s01-review.md
  - 2026-08-15-civic-governance-graph-migration-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Regional Imperial Graph Migration Review

## Review scope

- **Submission:** [Regional Imperial Graph Migration](../../intake/submissions/2026-08-15-regional-imperial-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to applying the already
  established incremental graph-migration policy
- **Review objective:** Migrate a bounded regional imperial navigation cluster
  without changing lore, authority, legacy navigation, existing provenance,
  or relationship semantics.

## Audit baseline evaluation

- **Lore review:** `false`; the batch may only promote maintained generic
  `related` navigation into the controlled navigation-only `related-to` type.
- **Graph baseline:** `5fca5d21844f782212f9bab7a6c174d1da7f0b60`, the
  merged regional-trade migration from PR #36.
- **Current inventory:** 19 entities, 42 explicit relationships, and 11
  unmigrated legacy link rows.
- **Batch boundary:** Four entities, three unique symmetric relationship pairs,
  and five legacy link rows. Two pairs are reciprocal in legacy metadata; the
  Regional Imperial Structure–Upriver Highlands pair is maintained from the
  imperial record.
- **Targeted context:** Generated before authoritative mutation across all four
  target entities and the government, economy, and places neighborhood. It
  confirmed the target records, reciprocal backlinks for the civic-government
  and trade-system pairs, the one-way maintained Upriver Highlands link, the
  founding regional political-economic claims, later civic-government claims,
  and the existing story-reveal boundary.
- **Tier 3 assessment:** No lore facts, semantic relationship vocabulary,
  taxonomy, ownership, paths, aliases, political structure, economy, trade, or
  geography may change. This is a structural-equivalence migration, not a new
  lore baseline.

## Files inspected

The graph policy and controlled relationship registry; generated graph and
claim indexes; prior graph-migration cases; the four proposed entity records
and their current `related`, relationship, and provenance metadata; repository
validation and graph-generation tooling; the remaining migration inventory;
the founding regional political-economic and civic-government reviews; the
resolved regional-sovereignty question; the canon-change log; and the regional
imperial story-reveal record. Targeted context exposed no contradiction or
dependency requiring a wider mutation boundary.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION-S01-C001 | Build the identified regional imperial graph-migration round. | administrative | `explicit` | None | The three pairs already exist as maintained generic `related` navigation; PRs #33–#36 establish and demonstrate bounded incremental migration. | `link-only` | Regional Imperial Structure and the generated graph index | One controlled symmetric relationship per pair preserves existing generic navigation without asserting a stronger political, economic, geographic, or administrative fact. |
| CASE-2026-08-15-REGIONAL-IMPERIAL-GRAPH-MIGRATION-S01-C002 | Preserve lore, provenance, legacy links, and the stated exclusions. | administrative | `source-authority` | None | The established graph policy and accepted referenced scope prohibit semantic strengthening. | `no-change` | All non-relationship canon content and excluded graph inventory | Explicit non-change boundaries prevent navigation migration from altering imperial, governmental, trade, or regional-place claims or absorbing unresolved links. |

## Planned relationship batch

The batch contains these three existing generic navigation pairs:

1. Highwall Civic Government—Regional Imperial Structure
2. Regional Imperial Structure—Regional Trade System
3. Regional Imperial Structure—Upriver Highlands

Implementation will create exactly one addressable `related-to` object per
pair on the Regional Imperial Structure record, preserve every legacy link,
and point relationship provenance to this review.

## Explicit exclusions

- Delta—Highwall, Ledger—Highwall, Upriver Highlands—Highwall, and Highwall
  Governmental Continuity—Highwall
- Hydrology—Storm Marshal
- The unresolved story link from Regional Imperial Structure
- New controlled relationship types or inference of political authority,
  trade dependency, geography, location, ownership, obligation, chronology,
  causation, or any other domain semantics
- Canon prose, status, canon level, aliases, tags, existing `related` links,
  and existing cumulative provenance

## Expected repository effects

- Add three controlled relationship objects to the Regional Imperial Structure
  record.
- Regenerate `knowledge-graph.json`, increasing explicit relationships from 42
  to 45 and reducing unmigrated legacy rows from 11 to 6.
- Regenerate the claim index for this review's two claims.
- Validate unique IDs, controlled types, endpoints, provenance, deterministic
  index freshness, and semantic equivalence.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `canon/government/regional-imperial-structure.md` | Add three addressable `related-to` objects for its existing civic-government, trade-system, and Upriver Highlands navigation pairs. | C001 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 19 entities, 45 relationships, and 6 unmigrated links. | C001-C002 |
| Submission, review, and claim index | Preserve the instruction, reviewed boundary, dispositions, and generated claim navigation. | C001-C002 |

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| `canon/government/highwall-civic-government.md` | Its in-scope pair is owned once on the Regional Imperial Structure record; duplicating it would create a duplicate graph relationship. | C001-C002 |
| `canon/economy/regional-trade-system.md` | Its in-scope pair is owned once on the Regional Imperial Structure record; duplicating it would create a duplicate graph relationship. | C001-C002 |
| `canon/places/upriver-highlands.md` | Its in-scope pair is owned on the record that already maintains the imperial association. | C001-C002 |
| Canon prose and existing front-matter fields | Status, canon level, aliases, tags, legacy `related`, and cumulative provenance remain unchanged. | C002 |
| All 6 remaining inventory rows | Highwall, hydrology, and unresolved story links remain outside this batch. | C002 |
| Relationship-type registry and graph policy | No vocabulary or governance change was authorized or required. | C002 |

## Exceptions created

None. Existing questions and the unresolved story link remain unchanged because
this navigation-equivalent batch does not answer or reinterpret them.

## Verification plan

- [x] Targeted context confirms the batch boundary before canon edits.
- [x] Exactly three unique relationship IDs are added.
- [x] Every relationship uses navigation-only `related-to`.
- [x] Every endpoint resolves and every relationship points to this review.
- [x] Existing canon prose and metadata remain otherwise unchanged.
- [x] The generated graph reports 19 entities, 45 relationships, and 6
  unmigrated legacy links.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 194 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 19 entities, 45
  relationships, and 6 unmigrated legacy links.
- `python scripts/build_claim_index.py --check`: current at 413 claims.
- `git diff --check`: passed.
- The complete canon diff contains only the three reviewed relationship
  objects; no narrative or pre-existing metadata line changed.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit and require both GitHub
  checks. Merge still requires a distinct author instruction.

## Amendments

None.
