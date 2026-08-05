---
title: Lore Seed Authoring Boundaries Review
type: intake-review
status: complete
reviewed_on: 2026-08-04
submission: "../../intake/submissions/2026-08-04-lore-seed-boundaries-s01.md"
case_id: CASE-2026-08-04-LORE-SEED-BOUNDARIES
submission_id: CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../../templates/lore-seed.md"
  - "../../references/repository-standards.md"
---

# Lore Seed Authoring Boundaries Review

## Review scope

- **Submission:** [Lore Seed Authoring Boundaries](../../intake/submissions/2026-08-04-lore-seed-boundaries-s01.md)
- **Case:** `CASE-2026-08-04-LORE-SEED-BOUNDARIES`
- **Submission ID:** `CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Strengthen source fidelity, missing-information
  semantics, subject boundaries, truth levels, and real-world comparison
  handling in lore-seed authoring.

## Files inspected

The current lore-seed template, repository standards, design principles,
intake workflow, and the author's approved revised prompt were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C001 | Prefer author-supplied facts to polished prose and prohibit unsupplied explanatory or connective text. | administrative | `explicit` | None | The template prohibits invention but does not specifically constrain editorial connective prose. | `update` | `templates/lore-seed.md` | The approved rule directly addresses prose that can strengthen or invent claims. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C002 | Distinguish `Not established.`, `None.`, and `TODO:` according to whether information is absent, explicitly negative, or an actionable known gap. | administrative | `explicit` | None | Current guidance mentions TODO and unknowns but does not define these three states. | `update` | `templates/lore-seed.md`; `references/repository-standards.md` | Controlled semantics prevent absence of evidence from becoming a negative fact. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C003 | Keep facts owned by another planned seed brief and contextual rather than expanding or duplicating them. | administrative | `explicit` | None | Repository standards require one authoritative home, but the authoring prompt lacks a planned-seed boundary. | `update` | `templates/lore-seed.md` | Applying ownership discipline during authoring reduces later duplication. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C004 | Define objective truth as true regardless of personal or institutional belief. | administrative | `explicit` | None | The current placeholder says only “what is actually true.” | `update` | `templates/lore-seed.md` | The clarification makes truth-level separation explicit. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C005 | Sources must be author-supplied and inferred inspirations must not be added. | administrative | `explicit` | None | The current source placeholder is broad and does not prohibit inferred inspirations. | `update` | `templates/lore-seed.md` | The tightened wording protects provenance and source fidelity. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C006 | Real-world comparisons are out-of-world development or source context, never fictional facts, and remain outside canon sections. | administrative | `explicit` | None | Design guidance cannot establish setting facts, but real-world comparison handling is not explicit. | `update` | `templates/lore-seed.md`; `references/repository-standards.md` | The approved boundary prevents brainstorming analogues from becoming in-world entities or canon evidence. |
| CASE-2026-08-04-LORE-SEED-BOUNDARIES-S01-C007 | Retain the deterministic end-of-seed marker. | administrative | `explicit` | None | The marker is already required by merged policy. | `no-change` | `templates/lore-seed.md` | The revised prompt preserves the established completeness mechanism exactly. |

## Conversation checkpoint

### Established decisions

All seven administrative claims are approved repository policy.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

None.

### Expected repository effects

Update the lore-seed authoring prompt and output placeholders, and add durable
repository guidance for missing-information semantics and real-world
comparisons.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-04-lore-seed-boundaries-s01.md` | Preserve the approved authoring policy. | C001-C007 |
| `development/intake-reviews/2026-08-04-lore-seed-boundaries-s01-review.md` | Record all policy dispositions and verification. | C001-C007 |
| `templates/lore-seed.md` | Apply approved authoring rules and placeholder refinements. | C001-C007 |
| `references/repository-standards.md` | Define missing-information and real-world comparison boundaries. | C002; C006 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| Canon, story, and existing design pages | This case establishes authoring policy and does not independently integrate the Rome example as lore. | C006 |
| `development/canon-changes.md` | No canon facts change. | C001-C007 |
| Intake workflow and validator | The existing completeness marker and validation policy require no change. | C007 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; the intake audit records direct approval.
- **Retired ideas:** None.

## Verification

- [x] Every substantive policy claim has a disposition.
- [x] The author-approved source is preserved in an immutable submission.
- [x] Each claim records explicit authority.
- [x] The Rome example is not promoted to a separate canon claim.
- [x] Existing submissions remain unchanged.
- [x] Relative links resolve.
- [x] The Git diff matches the recorded file list.
- [x] Repository validation and `git diff --check` pass.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None
- **Git commit:** `ed093df7e1b6968fac5ac7275ae316782436ef08`
- **Outstanding actions:** None. Publication is tracked in
  [PR #10](https://github.com/smichaelcheeks/Highwall/pull/10), and both required
  GitHub checks pass.

## Amendments

None.
