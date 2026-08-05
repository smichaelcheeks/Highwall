---
title: Intake Completeness and GitHub Approval Workflow Review
type: intake-review
status: complete
reviewed_on: 2026-08-04
submission: "../../intake/submissions/2026-08-04-intake-completeness-github-approvals-s01.md"
case_id: CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS
submission_id: CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../../references/intake-workflow.md"
  - "../../references/git-workflow.md"
---

# Intake Completeness and GitHub Approval Workflow Review

## Review scope

- **Submission:** [Intake Completeness and GitHub Approval Workflow](../../intake/submissions/2026-08-04-intake-completeness-github-approvals-s01.md)
- **Case:** `CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS`
- **Submission ID:** `CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Prevent partial intake from truncated transmissions and
  streamline credential-backed GitHub CLI work without weakening sandbox
  protections.

## Files inspected

Repository-wide agent instructions, intake and Git workflows, canon intake
quickstart, intake and addendum templates, the lore-seed template, submission
and review indexes, the repository validator, the current sandbox behavior, and
the completed regional geography case were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01-C001 | Require an end marker or explicit completeness confirmation and stop before repository mutations when a transmission is incomplete or suspicious. | administrative | `explicit` | None | Current rules prohibit guessing but contain no pre-intake transmission gate. | `update` | `AGENTS.md`; `references/intake-workflow.md`; `references/canon-intake-quickstart.md`; `templates/lore-seed.md` | A pre-mutation gate prevents a partial source from becoming an immutable intake record or partial canon update. |
| CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01-C002 | Record and mechanically validate transmission completeness for every newly added seed or addendum. | administrative | `explicit` | None | Intake metadata and validation currently do not represent source completeness. | `update` | `templates/intake-submission.md`; `templates/conversation-addendum.md`; `scripts/validate_repository.py`; intake documentation | New-only validation enforces the policy without retroactively invalidating merged submissions. |
| CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01-C003 | Use first-attempt scoped escalation for Windows `gh` commands needing Credential Manager and retain narrow reusable approvals instead of disabling the sandbox. | administrative | `explicit` | None | The regional case showed sandboxed `gh` could not read the keyring while escalated `gh` succeeded; `git push` already had its own approval. | `update` | `AGENTS.md`; `references/git-workflow.md` | The policy removes a known failed retry while preserving least-privilege boundaries and explicit authorization for external mutations. |

## Conversation checkpoint

### Established decisions

All three administrative claims are established repository policy.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

None.

### Expected repository effects

Add a completeness gate and metadata, enforce it for new submissions, document
the author-facing terminator, and route Windows credential-backed `gh`
operations through scoped escalation on the first attempt.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-04-intake-completeness-github-approvals-s01.md` | Preserve the approved policy instruction. | C001-C003 |
| `development/intake-reviews/2026-08-04-intake-completeness-github-approvals-s01-review.md` | Record policy dispositions and verification. | C001-C003 |
| `AGENTS.md`; `CONTRIBUTING.md` | Make the completeness gate and Windows `gh` route mandatory in contributor guidance. | C001-C003 |
| `references/intake-workflow.md`; `references/canon-intake-quickstart.md` | Define intake completeness and fresh-chat behavior. | C001-C002 |
| `templates/lore-seed.md`; `templates/intake-submission.md`; `templates/conversation-addendum.md` | Add author marker and completion metadata. | C001-C002 |
| `intake/submissions/README.md` | Document required metadata for new submissions. | C002 |
| `scripts/validate_repository.py` | Enforce completeness fields for submissions absent from the base ref. | C002 |
| `references/git-workflow.md` | Document scoped Windows Credential Manager escalation. | C003 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| Existing merged submissions | New-only validation preserves immutable historical records. | C002 |
| Codex global configuration | Repository policy cannot safely disable or broaden the product sandbox; reusable approvals remain user-controlled. | C003 |
| Canon, story, and design content | This case establishes process only and grants no lore authority. | C001-C003 |
| `development/canon-changes.md` | No canon fact changes. | C001-C003 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; this intake audit records direct approval.
- **Retired ideas:** None.

## Verification

- [x] Every substantive policy claim has a disposition.
- [x] The approved conversation is preserved in an immutable submission.
- [x] Each claim records an explicit authority basis.
- [x] Existing merged submissions remain unchanged.
- [x] No lore authority is granted or exercised.
- [x] Sandbox protections remain enabled.
- [x] New submissions without completeness metadata fail validation.
- [x] `end-marker` submissions without the marker fail validation.
- [x] Valid new submissions and historical submissions pass validation.
- [x] Relative links resolve.
- [x] The Git diff matches the recorded file list.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None
- **Git commit:** `bd845c067660b66a470754c16c1f771b5742b2f2`
- **Outstanding actions:** None. Publication is tracked in
  [PR #9](https://github.com/smichaelcheeks/Highwall/pull/9), and both required
  GitHub checks pass.

## Amendments

None.
