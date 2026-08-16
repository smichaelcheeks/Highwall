# CLOTH / THREAD Model

Highwall is an instance of a **CLOTH**: a **Coherent Library of Ongoing
Thought and History**. A CLOTH is a governed knowledge system that maintains a
coherent, traceable body of evolving knowledge over time. Highwall is this
CLOTH's subject matter; the architecture is domain-independent.

The CLOTH contains more than authoritative current-state knowledge. It may
also preserve working knowledge, unresolved questions, contradictions,
proposals, retired knowledge, sources, decisions, claim relationships, and the
recorded consequences of accepted changes. Its purpose is to preserve
coherence, provenance, history, uncertainty, authority, and change
relationships so future human or machine work can identify both the current
knowledge state and how it arose.

## THREADs

A **THREAD** is a **Traceable History of Requirements, Evidence, Authority,
and Decisions**: a provenance and dependency chain through knowledge in the
CLOTH. The expansion identifies information a THREAD may connect; every THREAD
need not contain every category.

A THREAD may connect an intended outcome, source evidence, assumptions,
claims, authority decisions, open questions, contradictions, clarifications,
supersessions, authoritative knowledge, and downstream effects. A claim may
participate in multiple THREADs, a patch may affect multiple THREADs, and
THREADs may intersect through shared knowledge. THREAD names the relationship,
not every claim or document participating in it.

To **pull a thread** is to trace provenance backward or dependencies forward.
Backward tracing asks where a claim originated, what supported and authorized
it, and what it superseded. Forward tracing asks what depends on it, where it is
expressed, and what would require reconsideration if it changed. Targeted and
repository-wide semantic consistency review are mechanisms for pulling
affected THREADs. Discovery alone grants no authority to alter knowledge.

A **loose thread** is an explicitly unresolved or attention-requiring
relationship, such as a contradiction, unanswered question, provisional or
potentially stale claim, or dependency awaiting review. Loose threads can be
legitimate coherent states and are not automatically errors.

A **broken thread** is a provenance or traceability failure, such as
authoritative knowledge without identifiable authority or a downstream claim
disconnected from its supporting decision. Repair a broken thread when
possible; otherwise document the deficiency explicitly.

## Patches and stitching

A **patch** is the author-facing unit of intentional semantic change prepared
for a CLOTH. It is a bounded, declarative delta that may add, clarify,
supersede, retire, relate, reclassify, or otherwise change knowledge or
repository governance.

To **stitch a patch into CLOTH** is to perform the governed semantic
integration that determines the patch's consequences across the coherent
current state. Stitching is broader than editing the most obvious target file.
It pulls every affected THREAD, identifies dependencies and supersessions,
creates required exception records, updates authoritative locations and
provenance, and applies the required consistency review.

The conceptual order is:

**Patch → review and authority determination → stitch/integration → integration
review and current-state changes → validation → publication**

The accepted delta authorizes the integration. The integration determines the
consequences. The resulting diff records current-state changes; the review
records how and why they were derived; Git and the pull request record
publication.

Patch is a conceptual change unit, not a replacement for the distinct
technical records used to process it. Continue to preserve separately:

1. the immutable submission or author instruction;
2. the intake or integration review and its claim dispositions;
3. resulting current-state changes;
4. required exception records; and
5. Git and pull-request publication history.

Technical names such as `intake-submission` and `intake-review` remain correct.
Do not rename every participating record to “patch.”

## Graph-oriented knowledge abstraction

CLOTH uses a graph-oriented conceptual model. Highwall implements that model
with Markdown-first authoritative records and a generated graph index.

The core knowledge primitives are:

1. **Entity** — an addressable thing or concept in the knowledge domain.
2. **Relationship** — an addressable, typed connection between knowledge
   objects.
3. **Claim** — an assertion about an entity or relationship, with provenance,
   authority, lifecycle, confidence, and scope as applicable.
4. **Patch** — the bounded semantic transaction that changes claims, entities,
   relationships, or governance under traceable authority.

Documents remain useful human-readable projections and may remain the
maintained authoritative surfaces. The graph abstraction exists so agents can
follow explicit relationships instead of depending on semantic search for every
hop. Semantic search remains valuable for discovering missing, implicit, or
unmodeled relationships.

Highwall does not require a graph database or an atomic rewrite of all lore.
Stable entity IDs and addressable, controlled relationship objects are added
incrementally to maintained Markdown records. The generated
`development/indexes/knowledge-graph.json` projects those records for machine
traversal and inventories legacy `related` links that have not yet been
migrated. The Markdown records remain authoritative. See
[`graph-structure.md`](graph-structure.md).

