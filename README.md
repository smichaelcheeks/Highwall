# Highwall

Highwall is a governed knowledge repository for the original fantasy setting
of the same name. It is an instance of a **CLOTH**—a **Coherent Library of
Ongoing Thought and History**—and supports encyclopedic reference, novel
development, search, continuity review, and careful collaboration between
human authors and AI assistants.

A CLOTH preserves current knowledge together with provenance, authority,
uncertainty, history, and change relationships. **THREADs**—**Traceable
Histories of Requirements, Evidence, Authority, and Decisions**—connect that
knowledge through time. See the authoritative
[`CLOTH / THREAD model`](references/cloth-thread-model.md) for patches,
stitching, graph-oriented knowledge relationships, loose and broken threads,
and the boundaries that keep technical records distinct.

This repository begins as a structure, not a body of lore. No setting fact is canon unless it is explicitly recorded in an appropriate canon page.

## Repository map

- [`intake/`](intake/README.md) contains immutable submissions of new information awaiting or documenting review.
- [`canon/`](canon/README.md) contains authoritative facts about the setting.
- [`story/`](story/README.md) contains narrative-specific material: projects, character knowledge, reveals, and story chronology.
- [`design/`](design/README.md) contains authoritative out-of-world creative
  guidance that cannot establish in-world facts.
- [`development/`](development/README.md) contains proposals, questions, contradictions, decisions, and retired ideas.
- [`references/`](references/README.md) contains repository standards and external research notes.
- [`templates/`](templates/README.md) contains reusable page structures.

## CLOTH philosophy

Treat this repository like documentation for a large software project:

1. Give every fact one authoritative home.
2. Link to that home instead of copying the explanation elsewhere.
3. Keep objective setting truth separate from narrative presentation and character belief.
4. Keep proposals and brainstorming outside `canon/` until they are explicitly approved.
5. Surface contradictions; never resolve them silently.
6. Prefer explicit unknowns and TODOs over invented answers.

Coherence does not mean forcing every statement to agree. Explicitly
represented contradictions, provisional claims, historical accounts, and
unanswered questions are coherent states; collapsing those distinctions is
not.

CLOTH also uses an implemented graph-oriented model. Entities, relationships,
and claims are addressable knowledge objects; explicit relationships allow an
agent to pull a THREAD through known provenance and dependencies rather than
relying on semantic search for every hop. Highwall remains a Markdown-first
implementation: authoritative pages carry stable entity IDs and explicit,
controlled relationship objects, while a generated navigation index supports
machine traversal without requiring a graph database. Migration from legacy
links is incremental. See [`references/graph-structure.md`](references/graph-structure.md).

Directory placement describes the kind of information. Page metadata describes its maturity and authority. A file under `canon/` can therefore be marked `working` while it is being reviewed, but an idea in `development/` does not become canon merely because it is polished.

## Managing canon

Canon pages use YAML front matter as described in [`references/front-matter.md`](references/front-matter.md). Canon status and canon level are separate concepts: status tracks workflow maturity, while canon level records authority. Significant changes must be logged according to [`references/repository-standards.md`](references/repository-standards.md).

When sources disagree, create a contradiction report in [`development/contradictions/`](development/contradictions/README.md). Record both claims and their locations, describe the impact, and leave the resolution pending until an authorized decision is made.

## Information intake and audit trail

Author-facing semantic changes are prepared as **patches**. A patch enters
through [`intake/submissions/`](intake/submissions/README.md), where its source
is preserved as an immutable submission; corrections or additions arrive in a
new submission or addendum rather than rewriting the original source.

Each processed submission receives a separate report under [`development/intake-reviews/`](development/intake-reviews/README.md). The report gives every substantive claim a stable identifier and records its classification, disposition, target file, evidence, and concise rationale. This creates a traceable path from submitted information to repository changes without mixing source material with AI-generated analysis.

When a patch develops through conversation, related material remains grouped
under one case ID. Confirmed conversational decisions are preserved as
numbered, immutable addenda; exploratory discussion remains non-canonical
unless its outcome is explicitly approved or authorized by the declared
session mode.

To **stitch a patch into CLOTH** is to trace and integrate all of its affected
THREADs across the coherent repository state. The intake review, impact
manifest, controlled dispositions, consistency tiers, validation, and
publication history govern that integration.

The immutable submission archive remains the global paper trail, while
schema-v2 knowledge objects maintain concise histories pointing back to the
patches, intake claims, and decisions that changed them. This lets normal
retrieval start from the object and follow its THREADs before opening the full
historical patch. The staged schema-v2 migration and incomplete coverage are
reported in the
[`public migration ledger`](development/knowledge-object-schema-v2-migration.md).

The complete workflow and controlled decision vocabulary are defined in [`references/intake-workflow.md`](references/intake-workflow.md).

## Canon, story, design, and development

- **Canon** answers what is true in the setting.
- **Story** answers what a particular narrative, viewpoint character, or reader knows and when they know it.
- **Design** guides how authors and AI collaborators construct the setting and
  stories without serving as evidence for fictional truth.
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

To begin a canon case in a fresh Codex chat, use [`references/canon-intake-quickstart.md`](references/canon-intake-quickstart.md). Codex-specific mandatory instructions live in [`AGENTS.md`](AGENTS.md).
