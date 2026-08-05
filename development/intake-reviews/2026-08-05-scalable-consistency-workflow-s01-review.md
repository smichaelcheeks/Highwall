---
title: Scalable Consistency Workflow Review
type: intake-review
status: complete
reviewed_on: 2026-08-05
submission: "../../intake/submissions/2026-08-05-scalable-consistency-workflow-s01.md"
case_id: CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW
submission_id: CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
subjects:
  - repository-consistency
  - intake-workflow
domains:
  - administration
search_terms:
  - consistency
  - impact manifest
  - claim index
  - publication
authoritative_targets:
  - references/consistency-workflow.md
  - references/intake-workflow.md
  - references/git-workflow.md
related:
  - "../../references/consistency-workflow.md"
---

# Scalable Consistency Workflow Review

## Review scope

- **Submission:** [Scalable Consistency Workflow](../../intake/submissions/2026-08-05-scalable-consistency-workflow-s01.md)
- **Case:** `CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW`
- **Submission ID:** `CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Make ordinary consistency work proportional to the
  affected subjects while retaining deterministic full-repository validation
  and periodic semantic audits.

## Files inspected

Repository instructions, contribution rules, intake and Git workflows, review
templates, validator, GitHub workflow, existing review records, and current
repository indexes were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C001 | Require impact manifests on new intake reviews. | administrative | `explicit` | None | Reviews currently lack machine-readable scope metadata. | `update` | Review template, validator, and intake workflow | Stable subjects, domains, terms, and targets enable bounded discovery. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C002 | Use three consistency tiers. | administrative | `explicit` | None | Current guidance encourages broad inspection for every case. | `create` | `references/consistency-workflow.md` | Tiering preserves deterministic safety while bounding routine semantic review. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C003 | Generate a non-authoritative claim index. | administrative | `explicit` | None | Claims are distributed across review tables. | `create` | `scripts/build_claim_index.py`; `development/indexes/claim-index.json` | A deterministic navigation artifact makes prior-claim discovery cheaper without becoming canon. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C004 | Use controlled discovery metadata. | administrative | `explicit` | None | Canon has tags and relations, but reviews have no controlled impact vocabulary. | `update` | Review template, validator, and consistency workflow | Validated kebab-case subjects and controlled domains reduce naming drift. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C005 | Add a targeted context builder. | administrative | `explicit` | None | Context is currently assembled through repeated broad searches. | `create` | `scripts/build_case_context.py` | The tool assembles relevant claims, targets, matches, and backlinks before semantic review. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C006 | Use lightweight records for routine process-only maintenance. | administrative | `explicit` | None | CONTRIBUTING makes intake optional but gives no concrete lightweight path. | `create` | Maintenance template and consistency workflow | Routine non-lore work does not need full claim-level intake; major governance changes still do. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C007 | Use one-pass publication without check-result audit commits. | administrative | `explicit` | None | Prior cases repeatedly committed GitHub check outcomes, triggering duplicate runs. | `update` | Git workflow, review template, and agent instructions | GitHub remains the authority for check history; reviews and publication status are separated. |
| CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C008 | Run full semantic audits periodically and for high-risk changes. | administrative | `explicit` | None | No explicit cadence or risk trigger exists. | `create` | `references/consistency-workflow.md` | Periodic full review catches cross-domain drift without charging every small case for a repository-wide semantic pass. |

## Conversation checkpoint

### Established decisions

All eight administrative claims are established policy.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

None.

### Expected repository effects

Add scoped discovery metadata and tools, document tiered consistency review,
streamline maintenance and publication, and validate the generated index in CI.

## Files changed

- `.github/workflows/repository-integrity.yml`: rejects stale generated claim
  indexes in CI.
- `AGENTS.md` and `CONTRIBUTING.md`: require impact mapping, proportional
  semantic review, index verification, and one-pass publication reporting.
- `references/consistency-workflow.md`: defines impact manifests, three review
  tiers, the audit cadence, maintenance boundary, and publication boundary.
- `references/intake-workflow.md` and `references/git-workflow.md`: integrate
  scoped discovery and separate completed review from external publication.
- `references/README.md`, `templates/README.md`, `development/README.md`, and
  `development/intake-reviews/README.md`: expose the new workflow and records.
- `templates/intake-review.md`: adds the impact manifest and publication state.
- `templates/maintenance-review.md` and
  `development/maintenance-reviews/README.md`: provide the lightweight
  process-only path.
- `scripts/consistency_common.py`, `scripts/build_claim_index.py`, and
  `scripts/build_case_context.py`: generate the navigation index and targeted
  review context.
- `scripts/validate_repository.py`: validates prospective impact manifests
  while grandfathering merged historical reviews.
- `development/indexes/README.md` and
  `development/indexes/claim-index.json`: document and contain the generated,
  non-authoritative claim index.
- The submission and this review preserve the instruction and its processing
  decisions.

## Files deliberately unchanged

- Canon, story, and design content: this case grants no lore authority.
- Existing merged reviews: new impact-manifest requirements are prospective.
- `development/canon-changes.md`: no canon facts change.

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; this review records direct approval.
- **Retired ideas:** None.

## Verification

- [x] Every substantive policy claim has a disposition.
- [x] The complete instruction is preserved in an immutable submission.
- [x] New review impact manifests are validated.
- [x] Claim index generation and stale-index detection pass.
- [x] Targeted context generation returns the expected policy neighborhood and
  indexed claims.
- [x] Historical reviews remain valid without retroactive manifests.
- [x] Relative links resolve.
- [x] Repository validation and `git diff --check` pass using the bundled
  Python runtime; `python` is not on this Windows PATH.
- [x] The complete diff matches this review and contains no lore changes.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** Pending
- **Outstanding actions:** Publish and verify GitHub checks.

## Amendments

None.
