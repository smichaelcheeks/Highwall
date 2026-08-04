---
title: Author-Facing Lore Seed Template Review
type: intake-review
status: in-progress
reviewed_on: 2026-08-04
submission: "../../intake/submissions/2026-08-04-lore-seed-template-s01.md"
case_id: CASE-2026-08-04-LORE-SEED-TEMPLATE
submission_id: CASE-2026-08-04-LORE-SEED-TEMPLATE-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../../templates/lore-seed.md"
  - "../../references/canon-intake-quickstart.md"
---

# Author-Facing Lore Seed Template Review

## Review scope

- **Submission:** [Author-Facing Lore Seed Template](../../intake/submissions/2026-08-04-lore-seed-template-s01.md)
- **Case:** `CASE-2026-08-04-LORE-SEED-TEMPLATE`
- **Submission ID:** `CASE-2026-08-04-LORE-SEED-TEMPLATE-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Provide a safe, reusable way to prepare lore with a conversational assistant before formal repository intake.

## Files inspected

The repository README, contribution rules, repository standards, intake
workflow, front-matter rules, Git workflow, canon-intake quick start, template
index, and submission, addendum, and review templates were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-04-LORE-SEED-TEMPLATE-S01-C001 | Add a reusable assistant instruction for preparing raw lore. | Administrative | `explicit` | None | Existing templates begin at repository intake or authoritative-page creation. | `create` | `templates/lore-seed.md` | A pre-intake prompt fills the identified authoring gap without changing intake authority. |
| CASE-2026-08-04-LORE-SEED-TEMPLATE-S01-C002 | Make authority and information boundaries explicit in the prepared seed. | Administrative | `explicit` | None | Repository standards distinguish truth, belief, story, and development material. | `create` | `templates/lore-seed.md` | Carrying those distinctions into seed preparation reduces later ambiguity. |
| CASE-2026-08-04-LORE-SEED-TEMPLATE-S01-C003 | Prevent the drafting assistant from inventing gaps or repository metadata. | Administrative | `explicit` | None | Canon safety reserves interpretation, IDs, and dispositions for audited intake. | `create` | `templates/lore-seed.md` | Explicit constraints preserve source fidelity and responsibility boundaries. |
| CASE-2026-08-04-LORE-SEED-TEMPLATE-S01-C004 | Connect the preparation template to the existing intake workflow. | Administrative | `explicit` | None | The canon-intake quick start currently begins with an already prepared seed. | `update` | `templates/README.md`; `references/canon-intake-quickstart.md` | Cross-links explain when to use each template without duplicating the intake procedure. |

## Conversation checkpoint

### Established decisions

Create the proposed author-facing lore-seed template and integrate it with the
existing intake documentation.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

None.

### Expected repository effects

One new author-facing template, two navigation updates, and this case's audit
records. No canon or story pages change.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `templates/lore-seed.md` | Add the assistant prompt, structured output format, and intake handoff. | S01-C001 through S01-C003 |
| `templates/README.md` | Distinguish pre-intake authoring from repository intake. | S01-C004 |
| `references/canon-intake-quickstart.md` | Link the optional preparation step. | S01-C004 |
| `intake/submissions/2026-08-04-lore-seed-template-s01.md` | Preserve the author instruction and approved scope. | S01-C001 through S01-C004 |
| `development/intake-reviews/2026-08-04-lore-seed-template-s01-review.md` | Record claim-level decisions and verification. | S01-C001 through S01-C004 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| `templates/intake-submission.md` | It remains the internal archival wrapper and already serves that role. | S01-C001 through S01-C004 |
| `canon/` and `story/` | This case changes process only and supplies no setting or narrative facts. | S01-C001 through S01-C004 |
| `development/canon-changes.md` | No canon content changes. | S01-C001 through S01-C004 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] Every integrated conversational claim exists in an immutable submission.
- [x] Each claim records an explicit authority basis.
- [x] The original submission remains unchanged after review begins.
- [x] No setting or story facts were introduced.
- [x] Canon, story, belief, and proposal boundaries remain distinct.
- [x] No contradiction was silently resolved.
- [x] Repository roles are linked rather than duplicated.
- [x] Relative links resolve and repository validation passes.
- [ ] Markdown style passes.
- [x] The Git diff matches the recorded file list.
- [ ] Both GitHub checks pass on the draft PR.

## Outcome

- **Review status:** `in-progress`
- **Canon change-log entry:** None
- **Git commit:** Not yet committed
- **Outstanding actions:** Commit, push, open a draft PR, and verify both GitHub checks, including Markdown style.

## Amendments

None.
