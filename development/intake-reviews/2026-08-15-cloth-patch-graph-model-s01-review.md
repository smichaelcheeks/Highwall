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
reviewer: Codex
lore_review: false
subjects:
  - cloth-architecture
  - thread-traceability
  - patch-processing
  - knowledge-graph
  - transmission-completeness
domains:
  - administration
  - design
  - terminology
search_terms:
  - CLOTH
  - THREAD
  - stitch
  - weave
  - patch
  - END OF PATCH
  - END OF STITCH
  - relationship
  - graph
authoritative_targets:
  - references/cloth-thread-model.md
  - references/repository-standards.md
  - references/intake-workflow.md
  - references/consistency-workflow.md
  - references/git-workflow.md
  - references/canon-intake-quickstart.md
  - README.md
  - CONTRIBUTING.md
  - AGENTS.md
  - templates/lore-seed.md
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
- **Review objective:** Replace stitch-as-change-unit with patch, define stitching as governed integration, establish the current patch completion marker and indefinite legacy compatibility, and establish the graph-oriented CLOTH abstraction without changing Highwall lore or storage architecture.

This is a process-only policy review. It changes repository governance and terminology but establishes no lore or story authority.

## Audit baseline evaluation

- **Lore review:** `false`; no canon, story, character knowledge, or setting relationship changes.
- **Consistency scope:** Repository-wide semantic terminology and governance pass plus deterministic Tier 1 validation.
- **Prior policy baseline:** `e6a952a9c848a5765145a0abab9fa1227a71cd4f`, the current `main` commit and merge result of the prior CLOTH / THREAD terminology case.
- **Prior relationship outcomes:** The prior policy claims named in the submission's `supersedes_claims` were inspected directly; their authority remains historical but their current lifecycle will be superseded by C001-C003 below.

Lore-only semantic-audit baseline fields and canon-case counting do not apply to this process-only review.

## Files inspected

The complete submission; prior CLOTH terminology submission and review; CLOTH model; repository overview; contributor and agent instructions; repository, intake, consistency, and Git workflows; intake quickstart; reference, intake, submission, review, and template navigation pages; author-facing and repository-facing templates; completion validator; fixtures and tests; generated claim index; and repository-wide searches for stitch, weaving, patch, relationship, graph, and all recognized marker literals.

