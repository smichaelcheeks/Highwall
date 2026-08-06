---
title: Inland Basin Lake Chronology Clarification Review
type: intake-review
status: complete
reviewed_on: 2026-08-06
submission: "../../intake/submissions/2026-08-06-regional-hydrology-a01.md"
case_id: CASE-2026-08-06-REGIONAL-HYDROLOGY
submission_id: CASE-2026-08-06-REGIONAL-HYDROLOGY-A01
authority: establish-canon
session_mode: direct-integration
reviewer: Codex
subjects:
  - inland-basin
  - highwall
  - dryrun
  - old-wall
domains:
  - places
  - history
search_terms:
  - saline lake
  - inland basin
  - canyon entrance
  - 185 years
  - Old Wall
  - overflow
authoritative_targets:
  - canon/places/highwall-region-hydrology.md
  - canon/places/highwall-region-geology.md
  - canon/places/highwall.md
related:
  - "2026-08-06-regional-hydrology-s01-review.md"
  - "../contradictions/inland-basin-standing-water.md"
---

# Inland Basin Lake Chronology Clarification Review

## Review scope

- **Submission:** [Inland Basin Lake Chronology Clarification](../../intake/submissions/2026-08-06-regional-hydrology-a01.md)
- **Case:** `CASE-2026-08-06-REGIONAL-HYDROLOGY`
- **Submission ID:** `CASE-2026-08-06-REGIONAL-HYDROLOGY-A01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-canon`
- **Review objective:** Resolve the apparent standing-water conflict by
  distinguishing the ancient, present, and later canyon-entrance lakes without
  inferring a causal link to the Old Wall flood.

## Files inspected

Targeted context was regenerated for the inland basin, Highwall, Dryrun, lake
overflow, canyon entrance, and 185-year chronology. The regional geology and
hydrology pages, Highwall history, the S01 review, the contradiction report,
and all matching indexed claims were inspected. The addendum reconciles the
standing-water claims. No source establishes whether the later lake collapse
caused the Old Wall flood.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-06-REGIONAL-HYDROLOGY-A01-C001 | The ancient lake filled the entire basin, collapsed millennia ago, and rapidly carved Highwall's canyon. | canon | `explicit` | None | Geology establishes the catastrophic drainage and rapid canyon excavation but not the millennia-scale dating or full-basin extent. | `update` | `canon/places/highwall-region-hydrology.md`; `canon/places/highwall-region-geology.md` | The addendum confirms and refines the ancient event without exact dating. |
| CASE-2026-08-06-REGIONAL-HYDROLOGY-A01-C002 | A much smaller present saline lake overflows roughly once per decade into the drainage basin for Highwall's river. | canon | `explicit` | None | Geology establishes a remaining saline lake that periodically overflows; S01 says the ancient lake no longer remains. | `update` | `canon/places/highwall-region-hydrology.md`; `canon/places/highwall-region-geology.md`; [standing-water contradiction](../contradictions/inland-basin-standing-water.md) | Distinguishing the two lakes reconciles both claims and adds bounded frequency and drainage. |
| CASE-2026-08-06-REGIONAL-HYDROLOGY-A01-C003 | Another lake at the inland-side canyon entrance collapsed around 185 years ago. | canon | `explicit` | None | Highwall canon separately records an Old Wall-destroying flood at approximately the same time. | `update` | `canon/places/highwall-region-hydrology.md` | Record the lake and collapse without inferring that it caused the known flood. |

## Conversation checkpoint

### Established decisions

A01-C001 through A01-C003 are established canon.

### Proposals under consideration

None.

### Corrections and supersessions

None. A01 clarifies the referents of earlier claims rather than replacing them.

### Open questions

The relationship between the 185-year canyon-entrance lake collapse and the
Old Wall flood remains unestablished.

### Expected repository effects

Clarify the lake chronology, resolve the contradiction, update provenance and
the canon change entry, and leave the Old Wall account causally unchanged.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-06-regional-hydrology-a01.md` | Preserve the confirmed clarification. | A01-C001-C003 |
| `development/intake-reviews/2026-08-06-regional-hydrology-a01-review.md` | Record claim dispositions and verification. | A01-C001-C003 |
| `canon/places/highwall-region-hydrology.md` | Distinguish all three lakes and establish present overflow behavior. | A01-C001-C003 |
| `canon/places/highwall-region-geology.md` | Clarify the ancient and present lakes and remove the resolved conflict notice. | A01-C001-C002 |
| `development/contradictions/inland-basin-standing-water.md` | Record the explicit resolution. | A01-C001-C002 |
| `development/open-questions/regional-hydrology-details.md` | Replace the resolved basin-drainage unknown with the narrower remaining question. | A01-C002-C003 |
| `development/canon-changes.md` | Extend the case entry with the clarification. | A01-C001-C003 |
| `development/indexes/claim-index.json` | Regenerate claim navigation. | A01-C001-C003 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| `canon/places/highwall.md` | The addendum does not state that the later lake collapse caused the Old Wall flood; existing history remains accurate. | A01-C003 |
| `canon/history/` | The lake chronology has one regional authority; no separate historical-event page is needed. | A01-C001-C003 |

## Exceptions created

- **Open questions:** No new record; the narrower causal unknown remains in the regional hydrology details record.
- **Proposals:** None.
- **Contradictions:** Existing standing-water contradiction resolved.
- **Decision records:** None; A01 conveys direct authority.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] Every integrated conversational claim exists in immutable A01.
- [x] Each claim records explicit authority.
- [x] No prior source claim was erased or silently superseded.
- [x] All new facts have provenance.
- [x] Canon and story information remain separate.
- [x] The contradiction is explicitly resolved.
- [x] No causal relationship to the Old Wall flood was invented.
- [x] Relative links and front matter validate.
- [x] The diff matches the recorded file list.
- [x] The canon change log is updated.
- [x] Targeted context and chronology review were performed.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** [2026-08-06 regional hydrology](../canon-changes.md)
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** `pending`
- **Outstanding actions:** Publication and required GitHub checks. The causal
  relationship between the later lake collapse and Old Wall flood remains
  unestablished.

## Amendments

None.
