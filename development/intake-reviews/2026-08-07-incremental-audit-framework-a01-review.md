---
title: Incremental Audit Framework Canon-Intake Clarification Review
type: intake-review
status: complete
reviewed_on: 2026-08-08
submission: "../../intake/submissions/2026-08-07-incremental-audit-framework-a01.md"
case_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK
submission_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - incremental-audit
  - canon-intake
  - repository-consistency
domains:
  - administration
search_terms:
  - audit baseline
  - canon case count
  - incremental context
  - intake review
  - Tier 3 trigger
authoritative_targets:
  - references/intake-workflow.md
  - references/consistency-workflow.md
  - references/incremental-audit-workflow.md
  - templates/intake-review.md
  - scripts/validate_repository.py
related:
  - "2026-08-07-incremental-audit-framework-s01-review.md"
  - "../../references/incremental-audit-workflow.md"
---

# Incremental Audit Framework Canon-Intake Clarification Review

## Review scope

- **Submission:** [Incremental Audit Framework Canon-Intake Clarification](../../intake/submissions/2026-08-07-incremental-audit-framework-a01.md)
- **Case:** `CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK`
- **Submission ID:** `CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Lore review:** `false`; this addendum governs process and grants no lore
  authority.
- **Review objective:** Make audit-baseline evaluation a required part of every
  new lore intake review, with deterministic prompts and enforceable Tier 3
  trigger relationships where repository records can establish them.

## Files inspected

- Parent submission and completed S01 review.
- Intake, consistency, and incremental-audit workflows.
- Intake-review and conversation-addendum templates.
- Repository validator, test fixtures, and validator regression tests.
- `AGENTS.md`, `CONTRIBUTING.md`, the generated claim index, and the existing
  draft PR state.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C001 | Integrate audit-baseline evaluation into every new lore intake review instead of leaving it as optional standalone maintenance. | administrative | `explicit` | None | S01 establishes incremental audits but the regular intake workflow does not require a baseline checkpoint. | `update` | Intake, consistency, incremental-audit, contributor, and agent guidance | Making the checkpoint part of ordinary intake prevents contributors from skipping prior-audit evaluation. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C002 | Require each lore review to record the baseline, Git range, context-generation state, prior relationships, four result categories, required/performed tier, Tier 3 state, and canon-case count. | administrative | `explicit` | None | The S01 incremental template records these fields only for standalone audit records. | `update` | `templates/intake-review.md` and validator schema | Structured prospective fields make the evaluation visible and deterministically checkable without retroactively changing historical reviews. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C003 | Require a fresh Tier 3 audit after ten completed canon cases and before tagged snapshots or sustained story drafting. | administrative | `explicit` | None | Existing periodic guidance states these checkpoints but the intake process does not make them blocking. | `update` | Consistency, intake, incremental-audit, and template guidance | Converting cadence and publication/drafting checkpoints into requirements closes the optionality gap. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C004 | Require Tier 3 after major regional, chronological, political, taxonomy, ownership, path, or alias changes and whenever three or more semantic domains are affected. | administrative | `explicit` | None | Existing Tier 3 guidance covers related categories but lacks the clarified mandatory intake evaluation and complete list. | `update` | Consistency, intake, incremental-audit, template, and validator | The clarified triggers protect shared identity, ownership, and navigation relationships across domains. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C005 | Require Tier 3 when repeated unexpected dependencies appear or the prior baseline is missing, incomplete, or unreliable. | administrative | `explicit` | None | S01 already rejects guessed reuse from unreliable baselines but does not bind every lore intake review to a fresh Tier 3 response. | `update` | Consistency, intake, incremental-audit, template, and validator | A fresh baseline is the only safe response when incremental evidence cannot support reuse. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C006 | Derive counters and trigger evaluation from Git history and review records, not solely from manifests or the canon change log, and use semantic judgment for ambiguity. | administrative | `explicit` | None | S01 makes Git authoritative for changed paths and treats manifests/change log as aids. | `update` | Intake, consistency, incremental-audit, and template guidance | Review records identify completed cases while Git fixes their committed range; neither deterministic aid can settle semantic ambiguity alone. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C007 | Extend validation and isolated tests so new reviews declare whether they are lore reviews and complete the required baseline evaluation when they are. | administrative | `explicit` | None | The validator already applies prospective completeness and impact-manifest rules using the base ref. | `update` | `scripts/validate_repository.py`, `tests/fixtures.py`, and `tests/test_validate_repository.py` | Prospective validation prompts contributors while grandfathering merged historical reviews and leaving semantic accuracy to review. |
| CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-A01-C008 | Preserve the clarification as A01 and do not change lore, historical audits, claim authority, or existing deferred policy questions. | administrative | `explicit` | None | The parent case grants process-policy authority only. | `no-change` | Immutable A01, canon/story/design, historical records, and deferred policy areas | The addendum extends process requirements without granting adjacent authority. |

## Conversation checkpoint

### Established decisions

All eight administrative claims are established policy or binding
implementation constraints.

### Proposals under consideration

None.

### Corrections and supersessions

None. A01 clarifies and extends the application of S01 without rewriting or
superseding its claims.

### Open questions

None newly discovered. Semantic ambiguity in baseline applicability, case
counting, or trigger interpretation requires reviewer judgment and, when it
makes the baseline unreliable, a fresh Tier 3 audit.

### Expected repository effects

Add structured prospective lore-review fields, enforce deterministic
relationships among those fields, make Tier 3 triggers mandatory, update
regular intake guidance, extend tests, and regenerate the claim index.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-07-incremental-audit-framework-a01.md` | Preserved the authorized clarification as immutable A01. | C008 |
| `development/intake-reviews/2026-08-07-incremental-audit-framework-a01-review.md` | Recorded A01's impact manifest, claims, dispositions, and verification. | C001-C008 |
| `development/intake-reviews/2026-08-07-incremental-audit-framework-s01-review.md` | Classified the already-added process review as non-lore in a dated amendment. | C007-C008 |
| `references/intake-workflow.md` | Made baseline evaluation part of every lore review and defined Git-and-review case counting. | C001-C006 |
| `references/consistency-workflow.md` | Replaced optional periodic guidance with mandatory fresh Tier 3 triggers. | C001, C003-C006 |
| `references/incremental-audit-workflow.md` | Linked A01 and integrated incremental evidence into normal lore intake. | C001, C003-C006 |
| `references/canon-intake-quickstart.md` | Added the baseline checkpoint to new-case instructions and review checks. | C001-C006 |
| `templates/intake-review.md` | Added structured lore-review, baseline, range, outcomes, tier, trigger, and count prompts. | C002-C006 |
| `development/intake-reviews/README.md` | Directed every new lore review to complete baseline evaluation. | C001, C006 |
| `CONTRIBUTING.md` | Added baseline evaluation to the contribution sequence. | C001, C006 |
| `AGENTS.md` | Made baseline recording and fresh Tier 3 triggers mandatory agent steps. | C001-C006 |
| `scripts/validate_repository.py` | Added prospective lore-review schema and deterministic trigger validation without semantic approval. | C002-C007 |
| `tests/fixtures.py` | Added process/lore review and valid audit-baseline fixture support. | C007 |
| `tests/test_validate_repository.py` | Added focused regression cases for baseline fields and deterministic Tier 3 relationships. | C007 |
| `tests/README.md` | Documented audit-baseline validator coverage and its semantic boundary. | C007 |
| `development/indexes/claim-index.json` | Regenerated navigation for the eight A01 claims. | C001-C008 |

