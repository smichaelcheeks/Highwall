---
title: CLOTH / THREAD Terminology and Repository Self-Model Review
type: intake-review
status: complete
reviewed_on: 2026-08-13
submission: "../../intake/submissions/2026-08-13-cloth-thread-terminology-s01.md"
case_id: CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY
submission_id: CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - cloth-architecture
  - thread-traceability
  - stitch-processing
  - transmission-completeness
domains:
  - administration
  - terminology
search_terms:
  - CLOTH
  - THREAD
  - stitch
  - weave
  - seed
  - END OF SEED
  - completion_basis
authoritative_targets:
  - references/cloth-thread-model.md
  - references/repository-standards.md
  - references/intake-workflow.md
  - references/consistency-workflow.md
  - references/git-workflow.md
related: []
---

# CLOTH / THREAD Terminology and Repository Self-Model Review

## Review scope

- **Submission:** [CLOTH / THREAD terminology stitch](../../intake/submissions/2026-08-13-cloth-thread-terminology-s01.md)
- **Case:** `CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY`
- **Submission ID:** `CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Establish the CLOTH / THREAD repository self-model, adopt stitch/weave terminology without collapsing technical records, and migrate the completeness marker with indefinite legacy compatibility.

## Audit baseline evaluation

- **Lore review:** `false`; this stitch changes governance and terminology but no lore, canon authority, or story state.
- **Consistency scope:** Repository-wide semantic terminology pass plus deterministic Tier 1 validation.

## Files inspected

Repository overview, contributor and agent instructions, repository standards,
intake and consistency workflows, Git workflow, intake quickstart, intake and
review directory guides, author-facing and repository-facing templates,
completion validator and tests, historical submissions and reviews, generated
claim index, canon provenance links, and development history.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C001 | Highwall is an instance of a domain-independent CLOTH: a governed, coherent, traceable body of evolving knowledge. | administrative | `explicit` | None | The repository describes a controlled canon system but has no unifying architectural name. | `create` | `references/cloth-thread-model.md`; `README.md` | A dedicated policy home plus overview establishes the authorized repository identity without changing lore. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C002 | THREAD names a traceable provenance and dependency chain; claims and stitches may participate in multiple intersecting THREADs. | administrative | `explicit` | None | Intake records and semantic audits already model these relationships without this name. | `create` | `references/cloth-thread-model.md`; `references/consistency-workflow.md` | The new term clarifies existing traceability mechanisms without renaming records. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C003 | Pulling a thread traces provenance backward or dependencies forward but grants no authority to change knowledge. | administrative | `explicit` | None | Targeted and repository-wide consistency workflows already perform this discovery. | `update` | `references/consistency-workflow.md` | Connecting the term to current workflows preserves the authority boundary. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C004 | Loose threads are legitimate unresolved relationships; broken threads are provenance or traceability failures. | administrative | `explicit` | None | Open questions and contradictions are represented, but traceability failure lacks shared terminology. | `create` | `references/cloth-thread-model.md`; `references/repository-standards.md` | The distinction preserves legitimate uncertainty while identifying repairable deficiencies. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C005 | Stitch is the preferred author-facing semantic change unit and must not collapse submissions, reviews, current-state changes, exception records, or publication history. | administrative | `explicit` | Generic author-facing use of “seed” | Current workflows already preserve these distinct technical records. | `update` | `references/intake-workflow.md`; templates and navigation documentation | The authorized vocabulary changes the conceptual unit while retaining precise artifact names and guarantees. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C006 | Weaving is governed integration across the affected knowledge state, not merely editing an obvious target. | administrative | `explicit` | None | Impact manifests, dispositions, and consistency tiers already govern integration consequences. | `update` | `references/intake-workflow.md`; `references/git-workflow.md`; `AGENTS.md` | The term makes the existing integration obligation explicit. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C007 | Semantic integration follows stitch, review/authority, weave, current-state changes, validation, and publication; semantic changes require traceable authority. | administrative | `explicit` | None | The workflow has the same operational order but no compact conceptual statement. | `update` | `references/cloth-thread-model.md`; workflow documentation | The policy codifies ordering and the governing invariant without converting the repository to event sourcing. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C008 | Semantic and mechanical changes remain distinct, and mechanical edits gain no semantic authority. | administrative | `explicit` | None | The maintenance boundary distinguishes process maintenance from governed changes. | `update` | `references/repository-standards.md`; `references/cloth-thread-model.md` | Explicit classification prevents file mutation from being mistaken for authority. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C009 | Coherence preserves conflicts, uncertainty, perspective, lifecycle, authority, and confidence distinctions rather than forcing agreement. | administrative | `explicit` | None | Canon safety and truth-kind rules already require these distinctions. | `update` | `references/cloth-thread-model.md`; `README.md` | The definition unifies current safeguards without changing their meaning. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C010 | CLOTH governance is itself governed knowledge; process self-modification must remain explicit and auditable. | administrative | `explicit` | None | Significant policy already uses full intake, but self-governance is implicit. | `update` | `references/repository-standards.md`; `CONTRIBUTING.md` | The policy makes the existing governance boundary self-applicable. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C011 | `<!-- END OF STITCH -->` becomes the current marker; either it or legacy `<!-- END OF SEED -->` satisfies `completion_basis: end-marker`. | administrative | `explicit` | Single-marker author-facing convention | Validator and tests currently recognize only the legacy literal. | `update` | `scripts/validate_repository.py`; tests; templates; instructions | Explicit dual-marker handling changes vocabulary without weakening deterministic completeness. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C012 | Historical submissions and specifically named legacy artifacts remain unchanged; technical record names remain where precise. | administrative | `explicit` | None | Historical provenance and generated claim records contain many legitimate uses of “seed.” | `no-change` | Immutable submissions, historical reviews, canon provenance labels, generated historical claims | Retaining these occurrences preserves provenance, compatibility, and artifact identity. |
| CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C013 | The repository must not adopt pure event sourcing, a graph database, wholesale record renames, weakened validation, or altered lore authority. | administrative | `explicit` | None | Current repository is maintained Markdown current state with immutable sources and Git history. | `no-change` | Storage architecture, technical record types, lore and story corpus | These exclusions constrain implementation and preserve existing guarantees. |

## Conversation checkpoint

### Established decisions

Claims C001-C013 are explicitly established as repository policy.

### Proposals under consideration

None.

### Corrections and supersessions

The author-facing generic term “seed” is superseded by “stitch.” Historical and
technical uses remain valid, and the legacy completion marker remains accepted.

### Open questions

None.

### Expected repository effects

Add a single authoritative terminology page; update high-level self-description,
governance workflows, agent instructions, author-facing templates, validator
constants, and focused tests; preserve historical records and lore unchanged.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-13-cloth-thread-terminology-s01.md` | Preserve the complete transition stitch under the legacy marker in force at submission. | C001-C013 |
| `.gitattributes` | Preserve seven author-supplied Markdown hard breaks in the immutable transition source while retaining normal whitespace checks for every other path. | C012 |
| `development/intake-reviews/2026-08-13-cloth-thread-terminology-s01-review.md` | Record policy dispositions, integration scope, terminology decisions, and verification. | C001-C013 |
| `references/cloth-thread-model.md` | Define CLOTH, THREAD, pulling, loose and broken threads, stitch, weave, coherence, authority, change classes, self-governance, and marker compatibility. | C001-C013 |
| `README.md` | Make the CLOTH identity and THREAD model visible in the repository overview. | C001, C002, C005, C006, C009 |
| `CONTRIBUTING.md` | Adopt stitch/weave language and dual-marker completeness guidance. | C005, C006, C010, C011 |
| `AGENTS.md` | Require current and legacy markers, verbatim stitch preservation, affected-THREAD tracing, and the conceptual integration order. | C005-C007, C011, C012 |
| `references/repository-standards.md` | Connect standards to CLOTH architecture and distinguish loose/broken THREADs and semantic/mechanical change. | C001, C004, C008, C010 |
| `references/intake-workflow.md` | Adopt stitch/weave terminology while preserving submission, review, ID, and compatibility boundaries. | C005-C007, C011, C012 |
| `references/consistency-workflow.md` | Define targeted and repository-wide semantic review as mechanisms for pulling THREADs. | C002, C003, C006 |
| `references/git-workflow.md` | Place Git/PR publication after the governed stitch and weave. | C007 |
| `references/canon-intake-quickstart.md` | Make stitch and `<!-- END OF STITCH -->` the current author-facing convention. | C005, C011 |
| `references/README.md` | Index the authoritative model and describe the quickstart as stitch processing. | C001-C007 |
| `intake/README.md` | Describe intake as preserving stitch sources before weaving. | C005, C006 |
| `intake/submissions/README.md` | Use stitch submission language and document both accepted markers. | C005, C011, C012 |
| `development/intake-reviews/README.md` | Describe case history as stitch-to-conversation while retaining the review record name. | C005, C012 |
| `templates/README.md` | Present the author-facing lore stitch template and explain its stable legacy filename. | C005, C012 |
| `templates/lore-seed.md` | Convert current author-facing content and output to stitch terminology and the current marker while retaining the filename for compatibility. | C005, C011, C012 |
| `templates/intake-submission.md` | Describe stitch authority and both recognized end markers. | C005, C011 |
| `scripts/validate_repository.py` | Replace the single marker constant with explicit current and legacy marker constants and accept either for `end-marker`. | C011 |
| `tests/fixtures.py` | Default new synthetic submissions to the current marker while allowing explicit legacy coverage. | C011 |
| `tests/test_validate_repository.py` | Test current acceptance, legacy acceptance, missing-marker failure, and prose-only near misses. | C011 |
| `development/indexes/claim-index.json` | Regenerate navigation for the thirteen reviewed policy claims. | C001-C013 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| Existing `intake/submissions/2026-*.md` files | Immutable historical sources retain their original wording and legacy markers. | C012, C013 |
| Existing dated intake reviews and `development/canon-changes.md` | “Seed” remains where it names a historical artifact or provenance label; rewriting would blur history. | C012 |
| Canon, story, design, and exception content | This stitch establishes repository policy and explicitly changes no lore, story truth, or existing authority. | C009, C013 |
| Technical `intake-submission`, `intake-review`, case, `S01`, and addendum record types | These names preserve distinct implementation responsibilities and are not conceptually replaced by “stitch.” | C005, C012, C013 |
| Repository storage and publication architecture | No graph database, pure event sourcing, or wholesale artifact rename is authorized. | C007, C013 |

