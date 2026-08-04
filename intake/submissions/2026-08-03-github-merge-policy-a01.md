---
title: GitHub Repository Safety Settings
type: conversation-addendum
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-A01
sequence: 1
submitted_on: 2026-08-03
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
parent_submission: CASE-2026-08-03-GITHUB-MERGE-POLICY-S01
supersedes_claims: []
related:
  - "../../references/git-workflow.md"
  - "../../development/open-questions/main-branch-protection.md"
---

# GitHub Repository Safety Settings

## Conversation scope

- **Case:** `CASE-2026-08-03-GITHUB-MERGE-POLICY`
- **Parent submission:** `CASE-2026-08-03-GITHUB-MERGE-POLICY-S01`
- **Session mode:** `direct-integration`
- **Period or session:** PR #2 policy discussion on 2026-08-03

## Authority checkpoint

The author explicitly approved the recommended Actions security, squash metadata, and repository feature settings.

## Confirmed decisions and additions

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C001 — Pin Actions and automate reviewed updates

- **Decision:** Pin every GitHub Action to a full immutable commit SHA, require SHA pinning in repository settings, and use monthly Dependabot PRs for GitHub Actions updates.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Version comments remain beside SHAs for human readability.

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C002 — Standardize squash metadata

- **Decision:** Use the PR title and body as the default squash commit title and message.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Accepted Git history should reflect the reviewed PR description.

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C003 — Limit auxiliary GitHub surfaces

- **Decision:** Keep Issues enabled and disable Projects, Wiki, and Discussions.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** The repository remains the authoritative documentation surface.

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A01-C004 — Keep the repository private

- **Decision:** Do not make Highwall public merely to obtain branch-protection features unavailable on the current plan.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Revisit protection if the plan or visibility changes for independent reasons.

## Corrections and supersessions

None.

## Proposals retained for consideration

None.

## Open questions

Branch-protection enforcement remains tracked in [`main-branch-protection.md`](../../development/open-questions/main-branch-protection.md).

## Expected repository effects

Pin workflow actions, add Dependabot configuration, update Git workflow policy, and apply the approved repository settings.

## Transcript provenance

Summarized from the PR #2 policy discussion on 2026-08-03.
