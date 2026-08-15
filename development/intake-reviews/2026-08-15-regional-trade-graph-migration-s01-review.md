---
title: Regional Trade Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-regional-trade-graph-migration-s01.md"
case_id: CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - regional-trade
  - graph-migration
  - related-navigation
domains:
  - administration
  - economy
  - places
search_terms:
  - related-to
  - entity-regional-trade-system
  - entity-delta
  - entity-forge
  - entity-ledger
  - entity-stormlands
  - entity-upriver-highlands
authoritative_targets:
  - canon/economy/regional-trade-system.md
  - canon/places/delta.md
  - canon/places/forge.md
  - canon/places/ledger.md
  - canon/places/stormlands.md
  - canon/places/upriver-highlands.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-regional-environment-graph-migration-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Regional Trade Graph Migration Review

## Review scope

- **Submission:** [Regional Trade Graph Migration](../../intake/submissions/2026-08-15-regional-trade-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to applying the already
  established incremental graph-migration policy
- **Review objective:** Migrate a bounded regional trade and production
  navigation cluster without changing lore, authority, legacy navigation,
  existing provenance, or relationship semantics.

## Audit baseline evaluation

- **Lore review:** `false`; the batch may only promote maintained generic
  `related` navigation into the controlled navigation-only `related-to` type.
- **Graph baseline:** `91f034a5b4a5f42e1b00179568293308e1b3c756`, the
  merged regional-environment migration from PR #35.
- **Current inventory:** 19 entities, 35 explicit relationships, and 25
  unmigrated legacy link rows.
- **Batch boundary:** Six economy-and-place entities, seven unique symmetric
  relationship pairs, and 14 legacy link rows.
- **Targeted context:** Generated before authoritative mutation with all six
  targets, the `economy` and `places` domains, the `regional-trade` subject,
  and each entity name as a term. It confirmed the target records, their
  backlinks, the founding regional economy case, later clarifications, and the
  prior Tier 3 and provenance audits.
- **Tier 3 assessment:** No lore facts, semantic relationship vocabulary,
  taxonomy, ownership, paths, aliases, geography, economy, production, or
  trade model may change. This is a structural-equivalence migration, not a
  new lore baseline.

## Files inspected

The graph policy and controlled relationship registry; generated graph and
claim indexes; all prior graph-migration cases; all six proposed records and
their current `related`, relationship, and provenance metadata; repository
validation and graph-generation tooling; the remaining migration inventory;
and targeted context across the affected neighborhood. Context also surfaced
Highwall, regional imperial, climate, hydrology, open-question, and government
backlinks; none requires content changes because this batch preserves generic
navigation only and already excludes those cross-domain pairs.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION-S01-C001 | Build the identified regional trade graph-migration round. | administrative | `explicit` | None | PRs #33–#35 establish and demonstrate bounded incremental migration. | `link-only` | Six scoped economy-and-place records and the generated graph index | Each planned pair already exists as reciprocal generic navigation, so one controlled symmetric relationship may preserve it without asserting a stronger fact. |
| CASE-2026-08-15-REGIONAL-TRADE-GRAPH-MIGRATION-S01-C002 | Preserve lore, provenance, legacy links, and the stated exclusions. | administrative | `source-authority` | None | The established graph policy and accepted referenced scope prohibit semantic strengthening. | `no-change` | All non-relationship canon content and excluded graph inventory | Explicit non-change boundaries prevent navigation migration from altering trade or regional-place claims or absorbing cross-domain links. |

## Planned relationship batch

The batch contains these seven existing symmetric pairs:

1. Delta—Regional Trade System
2. Delta—Stormlands
3. Forge—Regional Trade System
4. Forge—Stormlands
5. Ledger—Regional Trade System
6. Regional Trade System—Stormlands
7. Regional Trade System—Upriver Highlands

Each pair exists reciprocally in the pre-migration
`unmigrated_related_links` inventory. Implementation will create exactly one
addressable `related-to` object per pair, preserve every legacy link, and point
relationship provenance to this review.

## Explicit exclusions

- Delta—Highwall, Ledger—Highwall, and Upriver Highlands—Highwall
- Highwall Governmental Continuity—Highwall
- Highwall Civic Government—Regional Imperial Structure
- Regional Imperial Structure—Regional Trade System and Upriver Highlands
- Hydrology—Storm Marshal
- The unresolved story link from Regional Imperial Structure
- New controlled relationship types or inference of production dependency,
  trade direction, geography, location, ownership, government, obligation,
  chronology, causation, or any other domain semantics
- Canon prose, status, canon level, aliases, tags, existing `related` links,
  and existing cumulative provenance

## Expected repository effects

- Add seven controlled relationship objects across the scoped owner records.
- Regenerate `knowledge-graph.json`, increasing explicit relationships from 35
  to 42 and reducing unmigrated legacy rows from 25 to 11.
- Regenerate the claim index for this review's two claims.
- Validate unique IDs, controlled types, endpoints, provenance, deterministic
  index freshness, and semantic equivalence.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `canon/economy/regional-trade-system.md` | Add two addressable `related-to` objects for its existing Stormlands and Upriver Highlands pairs. | C001 |
| `canon/places/delta.md` | Add two addressable `related-to` objects for its existing trade-system and Stormlands pairs. | C001 |
| `canon/places/forge.md` | Add two addressable `related-to` objects for its existing trade-system and Stormlands pairs. | C001 |
| `canon/places/ledger.md` | Add its existing trade-system pair as an addressable `related-to` object. | C001 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 19 entities, 42 relationships, and 11 unmigrated links. | C001-C002 |
| Submission, review, and claim index | Preserve the instruction, reviewed boundary, dispositions, and generated claim navigation. | C001-C002 |

Each reciprocal relationship is stored once on a record that already
maintained the legacy association. The owning-record choices prevent duplicate
objects while retaining both human-readable legacy links.

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| `canon/places/stormlands.md` | Its three in-scope symmetric pairs are owned once on counterpart records; duplicating them would create duplicate graph relationships. | C001-C002 |
| `canon/places/upriver-highlands.md` | Its in-scope trade-system pair is owned once on the trade-system record. | C001-C002 |
| Canon prose and existing front-matter fields | Status, canon level, aliases, tags, legacy `related`, and cumulative provenance remain unchanged. | C002 |
| All 11 remaining inventory rows | Highwall, government, imperial, hydrology, and unresolved story links remain outside this batch. | C002 |
| Relationship-type registry and graph policy | No vocabulary or governance change was authorized or required. | C002 |

## Exceptions created

None. Existing questions and cross-domain dependencies surfaced by targeted
context remain unchanged because this navigation-equivalent batch does not
answer or reinterpret them.

## Verification plan

- [x] Targeted context confirms the batch boundary before canon edits.
- [x] Every planned pair exists reciprocally in the pre-migration inventory.
- [x] Exactly seven unique relationship IDs are added.
- [x] Every relationship uses navigation-only `related-to`.
- [x] Every endpoint resolves and every relationship points to this review.
- [x] Existing canon prose and metadata remain otherwise unchanged.
- [x] The generated graph reports 19 entities, 42 relationships, and 11
  unmigrated legacy links.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 192 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 19 entities, 42
  relationships, and 11 unmigrated legacy links.
- `python scripts/build_claim_index.py --check`: current at 411 claims.
- `git diff --check`: passed.
- The complete canon diff contains only the seven reviewed relationship
  objects; no narrative or pre-existing metadata line changed.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit and require both GitHub
  checks. Merge still requires a distinct author instruction.

## Amendments

None.
