---
title: CLOTH Patch and Graph Model Review
type: intake-review
status: complete
reviewed_on: 2026-08-15
submission: "../../intake/submissions/2026-08-15-cloth-patch-graph-model-s01.md"
case_id: CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL
submission_id: CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01
authority: establish-policy
session_mode: direct-integration
reviewer: ChatGPT
lore_review: false
subjects:
  - cloth
  - thread
  - patch
  - knowledge-graph
domains:
  - administration
  - design
  - terminology
search_terms:
  - CLOTH
  - THREAD
  - stitch
  - patch
  - END OF STITCH
  - relationship
authoritative_targets:
  - references/cloth-thread-model.md
  - README.md
  - AGENTS.md
  - templates/intake-submission.md
  - scripts/validate_repository.py
related:
  - 2026-08-13-cloth-thread-terminology-s01-review.md
---

# CLOTH Patch and Graph Model Review

## Review scope

- **Submission:** [CLOTH Patch and Graph Model](../../intake/submissions/2026-08-15-cloth-patch-graph-model-s01.md)
- **Case:** `CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL`
- **Submission ID:** `CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Refine CLOTH terminology so patch is the bounded semantic delta and stitching is the integration operation; establish the graph-oriented entity/relationship/claim abstraction, recursive relationship rule, local paper trails, and patch-marker compatibility without changing Highwall lore.

This is a process-only policy review. It changes repository governance and terminology but establishes no lore authority.

## Files inspected

The existing CLOTH / THREAD model, README, AGENTS instructions, intake-submission template, completion-marker validator, marker tests and fixtures, prior CLOTH terminology submission/review, and repository-wide search results for current stitch terminology.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C001 | `patch` replaces `stitch` as the preferred author-facing noun for a bounded semantic change. | administrative | `explicit` | None | Prior CLOTH policy used `stitch` for the change unit. | `update` | `references/cloth-thread-model.md`; `README.md`; `AGENTS.md`; `templates/intake-submission.md` | Establishes the newly authorized terminology while preserving technical record names. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C002 | `stitch` / `stitching` becomes the governed integration operation that applies a patch to CLOTH. | administrative | `explicit` | None | Prior model used weaving as the primary integration metaphor. | `update` | `references/cloth-thread-model.md`; `README.md`; `AGENTS.md` | Gives patch and stitching distinct semantic roles. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C003 | New patches use `<!-- END OF PATCH -->`; stitch and seed markers remain valid legacy markers indefinitely. | administrative | `explicit` | None | Validator currently accepts stitch and seed markers. | `update` | `scripts/validate_repository.py`; `templates/intake-submission.md`; `references/cloth-thread-model.md`; `AGENTS.md`; `tests/test_completion_markers.py` | Migrates terminology without weakening completeness or rewriting history. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C004 | CLOTH has a graph-oriented conceptual layer with entities, relationships, claims, and patches as primary primitives. | administrative | `explicit` | None | Existing CLOTH model describes THREADs semantically but not as an explicit graph abstraction. | `update` | `references/cloth-thread-model.md`; `README.md` | Makes traversal and machine-operable structure explicit while remaining storage-agnostic. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C005 | Relationships are addressable knowledge objects and may participate as endpoints in additional relationships when the additional relation is specifically about that connection. | administrative | `explicit` | None | No prior recursive relationship rule exists. | `update` | `references/cloth-thread-model.md`; `AGENTS.md` | Supports scoped rules and relationship-specific knowledge without broadening claims to the wrong endpoint. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C006 | Complex relationships should be reified as entities once they develop substantial independent identity, rules, history, or structure. | administrative | `explicit` | None | No prior reification rule exists. | `update` | `references/cloth-thread-model.md`; `AGENTS.md` | Prevents uncontrolled edge-on-edge recursion while preserving expressiveness. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C007 | Durable relationship types should use controlled vocabulary; agents may propose but not silently mint ontology terms. | administrative | `explicit` | None | Existing governance controls claims and domains but does not state this graph-ontology rule. | `update` | `references/cloth-thread-model.md`; `AGENTS.md` | Keeps graph semantics stable and governed. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C008 | Entities and relationships may maintain local pointer-based histories while immutable submissions remain the global evidentiary trail. | administrative | `explicit` | None | Existing model centralizes provenance through submissions, reviews, and Git. | `update` | `references/cloth-thread-model.md`; `README.md` | Improves practical retrieval without duplicating or weakening global provenance. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C009 | Pulling a THREAD should follow explicit graph relationships where available and use semantic search to discover missing or implicit connections rather than for every hop. | administrative | `explicit` | None | Current semantic consistency workflow relies primarily on manifests, indexes, links, and semantic review. | `update` | `references/cloth-thread-model.md`; `README.md`; `AGENTS.md` | Defines the intended graph-native evolution while retaining semantic search as a discovery mechanism. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C010 | Highwall remains Markdown-first and is not converted wholesale into a graph database or atomic triple store by this patch. | administrative | `explicit` | None | Existing Highwall repository is document-first. | `no-change` | Repository storage architecture | The graph is an abstraction and future extension point, not an immediate storage migration. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C011 | Existing immutable seed and stitch submissions remain unchanged. | administrative | `explicit` | None | Submission immutability is already repository policy. | `no-change` | `intake/submissions/` historical records | Terminology migration must not rewrite the evidentiary record. |

## Conversation checkpoint

### Established decisions

Patch is the semantic change unit; stitching is the integration operation. CLOTH now explicitly includes a graph-oriented knowledge abstraction in which entities and relationships are addressable, claims attach to either, relationships may participate in further relationships, complex relationships are reified, and local histories point back to immutable global provenance.

### Proposals under consideration

None.

### Corrections and supersessions

The author-facing noun `stitch` is superseded by `patch` for new semantic change units. Historical use of stitch as a noun remains accurate in immutable records. `END OF PATCH` becomes the current marker while both earlier markers remain valid.

### Open questions

None created by this patch. A future patch may decide whether to add a generated graph-native index or storage representation.

### Expected repository effects

Update the authoritative CLOTH model, overview, agent workflow, intake template, completion-marker validation, and regression coverage. Preserve all lore and historical submissions.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-15-cloth-patch-graph-model-s01.md` | Preserve the complete policy patch under the marker rule in force at submission time. | C001-C011 |
| `development/intake-reviews/2026-08-15-cloth-patch-graph-model-s01-review.md` | Record policy authority, dispositions, impact, and compatibility decisions. | C001-C011 |
| `references/cloth-thread-model.md` | Replace stitch-as-noun with patch, define stitching, graph primitives, recursive relationships, reification, controlled relationship vocabulary, and local histories. | C001-C009 |
| `README.md` | Present patches, stitching, graph traversal, and local history at repository overview level. | C001-C002, C004, C008-C009 |
| `AGENTS.md` | Require patch terminology, graph-aware THREAD traversal, recursive relationship discipline, and current marker handling. | C001-C007, C009 |
| `templates/intake-submission.md` | Use patch terminology and current/legacy completion markers. | C001, C003 |
| `scripts/validate_repository.py` | Accept `END OF PATCH` plus both legacy markers. | C003 |
| `tests/test_completion_markers.py` | Verify current and legacy completion markers remain accepted. | C003 |

## Files deliberately unchanged

| File | Reason | Claim IDs |
| --- | --- | --- |
| Historical files under `intake/submissions/` | Immutable source records retain their original seed/stitch terminology and markers. | C003, C011 |
| `canon/` and `story/` | This process-only patch establishes no lore or narrative change. | C010 |
| Existing claim index format | Graph-native indexing is explicitly deferred to a future patch rather than inferred here. | C004, C009-C010 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a disposition.
- [x] The original submission remains unchanged after review creation.
- [x] No lore or story authority was created.
- [x] Historical seed/stitch submissions remain untouched.
- [x] Current and legacy completion markers are represented in validator policy and regression coverage.
- [x] The graph abstraction does not require a storage migration.
- [x] Recursive relationships have an explicit reification boundary.
- [x] Relationship vocabulary remains governed rather than agent-invented.
- [x] Local histories point back to global provenance rather than replacing it.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None; process-only policy change.
- **Git commit:** Recorded by branch history.
- **Publication:** pending
- **Outstanding actions:** GitHub CI and author merge decision.

## Amendments

None.
