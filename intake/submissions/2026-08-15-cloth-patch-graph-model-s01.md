---
title: CLOTH Patch and Graph Model
 type: intake-submission
case_id: CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL
submission_id: CASE-2026-08-15-CLOTH-PATCH-GRAPH-MODEL-S01
sequence: 1
submitted_on: 2026-08-15
submitted_by: Shawn Cheeks
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: end-marker
parent_submission: null
supersedes_claims: []
related:
  - 2026-08-13-cloth-thread-terminology-s01.md
---

# CLOTH Patch and Graph Model

## Author instruction

Establish the following refinements to the CLOTH / THREAD architecture as repository policy and integrate them consistently across current documentation, validation, and agent guidance. Preserve immutable historical submissions and their original terminology.

Highwall should serve as a concrete reference implementation for the more general CLOTH architecture without requiring an immediate rewrite of all lore into a graph database.

## Patch terminology

Replace **stitch** as the author-facing noun for a bounded semantic change with **patch**.

A **patch** is the declarative, bounded semantic delta proposed or authorized to change a CLOTH. It may create, update, supersede, retire, relate, or reclassify knowledge or governance.

Use **stitch** and **stitching** as verbs for the governed integration operation that applies a patch to the coherent current state.

Preferred language includes:

- prepare a patch
- review a patch
- stitch this patch into CLOTH
- this patch affects three THREADs
- stitching this patch exposed a loose thread

The conceptual order becomes:

**Patch → review and authority determination → stitch/integration → integration review and current-state changes → validation → publication**

Technical records such as `intake-submission` and `intake-review` remain distinct and should not be renamed merely for thematic consistency.

## Patch completion marker

New patches should use:

```text
<!-- END OF PATCH -->
```

The previously current marker:

```text
<!-- END OF STITCH -->
```

and the older:

```text
<!-- END OF SEED -->
```

remain valid legacy completion markers indefinitely. Do not modify immutable historical submissions to modernize their markers.

The validator and documentation should accept all three recognized markers while recommending `<!-- END OF PATCH -->` for newly prepared patches.

This submission itself uses `<!-- END OF STITCH -->` because that is the rule in force when the patch is submitted. Its integration authorizes the new marker.

## Graph abstraction

CLOTH should explicitly define a graph-oriented knowledge abstraction beneath or alongside human-readable documents.

The primary conceptual primitives are:

1. **Entity** — an addressable thing or concept in the knowledge domain.
2. **Relationship** — an addressable, typed connection between knowledge objects.
3. **Claim** — an assertion about an entity or relationship, with provenance, authority, lifecycle, confidence, and scope as applicable.
4. **Patch** — the bounded semantic transaction that changes claims, entities, relationships, or governance under traceable authority.

Documents remain useful and may remain authoritative human-readable projections. Highwall is not required by this patch to migrate storage from Markdown or to instantiate every fact as a database row.

The graph model exists so future agents can follow explicit knowledge relationships rather than relying exclusively on semantic search across prose.

## Recursive relationships

Entities and relationships are both addressable knowledge objects.

A relationship may therefore participate as an endpoint in another relationship when the second relationship is specifically about the first connection rather than merely about either endpoint.

Example:

`Process: Write Pull Request --applies_to--> Repository A`

A team-specific rule may then relate a team to that particular `applies_to` relationship rather than incorrectly attaching the rule globally to either the process or repository.

This recursion must remain controlled rather than arbitrary.

When a relationship accumulates substantial identity, behavior, rules, history, or additional relationships, prefer **reification**: promote the relationship concept into an entity and connect the original participants to that entity with simpler typed relationships.

The rule is:

> Relationships may be addressed and related to directly. When the relationship itself becomes a durable domain concept with substantial independent structure, reify it as an entity.

## Relationship vocabulary

Relationship types should come from a controlled vocabulary where practical.

Agents may propose new relationship types but must not silently mint durable ontology terms merely because a phrase is convenient during one integration.

Relationship vocabulary changes are semantic governance changes and require appropriate authority.

## Local paper trails

The immutable patch/submission archive remains the global evidentiary record.

For practical retrieval, each entity and relationship may maintain a local history containing pointers to the patches, claims, decisions, or evidence that changed that object.

The local history should normally reference the authoritative source records rather than duplicate their full rationale.

Normal retrieval should be able to proceed:

**knowledge object → current claims → local history → related objects → original patch only when deeper provenance is needed**

This allows an agent to pull a THREAD without replaying the full global intake history.

## THREAD as graph traversal

THREAD remains **Traceable History of Requirements, Evidence, Authority, and Decisions**.

Under the graph model, a THREAD can be understood concretely as a traversable provenance or dependency path through entities, relationships, claims, evidence, and decisions.

Pulling a THREAD should preferentially follow explicit graph relationships where available and use semantic search to discover missing or unmodeled relationships rather than requiring semantic search for every hop.

Explicit edges assist discovery but do not create authority by themselves.

## Highwall as reference implementation

Highwall should document this graph abstraction as part of the general CLOTH architecture while remaining a Markdown-first implementation for now.

Existing authoritative pages, intake reviews, claim indexes, provenance links, contradiction records, and consistency audits can be understood as partial projections of the graph model.

Do not perform a wholesale conversion of existing Highwall lore into explicit entity and relationship records under this patch.

Future work may incrementally add graph-native indexes or structured representations if they provide practical value and are introduced through a later authorized patch.

## Non-goals

This patch does not:

- change Highwall lore or story canon
- require a graph database
- require rewriting existing canon pages into atomic triples
- erase document-level authoritative homes
- authorize arbitrary recursive relationship nesting without semantic justification
- replace immutable global provenance with local histories
- permit inferred relationships to become authoritative merely because an agent generated them
- rewrite historical seed or stitch submissions

<!-- END OF STITCH -->