The closed, unmerged PR #31 patch was inspected only as a failed publication attempt and implementation warning. It supplies no authority and no commit from it is reused.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C001 | `patch` replaces `stitch` as the preferred author-facing noun for a bounded semantic change. | administrative | `explicit` | CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C005 | Current policy and guidance consistently use stitch as the change unit. | `update` | CLOTH model; repository workflows, navigation, instructions, and templates | Applies the replacement across every maintained author-facing and governance surface while preserving historical artifacts and stable technical filenames. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C002 | `stitch` and `stitching` become the governed integration operation that applies a patch to CLOTH. | administrative | `explicit` | CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C006; CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C007 | Current policy uses weave and weaving for integration and the earlier conceptual order. | `update` | CLOTH model; intake, consistency, and Git workflows; instructions and templates | Gives patch and stitching distinct semantic roles and updates the complete processing sequence. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C003 | New patches use `<!-- END OF PATCH -->`; stitch and seed markers remain valid legacy markers indefinitely. | administrative | `explicit` | CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01-C011 | Validator, fixtures, tests, templates, and guidance currently treat the stitch marker as current. | `update` | Validator; fixtures and tests; workflows, quickstart, instructions, and templates | Migrates the current convention without weakening completeness or rewriting history. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C004 | CLOTH has a graph-oriented conceptual layer with entities, relationships, claims, and patches as primary primitives. | administrative | `explicit` | None | The current model describes THREADs but not an explicit storage-independent graph abstraction. | `update` | `references/cloth-thread-model.md`; `README.md` | Establishes addressable graph concepts while retaining Markdown as the maintained implementation. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C005 | Relationships are addressable knowledge objects and may participate in additional relationships when the second relation is specifically about that connection. | administrative | `explicit` | None | No recursive relationship rule currently exists. | `update` | `references/cloth-thread-model.md`; `AGENTS.md` | Enables correctly scoped relationship-specific knowledge without broadening claims to either endpoint. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C006 | A relationship should be reified as an entity when it develops substantial independent identity, rules, history, or structure. | administrative | `explicit` | None | No current reification boundary exists. | `update` | `references/cloth-thread-model.md`; `AGENTS.md` | Prevents uncontrolled edge-on-edge recursion while preserving expressiveness. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C007 | Durable relationship types use governed vocabulary; agents may propose but not silently mint ontology terms. | administrative | `explicit` | None | Existing governance controls claims and domains but does not state this ontology rule. | `update` | `references/cloth-thread-model.md`; `references/repository-standards.md`; `AGENTS.md` | Keeps graph semantics attributable and prevents convenient wording from silently becoming policy. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C008 | Entities and relationships may maintain local pointer histories while immutable submissions remain the global evidentiary trail. | administrative | `explicit` | None | Current provenance is global through submissions, reviews, links, and Git. | `update` | `references/cloth-thread-model.md`; `README.md` | Improves object-first retrieval without duplicating or weakening authoritative provenance. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C009 | Pulling a THREAD should follow explicit graph relationships where available and use semantic search to discover missing or implicit connections. | administrative | `explicit` | None | Current consistency review uses manifests, links, indexes, searches, and semantic judgment without this traversal preference. | `update` | CLOTH model; consistency workflow; overview and agent instructions | Defines the intended graph-native evolution while retaining semantic search for discovery and audit widening. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C010 | Highwall remains Markdown-first and is not converted wholesale into a graph database or atomic triple store by this patch. | administrative | `explicit` | None | Current repository storage is document-first. | `no-change` | Repository storage and content architecture | The graph is an abstraction and future extension point, not an authorized migration. |
| CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01-C011 | Existing immutable seed and stitch submissions retain their original wording and markers. | administrative | `explicit` | None | Submission immutability and historical terminology compatibility are existing policy. | `no-change` | Historical submissions and dated reviews | Preserves the evidentiary record and keeps historical terminology accurate to its time. |

## Conversation checkpoint

### Established decisions

Claims C001-C011 are explicitly established as repository policy by the complete submission.

### Proposals under consideration

None.

### Corrections and supersessions

C001 supersedes the prior stitch-as-noun claim; C002 supersedes weaving and the prior conceptual order; C003 supersedes the stitch marker's status as current. Historical wording and marker compatibility remain valid.

### Open questions

None created by this patch. A future authorized patch may decide whether to add a generated graph-native index or storage representation.

### Expected repository effects

Update every maintained current-policy surface, the authoritative CLOTH model, agent and contributor guidance, author templates, completion-marker validation and tests, and the generated claim index. Preserve lore, story, historical submissions, dated reviews, stable technical record types, and storage architecture.

## Files changed

