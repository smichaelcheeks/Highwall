---
title: Repository Integrity CI Decisions
type: conversation-addendum
case_id: CASE-2026-08-03-REPOSITORY-FOUNDATION
submission_id: CASE-2026-08-03-REPOSITORY-FOUNDATION-A03
sequence: 3
submitted_on: 2026-08-03
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
parent_submission: CASE-2026-08-03-REPOSITORY-FOUNDATION-A02
supersedes_claims: []
related:
  - "../../references/git-workflow.md"
---

# Repository Integrity CI Decisions

## Conversation scope

- **Case:** `CASE-2026-08-03-REPOSITORY-FOUNDATION`
- **Parent submission:** `CASE-2026-08-03-REPOSITORY-FOUNDATION-A02`
- **Session mode:** `direct-integration`
- **Period or session:** PR #1 review on 2026-08-03

## Authority checkpoint

The author explicitly approved adding appropriate CI checks after reviewing the proposed categories.

## Confirmed decisions and additions

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C001 — Add deterministic repository validation

- **Decision:** Add a blocking repository-integrity job for internal links, canon front matter, intake relationships, controlled dispositions, required development records, and merged-submission immutability.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** The validator should use only the Python standard library so repository integrity does not depend on a package ecosystem.

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C002 — Add restrained Markdown linting

- **Decision:** Lint repository-maintained Markdown with non-substantive style rules while excluding immutable author submissions.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Formatting checks must not rewrite or reject submitted source documents.

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A03-C003 — Keep unstable checks non-blocking

- **Decision:** Do not make spelling or external-site availability blocking CI checks.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Fictional vocabulary makes generic spellcheck noisy, and external sites can fail independently of repository quality.

## Corrections and supersessions

None.

## Proposals retained for consideration

Scheduled external-link reporting may be added later if it proves useful.

## Open questions

Whether to make the CI jobs required through GitHub branch protection remains part of [`github-merge-policy.md`](../../development/open-questions/github-merge-policy.md).

## Expected repository effects

Add a GitHub Actions workflow, standard-library validator, restrained Markdown configuration, contributor command, and this intake audit.

## Transcript provenance

Summarized from the PR #1 review discussion on 2026-08-03.
