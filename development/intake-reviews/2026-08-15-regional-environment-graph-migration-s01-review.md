---
title: Regional Environment Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-regional-environment-graph-migration-s01.md"
case_id: CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - regional-environment
  - graph-migration
  - related-navigation
domains:
  - administration
  - places
search_terms:
  - related-to
  - entity-highwall-region-climate
  - entity-highwall-region-ecology
  - entity-highwall-region-flora-and-fauna
  - entity-highwall-region-geology
  - entity-highwall-region-hydrology
  - entity-stormlands
  - entity-upriver-highlands
authoritative_targets:
  - canon/places/highwall-region-climate.md
  - canon/places/highwall-region-ecology.md
  - canon/places/highwall-region-flora-and-fauna.md
  - canon/places/highwall-region-geology.md
  - canon/places/highwall-region-hydrology.md
  - canon/places/stormlands.md
  - canon/places/upriver-highlands.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-civic-governance-graph-migration-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Regional Environment Graph Migration Review

## Review scope

- **Submission:** [Regional Environment Graph Migration](../../intake/submissions/2026-08-15-regional-environment-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to applying the already
  established incremental graph-migration policy
- **Review objective:** Migrate a bounded regional environment and terrain
  cluster without changing lore, authority, legacy navigation, existing
  provenance, or relationship semantics.

## Audit baseline evaluation

- **Lore review:** `false`; the batch may only promote maintained generic
  `related` navigation into the controlled navigation-only `related-to` type.
- **Graph baseline:** `b33b98281aefc443d2a5a44d83b3d6d9ef12687b`, the
  merged civic-governance migration from PR #34.
- **Current inventory:** 19 entities, 22 explicit relationships, and 49
  unmigrated legacy link rows.
- **Batch boundary:** Seven place-domain entities, 13 unique symmetric
  relationship pairs, and 24 legacy link rows.
- **Targeted context:** Generated before authoritative mutation with all seven
  targets, the `places` domain, the `regional-environment` subject, and the
  Highwall Region, Stormlands, and Upriver Highlands terms. It confirmed the
  seven target records, their backlinks, prior climate, ecology, geology,
  hydrology, geography, and audit records, and the already documented open
  questions and contradictions.
- **Tier 3 assessment:** No lore facts, semantic relationship vocabulary,
  taxonomy, ownership, paths, aliases, chronology, geography, or environmental
  model may change. This is a structural-equivalence migration, not a new lore
  baseline.

## Files inspected

The graph policy and controlled relationship registry; generated graph and
claim indexes; the two prior graph-migration cases; all seven proposed records
and their current `related`, relationship, and provenance metadata; repository
validation and graph-generation tooling; the remaining migration inventory;
and targeted context across the affected neighborhood. Context also surfaced
economy, Highwall, Storm Marshal, open-question, proposal, and contradiction
backlinks; none requires content changes because this batch preserves generic
navigation only and already excludes those cross-domain pairs.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION-S01-C001 | Execute the identified regional environment graph-migration round. | administrative | `explicit` | None | PRs #33 and #34 establish and demonstrate bounded incremental migration. | `link-only` | Seven scoped place records and the generated graph index | Each planned pair already exists as generic navigation, so one controlled symmetric relationship may preserve it without asserting a stronger fact. |
| CASE-2026-08-15-REGIONAL-ENVIRONMENT-GRAPH-MIGRATION-S01-C002 | Preserve lore, provenance, legacy links, and the stated exclusions. | administrative | `source-authority` | None | The established graph policy and accepted referenced scope prohibit semantic strengthening. | `no-change` | All non-relationship canon content and excluded graph inventory | Explicit non-change boundaries prevent a navigation migration from altering environmental claims or absorbing cross-domain links. |

## Planned relationship batch

The batch contains these 13 existing symmetric pairs:

1. Climate—Ecology
2. Climate—Geology
3. Climate—Hydrology
4. Climate—Stormlands
5. Ecology—Flora and Fauna
6. Ecology—Geology
7. Ecology—Hydrology
8. Ecology—Stormlands
9. Flora and Fauna—Hydrology
10. Flora and Fauna—Stormlands
11. Geology—Hydrology
12. Geology—Upriver Highlands
13. Hydrology—Upriver Highlands

Each pair exists in the pre-migration `unmigrated_related_links` inventory.
Implementation will create exactly one addressable `related-to` object per
pair, preserve every legacy link, and point relationship provenance to this
review.

## Explicit exclusions

- Hydrology—Storm Marshal
- Regional economy, trade, and imperial relationships
- Highwall, Delta, Forge, and Ledger relationships
- The unresolved story link from Regional Imperial Structure
- New controlled relationship types or inference of climate mechanism,
  ecological dependency, geological causation, hydrological causation,
  location, ownership, chronology, government, or any other domain semantics
- Canon prose, status, canon level, aliases, tags, existing `related` links,
  and existing cumulative provenance

## Expected repository effects

- Add 13 controlled relationship objects across the scoped owner records.
- Regenerate `knowledge-graph.json`, increasing explicit relationships from 22
  to 35 and reducing unmigrated legacy rows from 49 to 25.
- Regenerate the claim index for this review's two claims.
- Validate unique IDs, controlled types, endpoints, provenance, deterministic
  index freshness, and semantic equivalence.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `canon/places/highwall-region-climate.md` | Add four addressable `related-to` objects for existing climate-cluster pairs. | C001 |
| `canon/places/highwall-region-ecology.md` | Add four addressable `related-to` objects for existing ecology-cluster pairs. | C001 |
| `canon/places/highwall-region-flora-and-fauna.md` | Add two addressable `related-to` objects for existing organism-cluster pairs. | C001 |
| `canon/places/highwall-region-geology.md` | Add two addressable `related-to` objects for existing geology-cluster pairs. | C001 |
| `canon/places/highwall-region-hydrology.md` | Add the existing Upriver Highlands pair as an addressable `related-to` object. | C001 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 19 entities, 35 relationships, and 25 unmigrated links. | C001-C002 |
| Submission, review, and claim index | Preserve the instruction, reviewed boundary, dispositions, and generated claim navigation. | C001-C002 |

Each relationship is stored once on a record that already maintained the
legacy association. Climate—Geology and Flora and Fauna—Hydrology were
one-way links, so their objects remain owned by those original source records.

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| `canon/places/stormlands.md` | Its three in-scope symmetric pairs are owned once on counterpart records; duplicating them would create duplicate graph relationships. | C001-C002 |
| `canon/places/upriver-highlands.md` | Its two in-scope symmetric pairs are owned once on geology and hydrology; duplicating them would create duplicate graph relationships. | C001-C002 |
| Canon prose and existing front-matter fields | Status, canon level, aliases, tags, legacy `related`, and cumulative provenance remain unchanged. | C002 |
| Hydrology—Storm Marshal and every other excluded pair | The batch boundary expressly leaves cross-domain and later migration work visible in the generated inventory. | C002 |
| Relationship-type registry and graph policy | No vocabulary or governance change was authorized or required. | C002 |

## Exceptions created

None. Existing environmental questions, proposals, and contradictions surfaced
by targeted context remain unchanged because this navigation-equivalent batch
does not answer, select, or reinterpret them.

## Verification plan

- [x] Targeted context confirms the batch boundary before canon edits.
- [x] Every planned pair exists in the pre-migration legacy inventory.
- [x] Exactly 13 unique relationship IDs are added.
- [x] Every relationship uses navigation-only `related-to`.
- [x] Every endpoint resolves and every relationship points to this review.
- [x] Existing canon prose and metadata remain otherwise unchanged.
- [x] The generated graph reports 19 entities, 35 relationships, and 25
  unmigrated legacy links.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 190 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 19 entities, 35
  relationships, and 25 unmigrated legacy links.
- `python scripts/build_claim_index.py --check`: current at 409 claims.
- `git diff --check`: passed.
- The complete canon diff contains only the 13 reviewed relationship objects;
  no narrative or pre-existing metadata line changed.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit and require both GitHub
  checks. Merge still requires a distinct author instruction.

## Amendments

None.
