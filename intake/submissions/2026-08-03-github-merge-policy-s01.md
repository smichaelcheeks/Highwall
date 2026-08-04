---
title: GitHub Merge and Branch-Deletion Policy
type: intake-submission
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-S01
sequence: 1
submitted_on: 2026-08-03
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
parent_submission: null
supersedes_claims: []
related:
  - "../../references/git-workflow.md"
  - "../../development/open-questions/github-merge-policy.md"
---

# GitHub Merge and Branch-Deletion Policy

## Author instruction

The author approved the recommended branch-deletion and merge-method policy after PR #1 merged.

## Submitted information

- Enable automatic deletion of merged remote head branches.
- Delete corresponding local branches after confirming `main` is synchronized and clean.
- Preserve open, unmerged, or undecided branches.
- Preserve abandoned work through a closed PR or development record before deletion.
- Do not reuse branch names.
- Use squash merging by default.
- Keep regular merge commits available for exceptional provenance needs.
- Disable rebase merging.

## Attachments or sources

- [PR #1](https://github.com/smichaelcheeks/Highwall/pull/1)

## Submission notes

The GitHub settings were applied directly following explicit approval. This submission records that administrative decision and grants no lore authority.
