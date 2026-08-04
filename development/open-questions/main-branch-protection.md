---
title: Main Branch Protection Enforcement
type: open-question
status: open
date_opened: 2026-08-03
related:
  - "../../references/git-workflow.md"
  - "github-merge-policy.md"
  - "../../intake/submissions/2026-08-03-github-merge-policy-s01.md"
---

# Main Branch Protection Enforcement

## Context

The repository has passing integrity and Markdown CI, but GitHub does not currently require those checks, a pull request, or an approving review before changes reach `main`.

## Why this matters

Enforcement can prevent accidental direct pushes or premature merges. This repository is currently maintained primarily by one author with AI assistance, so requirements should provide safety without creating an impossible self-review rule.

## Constraints

- CI jobs exist and are currently reliable.
- The author must retain a practical way to merge reviewed work.
- Canon-changing work should remain auditable through pull requests.
- Settings must not be changed without explicit approval.

## Possible answers

The following possibilities are unapproved:

- Require pull requests and passing CI but no independent approval.
- Block direct pushes to `main` while allowing repository-administrator bypass for emergencies.
- Require an approving review only after additional human collaborators join.
- Leave enforcement disabled and rely on documented procedure.

## Affected pages

- [`../../references/git-workflow.md`](../../references/git-workflow.md)
- GitHub rulesets or branch-protection settings

## Resolution

Pending.
