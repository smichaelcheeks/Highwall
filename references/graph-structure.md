# Knowledge Object Graph Structure

This document defines Highwall's explicit Markdown-first implementation of the
graph abstraction in the [`CLOTH / THREAD model`](cloth-thread-model.md).
Markdown records remain authoritative. Generated indexes are navigation-only
and cannot establish facts, relationship semantics, authority, or provenance.

Schema v2 is being introduced through the staged
[`migration ledger`](../development/knowledge-object-schema-v2-migration.md).
A current generated index does not mean that the migration inventories are
empty or that the overall program is complete.

## Identity classes

Schema v2 distinguishes maintained objects from immutable processing records:

- `entity-...` identifies an entity;
- `relationship-...` identifies a typed connection;
- `claim-...` identifies a maintained knowledge assertion;
- `history-...` identifies a local changelog event; and
- `CASE-...-C...` identifies an immutable intake-review claim.

Maintained and intake claim IDs are not interchangeable. The former identifies
knowledge expressed on an authoritative record; the latter identifies source
input and its review disposition.

All durable IDs use lowercase kebab case after their controlled prefix, remain
stable through ordinary wording, title, and path changes, and must never be
reused for another object.

## Entity records

An authoritative Markdown record becomes an explicit graph entity by declaring
a stable `entity_id` in front matter. Canon content pages require one. Other
record classes may opt in as their migration is reviewed.

```yaml
entity_id: entity-highwall
graph_status: active
history_coverage: prospective
supersedes: []
superseded_by: []
```

An entity's `graph_status` is `active`, `superseded`, or `retired`. Retired and
superseded objects remain indexed as tombstones. Supersession names the earlier
and later entity IDs in both directions, follows the same lifecycle integrity
rules as relationships and claims, and may not form a cycle. A page remains the
entity's authoritative human-readable surface; the index records its current
path and metadata without replacing it.

## Relationship records

An entity page may declare addressable relationship objects in its
`relationships` front-matter list:

```yaml
relationships:
  - relationship_id: relationship-highwall-related-to-regional-trade-system
    relationship_type: related-to
    source: entity-highwall
    target: entity-regional-trade-system
    graph_status: active
    history_coverage: prospective
    supersedes: []
    superseded_by: []
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - CASE-YYYY-MM-DD-EXAMPLE-S01-C001
```

Every migrated relationship requires:

- a unique `relationship-...` ID;
- a controlled type from
  [`relationship-types.md`](relationship-types.md);
- source and target IDs of kinds permitted by that registry row;
- an explicit lifecycle;
- the relationship type's controlled provenance policy;
- review paths and exact immutable intake-claim provenance; and
- a local history event.

Relationship type and endpoints are immutable after publication. Changing
either creates a new relationship and retires or supersedes the old one. Both
directions of supersession are recorded and the earlier object remains
addressable.

The registry controls directionality, authority effect, permitted endpoint
kinds, self-link behavior, inverse behavior, and provenance policy. Validation
rejects duplicate symmetric pairs, prohibited self-links, unauthorized or
irrelevant provenance, and ownership inconsistent with directionality.

## Maintained knowledge claims

A decision-worthy assertion becomes addressable through a stable `claim-...`
ID in the owning record's `claims` metadata:

```yaml
claims:
  - claim_id: claim-highwall-example
    content_id: claim-highwall-example
    truth_kind: objective
    authority_level: established
    lifecycle: active
    history_coverage: complete
    about:
      - entity-highwall
    supersedes: []
    superseded_by: []
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - CASE-YYYY-MM-DD-EXAMPLE-S01-C002
```

The assertion remains readable Markdown between exact hidden boundaries:

```markdown
<!-- claim:claim-highwall-example:start -->
The maintained assertion appears here.
<!-- claim:claim-highwall-example:end -->
```

The generated projection hashes the normalized bounded passage for change
detection. The hash remains navigation metadata; the bounded Markdown passage
is authoritative.

Prospective validation includes that content hash in the claim's canonical
state. Changing bounded content under an existing claim ID therefore requires
an appended compatible claim-history event. Semantic review must still decide
whether the change is a wording clarification or a materially different claim
that requires a new ID and supersession.

Only an assertion needing independent citation, authority, lifecycle,
contradiction, disclosure, or multi-object scope requires a maintained claim
ID. Ordinary descriptive prose does not become an atomic claim merely because
it appears on an entity page.

Controlled truth kinds distinguish objective setting truth, in-world belief,
historical claim, character knowledge, reader reveal, design, administrative
policy, proposal, and question. Authority and lifecycle remain separate.

The `about` list creates navigation bindings only. It does not assign semantic
roles, strengthen the bounded assertion, or make it true. Semantic
relationships to a claim require a separately authorized controlled type.

Exact claim provenance must authorize the maintained result. Established lore
requires an `establish-canon` review; working lore permits `establish-canon` or
`working-canon`; design and administrative claims require `establish-policy`;
and proposal or question claims may use `proposal-only`, `classify`, or
`establish-policy`. The intake claim must use an authorizing `create`, `update`,
or `retire` disposition and its target must name the maintained claim ID;
proposal and question claims may also use `defer`. `no-change`, `link-only`,
conflict, and out-of-scope claims cannot establish or change maintained claim
content, and `defer` cannot establish lore truth.

