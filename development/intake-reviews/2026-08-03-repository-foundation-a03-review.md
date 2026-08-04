---
title: Repository Integrity CI Review
type: intake-review
status: complete
reviewed_on: 2026-08-03
submission: "../../intake/submissions/2026-08-03-repository-foundation-a03.md"
case_id: CASE-2026-08-03-REPOSITORY-FOUNDATION
submission_id: CASE-2026-08-03-REPOSITORY-FOUNDATION-A03
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../../development/open-questions/github-merge-policy.md"
---

# Repository Integrity CI Review

## Review scope

- **Submission:** [Repository Integrity CI Decisions](../../intake/submissions/2026-08-03-repository-foundation-a03.md)
- **Case:** `CASE-2026-08-03-REPOSITORY-FOUNDATION`
- **Submission ID:** `CASE-2026-08-03-REPOSITORY-FOUNDATION-A03`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Add deterministic, proportionate validation for the documentation and intake system.

## Files inspected

Repository standards, front-matter rules, intake workflow, Git workflow, all current intake submissions and reviews, local Git history, and current official action versions were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C001 | Add deterministic integrity validation. | Administrative | `explicit` | None | Manual validation already exists. | `create` | `.github/workflows/repository-integrity.yml`; `scripts/validate_repository.py` | Automation makes established invariants repeatable on every PR. |
| CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C002 | Add restrained Markdown linting. | Administrative | `explicit` | None | Repository uses portable Markdown. | `create` | `.markdownlint-cli2.yaml`; workflow Markdown job | Maintained documentation benefits from consistent syntax while submissions remain immutable. |
| CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C003 | Keep spelling and external links non-blocking. | Administrative | `explicit` | None | Fictional terms and external availability are inherently unstable. | `no-change` | No blocking jobs added | Omitting noisy checks is an intentional reliability decision. |

## Conversation checkpoint

### Established decisions

Add deterministic integrity and restrained Markdown checks.

### Proposals under consideration

Scheduled, non-blocking external-link reporting.

### Corrections and supersessions

None.

### Open questions

Whether these jobs become required branch-protection checks.

### Expected repository effects

CI runs on pull requests, pushes to `main`, and manual dispatch.

## Files changed

The Actions workflow, validator, Markdown configuration, contribution guide, Git workflow, A03, and this review.

## Files deliberately unchanged

| File or system | Reason | Claim IDs |
| --- | --- | --- |
| Intake submission prose | Immutable author source is excluded from style linting. | A03-C002 |
| External URLs | Availability is not a blocking repository invariant. | A03-C003 |
| Spelling | Fictional terminology would create unreliable failures. | A03-C003 |

## Exceptions created

- **Open questions:** Required-check enforcement remains in [`github-merge-policy.md`](../open-questions/github-merge-policy.md).
- **Proposals:** Scheduled external-link reporting may be considered later.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] The validator uses only the Python standard library.
- [x] Merged submission modifications are detected when a base ref is supplied.
- [x] Author submissions are excluded from Markdown style enforcement.
- [ ] The validator passes locally.
- [ ] The GitHub Actions jobs pass on PR #1.

## Outcome

- **Review status:** `in-progress`
- **Canon change-log entry:** None
- **Git commit:** Not yet committed
- **Outstanding actions:** Run local validation, push the workflow, and observe both PR checks.

## Amendments

None.
