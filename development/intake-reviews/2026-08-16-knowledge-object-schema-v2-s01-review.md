---
title: Knowledge Object Schema V2 Review
type: intake-review
status: complete
reviewed_on: 2026-08-16
submission: "../../intake/submissions/2026-08-16-knowledge-object-schema-v2-s01.md"
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
submission_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01
authority: establish-policy
session_mode: direct-integration
reviewer: Codex
lore_review: false
subjects:
  - knowledge-object-schema
  - knowledge-claims
  - object-history
  - graph-validation
  - thread-traversal
domains:
  - administration
  - design
  - terminology
search_terms:
  - knowledge claim
  - intake claim
  - object history
  - graph_status
  - claim boundary
  - supersession
  - provenance
authoritative_targets:
  - references/cloth-thread-model.md
  - references/graph-structure.md
  - references/front-matter.md
  - references/relationship-types.md
  - references/consistency-workflow.md
  - development/knowledge-object-schema-v2-migration.md
  - scripts/graph_common.py
  - scripts/build_graph_index.py
  - scripts/validate_repository.py
related:
  - 2026-08-15-cloth-patch-graph-model-s01-review.md
  - 2026-08-15-entity-relationship-graph-s01-review.md
---

# Knowledge Object Schema V2 Review

## Review scope

- **Submission:** [Knowledge Object Schema V2](../../intake/submissions/2026-08-16-knowledge-object-schema-v2-s01.md)
- **Case:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2`
- **Submission ID:** `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01`
- **Session mode:** `direct-integration`
- **Authority conveyed:** `establish-policy`
- **Review objective:** Establish the complete knowledge-object schema-v2 target, implement its first structural stage, and publish an explicit migration ledger that prevents partial infrastructure from being described as a completed knowledge migration.

This is a process and storage-structure policy review. It authorizes no lore,
story fact, semantic relationship inference, or canon reinterpretation.

## Audit baseline evaluation

- **Lore review:** `false`; canon and story prose are deliberately unchanged.
- **Policy baseline:** `9840884cfa5b534a448352c284734efe111115b7`, the completed generic entity/relationship migration endpoint.
- **Consistency scope:** Repository-wide governance, schema, tooling, generated-index, and test inspection plus exact exclusion of canon and story prose changes.

Lore-only semantic-audit baseline fields and canon-case counting do not apply.

## Files inspected

The complete approved design; prior CLOTH graph-model and graph-implementation
submissions and reviews; repository, intake, front-matter, graph, consistency,
Git, and CLOTH policies; current graph and claim indexes; graph and review
parsers; builders; validator; templates; tests; and all current graph metadata.

## Claim decisions

| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C001 | Distinguish maintained knowledge claims from immutable intake-review claims. | administrative | `explicit` | None | Current claim index contains intake dispositions and does not identify maintained fact objects. | `update` | CLOTH and graph policy; schema-v2 tooling | Prevents audit claims from being misrepresented as current knowledge assertions. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C002 | Keep authoritative entity, relationship, claim, and history metadata on owning Markdown records. | administrative | `explicit` | None | Markdown pages are already the authoritative graph surfaces. | `update` | Graph and front-matter policy | Extends the existing authority boundary without creating a competing database. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C003 | Give decision-worthy claims stable IDs and exact bounded prose while avoiding sentence-level atomization. | administrative | `explicit` | None | Current review targets are page-level and cannot identify the maintained assertion they affected. | `create` | Knowledge-claim schema and boundary validation | Makes individual facts addressable without replacing readable documents. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C004 | Require append-only local histories, lifecycle, tombstones, and exact review-claim provenance for graph objects. | administrative | `explicit` | None | Current entities and relationships have no required local history or representable retirement. | `update` | Graph policy, validators, migration program | Supplies object-first changelogs while preserving immutable global evidence. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C005 | Generalize controlled relationships to registered object kinds without introducing unreviewed semantic lore types. | administrative | `explicit` | None | Current endpoints resolve only entity and relationship IDs; only `related-to` is controlled. | `update` | Relationship registry and graph validation | Enables later relationships to facts while keeping the present migration semantically neutral. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C006 | Build a unified navigation-only object projection and deterministic THREAD traversal. | administrative | `explicit` | None | Graph and intake claims are currently disconnected indexes. | `create` | Generated indexes and traversal tooling | Gives object-first retrieval without moving authority out of Markdown. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C007 | Audit every current entity, relationship, and intake claim through staged migrations with explicit coverage. | administrative | `explicit` | None | The earlier migration covered entity IDs and generic related pairs only. | `create` | Public schema-v2 migration ledger | Makes incomplete coverage visible and prevents partial completion claims. |
| CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2-S01-C008 | Require a final independent canon-equivalence and completion audit before declaring schema-v2 migration complete. | administrative | `explicit` | None | Deterministic validation cannot prove semantic equivalence. | `create` | Migration completion criteria | Preserves the required semantic boundary and supplies a terminal condition. |

## Conversation checkpoint

### Established decisions

Claims C001-C008 and the eight recommended design decisions are explicitly
established by the author's complete direct-integration instruction.

### Proposals under consideration

None.

### Corrections and supersessions

None. The schema-v2 policy extends the prior graph abstraction and makes its
previously optional or unimplemented layers mandatory for final completion.

### Open questions

None blocking the first infrastructure stage. Specific semantic relationship
types remain outside this case and require later authority.

### Expected repository effects

Establish schema-v2 policy, publish the complete migration ledger, add
schema-aware parsing and navigation projection, introduce controlled object
history and knowledge-claim representations, strengthen validation, update
templates and tests, and leave canon/story prose and semantic lore relationships
unchanged.

## Files changed

| File or group | Change | Claim IDs |
| --- | --- | --- |
| Submission, review, and migration ledger | Preserve the complete approved design, dispositions, fixed baseline inventory, terminal conditions, and honest staged status. | C001-C008 |
| CLOTH, graph, front-matter, repository, intake, and consistency policy | Establish schema-v2 identity classes, maintained claims, histories, lifecycle, provenance, registry semantics, and completion rules. | C001-C008 |
| `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, and index/template guidance | Align contributor and agent behavior with the new authority, history, and migration boundaries. | C001-C008 |
| `requirements.txt` and repository-integrity workflow | Add and install the pinned safe YAML parser required for structured metadata. | C002-C004 |
| Graph, shared parsing, builder, and validator scripts | Parse structured YAML, build the unified projection and inventories, validate claims and histories, and enforce base-ref evolution. | C001-C007 |
| Canon-page and intake-review templates | Provide lifecycle, claim, history, and review-checklist surfaces for prospective use. | C002-C004 |
| Graph and validator tests and fixtures | Cover schema-v2 claims, history, endpoint kinds, ownership, symmetric uniqueness, self-links, and append-only evolution. | C001-C007 |
| Generated claim and knowledge-object indexes | Add eight reviewed policy claims and project 20 entities, 51 relationships, 45 submissions, 45 reviews, and 427 intake claims with explicit incomplete migration inventories. | C001-C008 |