## Recursive relationships and reification

Entities and relationships are both addressable knowledge objects. A
relationship may therefore be the endpoint of another relationship when the
new relationship is specifically about that connection rather than merely
about either original endpoint.

For example, a generic process may `apply_to` a particular repository, while a
team-specific policy may govern that particular `applies_to` relationship.
Attaching the team rule directly to the generic process or repository would
incorrectly broaden its scope.

Relationship recursion must remain semantically justified rather than
arbitrary. When a relationship accumulates substantial independent identity,
behavior, rules, history, or additional relationships, **reify** it: represent
the relationship concept as an entity and connect its participants through
simpler typed relationships.

> Relationships may be addressed and related to directly. When a relationship
> becomes a durable domain concept with substantial independent structure,
> reify it as an entity.

Relationship types should use a controlled vocabulary where practical. Agents
may propose new types but may not silently mint durable ontology terms. A new
relationship type is a semantic governance change and requires appropriate
authority.

## Local paper trails

The immutable patch/submission archive remains the global evidentiary record.
For practical retrieval, every schema-v2 entity, relationship, and maintained
knowledge claim has an append-only local history that points to the patches,
intake claims, decisions, or evidence that changed that knowledge object.
Records not yet migrated expose that incomplete coverage rather than implying
that a missing history is complete.

Local history should reference authoritative records rather than duplicate
full rationale. Normal retrieval should therefore be able to proceed:

**knowledge object → current claims → local history → related objects → original
patch when deeper provenance is needed**

This makes pulling a THREAD efficient without requiring an agent to replay the
entire global intake history.

An immutable intake claim and a maintained knowledge claim are distinct
objects. Intake claims preserve what a patch submitted and how review disposed
it. Maintained claims identify decision-worthy current or historical
assertions on their natural owning Markdown records. One intake claim may
establish, change, supersede, or produce no change to a maintained claim.

## Coherence and authority

Coherence does not require every recorded statement to agree. A coherent CLOTH
may explicitly represent conflicting, uncertain, provisional, rejected,
historical, perspectival, and unresolved claims. A represented contradiction
is coherent; a provisional claim presented as established fact, or a character
belief presented as objective truth, is not.

Truth kind, lifecycle authority, and confidence remain distinct. Reviewer
confidence and repository presence do not create authority. An explicit graph
edge likewise assists discovery but does not create authority merely by
existing.

The repository is maintained current state with durable source and
supersession history, not a pure event-sourced system that must be mechanically
replayed byte for byte. Its governing invariant is:

> No semantic change to the maintained knowledge state should occur without
> traceable authority for that change.

## Semantic and mechanical change

A **semantic change** alters what the CLOTH says, treats as authoritative,
leaves unresolved, or requires future contributors to do. Lore, story truth,
authority, contradiction resolution, governance, taxonomy, ontology, and ownership
changes therefore require governed integration.

A **mechanical change** preserves meaning, as with an unambiguous typo,
formatting or broken-link repair, equivalent path maintenance, or generated
file refresh. Mechanical maintenance does not acquire semantic authority merely
because it changes files.

The CLOTH's operating rules are themselves governed knowledge. Changes to
intake, patches, stitching, consistency tiers, dispositions, authority,
templates, validation, terminology, ontology, agent instructions, or semantic
governance must use the governed process when available. The CLOTH may stitch
patches that change how later patches are stitched, but that self-modification
must remain explicit, attributable, reviewable, and auditable.

## Terminology compatibility

Use **patch** as the preferred general author-facing term for newly prepared
semantic change. Use **stitch** and **stitching** for the governed integration
operation. Retain **stitch** as a historical noun and **seed** where they
identify immutable historical submissions, specifically named legacy
artifacts, legacy completion markers, or compatibility behavior. Never rewrite
immutable submissions for terminology alone.

New patches use the completion marker:

```text
<!-- END OF PATCH -->
```

The prior marker remains accepted indefinitely:

```text
<!-- END OF STITCH -->
```

The oldest legacy marker also remains accepted indefinitely:

```text
<!-- END OF SEED -->
```

Any recognized literal marker satisfies `completion_basis: end-marker`. The
transmission-completeness guarantee and all distinct source, review, authority,
provenance, and publication boundaries remain unchanged.
