# Lore Stitch Authoring Template

Use this template before repository intake when you want ChatGPT or another
assistant to organize raw lore into a clear stitch. The finished stitch is
source material, not a canon page. Repository processing later preserves it
verbatim inside an intake submission and audits its claims separately.

The `lore-seed.md` filename is retained for compatibility with existing links;
new author-facing prose and output use stitch terminology.

## Copyable assistant instruction

```text
Help me turn my notes and answers into a structured Highwall lore stitch.

Rules:
- Do not invent facts, explanations, names, motives, dates, relationships, or
  connective details.
- Do not make an uncertain statement more definite than I made it.
- Prefer recording author-supplied facts over writing polished encyclopedia
  prose. Do not add explanatory or connective text unless I explicitly
  supplied it or request editorial assistance.
- Keep objective setting truth separate from in-world belief, disputed history,
  character knowledge, reader reveals, and ideas still under consideration.
- If two statements appear inconsistent, preserve both and flag the apparent
  conflict. Do not reconcile them yourself.
- If a required section has no supplied information, write `Not established.`
  Use `None.` only when I explicitly establish the absence of something. Use
  `TODO:` only for a specific known task or missing detail. Do not fill gaps.
- Ask focused clarification questions when an answer would materially change
  meaning. Otherwise, organize what I supplied and list the remaining unknowns.
- If I ask for an interview, ask one focused question at a time and periodically
  summarize what I have actually confirmed. Do not offer invented answers as if
  I supplied them, and do not treat my consideration of an option as approval.
- Preserve intentional ambiguity and spoiler boundaries exactly as I identify
  them.
- When a fact belongs primarily to another planned stitch, mention it only
  briefly if necessary for context. Do not expand or duplicate that material.
- Treat comparisons to real-world history, geography, cultures, or institutions
  as development context, never as fictional setting facts. Include them only
  when I explicitly identify them as inspirations or source context, and keep
  them out of canon sections.
- Do not assign repository case IDs, claim IDs, filenames, front matter, or
  processing dispositions. Codex will do that during repository intake.
- Before producing the final document, ask me to confirm its authority as one
  of: established canon, working canon, or proposal only; and its intended
  repository session mode as one of: exploration, canon-authoring, or
  direct-integration.
- Return the final result as plain Markdown using the stitch format below.
- Omit optional sections that have no supplied content; do not create filler
  prose.
- End the final document with the literal `<!-- END OF STITCH -->` marker on its
  own line. Do not emit that marker until the full document is complete.

My notes begin after this line:

[PASTE NOTES OR BEGIN THE INTERVIEW HERE]
```

## Optional repository context

```text
Highwall is a governed CLOTH and controlled canon repository. A lore stitch is
preserved source material, not automatically canon. Codex later preserves the finished stitch
verbatim, inventories every substantive claim in a separate review, records
every decision and deliberate non-change, and places authorized facts in one
authoritative location.

Canon contains objective setting truth. Story contains character knowledge,
reader knowledge, chronology, and reveals. Design contains out-of-world
authorial guidance but cannot establish fictional facts. Development contains
proposals, questions, contradictions, decisions, and retired ideas.

Once review begins, a submission is immutable. Later confirmed corrections and
additions are preserved in separately numbered addenda. Contradictions are
documented rather than silently resolved. Missing information remains unknown
or becomes an open question. Repository identifiers, dispositions, file
destinations, validation, branches, and draft pull requests are Codex's
responsibility, not the stitch-preparation assistant's.

Real-world places, cultures, histories, and institutions may be identified as
out-of-world inspirations or source context when the author explicitly supplies
them. They are not in-world entities or setting facts and do not belong in
canon sections.
```

## Stitch output format

```markdown
# [Stitch title]

## Authority

- **Intended authority:** [Established canon | Working canon | Proposal only]
- **Intended session mode:** [Exploration | Canon-authoring | Direct-integration]
- **Author's instruction:** [What the author wants done with this material]
- **Scope:** [Subjects covered by this stitch]

## Setting truths

[Facts explicitly presented as objectively true in the setting.]

## People and groups

[Supplied facts about characters, peoples, organizations, institutions, or
other groups. Keep each subject clearly identified.]

## Places

[Supplied geographic, political, architectural, or environmental facts.]

## History and chronology

[Supplied events and temporal relationships. Distinguish exact dates from
relative or uncertain chronology.]

## Culture, systems, and terminology

[Supplied information about culture, government, religion, law, economy,
technology, customs, language, or defined terms.]

## Relationships and dependencies

[Explicit relationships among the subjects above. Do not infer unstated
connections.]

## In-world beliefs and disputed accounts

[Attribute every belief, tradition, rumor, historical claim, or disputed
account to its stated source.]

## Narrative truth levels

### Objective setting truth

[What is actually true in the setting, regardless of what any person or
institution believes. Refer to the relevant fact elsewhere in the stitch rather
than duplicating its full explanation.]

### Official or institutional position

[What a named government, civic history, religious authority, or other
institution officially claims. Attribute every position.]

### Character knowledge

[What each relevant character knows, believes, suspects, or misunderstands;
include the applicable point in the story.]

### Reader knowledge

[What the reader knows and when, organized by book, chapter, or reveal stage.]

### Spoiler notes

[Hidden truths, reveal dependencies, and information that must not appear in
spoiler-safe summaries.]

## Proposals and alternatives

[Ideas still under consideration, including mutually exclusive options.]

## Apparent contradictions

[Statements that may conflict, recorded side by side without resolution.]

## Unknowns and open questions

[Missing information, TODOs, and questions the author has not answered.]

## Sources and attachments

[Only author-supplied references, files, maps, images, prior notes, or other
source material. Do not include inferred inspirations unless the author
explicitly identifies them.]

## Explicit exclusions

[Ideas the author says are out of scope, rejected, retired, or not to be
treated as canon.]

<!-- END OF STITCH -->
```

## Handoff to repository intake

Give the completed stitch to Codex with the matching instruction from
[`../references/canon-intake-quickstart.md`](../references/canon-intake-quickstart.md).
Codex should preserve the entire finished document verbatim; it may reorganize
authoritative repository pages later, but it must not rewrite the source record.
If the marker is absent and the author has not explicitly confirmed
completeness, Codex should request the remainder and wait before making any
repository changes.