## Intake claims

Existing `CASE-...-C...` claim IDs remain immutable review objects. They record
what a patch submitted, its classification, authority basis, disposition, and
resulting target. A maintained claim cites the exact intake claims that
established or changed it.

One intake claim may establish, revise, supersede, or produce no change to a
maintained claim. Administrative, deferred, rejected, and no-current-state
intake claims are not mechanically converted into maintained facts. The
schema-v2 migration must give every baseline intake claim an explicit crosswalk
result.

## Local object histories

Every migrated entity, relationship, and maintained claim has an append-only
history on its owning Markdown record:

```yaml
history:
  - history_id: history-highwall-001
    sequence: 1
    object_id: entity-highwall
    change_type: graph-registered
    review_claims:
      - CASE-YYYY-MM-DD-EXAMPLE-S01-C001
    summary: Registered the existing page as a graph entity.
```

History sequences are contiguous per object. Published events are never
rewritten. Their summaries remain concise and point to exact intake claims;
reviews retain full rationale and Git retains exact file changes. A migration
entry uses `graph-registered` and must not falsely claim that pre-existing lore
was newly established.

Base-ref validation compares isolated canonical state for each object. Entity
state excludes nested relationship, maintained-claim, and history metadata;
bounded claim passages are represented by stable claim markers rather than
their content. Relationship state contains that relationship's metadata, and
claim state contains its metadata plus its bounded-content hash. Every state or
owner-path change must append a compatible next event for that object. An older
event cannot satisfy a later change.

Historical coverage that has not been reconstructed remains explicitly
provenance-only in the migration ledger. Missing events are not presented as a
complete changelog.

`history_coverage` is controlled: `provenance-only` means local event coverage
has not been audited; `prospective` means it is complete from the first
schema-v2 event forward while earlier changes remain in cumulative provenance;
and `complete` means all known authoritative changes were reconstructed and
audited. New objects normally begin as `complete` because their establishment
is their first event.

## Ownership, recursion, and reification

Store an object on the Markdown record that owns its authoritative
explanation. A directed relationship lives on the authoritative record of its
source object. A symmetric relationship may live on the authoritative record
of either endpoint. Ownership compares record paths, not an owning page's
entity ID, so relationships and maintained claims can participate without
becoming separate entity pages. A record may own explicit knowledge metadata
without opting the entire page into entity identity. The explicit source and
target remain traversable without inferring them from storage.

Endpoints may name any registered addressable object kind when the controlled
relationship type permits it. Schema v2 currently recognizes entities,
relationships, maintained claims, local history events, and immutable intake
claims as addressable endpoint classes; a registry row may allow only the
subset appropriate to its meaning. This allows a relationship to be about
another relationship, fact, or change record. When a relationship develops
substantial identity, rules, history, or structure, reify it as an entity and
connect its participants through simpler relationships.

An explicit edge assists discovery but never creates authority. Its type,
endpoints, scope, and provenance must follow an authorized source.

## Generated projection

`development/indexes/knowledge-graph.json` is generated by
`scripts/build_graph_index.py`. Schema v2 includes:

- opted-in entities and their authoritative Markdown paths;
- explicit relationships and their owning records;
- maintained knowledge claims and bounded-content hashes;
- local history events;
- immutable submissions, reviews, and intake claims needed for traversal;
- decisions, exception records, and review-owned evidence references;
- the controlled relationship-type registry;
- validated endpoint and provenance pointers;
- legacy `related` links not represented by explicit relationships; and
- explicit schema-v2 migration inventories.

The specialized claim index remains a compatibility view during migration.
Edit Markdown records or the relationship registry and regenerate indexes;
never edit generated JSON directly.

## Incremental migration

Migration proceeds in governed stages:

1. Establish schema, lifecycle, history, provenance, and completion policy.
2. Implement structural parsing, projection, prospective validation, and
   visible migration inventories.
3. Audit and backfill every baseline entity and relationship history.
4. Crosswalk every baseline intake claim to a maintained claim or an explicit
   non-current-state category.
5. Add maintained knowledge claims without changing their bounded prose.
6. Add semantic relationship types only through separately authorized patches.
7. Implement deterministic THREAD traversal.
8. Run an independent canon-equivalence and completion audit.

Legacy `related` links remain compatibility navigation until a later policy
patch removes or redefines them. Generic links may migrate only to
navigation-only `related-to` and cannot support a stronger semantic type.

## Validation

Repository validation rejects malformed or duplicate identities, uncontrolled
types or provenance policies, invalid endpoint kinds, unresolved endpoints,
prohibited self-links, duplicate symmetric pairs, invalid ownership,
unauthorized or irrelevant provenance, invalid claim boundaries,
non-contiguous or unappended history, and broken lifecycle or supersession.

Prospective validation compares canonical object state with a supplied Git
base so stable IDs cannot disappear or change kind, every object change appends
a compatible event, published histories cannot be rewritten, and relationship
endpoints or type cannot be mutated in place. Owning paths remain mutable: a
move preserves the earlier event content and appends a controlled `moved`
event on the relocated record. A generic metadata event cannot stand in for a
move, lifecycle transition, or bounded claim-content change.

Structural validation cannot prove semantic correctness. Relationship scope,
claim meaning, authority, canon equivalence, and story boundaries still require
the governed patch and consistency workflow.
