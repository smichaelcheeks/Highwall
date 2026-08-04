# Highwall

Highwall is the canonical knowledge repository for the original fantasy setting of the same name. It is intended to support encyclopedic reference, novel development, search, continuity review, and careful collaboration between human authors and AI assistants.

This repository begins as a structure, not a body of lore. No setting fact is canon unless it is explicitly recorded in an appropriate canon page.

## Repository map

- [`intake/`](intake/README.md) contains immutable submissions of new information awaiting or documenting review.
- [`canon/`](canon/README.md) contains authoritative facts about the setting.
- [`story/`](story/README.md) contains narrative-specific material: projects, character knowledge, reveals, and story chronology.
- [`development/`](development/README.md) contains proposals, questions, contradictions, decisions, and retired ideas.
- [`references/`](references/README.md) contains repository standards and external research notes.
- [`templates/`](templates/README.md) contains reusable page structures.

## Organizational philosophy

Treat this repository like documentation for a large software project:

1. Give every fact one authoritative home.
2. Link to that home instead of copying the explanation elsewhere.
3. Keep objective setting truth separate from narrative presentation and character belief.
4. Keep proposals and brainstorming outside `canon/` until they are explicitly approved.
5. Surface contradictions; never resolve them silently.
6. Prefer explicit unknowns and TODOs over invented answers.

Directory placement describes the kind of information. Page metadata describes its maturity and authority. A file under `canon/` can therefore be marked `working` while it is being reviewed, but an idea in `development/` does not become canon merely because it is polished.

## Managing canon

Canon pages use YAML front matter as described in [`references/front-matter.md`](references/front-matter.md). Canon status and canon level are separate concepts: status tracks workflow maturity, while canon level records authority. Significant changes must be logged according to [`references/repository-standards.md`](references/repository-standards.md).

When sources disagree, create a contradiction report in [`development/contradictions/`](development/contradictions/README.md). Record both claims and their locations, describe the impact, and leave the resolution pending until an authorized decision is made.

## Information intake and audit trail

New batches of information enter through [`intake/submissions/`](intake/submissions/README.md). Once submitted, an intake file is treated as immutable: corrections or additions arrive in a new submission rather than rewriting the original source.

Each processed submission receives a separate report under [`development/intake-reviews/`](development/intake-reviews/README.md). The report gives every substantive claim a stable identifier and records its classification, disposition, target file, evidence, and concise rationale. This creates a traceable path from submitted information to repository changes without mixing source material with AI-generated analysis.

When a seed document develops through conversation, related material remains grouped under one case ID. Confirmed conversational decisions are preserved as numbered, immutable addenda; exploratory discussion remains non-canonical unless its outcome is explicitly approved or authorized by the declared session mode.

The complete workflow and controlled decision vocabulary are defined in [`references/intake-workflow.md`](references/intake-workflow.md).

## Canon, story, and development

- **Canon** answers what is true in the setting.
- **Story** answers what a particular narrative, viewpoint character, or reader knows and when they know it.
- **Development** answers what might become true, what is unresolved, and why a decision was made.
- **In-world belief** is documented as a belief held by a named person or group and must not be presented as objective truth without confirmation.

These boundaries preserve deliberate ambiguity and prevent a narrative claim from silently becoming world truth.

## Working in this repository

Before adding or changing material:

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Place new source material in [`intake/submissions/`](intake/submissions/README.md).
3. Review it using [`templates/intake-review.md`](templates/intake-review.md).
4. Identify the authoritative page or create one from [`templates/`](templates/README.md).
5. Use relative links for related material.
6. Record unresolved questions or contradictions in `development/`.
7. Review changes for accidental lore invention, duplication, and altered canon.

Human and AI contributors follow the same rules. AI assistance does not have authority to invent, promote, reinterpret, or reconcile canon unless explicitly instructed.

Substantial changes should follow the case-oriented branch and pull-request process in [`references/git-workflow.md`](references/git-workflow.md).
