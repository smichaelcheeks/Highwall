---
title: GitHub Merge and Branch-Deletion Policy Review
type: intake-review
status: complete
reviewed_on: 2026-08-03
submission: "../../intake/submissions/2026-08-03-github-merge-policy-s01.md"
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../open-questions/github-merge-policy.md"
  - "../open-questions/main-branch-protection.md"
---

# GitHub Merge and Branch-Deletion Policy Review

## Review scope

- **Submission:** [GitHub Merge and Branch-Deletion Policy](../../intake/submissions/2026-08-03-github-merge-policy-s01.md)
- **Case:** `CASE-2026-08-03-GITHUB-MERGE-POLICY`
- **Submission ID:** `CASE-2026-08-03-GITHUB-MERGE-POLICY-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Apply and document the approved GitHub merge and merged-branch policy.

## Files inspected

PR #1, local and remote branches, current GitHub repository merge settings, the Git workflow, and the existing merge-policy open question were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-S01-C001 | Automatically delete merged remote branches and clean local branches after verification. | Administrative | `explicit` | None | PR #1 was merged and both branch copies remained. | `update` | GitHub setting, `references/git-workflow.md`, and branch state | The approved policy reduces clutter without losing PR or Git provenance. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-S01-C002 | Use squash by default, retain regular merges, and disable rebase merges. | Administrative | `explicit` | None | All three methods were previously enabled. | `update` | GitHub settings and `references/git-workflow.md` | This preserves a clear default while allowing exceptional commit provenance. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-S01-C003 | Resolve the tracked merge-policy question. | Administrative | `explicit` | None | The development record was pending. | `update` | `development/open-questions/github-merge-policy.md` | The approved and applied settings answer the recorded questions in scope. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-S01-C004 | Enable required reviews and status checks now. | Administrative | `pending` | None | No enforcement decision was made. | `defer` | [`development/open-questions/main-branch-protection.md`](../open-questions/main-branch-protection.md) | Remaining protection choices require separate approval. |

## Conversation checkpoint

### Established decisions

Automatic merged-branch deletion, local cleanup after verification, squash as default, regular merges retained, and rebase merges disabled.

### Proposals under consideration

Required reviews, required checks, and direct-push protection.

### Corrections and supersessions

None.

### Open questions

[Main branch protection enforcement](../open-questions/main-branch-protection.md) remains unresolved.

### Expected repository effects

Update remote settings, delete the merged foundation branch, resolve the merge-method portion of the open question, and document the policy.

## Files changed

The Git workflow, merge-policy question, this submission, and this review.

## Files deliberately unchanged

| File or setting | Reason | Claim IDs |
| --- | --- | --- |
| Required reviews and checks | No explicit enforcement decision was made. | S01-C004 |

## Exceptions created

- **Open questions:** [Main branch protection enforcement](../open-questions/main-branch-protection.md) remains unresolved.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] GitHub automatically deletes merged head branches.
- [x] Squash and regular merges are enabled.
- [x] Rebase merges are disabled.
- [x] The merged foundation branch is deleted locally and remotely.
- [x] `main` was synchronized and clean before branch deletion.
- [ ] Repository integrity and Markdown CI pass on the follow-up PR.

## Outcome

- **Review status:** `in-progress`
- **Canon change-log entry:** None
- **Git commit:** Not yet committed
- **Outstanding actions:** Publish and validate the follow-up PR.

## Amendments

None.
