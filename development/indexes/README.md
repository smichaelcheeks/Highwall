# Development Indexes

Generated navigation artifacts belong here. They summarize repository records
for discovery and do not establish canon, resolve contradictions, or replace
their source documents.

`claim-index.json` is generated from intake-review claim tables by
`scripts/build_claim_index.py`. Edit the reviews, then regenerate the index;
never edit the generated JSON by hand.

`knowledge-graph.json` is generated from stable entity identities and explicit
relationship objects in Markdown front matter by
`scripts/build_graph_index.py`. It is a navigation projection, not an
authoritative lore source. Edit the Markdown records and relationship-type
registry, then regenerate it; never edit the generated JSON by hand.
