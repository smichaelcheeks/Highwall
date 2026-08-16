# Development Indexes

Generated navigation artifacts belong here. They summarize repository records
for discovery and do not establish canon, resolve contradictions, or replace
their source documents.

`claim-index.json` is generated from intake-review claim tables by
`scripts/build_claim_index.py`. Edit the reviews, then regenerate the index;
never edit the generated JSON by hand.

`knowledge-graph.json` is the unified schema-v2 projection generated from
entities, relationships, maintained claims, local histories, submissions,
reviews, and immutable intake claims by `scripts/build_graph_index.py`. It also
exposes incomplete migration inventories. It is a navigation projection, not
an authoritative lore source. Edit the owning Markdown records and controlled
registries, then regenerate it; never edit the JSON by hand.

`claim-index.json` remains a compatibility view of immutable intake-review
claims during schema-v2 migration. A fresh generated file proves index
determinism, not semantic correctness or migration completion.
