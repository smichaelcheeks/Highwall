# Controlled Graph Relationship Types

Relationship types are governed ontology. Add or change a type only through an
authorized semantic patch. The generated graph index reads this table as its
machine-visible registry.

| Relationship type | Directionality | Authority effect | Source kinds | Target kinds | Self-link | Inverse | Provenance policy | Definition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `related-to` | `symmetric` | `navigation-only` | `entity, relationship, claim` | `entity, relationship, claim` | `forbidden` | `related-to` | `navigation` | Preserves an explicitly maintained generic `related` association without asserting a more specific domain relationship. |

`related-to` does not establish location, membership, ownership, chronology,
causation, government, dependency, or any other setting fact. A later patch may
replace a generic association with a more specific controlled type only when
that semantic relationship has adequate authority and provenance.

Every registry row controls directionality, authority effect, permitted
endpoint kinds, self-link behavior, inverse behavior, and provenance policy.
`none` is the controlled inverse value when a directed type has no registered
inverse. Controlled provenance policies are `navigation`, `semantic-canon`,
`semantic-working`, and `administrative`. Changing any of these fields is
governed ontology work.

Provenance policies apply to every schema-v2 relationship and its exact intake
claims:

| Provenance policy | Permitted completed review authority | Permitted current-object provenance |
| --- | --- | --- |
| `navigation` | `establish-policy`, `establish-canon`, or `working-canon` | `create`, `update`, or `link-only`; `retire` only on a tombstone |
| `semantic-canon` | `establish-canon` | `create` or `update`; `retire` only on a tombstone |
| `semantic-working` | `establish-canon` or `working-canon` | `create` or `update`; `retire` only on a tombstone |
| `administrative` | `establish-policy` | `create` or `update`; `retire` only on a tombstone |

Every cited intake claim's target must name the relationship ID. A completed
review with `no-change`, `defer`, `conflict`, or `out-of-scope` disposition
cannot establish or change a relationship object. The relationship's history
event must also match the action: `relationship-added` uses `create` or, for a
navigation relationship, `link-only`; ordinary modification uses `update`;
supersession uses `update` or `retire`; and retirement uses `retire`. Current
provenance is cumulative, but no cited disposition authorizes a different
action merely because it is permitted elsewhere in that object's history.
