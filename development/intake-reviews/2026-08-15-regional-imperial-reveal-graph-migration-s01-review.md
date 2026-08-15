---
title: Regional Imperial Reveal Graph Migration Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-regional-imperial-reveal-graph-migration-s01.md"
case_id: CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION
submission_id: CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - regional-imperial-structure
  - regional-imperial-relationship-reveal
  - graph-migration
  - related-navigation
domains:
  - administration
  - government
  - story
search_terms:
  - related-to
  - entity-regional-imperial-structure
  - regional-imperial-relationship
  - reader reveal
authoritative_targets:
  - canon/government/regional-imperial-structure.md
  - story/reveals/regional-imperial-relationship.md
  - development/indexes/knowledge-graph.json
related:
  - 2026-08-15-storm-marshal-hydrology-graph-migration-s01-review.md
  - 2026-08-15-regional-imperial-graph-migration-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Regional Imperial Reveal Graph Migration Review

## Review scope

- **Submission:** [Regional Imperial Reveal Graph Migration](../../intake/submissions/2026-08-15-regional-imperial-reveal-graph-migration-s01.md)
- **Case:** `CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION`
- **Submission ID:** `CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`, limited to completing the
  established incremental graph-migration inventory
- **Review objective:** Resolve the final maintained generic navigation link
  by opting the existing story-reveal record into the graph and adding a
  navigation-only relationship without changing story or canon meaning.

## Audit baseline evaluation

- **Lore review:** `false`; this case may add structural graph metadata only.
- **Graph baseline:** `79b8b0f164ee8a6d57a16944660f2b42e72be938`, the
  merged Storm Marshal migration from PR #39.
- **Current inventory:** 19 entities, 50 explicit relationships, and 1
  unmigrated legacy link row.
- **Batch boundary:** One existing canon entity, one existing story-reveal
  record, one stable story entity identity, and one unique symmetric
  navigation relationship.
- **Targeted context:** Generated before authoritative mutation from the latest
  comprehensive regional Tier 3 baseline through the merged PR #39 commit,
  then narrowed to the imperial entity, reveal record, founding review, prior
  graph migrations, graph policy, and generated inventory. No story file has
  changed since that baseline, and no conflicting dependency was exposed.
- **Tier 3 assessment:** No lore, political structure, official terminology,
  reader knowledge, reveal timing, character knowledge, narrative order,
  relationship vocabulary, paths, or aliases may change. This is a reviewed
  structural-equivalence migration, not a new lore baseline.

## Files inspected

The graph policy, controlled relationship registry, CLOTH graph abstraction,
story/reveal boundary guidance, generated graph and claim indexes, graph
generation and validation tooling, the Regional Imperial Structure record,
the Regional Imperial Relationship Reveal record, their founding intake
review, the prior regional-imperial migration, the merged Storm Marshal case,
the regional Tier 3 audit, the canon-change log, and incremental Git context
for `723d457928ee357ad51e164340e1e7252bac9f30..79b8b0f164ee8a6d57a16944660f2b42e72be938`.
The evidence confirms one maintained navigation link, one existing reveal
record with no graph identity, and no need to change either record's prose.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION-S01-C001 | Merge the preceding migration if its checks remain satisfactory. | administrative | `explicit` | None | PR #39 was clean and mergeable at commit `43ac4a28a602561d8a3e3db33ac32c43aac58105`; both required checks passed. | `no-change` | Git and PR publication history | The requested merge was completed before this new case branch was created and requires no additional repository content. |
| CASE-2026-08-15-REGIONAL-IMPERIAL-REVEAL-GRAPH-MIGRATION-S01-C002 | Build what is needed for the last unresolved graph inventory item. | administrative | `explicit` | None | Regional Imperial Structure maintains the inventory's sole legacy link, targeting an existing story-reveal record that graph policy permits to opt in after review. | `link-only` | Regional Imperial Structure, Regional Imperial Relationship Reveal, and the generated graph index | A stable identity for the existing reveal record and one controlled `related-to` object preserve existing navigation without asserting new political or narrative facts. |

