---
title: GitHub Branch Protection and Merge Policy
type: open-question
status: open
date_opened: 2026-08-03
related:
  - "../../references/git-workflow.md"
  - "../../intake/submissions/2026-08-03-repository-foundation-a02.md"
---

# GitHub Branch Protection and Merge Policy

## Context

The repository now uses short-lived branches and draft pull requests for substantial changes. The preferred working practice is documented, but GitHub has not been configured to enforce branch protection, required reviews, status checks, or a single merge method.

## Why this matters

Remote enforcement can prevent accidental direct pushes or premature merges. Excessive enforcement can also add friction to a repository maintained primarily by one author with AI assistance.

## Constraints

- `main` should remain the accepted source of truth.
- Intake reviews should be complete before their changes merge.
- Semantic canon review matters even when Git reports no textual conflict.
- No remote repository setting should change without explicit author approval.
- Required status checks are useful only after corresponding CI workflows exist and are reliable.

## Possible answers

The following possibilities are unapproved:

- Protect `main` from direct pushes while allowing the author to merge without a second human reviewer.
- Require pull requests and passing documentation checks but no independent approval.
- Require at least one approving review if additional human collaborators join later.
- Allow squash merges only, or retain multiple merge methods and choose per case.
- Delete merged branches automatically.

## Affected pages

- [`../../references/git-workflow.md`](../../references/git-workflow.md)
- GitHub repository settings
- Future CI workflow documentation

## Resolution

Pending.