## Terminology integration report

- **CLOTH definition:** Authoritative in
  `references/cloth-thread-model.md` and summarized at the top of `README.md`.
- **THREAD definition:** Authoritative in the model; consistency guidance maps
  targeted and repository-wide semantic review to pulling affected THREADs.
- **Stitch and weave adoption:** Intake, contribution, agent, Git, quickstart,
  directory, and template guidance use stitch for the author-facing semantic
  delta and weave for governed integration.
- **Legacy seed retention:** Immutable submissions, dated reviews, canon
  provenance labels, generated historical claim text, the stable
  `templates/lore-seed.md` path, technical `S01` identifiers, and the legacy
  marker retain “seed” where changing it would damage provenance,
  compatibility, or artifact clarity.
- **Verbatim-format exception:** The submitted glossary uses seven Markdown
  hard breaks. A single-path Git whitespace attribute preserves those source
  bytes while leaving trailing-whitespace checks active everywhere else.
- **Marker compatibility:** The validator exposes separate current and legacy
  constants and accepts either exact literal for `completion_basis:
  end-marker`. New fixtures and author templates emit the stitch marker; tests
  cover both valid markers and invalid near misses. No completeness guarantee
  changes.
- **Automation required:** Validator constants, fixture defaults, focused unit
  tests, and the generated claim index changed. No other automation depended on
  the marker literal.
