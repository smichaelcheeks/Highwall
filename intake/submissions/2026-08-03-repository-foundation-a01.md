---
title: Auditable Intake Workflow Decisions
type: conversation-addendum
case_id: CASE-2026-08-03-REPOSITORY-FOUNDATION
submission_id: CASE-2026-08-03-REPOSITORY-FOUNDATION-A01
sequence: 1
submitted_on: 2026-08-03
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
parent_submission: CASE-2026-08-03-REPOSITORY-FOUNDATION-S01
supersedes_claims: []
related: []
---

# Auditable Intake Workflow Decisions

## Conversation scope

- **Case:** `CASE-2026-08-03-REPOSITORY-FOUNDATION`
- **Parent submission:** `CASE-2026-08-03-REPOSITORY-FOUNDATION-S01`
- **Session mode:** `direct-integration`
- **Period or session:** Repository-foundation discussion on 2026-08-03

## Authority checkpoint

The author explicitly approved implementing an intake workflow in which new information arrives in dedicated files and every decision to change or not change repository content is auditable.

## Confirmed decisions and additions

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A01-C001 — Preserve submissions independently

- **Decision:** Store each batch of new information as an immutable intake submission after review begins.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Corrections and additions arrive as later submissions instead of rewriting source history.

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A01-C002 — Review every substantive claim

- **Decision:** Create a separate claim-level review recording classification, disposition, target, evidence, and concise rationale for every substantive claim, including claims producing no change.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Source material and reviewer conclusions must remain distinguishable.

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A01-C003 — Use controlled dispositions

- **Decision:** Use the dispositions `create`, `update`, `no-change`, `link-only`, `defer`, `conflict`, `retire`, and `out-of-scope`.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** No-change decisions require reasons just as file-changing decisions do.

### CASE-2026-08-03-REPOSITORY-FOUNDATION-A01-C004 — Connect provenance and change history

- **Decision:** Link intake reviews to affected pages and concise canon change-log entries, and record relevant Git history.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Detailed rationale belongs in the review rather than being duplicated in the change log.

## Corrections and supersessions

None.

## Proposals retained for consideration

None.

## Open questions

None.

## Expected repository effects

Create the intake structure, workflow documentation, submission and review templates, review archive, controlled dispositions, and provenance metadata.

## Transcript provenance

Retroactively summarized from the repository-foundation conversation of 2026-08-03. This addendum preserves confirmed outcomes rather than reproducing the complete transcript.
