---
title: Knowledge Object Schema V2 Audit Remediation
type: conversation-addendum
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
submission_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A02
sequence: 2
submitted_on: 2026-08-16
submitted_by: Shawn Cheeks
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: explicit-confirmation
parent_submission: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01
supersedes_claims: []
related:
  - 2026-08-16-knowledge-object-schema-v2-a01.md
---

# Knowledge Object Schema V2 Audit Remediation

## Conversation scope

- **Case:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2`
- **Parent submission:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01`
- **Session mode:** `direct-integration`
- **Period or session:** 2026-08-16 read-only completion-audit follow-up

## Authority checkpoint

After receiving the read-only audit showing three validator loopholes and an
overstated completion record, the author instructed:

> Let's address those gaps

This is a short, unambiguous administrative continuation of the established
schema-v2 case. It authorizes correction of the reported policy, validator,
test, and completion-record gaps on draft PR #41. It authorizes no lore,
story, maintained lore claim, historical backfill, or semantic relationship.

## Transmission completeness

The instruction identifies the complete remediation scope by reference to the
immediately preceding audit findings. Its controlled `completion_basis` is
therefore `explicit-confirmation`.

## Confirmed decisions and additions

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A02-C001 — Bind event authority to the changed object and state

- **Decision:** Validate every appended history event against the authority
  required by its object kind, owning record, relationship provenance policy,
  maintained-claim truth and authority, and the actual state component
  changed. Policy-only authority may govern graph registration, relocation,
  and administrative metadata but may not authorize canon or story content.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C002.
- **Context:** The audit proved that an `establish-policy` event could authorize
  a materially changed body on an established canon entity.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A02-C002 — Match dispositions to object actions

- **Decision:** Require provenance and history dispositions to agree with the
  action they authorize. Creation events require creation authority,
  modifications require update, retirement requires retire, and navigation
  link creation may use link-only only where the relationship policy permits.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C002 and C003.
- **Context:** The audit proved that a `retire` disposition could create an
  active established maintained claim.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A02-C003 — Make tombstones permanent and cover compound changes

- **Decision:** Reject reactivation or lifecycle rewriting of published
  retired and superseded objects. When one integration changes multiple state
  components, require each controlled event class needed by those components;
  a move event cannot conceal a content or metadata change.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C001 and C006.
- **Context:** The audit proved that a retired entity could return to active
  and that event compatibility needed to be evaluated per changed component.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A02-C004 — Prove the repaired matrix and correct completion state

- **Decision:** Add positive and negative regression tests for entity content
  authority, object-specific history authority, action-specific dispositions,
  compound move/state changes, and tombstone permanence. Mark the foundation
  complete only after those probes and all repository checks pass.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C007 and C008.
- **Context:** The prior 184-test suite passed all three prohibited audit
  probes, so its completion claim exceeded its demonstrated coverage.

## Corrections and supersessions

None. This addendum narrows and completes enforcement of the already
established S01 and A01 policy.

## Proposals retained for consideration

None.

## Open questions

None.

## Expected repository effects

- Strengthen canonical state snapshots, history authorization, disposition
  matching, lifecycle evolution, and tests.
- Correct the schema-v2 review and migration ledger after validation.
- Regenerate navigation-only indexes for the four new policy claims.
- Leave `canon/`, `story/`, and all historical migration inventories unchanged.

## Transcript provenance

Confirmed in the 2026-08-16 PR #41 completion-audit follow-up. This addendum
preserves the author's exact remediation instruction and the findings it
explicitly accepted for correction.
