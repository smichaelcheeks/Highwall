# Repository Standards

These standards govern the Highwall CLOTH. The architecture and terminology
are defined in the [`CLOTH / THREAD model`](cloth-thread-model.md).

## Naming and layout

- Use lowercase kebab-case filenames, such as `example-place.md`.
- Use one primary subject per canon page.
- Use directories to classify domains, not canon authority.
- Add a short `README.md` when creating a new directory so its purpose and boundaries are explicit.
- Store media in a nearby `assets/` directory only when needed; use descriptive filenames and relative links.

## Content ownership

Every factual claim should have one authoritative page. Other pages may summarize only enough to provide context and should link back to that authority. If it is unclear which page owns a fact, resolve ownership before adding duplicate descriptions.

Use these boundaries:

| Information | Authoritative location |
| --- | --- |
| Original batch of submitted information | `intake/submissions/` |
| Objective setting truth | `canon/` |
| Plot, viewpoint knowledge, or reveal order | `story/` |
| Authoritative out-of-world creative guidance | `design/` |
| Unapproved possibility or unresolved issue | `development/` |
| External research or repository guidance | `references/` |
| Discarded material retained for history | `development/retired/` |
| Claim-level processing audit | `development/intake-reviews/` |

## Markdown

- Use a single level-one heading matching the page title.
- Use descriptive headings and short sections.
- Prefer relative Markdown links with meaningful link text.
- Do not use tool-specific embeds, transclusions, or query syntax in canonical content.
- Mark incomplete content with `TODO:` and state exactly what is missing.
- Avoid empty prose that could be mistaken for a claim; `Unknown` or `Not yet documented` is safer.

Use missing-information terms precisely:

- `Not established.` means the author has supplied no answer.
- `None.` means the author explicitly established that nothing exists in the
  stated category.
- `TODO:` identifies a specific known task or missing detail.

Never convert missing information into an explicit negative claim.

## Claims and perspectives

Label claims according to what they represent:

- **Setting truth:** an explicitly documented fact.
- **In-world belief:** attributed to a named person, culture, institution, text, or tradition.
- **Historical claim:** an account whose accuracy may be disputed.
- **Narrative information:** what a reader or character learns and when.
- **Development idea:** an unapproved possibility.

Do not use confident prose to erase these distinctions.

## Design guidance

Design principles may justify a creative or editorial choice but cannot
establish an in-world fact. When a principle relies on a setting premise, link
to its authoritative canon page. Do not infer missing lore from design intent.

Real-world history, geography, cultures, places, and institutions are
out-of-world development or source context, not fictional setting facts. Record
them only when the author explicitly identifies them as inspirations or source
material. Do not place the comparisons in canon sections, treat real-world
names as in-world entities, or use analogies as canon evidence.

## Canon changes

A significant canon change must:

1. Have explicit authorial authority.
2. Update the authoritative canon page.
3. Update affected links or dependent summaries.
4. Add an entry to [`../development/canon-changes.md`](../development/canon-changes.md).
5. Link the originating intake review when applicable.
6. Link a decision record when the rationale or rejected alternatives should be preserved.

## Provenance and auditability

Submission files are immutable after review begins. Derived classifications, decisions, and rationale belong in a separate intake review and must not be appended to or silently incorporated into the source file.

Every substantive claim must receive a disposition, even when no repository content changes. Reviews record concise, evidence-based rationale: the applicable repository rule, the source or existing page considered, and the reason the disposition follows. They do not need a transcript of private or exploratory reasoning.

Use stable submission and claim identifiers so canon changes, contradiction reports, decisions, and Git commits can refer back to the exact reviewed material. Follow [`intake-workflow.md`](intake-workflow.md).

Intake-review `CASE-...-C...` identifiers preserve submitted claims and their
dispositions. Maintained `claim-...` identifiers address decision-worthy
assertions on their natural authoritative Markdown records. A maintained claim
must bind exact prose, subjects, authority, lifecycle, and review-claim
provenance; do not mechanically promote every intake claim into one.

A traceable provenance or dependency chain is a THREAD. An explicitly
unresolved relationship may remain a loose thread without being erroneous; a
missing or irreconcilable provenance connection is a broken thread and should
be repaired or explicitly documented. Pulling a thread discovers sources and
consequences but does not grant authority to change knowledge.

## Semantic and mechanical changes

A semantic change alters what the CLOTH records, authorizes, leaves unresolved,
or requires contributors to do. Lore, story, governance, taxonomy, ontology,
authority, contradiction, and ownership changes require a governed patch and
stitching process.

Durable graph relationship types are governed ontology. Contributors may
propose a new relationship type but must not silently establish one while
integrating an otherwise unrelated patch. See the authoritative
[`CLOTH / THREAD model`](cloth-thread-model.md).
Explicit entities and relationships must follow
[`graph-structure.md`](graph-structure.md) and the controlled
[`relationship-types.md`](relationship-types.md) registry. The generated graph
index is navigation-only; its Markdown sources retain authority.

Every migrated knowledge object maintains append-only local history. A
materially different relationship or claim receives a new durable ID and
supersedes or retires the earlier tombstone; published relationship type and
endpoints, history events, and durable IDs are not rewritten or reused. Every
object change appends a compatible event, and every exact provenance claim
must have authority and disposition for the result and name its durable object
ID.

A mechanical change preserves meaning, such as an unambiguous typo,
formatting, link, equivalent-path, or generated-file repair. Mechanical edits
do not create semantic authority. Changes to these repository standards and
other CLOTH governance are themselves semantic and must use the governed
process when available.

## Contradictions

Do not choose a preferred version based on plausibility, recency, or prose quality alone. Create a report under [`../development/contradictions/`](../development/contradictions/README.md), document both claims and their locations, identify impact, and await an explicit decision.

## Deletion and retirement

Do not delete meaningful setting material solely because it is no longer canon. Move it to `development/retired/` when provenance matters, link the retiring decision, and remove or revise canon references only after authorization.
