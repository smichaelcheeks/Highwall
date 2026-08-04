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

My notes begin after this line:

[PASTE NOTES OR BEGIN THE INTERVIEW HERE]
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

## Story and knowledge boundaries

[Character knowledge, viewpoint limitations, reader reveals, plot usage, and
spoiler-sensitive information. Do not restate these as setting truth.]

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
```

## Handoff to repository intake

Give the completed seed to Codex with the matching instruction from
[`../references/canon-intake-quickstart.md`](../references/canon-intake-quickstart.md).
Codex should preserve the entire finished document verbatim; it may reorganize
authoritative repository pages later, but it must not rewrite the source record.
