# Controlled Graph Relationship Types

Relationship types are governed ontology. Add or change a type only through an
authorized semantic patch. The generated graph index reads this table as its
machine-visible registry.

| Relationship type | Directionality | Authority effect | Definition |
| --- | --- | --- | --- |
| `related-to` | symmetric | navigation-only | Preserves an explicitly maintained generic `related` association without asserting a more specific domain relationship. |

`related-to` does not establish location, membership, ownership, chronology,
causation, government, dependency, or any other setting fact. A later patch may
replace a generic association with a more specific controlled type only when
that semantic relationship has adequate authority and provenance.
