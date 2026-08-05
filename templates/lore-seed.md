# Lore Seed Authoring Template

Use this template before repository intake when you want ChatGPT or another
assistant to organize raw lore into a clear seed document. The finished seed is
source material, not a canon page. Repository processing later preserves it
verbatim inside an intake submission and audits its claims separately.

## Copyable assistant instruction

```text
Help me turn my notes and answers into a structured Highwall lore seed.

Rules:
- Do not invent facts, explanations, names, motives, dates, relationships, or
  connective details.
- Do not make an uncertain statement more definite than I made it.
- Keep objective setting truth separate from in-world belief, disputed history,
  character knowledge, reader reveals, and ideas still under consideration.
- If two statements appear inconsistent, preserve both and flag the apparent
  conflict. Do not reconcile them yourself.
- Use TODO or list a question when information is missing. Do not fill gaps.
- Ask focused clarification questions when an answer would materially change
  meaning. Otherwise, organize what I supplied and list the remaining unknowns.
- If I ask for an interview, ask one focused question at a time and periodically
  summarize what I have actually confirmed. Do not offer invented answers as if
  I supplied them, and do not treat my consideration of an option as approval.
- Preserve intentional ambiguity and spoiler boundaries exactly as I identify
  them.
- Do not assign repository case IDs, claim IDs, filenames, front matter, or
  processing dispositions. Codex will do that during repository intake.
- Before producing the final document, ask me to confirm its authority as one
  of: established canon, working canon, or proposal only; and its intended
  repository session mode as one of: exploration, canon-authoring, or
  direct-integration.
- Return the final result as plain Markdown using the seed format below. Omit
  optional sections that have no supplied content; do not create filler prose.
- End the final document with the literal `<!-- END OF SEED -->` marker on its
  own line. Do not emit that marker until the full document is complete.

My notes begin after this line:

[PASTE NOTES OR BEGIN THE INTERVIEW HERE]
```

## Optional repository context

```text
Highwall is a controlled canon repository. A lore seed is preserved source
material, not automatically canon. Codex later preserves the finished seed
verbatim, inventories every substantive claim in a separate review, records
every decision and deliberate non-change, and places authorized facts in one
authoritative location.

Canon contains objective setting truth. Story contains character knowledge,
reader knowledge, chronology, and reveals. Design contains out-of-world
authorial guidance but cannot establish fictional facts. Development contains
proposals, questions, contradictions, decisions, and retired ideas.

Once review begins, a seed is immutable. Later confirmed corrections and
additions are preserved in separately numbered addenda. Contradictions are
documented rather than silently resolved. Missing information remains unknown
or becomes an open question. Repository identifiers, dispositions, file
destinations, validation, branches, and draft pull requests are Codex's
responsibility, not the seed-preparation assistant's.
```

## Seed output format

```markdown
# [Seed title]

## Authority

- **Intended authority:** [Established canon | Working canon | Proposal only]
- **Intended session mode:** [Exploration | Canon-authoring | Direct-integration]
- **Author's instruction:** [What the author wants done with this material]
- **Scope:** [Subjects covered by this seed]

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

[What is actually true. Refer to the relevant fact elsewhere in the seed
rather than duplicating its full explanation.]

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

[Author-supplied references, files, prior notes, or source context.]

## Explicit exclusions

[Ideas the author says are out of scope, rejected, retired, or not to be
treated as canon.]

<!-- END OF SEED -->
```

## Handoff to repository intake

Give the completed seed to Codex with the matching instruction from
[`../references/canon-intake-quickstart.md`](../references/canon-intake-quickstart.md).
Codex should preserve the entire finished document verbatim; it may reorganize
authoritative repository pages later, but it must not rewrite the source record.
If the marker is absent and the author has not explicitly confirmed
completeness, Codex should request the remainder and wait before making any
repository changes.
