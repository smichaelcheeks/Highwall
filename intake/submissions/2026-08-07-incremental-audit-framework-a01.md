---
title: Incremental Audit Framework Canon-Intake Clarification
type: conversation-addendum
case_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK
submission_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01
sequence: 1
submitted_on: 2026-08-08
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: explicit-confirmation
parent_submission: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-S01
supersedes_claims: []
related:
  - "2026-08-07-incremental-audit-framework-s01.md"
  - "../../references/incremental-audit-workflow.md"
---

# Incremental Audit Framework Canon-Intake Clarification

## Authorized clarification

Treat this as an authorized clarification to the incremental-audit-framework policy:

Integrate audit-baseline evaluation into the regular canon intake process rather than leaving incremental auditing as an optional standalone maintenance activity.

For every new lore intake review, require the reviewer to record:

- The latest applicable semantic-audit baseline.
- The Git range examined since that baseline.
- Whether incremental audit context was generated.
- Prior audited relationships considered.
- Results carried forward, revalidated, invalidated, or widened.
- The consistency tier required and actually performed.
- Whether any Tier 3 trigger is active.
- The number of completed canon cases since the latest comprehensive Tier 3 baseline, where deterministically available.

Update the intake workflow, intake-review template, consistency workflow, and applicable validation/tests so a future contributor is prompted to perform this evaluation.

The process must require a fresh Tier 3 audit:

- After every ten completed canon cases since the last Tier 3 baseline.
- Before a tagged canon snapshot.
- Before sustained story drafting.
- After major regional, chronological, political, taxonomy, ownership, path, or alias changes.
- When a change affects three or more semantic domains.
- When incremental or targeted reviews repeatedly expose unexpected dependencies.
- When the prior baseline is missing, incomplete, or unreliable.

The counter and trigger evaluation must not be inferred solely from the canon change log or impact manifests. Use Git history and review records, and require semantic judgment for ambiguous cases.

Preserve this clarification as the next immutable addendum before integrating it.

<!-- END OF ADDENDUM -->
