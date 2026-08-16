---
title: Knowledge Object Schema V2 Transition Enforcement
type: conversation-addendum
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
submission_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03
sequence: 3
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
  - 2026-08-16-knowledge-object-schema-v2-a02.md
---

# Knowledge Object Schema V2 Transition Enforcement

## Conversation scope

- **Case:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2`
- **Parent submission:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01`
- **Session mode:** `direct-integration`
- **Period or session:** 2026-08-16 second completion-audit follow-up

## Authority checkpoint

After a second read-only audit found that the A01 and A02 repairs still
accepted adjacent prohibited states, the author approved the robust corrective
design and instructed:

> Apply the corrective A03 plan above as establish-policy in direct-integration mode. Transmission complete.

This instruction authorizes the parser, transition, authority, history,
registry, test, policy, and completion-gate repairs below on draft PR #41. It
authorizes no lore, story, maintained lore claim, historical backfill, or
semantic relationship.

## Transmission completeness

The author explicitly identified the complete corrective plan, authority, and
session mode and stated that transmission was complete. The controlled
`completion_basis` is `explicit-confirmation`.

## Confirmed decisions and additions

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C001 — Parse claim boundaries before state exclusion

- **Decision:** Parse every maintained-claim boundary structurally, require a
  one-to-one match between declared claims and bounded passages, reject
  malformed, undeclared, duplicate, nested, overlapping, or unmatched
  boundaries, and exclude content from entity state only after that binding
  succeeds.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C001 and S01 C003-C004.
- **Context:** The second audit proved that an undeclared marker block could
  conceal arbitrary entity prose from change detection.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C002 — Classify complete baseline-to-result transitions

- **Decision:** Replace generic state-change matching with one canonical
  transition classifier that considers both baseline and resulting objects,
  paths, lifecycles, authorities, and independently governed components.
  Unknown changes fail closed rather than receiving a permissive metadata
  fallback.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C001 and A02 C001-C003.
- **Context:** The existing validator repaired known examples but did not model
  the complete operation being authorized.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C003 — Bind histories to exact transitions

- **Decision:** Give every newly appended prospective history event a
  deterministic transition hash covering object identity, baseline and result
  state, paths, and the complete action set. All events for one compound
  transition share that binding and must collectively cover every required
  event class.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C001 and A02 C003.
- **Context:** A broad compatible `change_type` alone does not prove that an
  event records the state transition that actually occurred.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C004 — Derive authority from both states

- **Decision:** Determine required authority from the baseline object, the
  resulting object, and every changed semantic component. Demotion,
  retirement, or supersession cannot lower its own authorization threshold;
  policy and classify authority cannot alter established or working lore.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C002 and A02 C001-C002.
- **Context:** The second audit proved that weak authority could first lower an
  object's resulting authority or lifecycle and then be judged against that
  weaker state.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C005 — Govern supersession as semantic identity

- **Decision:** Treat lifecycle and supersession as semantic identity changes,
  require reciprocal atomic state, local histories on every changed object,
  explicit review relevance to all affected IDs, and authority sufficient for
  the strongest affected object. Policy-only graph maintenance cannot rewire a
  published replacement.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C006 and A02 C001-C003.
- **Context:** The second audit proved that `supersedes` and `superseded_by`
  were excluded from every authority-classified entity component.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C006 — Require truthful initial events

- **Decision:** Derive initial event type from Git state: a newly published
  entity requires `established`, while a pre-existing readable record entering
  the graph requires `graph-registered`. Relationships and maintained claims
  require their own controlled creation events.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C001 and A02 C002.
- **Context:** The second audit proved that new and pre-existing entity records
  could use either initial event label.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C007 — Validate the complete relationship-type contract

- **Decision:** Require a nonempty definition, reciprocal inverse declarations,
  compatible directionality, reversed endpoint-kind compatibility, symmetric
  self-inverse behavior, and coherent authority-effect and provenance-policy
  combinations for every controlled relationship type.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Clarifies A01 C003 and C007.
- **Context:** The second audit proved that empty definitions and incoherent
  directed inverse declarations passed validation.

### CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-A03-C008 — Use an invariant matrix and independent completion gate

- **Decision:** Add negative and positive tests across object kind, baseline
  and result authority, lifecycle, component, disposition, event type, marker
  structure, and registry mutation. Keep prospective validation reopened until
  the full suite and a separate read-only adversarial audit pass. Do not
  advance historical migration stages in this repair.
- **Authority basis:** `explicit`
- **Clarifies or supersedes:** Corrects the completion conclusion of A02 C004
  without rewriting the immutable addendum.
- **Context:** Both earlier green suites covered reproduced examples rather
  than the invariant space and therefore overstated completion.

## Corrections and supersessions

A03 corrects the completion conclusion attached to A02 C004. The earlier
addendum remains immutable and traceable; the migration ledger is reopened
until A03 enforcement and independent audit are complete.

## Proposals retained for consideration

None.

## Open questions

None.

## Expected repository effects

- Add fail-closed maintained-claim boundary parsing.
- Add canonical transition classification and exact history binding.
- Enforce two-state, component-aware authority and semantic supersession.
- Require truthful initial events and a coherent relationship registry.
- Add an adversarial transition matrix and correct the completion ledger.
- Regenerate navigation-only indexes for the eight A03 intake claims.
- Leave `canon/`, `story/`, and all historical migration inventories unchanged.

## Transcript provenance

Confirmed in the 2026-08-16 PR #41 second completion-audit follow-up. This
addendum preserves the author's exact integration instruction and the complete
corrective design it approved.
