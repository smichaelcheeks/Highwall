---
title: Fresh Codex Canon Intake Readiness Review
type: intake-review
status: in-progress
reviewed_on: 2026-08-03
submission: "../../intake/submissions/2026-08-03-github-merge-policy-a02.md"
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-A02
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../../AGENTS.md"
  - "../../references/canon-intake-quickstart.md"
---

# Fresh Codex Canon Intake Readiness Review

## Review scope

- **Submission:** [Fresh Codex Canon Intake Readiness](../../intake/submissions/2026-08-03-github-merge-policy-a02.md)
- **Case:** `CASE-2026-08-03-GITHUB-MERGE-POLICY`
- **Submission ID:** `CASE-2026-08-03-GITHUB-MERGE-POLICY-A02`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Make safe canon intake reproducible from a fresh Codex session.

## Files inspected

The README, contribution rules, intake workflow, Git workflow, templates, current machine Python and VS Code configuration, and Codex durable-instruction guidance were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C001 | Add mandatory fresh-session Codex guidance. | Administrative | `explicit` | None | No root `AGENTS.md` existed. | `create` | `AGENTS.md` | Durable repository guidance ensures new sessions load the required workflow. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C002 | Add a canon-intake quick start. | Administrative | `explicit` | None | Workflow documentation existed but lacked a concise entry point. | `create` | `references/canon-intake-quickstart.md` | Copyable authority-specific prompts reduce ambiguity without weakening detailed standards. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C003 | Enable local Python validation in VS Code. | Administrative | `explicit` | None | Python was absent locally; CI provisioned it remotely. | `update` | Windows user environment and VS Code extensions | Matching Python 3.13 enables the same validator before push. |

## Conversation checkpoint

### Established decisions

Root Codex guidance, fresh-chat quick start, and local Python validation.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

None for this addendum.

### Expected repository effects

Fresh Codex sessions receive mandatory rules and an actionable canon-intake entry point.

## Files changed

`AGENTS.md`, README navigation, reference index, canon-intake quick start, A02, and this review.

## Files deliberately unchanged

| File or setting | Reason | Claim IDs |
| --- | --- | --- |
| Canon pages | This addendum changes process only. | A02-C001 through A02-C003 |
| Python repository dependencies | The validator uses only the standard library. | A02-C003 |

## Exceptions created

None.

## Verification

- [x] Python 3.13.14 and pip are installed for the Windows user.
- [x] Microsoft Python, Pylance, debugger, and environment extensions are installed in VS Code.
- [x] The repository validator passes locally.
- [ ] Repository links and Markdown style pass after adding the guidance.
- [ ] Both GitHub checks pass on PR #2.

## Outcome

- **Review status:** `in-progress`
- **Canon change-log entry:** None
- **Git commit:** Not yet committed
- **Outstanding actions:** Validate, push, and observe PR #2 checks.

## Amendments

None.