## Planned relationship batch

The batch contains the one remaining generic navigation pair:

1. Regional Imperial Structure—Regional Imperial Relationship Reveal

Implementation will opt the maintained story-reveal record into the graph with
a stable entity ID, create one addressable `related-to` object on Regional
Imperial Structure, preserve the legacy link, and point relationship
provenance to this review.

## Explicit exclusions

- Changes to canon or story prose
- Changes to objective truth, official position, early reader knowledge,
  later reveal content, character knowledge, or reveal timing
- Treating story information as objective canon
- New controlled relationship types or stronger political, epistemic,
  chronological, causal, or narrative semantics
- Removal of legacy compatibility links

## Expected repository effects

- Add graph front matter and a stable entity ID to the existing reveal record.
- Add one controlled relationship object to Regional Imperial Structure.
- Regenerate `knowledge-graph.json`, increasing entities from 19 to 20,
  relationships from 50 to 51, and reducing unmigrated links from 1 to 0.
- Regenerate the claim index for this review's two claims.
- Validate identity, endpoint, provenance, deterministic index freshness, and
  preservation of the canon/story boundary.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| `story/reveals/regional-imperial-relationship.md` | Add graph and lifecycle metadata, including the stable reveal entity ID, while retaining the complete original story body. | C002 |
| `canon/government/regional-imperial-structure.md` | Add its existing reveal association as one addressable `related-to` object. | C002 |
| `development/indexes/knowledge-graph.json` | Regenerate the navigation index at 20 entities, 51 relationships, and 0 unmigrated links. | C002 |
| Submission, review, and claim index | Preserve the instruction, review boundary, dispositions, and generated claim navigation. | C001-C002 |

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| Canon and story prose | The migration adds front-matter graph metadata only; objective truth and reveal guidance remain unchanged. | C002 |
| Story `canon_level` | No canon level is introduced on the reveal record, so graph participation cannot be read as promoting narrative information into objective canon. | C002 |
| Legacy canon `related` link | Compatibility navigation remains in place under incremental migration policy. | C002 |
| Relationship-type registry and graph policy | The existing navigation-only `related-to` type and non-canon opt-in rule already cover this case. | C002 |
| Canon change log | No objective or story fact changed. | C002 |

## Exceptions created

None. The source already establishes both the objective canon
record and separate story-reveal record; this case changes neither meaning.

## Verification plan

- [x] Targeted context confirms the batch boundary before graph metadata edits.
- [x] Exactly one stable entity ID and one unique relationship ID are added.
- [x] The relationship uses navigation-only `related-to`.
- [x] Both endpoints resolve and relationship provenance points to this review.
- [x] Existing canon and story prose remain byte-for-byte unchanged.
- [x] The generated graph reports 20 entities, 51 relationships, and 0
  unmigrated legacy links.
- [x] Unit tests and required repository validation pass.
- [x] The complete diff contains no unrelated changes.

Local verification completed on 2026-08-15:

- `python -m unittest discover -s tests -v`: 163 tests passed.
- `python scripts/validate_repository.py --base-ref origin/main`: passed
  across 200 Markdown files.
- `python scripts/build_graph_index.py --check`: current at 20 entities, 51
  relationships, and 0 unmigrated legacy links.
- `python scripts/build_claim_index.py --check`: current at 419 claims.
- `git diff --check`: passed.
- Complete diff inspection confirms the original canon and story prose is
  unchanged and every current-state edit belongs to this case.

## Outcome

- **Review status:** `complete`
- **Integration status:** Complete locally; publication pending.
- **Exceptions:** None.
- **Outstanding action:** Publish the final commit and require both GitHub
  checks. Merge still requires a distinct author instruction.

## Amendments

None.
