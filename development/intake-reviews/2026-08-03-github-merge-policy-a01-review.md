---
title: GitHub Repository Safety Settings Review
type: intake-review
status: complete
reviewed_on: 2026-08-03
submission: "../../intake/submissions/2026-08-03-github-merge-policy-a01.md"
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-A01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
related:
  - "../open-questions/main-branch-protection.md"
---

# GitHub Repository Safety Settings Review

## Review scope

- **Submission:** [GitHub Repository Safety Settings](../../intake/submissions/2026-08-03-github-merge-policy-a01.md)
- **Case:** `CASE-2026-08-03-GITHUB-MERGE-POLICY`
- **Submission ID:** `CASE-2026-08-03-GITHUB-MERGE-POLICY-A01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Apply the approved repository-surface, squash-history, and Actions supply-chain settings.

## Files inspected

The repository settings API, Actions permissions, current workflow action references, GitHub plan limitations, Git workflow, and branch-protection question were inspected.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C001 | Require immutable Actions and reviewed updates. | Administrative | `explicit` | None | Actions used movable major-version tags; SHA pinning was disabled. | `update` | Workflow, Dependabot, GitHub Actions setting, and Git workflow | Immutable references reduce supply-chain risk while Dependabot preserves maintainability. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C002 | Use PR title and body for squash commits. | Administrative | `explicit` | None | Defaults used commit-derived titles and messages. | `update` | GitHub merge settings and Git workflow | The reviewed PR description is the clearest accepted change record. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C003 | Keep Issues and disable Projects, Wiki, and Discussions. | Administrative | `explicit` | None | Projects was enabled; other selected surfaces already matched policy. | `update` | GitHub repository settings and Git workflow | Avoid parallel documentation surfaces while retaining issue tracking. |
| CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C004 | Keep the repository private. | Administrative | `explicit` | None | Private visibility blocks branch protection under the current plan. | `no-change` | Repository visibility and branch-protection question | Privacy takes priority over obtaining enforcement features. |

## Conversation checkpoint

### Established decisions

Immutable Actions, Dependabot updates, standardized squash metadata, limited auxiliary surfaces, and continued private visibility.

### Proposals under consideration

None.

### Corrections and supersessions

None.

### Open questions

Branch-protection enforcement if availability changes.

### Expected repository effects

Update workflow references, Dependabot, repository settings, and policy documentation.

## Files changed

The integrity workflow, Dependabot configuration, Git workflow, branch-protection question, A01, and this review.

## Files deliberately unchanged

| File or setting | Reason | Claim IDs |
| --- | --- | --- |
| Repository visibility | Explicit decision to remain private. | A01-C004 |
| Issues | Already enabled and retained. | A01-C003 |
| Wiki and Discussions | Already disabled. | A01-C003 |

## Exceptions created

- **Open questions:** Branch-protection enforcement remains open.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [x] Action tags resolve to the pinned commits recorded in the workflow.
- [x] Workflow token permissions remain read-only.
- [x] Pinned workflow checks pass on PR #2.
- [x] SHA pinning is required in GitHub settings.
- [x] Squash metadata settings match policy.
- [x] Projects is disabled; Issues remains enabled.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None
- **Git commit:** `1481094ba2e8c84c0d9b87405e2c27fb35c08393`
- **Outstanding actions:** None. Publication is tracked in [PR #2](https://github.com/smichaelcheeks/Highwall/pull/2).

## Amendments

None.
