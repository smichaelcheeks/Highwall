---
title: Intake Completeness and GitHub Approval Workflow
type: intake-submission
case_id: CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS
submission_id: CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS-S01
sequence: 1
submitted_on: 2026-08-04
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: explicit-confirmation
parent_submission: null
supersedes_claims: []
related:
  - "../../references/intake-workflow.md"
  - "../../references/git-workflow.md"
---

# Intake Completeness and GitHub Approval Workflow

## Author instruction

Establish the approved repository-process changes on a maintenance branch.
These changes govern intake transmission completeness and scoped GitHub CLI
execution; they grant no lore authority.

## Session mode

`direct-integration`

## Submitted information

The author asked:

> Now how can we update processes so that if a seed is incomplete, the next
> chat will wait for the rest of it? And also be able to skip the sandbox gh
> push issues

The proposed process was:

- Require a visible end-of-seed marker or explicit author confirmation that a
  transmission is complete before beginning repository intake.
- If the marker or confirmation is absent, or the source appears truncated,
  pause before creating a branch, submission, review, or authoritative change
  and request the remainder.
- Record transmission completeness in intake metadata and validate the fields
  for newly added submissions while preserving historical compatibility.
- On Windows, use scoped escalation on the first attempt for authenticated
  GitHub CLI operations that need Windows Credential Manager.
- Preserve the sandbox and use narrowly scoped, reusable command approvals
  rather than granting unrestricted shell access.

The author approved implementation:

> Ah OK, let's make that maintenance branch and make those changes

## Attachments or sources

None.

## Submission notes

The administrative conversation above is preserved as the authority for this
policy case. The author explicitly confirmed implementation, establishing that
the transmission is complete.
