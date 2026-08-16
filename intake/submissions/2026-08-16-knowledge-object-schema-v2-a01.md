---
title: Knowledge Object Schema V2 Completion Addendum
type: conversation-addendum
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
submission_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01
sequence: 1
submitted_on: 2026-08-16
submitted_by: Shawn Cheeks
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: explicit-confirmation
parent_submission: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01
supersedes_claims: []
related:
  - 2026-08-16-knowledge-object-schema-v2-s01.md
---

# Knowledge Object Schema V2 Completion Addendum

## Conversation scope

- **Case:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2`
- **Parent submission:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01`
- **Session mode:** `direct-integration`
- **Period or session:** 2026-08-16 audit follow-up for draft PR #41

## Authority checkpoint

The author issued the following explicit instruction after reviewing the
read-only completion audit and recommended repair plan:

> Apply this PR #41 completion plan as an establish-policy addendum in direct-integration mode. Transmission complete.

This authorizes repository-policy and implementation corrections only. It does
not authorize lore, story, maintained-canon-claim, or semantic-relationship
changes.

## Transmission completeness

The author explicitly stated `Transmission complete.` The controlled
`completion_basis` is therefore `explicit-confirmation`.

## Confirmed decisions and additions

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C001 — Enforce a history event for every object change

- **Decision:** Compare canonical per-object state against the Git base and
  require every changed schema-v2 entity, relationship, or maintained claim to
  append a compatible, contiguous local history event. Include bounded claim
  content in claim state while excluding nested objects and history from entity
  state.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies the enforcement required by
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C004`.
- **Context:** Merely having an older history event does not satisfy the
  changelog rule for a later change.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C002 — Enforce authorized, relevant provenance

- **Decision:** Validate review authority and claim disposition against the
  object being established or changed, and require prospective exact
  provenance claims to name the resulting object ID. Administrative,
  proposal-only, deferred, rejected, and no-change claims cannot establish
  lore objects.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C004`.
- **Context:** A completed review is necessary but is not sufficient when its
  authority or disposition does not authorize the cited result.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C003 — Register provenance policy per relationship type

- **Decision:** Every controlled relationship type declares a controlled
  provenance policy so navigation, semantic-canon, working-canon, and
  administrative relationships can enforce distinct authority requirements.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C005`.
- **Context:** A global review-exists check cannot express type-specific
  authority requirements.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C004 — Complete the unified projection

- **Decision:** Project complete intake-claim objects rather than an ID-to-path
  map, and add explicit decision, exception, and evidence-reference
  collections while retaining specialized compatibility indexes.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C006`.
- **Context:** The unified projection must contain enough structured data for
  later THREAD traversal without pretending that generated JSON is authority.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C005 — Generalize endpoint ownership correctly

- **Decision:** Support every registered addressable endpoint kind permitted by
  a relationship-type row and validate ownership through an endpoint object's
  authoritative record, not by equating the container page's entity ID with
  the endpoint ID.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C005`.
- **Context:** Relationships and maintained claims may own or participate in
  relationships without becoming independent entity pages.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C006 — Complete lifecycle, relocation, and identity safeguards

- **Decision:** Add entity supersession pointers; enforce lifecycle/link
  agreement, reverse links, compatible kinds, replacement existence, and cycle
  rejection; preserve published history through path moves while requiring a
  new move event; and prevent durable ID reuse or object-kind mutation.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C004`.
- **Context:** An owning path is mutable navigation metadata, not part of an
  immutable published history event.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C007 — Add negative and positive invariant tests

- **Decision:** Add deterministic tests proving that missing change events,
  unauthorized provenance, incomplete projections, invalid registry policy,
  broken recursive ownership, inconsistent supersession, and improper moves
  fail, while their governed counterparts pass.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C005` and
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C006`.
- **Context:** Passing tests must demonstrate the intended invariant rather
  than only exercise the happy path.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A01-C008 — Preserve the staged migration boundary

- **Decision:** Finish the schema-v2 foundation in PR #41 without performing
  entity-history backfill, relationship-history backfill, intake-claim
  crosswalk, maintained-claim migration, semantic relationship introduction,
  THREAD traversal, or the final canon-equivalence audit.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C007` and
  `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C008`.
- **Context:** These remain later staged cases in the public migration ledger.

## Corrections and supersessions

None. This addendum corrects incomplete implementation of the established
foundation requirements without replacing the original schema-v2 decisions.

## Proposals retained for consideration

None.

## Open questions

None.

## Expected repository effects

- Strengthen graph parsing, projection, base-ref evolution validation, and
  tests.
- Complete the relationship registry's machine-visible provenance policy.
- Align graph, front-matter, consistency, contributor, template, index, and
  migration-ledger guidance with enforced behavior.
- Leave `canon/` and `story/` unchanged.

## Transcript provenance

Confirmed in the 2026-08-16 PR #41 completion-audit conversation. This
addendum preserves the approved outcomes and exact integrating instruction,
not exploratory reasoning.