## Files deliberately unchanged

- Canon, story, and design content: no lore authority is granted.
- Historical submissions, merged reviews, and completed audit reports: the
  prospective policy does not rewrite them.
- Claim authority, disposition, supersession, and exceptional-record state.
- Deprecated-page, supersession-cycle, and general-YAML policy questions.
- The minimal front-matter parser: new field names avoid digits rather than
  broadening the deferred general-YAML policy.
- GitHub workflows and external automation.

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; A01 supplies direct policy authority.
- **Retired ideas:** None.

## Verification

- [x] The clarification is preserved in immutable A01 before policy mutation.
- [x] Every substantive clarification claim has a controlled disposition.
- [x] Every claim uses explicit authority.
- [x] Targeted policy context was generated and inspected.
- [x] New lore reviews are prompted and validated prospectively.
- [x] Mandatory Tier 3 relationships are validated where deterministic.
- [x] Semantic ambiguity remains a reviewer judgment rather than a mechanical
  inference.
- [x] All 149 standard-library tests pass using the installed Python 3.13.14
  runtime because `python` is not available on `PATH`.
- [x] Repository validation passes against `origin/main` across 163 Markdown
  files.
- [x] The claim index is current with 292 claims.
- [x] `git diff --check` passes and the complete diff is clean and scoped.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** Pending update to draft PR #25
- **Outstanding actions:** Commit and push the coherent clarification update,
  then require both GitHub checks to pass on draft PR #25.

## Amendments

None.