- **Ambiguity assessment:** “Stitch” could have been confused with submission
  or review records, and “THREAD” with claims or documents. The authoritative
  model explicitly treats stitch as the semantic delta and THREAD as a
  relationship, preserving all technical record names.
- **Governance THREADs affected:** Repository identity and terminology;
  semantic authority and self-governance; intake completeness and immutable
  provenance; review and controlled dispositions; dependency discovery and
  audit scope; templates and agent behavior; validation; and Git/PR
  publication.
- **Deferred migration:** Historical records and labels remain untouched.
  Renaming the `templates/lore-seed.md` path or technical `S01` identifier is
  deferred indefinitely unless a future stitch supplies a compatibility-safe
  reason. No unreviewed terminology migration is implied.

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; the immutable stitch supplies direct policy authority.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] The original submission remains unchanged.
- [x] No lore or story authority changes.
- [x] Technical artifact boundaries remain distinct.
- [x] Historical “seed” terminology remains intact where provenance requires it.
- [x] Both recognized completion markers receive positive and negative tests.
- [x] Relative links resolve and required metadata is present.
- [x] The complete repository terminology neighborhood was inspected.
- [x] The Git diff matches the recorded file list and contains no unrelated changes.
- [x] Tier 1 validation and the claim-index freshness check pass.

Verification performed:

- Full unit suite: 152 tests passed.
- Repository validation against `origin/main`: passed for 180 Markdown files.
- Claim index freshness: passed after regeneration with 390 claims.
- `git diff --check`: passed with the immutable transition source's seven
  author-supplied Markdown hard breaks covered by its path-specific attribute.
- Complete semantic diff inspection: no invented lore, authority change,
  collapsed record boundary, unrecorded decision, or unrelated change found.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None; this policy stitch does not change lore canon.
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** pending
- **Outstanding actions:** Publish the branch as a draft PR and require both GitHub checks to pass.

## Amendments

None.
