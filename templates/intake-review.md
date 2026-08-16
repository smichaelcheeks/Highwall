---
title: TODO
type: intake-review
status: in-progress
reviewed_on: YYYY-MM-DD
submission: "../../intake/submissions/TODO.md"
case_id: CASE-YYYY-MM-DD-SLUG
submission_id: CASE-YYYY-MM-DD-SLUG-S01
authority: classify
session_mode: exploration
reviewer: TODO
lore_review: TODO
semantic_audit_baseline: TODO
audit_git_range: TODO
incremental_context_generated: pending
consistency_tier_required: TODO
consistency_tier_performed: pending
tier_three_trigger_active: pending
completed_canon_cases_since_tier_three: pending
subjects:
  - TODO
domains:
  - TODO
search_terms:
  - TODO
authoritative_targets:
  - TODO
prior_audited_relationships: []
audit_results_carried_forward: []
audit_results_revalidated: []
audit_results_invalidated: []
audit_results_widened: []
tier_three_triggers: []
related: []
---

# TODO: Intake review title

## Review scope

- **Submission:** [TODO](../../intake/submissions/TODO.md)
- **Case:** TODO
- **Submission ID:** TODO
- **Session mode:** TODO: `exploration`, `canon-authoring`, or `direct-integration`
- **Authority conveyed:** TODO: `establish-canon`, `working-canon`, `establish-policy`, `proposal-only`, or `classify`
- **Review objective:** TODO

The front-matter impact manifest is required for new reviews. Use stable
kebab-case subject IDs, controlled domains from
`../../references/consistency-workflow.md`, literal search terms, and
repository-relative authoritative targets.

## Audit baseline evaluation

- **Lore review:** TODO: `true` for a new lore intake review; otherwise `false`.
- **Latest applicable semantic-audit baseline:** TODO: full commit hash or `none`.
- **Git range examined:** TODO: `BASELINE..HEAD` using full commit hashes, or
  `fresh-tier-3-required` when no usable baseline exists.
- **Incremental context generated:** TODO: `yes` or `no`.
- **Prior audited relationships considered:** TODO: identify relationships or
  `None`.
- **Results carried forward:** TODO: relationship IDs or `None`.
- **Results revalidated:** TODO: relationship IDs or `None`.
- **Results invalidated:** TODO: relationship IDs or `None`.
- **Results widened:** TODO: relationship IDs and Tier 2 or Tier 3 scope, or
  `None`.
- **Consistency tier required:** TODO: `tier-2` or `tier-3`.
- **Consistency tier performed:** TODO: `tier-2` or `tier-3`.
- **Tier 3 trigger active:** TODO: `yes` or `no`.
- **Tier 3 triggers:** TODO: controlled trigger IDs or `None`.
- **Completed canon cases since latest comprehensive Tier 3 baseline:** TODO:
  nonnegative integer or `unknown`.

Complete this section for every lore review and mirror its controlled values in
front matter. Put each exact prior relationship ID in exactly one result list;
record evidence and explanation in this section. Use Git history and completed
review records to identify the baseline, range, and case count. The canon change
log and impact manifests may assist discovery but are not sufficient evidence
by themselves. Generate and inspect incremental context when a reliable prior
baseline exists. Apply semantic judgment to ambiguous dependencies or triggers;
an incomplete, missing, or unreliable baseline requires a fresh Tier 3 review.

## Files inspected

TODO: List authoritative and related pages searched during review.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-YYYY-MM-DD-SLUG-S01-C001 | TODO | TODO | TODO | None | TODO | TODO | TODO | TODO |

Use only dispositions defined in `../../references/intake-workflow.md` after this template is copied into `development/intake-reviews/`. Every substantive claim must appear in this table, including claims producing no change.

## Conversation checkpoint

### Established decisions

TODO or `None`.

### Proposals under consideration

TODO or `None`.

### Corrections and supersessions

TODO or `None`.

### Open questions

TODO or `None`.

### Expected repository effects

TODO or `None`.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| TODO | TODO | TODO |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| TODO | TODO | TODO |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [ ] Every substantive claim has a disposition.
- [ ] Every integrated conversational claim exists in an immutable addendum.
- [ ] Each claim records an explicit, session-mode, source-authority, or pending authority basis.
- [ ] Superseded claims remain traceable.
- [ ] The original submission remains unchanged.
- [ ] All new facts have explicit authority and provenance.
- [ ] Maintained knowledge claims are distinct from intake claims and bind
      exact prose, lifecycle, subjects, and review-claim provenance.
- [ ] Every changed schema-v2 object has an appended local history event.
- [ ] Canon and story information remain separate.
- [ ] Beliefs and disputed claims are attributed.
- [ ] No contradiction was silently resolved.
- [ ] No authoritative explanation was unnecessarily duplicated.
- [ ] Relative links resolve.
- [ ] Required front matter is present.
- [ ] The Git diff matches the recorded file list.
- [ ] Significant canon changes are in the canon change log.
- [ ] The impact manifest covers every affected subject, domain, search term,
  and authoritative target.
- [ ] Targeted context was generated and inspected before widening the search.
- [ ] Lore-review status and audit-baseline fields are complete.
- [ ] Git history and review records support the baseline, range, trigger, and
  completed-case evaluation.
- [ ] Every prior audited relationship considered has a recorded audit outcome.
- [ ] The required consistency tier was performed, including any mandatory
  fresh Tier 3 audit.

## Outcome

- **Review status:** TODO: `in-progress`, `awaiting-confirmation`, `awaiting-decision`, `complete`, or `blocked`
- **Canon change-log entry:** TODO or `None`
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** TODO: `pending`, PR link, or merged PR link
- **Outstanding actions:** TODO or `None`

## Amendments

None.
