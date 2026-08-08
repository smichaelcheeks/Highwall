# Maintenance Review: Claim Lifecycle Discovery

## Scope

- **Objective:** Resolve `PROV-2026-08-07-F03` by making accepted-claim
  supersession and exceptional-disposition state visible in generated claim
  discovery.
- **Why this is maintenance:** The change derives navigation from existing
  intake reviews and development-record metadata. It introduces no lore,
  changes no authority or disposition, resolves no contradiction, and creates
  no repository policy.
- **Impact:** Claim-index schema version 3, targeted case-context output,
  deterministic lifecycle validation, and documentation of the derived
  fields.

## Files inspected

- `development/maintenance-reviews/2026-08-07-claim-to-canon-provenance-audit.md`
- All intake-review claim tables containing a nonempty `Supersedes` cell or a
  `defer`, `conflict`, or `retire` disposition
- All development records linked by those exceptional dispositions
- `scripts/consistency_common.py`
- `scripts/build_claim_index.py`
- `scripts/build_case_context.py`
- `references/consistency-workflow.md`

## Changes

- Preserve full claim IDs from the review table's `Supersedes` column.
- Derive reverse `superseded_by` relationships across the accepted claim set.
- Derive linked exception-record paths and their current front-matter status
  for `defer`, `conflict`, and `retire` claims.
- Fail index generation when a superseded claim is absent, an exceptional
  disposition has no linked development record, a linked record is absent, or
  the record has no status.
- Display lifecycle relationships in targeted case context and regenerate the
  non-authoritative claim index at schema version 3.

## Deliberate non-changes

- No intake submission, intake review, canon page, story page, design page,
  claim disposition, authority declaration, or development-record status is
  changed.
- Clarifications that do not identify a full superseded claim ID remain review
  prose rather than being promoted by inference into formal supersession.
- A resolved exception record remains attached to the historical exceptional
  claim; generated status aids discovery but does not rewrite that claim's
  recorded disposition.

## Verification

- [x] No setting, story, belief, historical, or design claim was introduced.
- [x] No authority or contradiction decision was made.
- [x] Generated supersession links are bidirectional and reference existing
  indexed claims.
- [x] Every exceptional claim exposes at least one existing development record
  with status.
- [x] Targeted context displays supersession and resolved-exception examples.
- [x] Relevant deterministic validation passed.
- [x] The complete diff contains no unrelated changes.
- [x] Publication status is reported from GitHub rather than copied into an
  audit-only commit.

## Publication

Pending.
