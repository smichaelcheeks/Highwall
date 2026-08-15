# Front Matter

All canon content pages must begin with YAML front matter. Index `README.md` files are navigational documents and do not require it. Story and development pages may reuse this schema or their dedicated templates.

## Base schema

```yaml
---
title: TODO
type: TODO
entity_id: entity-stable-slug
relationships: []
status: draft
canon_level: working
aliases: []
tags: []
related: []
provenance: []
---
```

## Fields

| Field | Required | Purpose |
| --- | --- | --- |
| `title` | Yes | Human-readable canonical title |
| `type` | Yes | Subject kind, such as `character`, `place`, or `historical-event` |
| `entity_id` | Yes | Stable graph identity in the form `entity-<slug>` |
| `relationships` | Yes | Addressable typed graph relationships maintained on this record |
| `status` | Yes | Document workflow state |
| `canon_level` | Yes | Authority of the page's approved claims |
| `aliases` | Yes | Alternate names and spellings; use an empty list when none are documented |
| `tags` | Yes | Broad discovery labels; do not use tags as a substitute for links or taxonomy |
| `related` | Yes | Relative links to directly related authoritative pages |
| `provenance` | Yes | Intake reviews or decision records that established or materially changed the page |

## Controlled values

### `status`

- `draft`: incomplete or newly created
- `review`: ready for authorial review
- `active`: maintained and accepted for its stated canon level
- `deprecated`: superseded; must link to the replacement or retirement record

### `canon_level`

- `established`: explicitly approved setting truth
- `working`: provisionally accepted but still subject to revision
- `unresolved`: competing or incomplete claims; link to an open question or contradiction report

Do not use `discarded` as a canon level. Move discarded material to [`../development/retired/`](../development/retired/README.md).

## Links in metadata

Use repository-relative Markdown paths as quoted strings:

```yaml
related:
  - "../places/example-place.md"
```

Keep relationships meaningful and reciprocal when useful. Do not list every page that happens to mention the subject.

`related` remains the human-readable compatibility field during incremental
migration. New graph relationships use the controlled schema in
[`graph-structure.md`](graph-structure.md); do not infer a typed relationship
from prose or silently mint a relationship type.

`provenance` is cumulative. Add the intake review or decision record responsible for a material change; do not remove earlier entries merely because a later submission revises the page. The detailed review identifies which individual claims were affected.
