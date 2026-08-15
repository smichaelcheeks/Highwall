---
title: Civic Governance Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-civic-governance-graph-migration-s01.md"
case_id: CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - civic-governance
  - graph-migration
  - related-navigation
domains:
  - administration
  - government
  - institutions
search_terms:
  - related-to
  - entity-arbiter
  - entity-council-of-highwall
  - entity-highwall-civic-government
  - entity-storm-marshal
  - entity-professional-civic-institutions
  - entity-highwall-governmental-continuity
authoritative_targets:
  - canon/government/arbiter.md
  - canon/government/council.md
  - canon/government/highwall-civic-government.md
  - canon/government/storm-marshal.md
  - canon/institutions/professional-civic-institutions.md
  - canon/history/highwall-governmental-continuity.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Civic Governance Graph Migration Review

## Review scope

- **Submission:** [Civic Governance Graph Migration Setup](../../intake/submissions/2026-08-15-civic-governance-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to applying the already
  established incremental graph-migration policy
- **Review objective:** Prepare and execute a bounded second migration batch
  over the civic-governance cluster without changing lore, authority, legacy
  navigation, or existing provenance.

## Audit baseline evaluation

- **Lore review:** `false`; this batch may only promote existing generic
  `related` navigation into the controlled navigation-only `related-to` type.
- **Graph baseline:** `b124c50fa941e7eb997df5a6e366702507f2ba42`, the
  merged implementation from PR #33.
- **Current inventory:** 19 entities, 9 explicit relationships, and 74
  unmigrated legacy link rows.
- **Batch boundary:** Six civic-governance entities, 13 unique symmetric
  relationship pairs, and 25 legacy link rows.
- **Tier 3 assessment:** No lore facts, semantic relationship vocabulary,
  taxonomy, ownership, paths, aliases, chronology, geography, or political
  structure may change. This is a bounded structural-equivalence migration,
  not a new lore baseline.

## Files inspected

The graph policy and controlled relationship registry; the generated graph
index; the prior implementation submission and review; all six proposed owner
records and their existing `related` and provenance metadata; repository
validation and graph-generation tooling; and the remaining migration inventory.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION-S01-C001 | Set up the next round of graph integration. | administrative | `explicit` | None | PR #33 establishes incremental migration and exposes the remaining inventory. | `create` | This case branch, submission, and review | A separate case preserves the prior pilot boundary and makes the next batch independently reviewable. |
| CASE-2026-08-15-CIVIC-GOVERNANCE-GRAPH-MIGRATION-S01-C002 | Apply the established migration policy without introducing new lore or relationship semantics. | administrative | `derived` | None | The graph policy authorizes governed batches using navigation-only `related-to` for existing generic links. | `update` | Six scoped canon records and the generated graph index | The civic cluster is a bounded, highly reciprocal subset; one addressable symmetric relationship per existing pair preserves rather than strengthens navigation. |

## Planned relationship batch

The batch contains these 13 existing symmetric pairs:

1. Arbiter—Council of Highwall
2. Arbiter—Highwall Civic Government
3. Arbiter—Continuity of Highwall Government
4. Arbiter—Professional Civic Institutions
5. Arbiter—Storm Marshal
6. Council of Highwall—Highwall Civic Government
7. Council of Highwall—Continuity of Highwall Government
8. Council of Highwall—Professional Civic Institutions
9. Council of Highwall—Storm Marshal
10. Highwall Civic Government—Continuity of Highwall Government
11. Highwall Civic Government—Professional Civic Institutions
12. Highwall Civic Government—Storm Marshal
13. Professional Civic Institutions—Storm Marshal

Each pair is already represented by at least one maintained legacy `related`
link. Implementation will create exactly one addressable `related-to` object
per pair, preserve all legacy links, and point local relationship provenance to
this review.

## Explicit exclusions

- Regional imperial structure and its unresolved story link
- Regional economy and trade relationships
- Geology, climate, hydrology, ecology, flora and fauna relationships
- Delta, Forge, Ledger, Stormlands, Upriver Highlands, and other place links
- New controlled relationship types or any inference of office, membership,
  authority, oversight, chronology, causation, or dependency semantics
- Canon prose, status, canon level, aliases, tags, existing `related` links,
  and existing cumulative provenance

## Expected repository effects

- Add 13 controlled relationship objects across the scoped owner records.
- Regenerate `knowledge-graph.json`, increasing explicit relationships from 9
  to 22 and reducing unmigrated legacy rows from 74 to 49.
- Regenerate the claim index for this review's two claims.
- Validate unique IDs, controlled types, endpoints, provenance, deterministic
  index freshness, and semantic equivalence.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `canon/government/arbiter.md` | Add five addressable `related-to` objects for its existing civic-cluster pairs. | C002 |
| `canon/government/council.md` | Add three addressable `related-to` objects for its existing civic-cluster pairs. | C002 |
| `canon/government/highwall-civic-government.md` | Add three addressable `related-to` objects for its existing civic-cluster pairs. | C002 |
| `canon/history/highwall-governmental-continuity.md` | Add the existing one-way Council association as an addressable `related-to` object. | C002 |
| `canon/institutions/professional-civic-institutions.md` | Add the existing Storm Marshal pair as an addressable `related-to` object. | C002 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 19 entities, 22 relationships, and 49 unmigrated links. | C002 |
| Submission, review, and claim index | Preserve the instruction, scope and dispositions; index both case claims. | C001-C002 |

For reciprocal pairs, the relationship object is stored once on a record that
already maintained the legacy association. The Council-continuity pair was
one-way, so its object remains owned by the continuity record that maintained
that link.

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| `canon/government/storm-marshal.md` | Its four in-scope symmetric pairs are owned once on the counterpart records; duplicating them would create duplicate graph relationships. | C002 |
| Canon prose and existing front-matter fields | The batch migrates navigation structure only; status, canon level, aliases, tags, legacy `related`, and cumulative provenance remain unchanged. | C002 |
| All excluded domains and the relationship-type registry | No other migration batch or semantic vocabulary was authorized. | C002 |

## Exceptions created

None. No open question, proposal, contradiction, decision, or retired record is
required for a navigation-equivalent migration.

## Verification plan

- [x] Every planned pair exists in the pre-migration legacy inventory.
- [x] Exactly 13 unique relationship IDs are added.
- [x] Every relationship uses navigation-only `related-to`.
- [x] Every endpoint resolves and every relationship points to this review.
- [x] Existing canon prose and metadata remain otherwise byte-equivalent.
- [x] The generated graph reports 19 entities, 22 relationships, and 49
  unmigrated legacy links.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 188 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 19 entities, 22
  relationships, and 49 unmigrated legacy links.
- `python scripts/build_claim_index.py --check`: current at 407 claims.
- `git diff --check`: passed.
- The complete canon diff contains only the 13 reviewed relationship objects;
  no narrative or pre-existing metadata line changed.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit, require both GitHub checks,
  and merge under the author's explicit instruction.

## Amendments

None.
