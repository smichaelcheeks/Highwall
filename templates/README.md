# Templates

Copy the closest template when creating a page; do not edit a template to contain Highwall-specific facts. Replace every `TODO` intentionally and remove optional sections that do not apply.

## Canon templates

- [`character.md`](character.md)
- [`place.md`](place.md)
- [`institution.md`](institution.md)
- [`historical-event.md`](historical-event.md)
- [`culture.md`](culture.md)
- [`government-office.md`](government-office.md)
- [`organization.md`](organization.md)
- [`technology.md`](technology.md)

## Development templates

- [`lore-seed.md`](lore-seed.md) prepares a lore patch with ChatGPT or another
  assistant before repository intake; it is not itself an intake record. The
  legacy filename remains stable for links and compatibility.
- [`intake-submission.md`](intake-submission.md)
- [`conversation-addendum.md`](conversation-addendum.md)
- [`intake-review.md`](intake-review.md)
- [`maintenance-review.md`](maintenance-review.md)
- [`incremental-audit-review.md`](incremental-audit-review.md)
- [`decision-record.md`](decision-record.md)
- [`open-question.md`](open-question.md)
- [`contradiction-report.md`](contradiction-report.md)

Canon templates default to `status: draft` and `canon_level: working`. Those defaults do not grant approval; change `canon_level` to `established` only when explicitly authorized.

Replace `entity_id: TODO` with a stable ID under
[`../references/graph-structure.md`](../references/graph-structure.md). Leave
`relationships: []` empty unless an authorized, controlled relationship is
being recorded with resolvable endpoints and provenance.

The lore-patch template is author-facing. The intake-submission template is
the repository-facing wrapper that assigns identifiers and preserves a
completed patch source verbatim. Do not ask a drafting assistant to manufacture repository
metadata or processing decisions.
