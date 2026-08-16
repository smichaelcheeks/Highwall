---
title: Knowledge Object Schema V2
type: intake-submission
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
submission_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01
sequence: 1
submitted_on: 2026-08-16
submitted_by: Shawn Cheeks
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: explicit-confirmation
parent_submission: null
supersedes_claims: []
related:
  - 2026-08-15-cloth-patch-graph-model-s01.md
  - 2026-08-15-entity-relationship-graph-s01.md
---

# Knowledge Object Schema V2

## Author instruction

The author supplied the following exact instruction after reviewing the design
reproduced below:

> Establish this design as repository policy in direct-integration mode. Transmission complete. Use the recommended decisions.

## Session mode

`direct-integration`

## Transmission completeness

The author explicitly stated `Transmission complete.`

## Submitted information

The following is the complete design presented for approval and incorporated by
the author's instruction above.

> Yes. The right implementation is a schema-v2 program, not another bulk metadata migration declared complete after adding IDs.
>
> The current repository has 20 entities, 51 relationships, and 419 intake-review claims. Those 419 claims are audit records—not necessarily maintained facts. A first-class knowledge-claim layer must therefore be introduced separately and mapped deliberately.
>
> ## Recommended final model
>
> | Object | Authoritative location | Purpose |
> | --- | --- | --- |
> | Entity | Its readable Markdown page | Current information about a thing or concept |
> | Relationship | Metadata on its owning page | A typed, addressable connection |
> | Knowledge claim | Metadata plus a bounded passage on the natural owning page | A maintained assertion with stable identity |
> | Intake claim | Existing immutable review row | What a patch submitted and how it was disposed |
> | History event | Local object metadata | What changed, under which review claims |
> | Generated index | `development/indexes/` | Reverse links, traversal, search, and assembled views |
> | Git/PR | Repository history | Exact published file changes |
>
> The critical distinction is:
>
> ```text
> CASE-...-C001     = immutable intake/review claim
> claim-highwall-... = maintained knowledge claim
> ```
>
> An intake claim may establish, revise, supersede, or leave unchanged a knowledge claim. They must not be treated as the same object.
>
> ## Proposed page structure
>
> A page remains normal readable prose. Its structured front matter would contain something like:
>
> ```yaml
> entity_id: entity-highwall
> graph_status: active
>
> relationships:
>   - relationship_id: relationship-highwall-related-to-regional-trade-system
>     relationship_type: related-to
>     source: entity-highwall
>     target: entity-regional-trade-system
>     graph_status: active
>     provenance:
>       reviews:
>         - ../../development/intake-reviews/example-review.md
>       review_claims:
>         - CASE-...-C001
>
> claims:
>   - claim_id: claim-highwall-example
>     content_id: claim-highwall-example
>     truth_kind: objective
>     authority_level: established
>     lifecycle: active
>     about:
>       - entity-highwall
>     provenance:
>       reviews:
>         - ../../development/intake-reviews/example-review.md
>       review_claims:
>         - CASE-...-C002
>
> history:
>   - history_id: history-highwall-001
>     sequence: 1
>     object_id: entity-highwall
>     change_type: graph-registered
>     review_claims:
>       - CASE-...-C001
>     summary: Registered the existing canon page as a graph entity.
> ```
>
> The corresponding fact remains readable in the body:
>
> ```markdown
> <!-- claim:claim-highwall-example:start -->
> Highwall is an established example fact.
> <!-- claim:claim-highwall-example:end -->
> ```
>
> Those hidden boundaries give the claim an exact authoritative passage. The builder can hash that passage and detect changes without duplicating its wording in metadata.
>
> Only decision-worthy assertions need these markers—not every sentence.
>
> ## Relationship-to-fact behavior
>
> Graph endpoints would expand from only entities and relationships to any registered knowledge object:
>
> ```text
> entity-character ── knows ──> claim-highwall-example
> entity-council ── denies ──> claim-highwall-example
> entity-story-reveal ── reveals ──> claim-highwall-example
> ```
>
> These types cannot be invented during migration. Each must be defined in the controlled registry with:
>
> - Directionality.
> - Authority effect.
> - Permitted endpoint kinds.
> - Self-link policy.
> - Inverse behavior, if any.
> - Semantic definition.
> - Required provenance.
>
> Until such types are authorized, the migration would retain only `related-to`. Claim `about` references would initially be navigation bindings and would not silently assert semantic roles.
>
> ## Changelog rules
>
> Every entity, relationship, and knowledge claim should have local history.
>
> The rules should be:
>
> - History is mandatory and append-only.
> - Sequences are contiguous per object.
> - Every event has a controlled change type.
> - Every event resolves to exact review claim IDs.
> - Existing events cannot be edited after publication.
> - A wording-only clarification may retain the object ID and add an event.
> - A materially different claim gets a new claim ID and supersedes the old one.
> - Relationship type and endpoints are immutable.
> - Changing relationship type or endpoints creates a new relationship.
> - Superseded and retired objects remain as tombstones.
> - Git commit hashes are not required inside the same commit; Git and the PR provide publication evidence afterward.
>
> For the historical migration, we should not pretend the new changelog has always existed. Each object should declare its history coverage. Earlier history can be audited and backfilled, but anything not reconstructed remains explicitly `provenance-only`, not silently “complete.”
>
> ## Implementation phases
>
> 1. **Establish schema-v2 policy**
>
>    Define knowledge claims versus intake claims, mandatory histories, lifecycle rules, endpoint kinds, provenance requirements, and program completion criteria.
>
> 2. **Replace the fragile metadata parser**
>
>    The current code uses purpose-built regular expressions that reject new relationship fields. I recommend parsing the existing YAML front matter with a real safe YAML parser rather than extending that parser repeatedly.
>
> 3. **Implement structural validation**
>
>    Add checks for:
>
>    - Object identity persistence and non-reuse.
>    - Append-only histories.
>    - Relationship endpoint/type immutability.
>    - Tombstones and bidirectional supersession.
>    - Symmetric-pair uniqueness.
>    - Ownership/source agreement.
>    - Registry-controlled directionality and endpoint kinds.
>    - Completed, authorized provenance reviews.
>    - Exact claim-content boundaries.
>    - Claim lifecycle and supersession integrity.
>
> 4. **Build a unified generated projection**
>
>    Produce a knowledge-object index containing entities, relationships, knowledge claims, intake claims, patches, reviews, histories, decisions, and evidence references. Existing specialized indexes can remain compatibility views during migration.
>
> 5. **Backfill entity and relationship histories**
>
>    Audit all 20 entities and 51 relationships. Registration events must say `graph-registered`, not falsely claim the lore object was newly established.
>
> 6. **Audit all 419 intake claims**
>
>    Every intake claim receives one explicit mapping result:
>
>    - Materializes a maintained knowledge claim.
>    - Changes an existing knowledge claim.
>    - Administrative only.
>    - Proposal/question/exception only.
>    - No current-state effect.
>    - Superseded or retired.
>
>    The preliminary inventory suggests approximately 231 canon, story, belief, or historical intake claims could be candidates, but each must be reviewed rather than converted mechanically.
>
> 7. **Add governed semantic relationship types**
>
>    Introduce types such as `knows`, `denies`, or `reveals` only when their meanings and existing source support are separately authorized.
>
> 8. **Implement thread traversal**
>
>    A command such as:
>
>    ```powershell
>    python scripts/pull_thread.py entity-highwall
>    ```
>
>    should return current claims, direct and incoming relationships, local history, provenance, supersessions, contradictions, decisions, and story-boundary information without manually opening every pointer.
>
> 9. **Run a completion audit**
>
>    Do not call the program complete until every existing object and intake claim has an explicit migration disposition, all histories meet their declared coverage, all indexes are current, and canon-equivalence has been independently verified.
>
> ## Decisions I recommend approving
>
> 1. Use separate stable knowledge-claim IDs; preserve existing `CASE-...-C...` IDs as immutable intake claims.
> 2. Keep authoritative object metadata on the owning Markdown page.
> 3. Use bounded hidden claim markers so facts remain readable and machine-addressable.
> 4. Make local history mandatory and append-only.
> 5. Preserve incomplete historical coverage honestly while performing an audited backfill.
> 6. Use a unified generated index for retrieval, while Markdown remains authoritative.
> 7. Roll this out through staged PRs with a single public completion checklist.
> 8. Do not introduce semantic lore relationships during the structural migration.

## Attachments or sources

None.

## Submission notes

This submission preserves the complete conversational design and the exact
author instruction that established it. Processing decisions belong in the
separate intake review.
