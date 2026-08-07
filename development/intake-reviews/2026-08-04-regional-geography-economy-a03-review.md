---
title: Forge Downriver Position Clarification Review
type: intake-review
status: complete
reviewed_on: 2026-08-07
submission: "../../intake/submissions/2026-08-04-regional-geography-economy-a03.md"
case_id: CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY
submission_id: CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A03
authority: establish-canon
session_mode: direct-integration
reviewer: Codex
subjects:
  - forge
  - stormlands
  - ledger
  - delta
domains:
  - places
  - economy
  - terminology
search_terms:
  - downriver
  - downstream
  - upstream
  - coastal plain
  - supply chain
authoritative_targets:
  - canon/places/forge.md
  - canon/economy/regional-trade-system.md
related:
  - "2026-08-04-regional-geography-economy-s01-review.md"
  - "../maintenance-reviews/2026-08-07-claim-to-canon-provenance-audit.md"
---

# Forge Downriver Position Clarification Review

## Review scope

- **Submission:** [Forge Downriver Position Clarification](../../intake/submissions/2026-08-04-regional-geography-economy-a03.md)
- **Case:** `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY`
- **Submission ID:** `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A03`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-canon`
- **Review objective:** Supply the missing authority for Forge's broad
  location, define the regional meaning of `downriver`, and preserve the
  authorized relative order without inventing precise geography.

## Files inspected

Targeted context was generated for Forge, Highwall, `downriver`, `downstream`,
`upstream`, supply chains, and the affected place, economy, and government
targets. The regional geography S01 source and review, all current place and
trade passages involving Forge, the regional-distance and additional-region
questions, the claim index, canon change log, and provenance finding
`PROV-2026-08-07-F02` were inspected. No later claim supplied or contradicted
the clarified location and order.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A03-C001 | In Highwall shorthand, `downriver` means on the coastal plain. | terminology | `explicit` | None | Existing canon uses upriver, downriver, downstream, coastal plain, and lowlands without defining their exact relationship. | `update` | `canon/places/forge.md` | Forge is the immediate authority needing the definition; broader terminology remains bounded to the supplied shorthand. |
| CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A03-C002 | Forge is downriver and therefore on the coastal plain. | canon | `explicit` | None | Forge currently says `downstream` without an authorizing claim; the audit identifies the gap. | `update` | `canon/places/forge.md`; original S01 review amendment | Explicit authority now supports the broad location while preserving the open specific place type and position. |
| CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A03-C003 | Forge is downstream of the Stormlands and upstream of Ledger and Delta in literal and supply-chain senses. | canon | `explicit` | None | S01 establishes the Stormlands-to-Forge production dependency but no complete relative order. | `update` | `canon/places/forge.md`; `canon/economy/regional-trade-system.md` | The place page owns relative location; the trade page records only the supplied supply-chain order. No route, waterway, or distance is inferred. |

## Conversation checkpoint

### Established decisions

A03-C001 through C003 are established at the authority recorded above.

### Proposals under consideration

None.

### Corrections and supersessions

None. The addendum supplies previously missing authority and clarifies existing
regional language.

### Open questions

Forge's specific place type, exact position, distances, routes, and waterway
identities remain unestablished.

### Expected repository effects

Update Forge and the regional trade system, append a historical-review
amendment, add cumulative provenance, log the clarification, and regenerate
the claim index.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-04-regional-geography-economy-a03.md` | Preserve the confirmed decisions in an immutable addendum. | A03-C001-C003 |
| `development/intake-reviews/2026-08-04-regional-geography-economy-a03-review.md` | Record the claims, targets, and bounded rationale. | A03-C001-C003 |
| `development/intake-reviews/2026-08-04-regional-geography-economy-s01-review.md` | Append an amendment exposing the later location authority. | A03-C001-C003; S01 C013-C015 |
| `canon/places/forge.md` | Establish Forge's downriver coastal-plain location and relative order. | A03-C001-C003 |
| `canon/economy/regional-trade-system.md` | Record the confirmed supply-chain order. | A03-C003 |
| `development/canon-changes.md` | Log the significant location clarification. | A03-C001-C003 |
| `development/indexes/claim-index.json` | Regenerate navigation for the new claims. | A03-C001-C003 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| `canon/places/stormlands.md`, `ledger.md`, and `delta.md` | Their current identities and owned facts remain accurate; duplicating Forge's relative-order explanation is unnecessary. | A03-C003 |
| `canon/government/regional-imperial-structure.md` | The clarification changes no political relationship or authority. | A03-C001-C003 |
| Open geography questions | Precise location, distances, routes, and waterways remain unresolved. | A03-C001-C003 |
| Claim-to-canon provenance audit | It remains the historical baseline that identified the pre-clarification gap. | A03-C002 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; the immutable addendum carries direct authority.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] Every integrated conversational claim exists in an immutable addendum.
- [x] Each claim records an explicit authority basis.
- [x] Superseded claims remain traceable; none are superseded here.
- [x] The original submission remains unchanged.
- [x] All new facts have explicit authority and provenance.
- [x] Canon and story information remain separate.
- [x] Beliefs and disputed claims are attributed.
- [x] No contradiction was silently resolved.
- [x] No authoritative explanation was unnecessarily duplicated.
- [x] Relative links resolve.
- [x] Required front matter is present.
- [x] The Git diff matches the recorded file list.
- [x] Significant canon clarifications are in the canon change log.
- [x] The impact manifest covers every affected subject, domain, search term,
  and authoritative target.
- [x] Targeted context was generated and inspected before widening the search.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** [2026-08-07 Forge downriver position and Highwall interface scope](../canon-changes.md)
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** `pending`
- **Outstanding actions:** Publication and required GitHub checks.

## Amendments

None.