| File | Change | Claim IDs |
| --- | --- | --- |
| `intake/submissions/2026-08-15-cloth-patch-graph-model-s01.md` | Preserve the complete policy patch and name the prior claims its explicit replacements supersede. | C001-C011 |
| `development/intake-reviews/2026-08-15-cloth-patch-graph-model-s01-review.md` | Record policy authority, dispositions, supersessions, full impact, verification, and publication boundary. | C001-C011 |
| `references/cloth-thread-model.md` | Establish patch/stitching terminology, graph primitives, recursive relationships, reification, controlled vocabulary, local histories, and marker compatibility. | C001-C009 |
| `references/repository-standards.md` | Require governed patches and relationship vocabulary for semantic ontology changes. | C001-C002, C007 |
| `references/intake-workflow.md` | Apply patch/stitching terminology, three-marker compatibility, and the new processing sequence. | C001-C003 |
| `references/consistency-workflow.md` | Prefer explicit graph traversal while retaining semantic discovery and widening. | C002, C009 |
| `references/git-workflow.md` | Place publication after patch review, stitching, current-state changes, and validation. | C001-C002 |
| `references/canon-intake-quickstart.md` | Make patch and `END OF PATCH` the current author-facing convention. | C001-C003 |
| `references/README.md` | Index patches, stitching, graph relationships, and patch intake. | C001-C004 |
| `README.md` | Present patches, stitching, the graph abstraction, traversal, and local history at overview level. | C001-C002, C004, C008-C009 |
| `CONTRIBUTING.md` | Require patch completeness and stitching in the contributor workflow. | C001-C003 |
| `AGENTS.md` | Require patch terminology, graph-aware traversal, recursive relationship discipline, and current marker handling. | C001-C009 |
| `intake/README.md` | Describe patch sources and stitching into CLOTH. | C001-C002 |
| `intake/submissions/README.md` | Make patch and the patch marker current while preserving both legacy markers. | C001, C003 |
| `development/intake-reviews/README.md` | Describe a case's patch-to-conversation history. | C001 |
| `templates/README.md` | Present the author-facing lore patch template while preserving its stable filename. | C001, C010-C011 |
| `templates/lore-seed.md` | Emit lore patches with the current patch marker while retaining the legacy path. | C001, C003, C011 |
| `templates/intake-submission.md` | Use patch terminology and document current and legacy markers. | C001, C003 |
| `scripts/validate_repository.py` | Accept the current patch marker followed by both explicit legacy markers. | C003 |
| `tests/fixtures.py` | Default new synthetic submissions to the current patch marker. | C003 |
| `tests/test_validate_repository.py` | Cover current patch, legacy stitch, legacy seed, missing-marker, and prose-only cases. | C003 |
| `development/indexes/claim-index.json` | Regenerate eleven policy claims and all forward/reverse supersession lifecycle fields. | C001-C011 |

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| Historical files under `intake/submissions/` and dated intake reviews | Immutable and historical records retain their original seed/stitch wording and markers. | C003, C011 |
| `canon/`, `story/`, and lore exception records | This process-only patch establishes no setting or narrative change. | C010 |
| Stable technical paths and record types, including `templates/lore-seed.md`, `intake-submission`, and `intake-review` | The submission explicitly preserves technical identities; only maintained contents change where author-facing terminology is current. | C001, C010-C011 |
| Repository storage architecture | No graph database, triple-store conversion, or wholesale atomization is authorized. | C004, C010 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; the complete submission supplies direct policy authority.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a controlled disposition.
- [x] Each policy claim records explicit authority.
- [x] Superseded prior policy claims are named by exact claim ID.
- [x] Historical submissions and dated reviews are excluded from terminology rewriting.
- [x] No lore or story authority is created.
- [x] The complete maintained terminology neighborhood uses the new current convention.
- [x] Validator, fixtures, and tests distinguish current and legacy markers.
- [x] Relative links and required metadata validate.
- [x] The generated claim index is current and exposes supersession lifecycle.
- [x] The complete diff matches the final recorded file list and contains no unrelated changes.
- [x] Required local validation and semantic inspection pass.

Verification performed:

- Full unit suite: 153 tests passed.
- Repository validation against `origin/main`: passed for 182 Markdown files.
- Claim index: current after regeneration with 401 claims.
- Supersession inspection: prior C005, C006, C007, and C011 each expose the
  intended replacement in `superseded_by`; new C001-C003 expose the inverse
  `supersedes` links.
- `git diff --check`: passed; only expected Windows line-ending notices were
  emitted.
- Repository-wide maintained-content search: all remaining stitch terminology
  is an authorized integration verb or explicit legacy compatibility wording.
- Complete semantic diff inspection: no lore change, storage migration,
  historical-source rewrite, unrecorded policy claim, duplicated authority, or
  unrelated change found.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None; process-only policy change.
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** pending
- **Outstanding actions:** Publish once as a replacement draft PR and require both GitHub checks to pass.

## Amendments

None.
