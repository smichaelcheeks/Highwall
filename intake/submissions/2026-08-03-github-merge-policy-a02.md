---
title: Fresh Codex Canon Intake Readiness
type: conversation-addendum
case_id: CASE-2026-08-03-GITHUB-MERGE-POLICY
submission_id: CASE-2026-08-03-GITHUB-MERGE-POLICY-A02
sequence: 2
submitted_on: 2026-08-03
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
parent_submission: CASE-2026-08-03-GITHUB-MERGE-POLICY-A01
supersedes_claims: []
related:
  - "../../AGENTS.md"
  - "../../references/canon-intake-quickstart.md"
---

# Fresh Codex Canon Intake Readiness

## Conversation scope

- **Case:** `CASE-2026-08-03-GITHUB-MERGE-POLICY`
- **Parent submission:** `CASE-2026-08-03-GITHUB-MERGE-POLICY-A01`
- **Session mode:** `direct-integration`
- **Period or session:** Fresh-chat readiness discussion on 2026-08-03

## Authority checkpoint

The author explicitly approved completing the remaining setup recommended for safe canon intake from a fresh Codex chat.

## Confirmed decisions and additions

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C001 — Add mandatory Codex repository guidance

- **Decision:** Add a root `AGENTS.md` requiring fresh Codex sessions to follow canon safety, intake, branch, validation, and reporting rules.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** Contributor documentation alone is not sufficient durable guidance for a fresh Codex session.

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C002 — Add a canon-intake quick start

- **Decision:** Provide copyable prompts for established canon, working canon, and exploration, plus a concise expected workflow and review checklist.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** “Put this where it goes” is insufficient when authority is not otherwise explicit.

### CASE-2026-08-03-GITHUB-MERGE-POLICY-A02-C003 — Enable local Python validation

- **Decision:** Install Python 3.13 and the Microsoft Python tooling for VS Code so the repository validator can run before pushing.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** None
- **Context:** GitHub CI remains the final execution gate, but local feedback should be available.

## Corrections and supersessions

None.

## Proposals retained for consideration

None.

## Open questions

None for fresh-chat readiness.

## Expected repository effects

Add `AGENTS.md`, a canon-intake quick-start guide, navigation links, this addendum, and its review. Machine-level Python and VS Code installation is recorded here but not stored in repository configuration.

## Transcript provenance

Summarized from the fresh-chat readiness and Python setup discussion on 2026-08-03.
