# Repository Standards

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

## Claims and perspectives

Label claims according to what they represent:

- **Setting truth:** an explicitly documented fact.
- **In-world belief:** attributed to a named person, culture, institution, text, or tradition.
- **Historical claim:** an account whose accuracy may be disputed.
- **Narrative information:** what a reader or character learns and when.
- **Development idea:** an unapproved possibility.

Do not use confident prose to erase these distinctions.

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

## Contradictions

Do not choose a preferred version based on plausibility, recency, or prose quality alone. Create a report under [`../development/contradictions/`](../development/contradictions/README.md), document both claims and their locations, identify impact, and await an explicit decision.

## Deletion and retirement

Do not delete meaningful setting material solely because it is no longer canon. Move it to `development/retired/` when provenance matters, link the retiring decision, and remove or revise canon references only after authorization.