## Files deliberately unchanged

| File or group | Reason | Claim IDs |
| --- | --- | --- |
| Canon and story prose | This case establishes structure and program state, not lore or narrative content. | C001-C008 |
| Existing semantic relationship vocabulary | No lore relationship type beyond navigation-only `related-to` is authorized. | C005 |
| Immutable historical submissions and completed reviews | Historical evidence remains unchanged. | C001-C008 |

## Exceptions created

- **Open questions:** None.
- **Proposals:** None.
- **Contradictions:** None.
- **Decision records:** None; the complete submission directly establishes policy.
- **Retired ideas:** None.

## Verification

- [x] Every substantive claim has a controlled disposition.
- [x] The immutable source preserves the approved design and exact authorization.
- [x] Maintained knowledge claims remain distinct from intake claims.
- [x] Object histories are locally addressable and append-only.
- [x] Relationship and claim lifecycles preserve tombstones and supersession.
- [x] No semantic relationship type or lore claim was inferred.
- [x] The migration ledger exposes every incomplete stage.
- [x] Canon and story prose remain unchanged.
- [x] Generated indexes are deterministic and navigation-only.
- [x] Required local validation and complete diff inspection pass.

Verification performed:

- Full unit suite: 171 tests passed.
- Repository validation against `origin/main`: passed for 203 Markdown files.
- Claim index: current at 427 immutable intake claims.
- Unified knowledge-object index: current at schema version 2 with 20 entities,
  51 relationships, zero maintained claims, zero history events, zero
  unmigrated legacy links, and explicit schema-v2 migration inventories.
- `git diff --check`: passed; Windows line-ending notices are configuration
  notices rather than whitespace errors.
- Complete changed-path and semantic diff inspection: no file under `canon/`
  or `story/` changed, no semantic relationship type was added, and no lore,
  authority level, story reveal, or existing provenance was altered.

## Outcome

- **Review status:** `complete`
- **Canon change-log entry:** None; process-only policy and storage structure.
- **Git commit:** Recorded by the case PR and Git history after publication.
- **Publication:** pending
- **Outstanding actions:** Publish this foundation once. Entity history,
  relationship history, intake-claim crosswalk, maintained-claim migration,
  THREAD traversal, and the final independent audit remain explicitly pending
  in the public ledger and must proceed through later staged cases.

## Amendments

None.
