---
title: CLOTH / THREAD Terminology and Repository Self-Model
type: intake-submission
case_id: CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY
submission_id: CASE-2026-08-13-CLOTH-THREAD-TERMINOLOGY-S01
sequence: 1
submitted_on: 2026-08-13
submitted_by: author
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: end-marker
parent_submission: null
supersedes_claims: []
related: []
---

# CLOTH / THREAD Terminology and Repository Self-Model

## Author instruction

Establish the terminology and conceptual model in this stitch as repository policy.

Integrate it across repository documentation, templates, agent instructions, and workflow references wherever needed for consistency. Preserve existing functional guarantees unless this stitch explicitly changes them.

This stitch primarily establishes a clearer conceptual vocabulary for mechanisms that already exist. Do not perform a wholesale mechanical rename where doing so would reduce clarity, break compatibility, or conflate records that currently have distinct responsibilities.

The repository should describe itself using the CLOTH / THREAD model after integration.

## Authority

`establish-policy`

## Session mode

`direct-integration`

## Repository identity

The Highwall knowledge repository is an instance of a **CLOTH**:

**CLOTH — Coherent Library of Ongoing Thought and History**

A CLOTH is a governed knowledge system that maintains a coherent, traceable body of evolving knowledge over time.

A CLOTH may contain:

- authoritative current-state knowledge
- working or provisional knowledge
- unresolved questions
- contradictions
- proposals
- superseded or retired knowledge
- provenance and source records
- decisions and their history
- relationships among claims
- records of how accepted changes affected the broader knowledge state

The purpose of a CLOTH is not merely to store documentation.

Its purpose is to preserve **coherence, provenance, history, uncertainty, authority, and change relationships** so that future human or machine work can determine both what the current knowledge state is and how it came to be that way.

Highwall is the subject matter of this particular CLOTH. The CLOTH architecture itself is intended to be domain-independent.

## THREAD

A **THREAD** is a traceable chain through the knowledge represented in a CLOTH.

**THREAD — Traceable History of Requirements, Evidence, Authority, and Decisions**

Not every THREAD must contain every category named in the acronym. The expansion describes the major kinds of information that a THREAD may connect.

A THREAD may connect, for example:

- a requirement or intended outcome
- evidence or source material
- assumptions and claims
- authority decisions
- open questions
- contradictions
- later clarifications
- supersessions
- resulting authoritative knowledge
- downstream consequences
- implementation or narrative effects

THREAD is primarily a relationship and traceability concept, not a replacement name for every claim or document.

A single claim may participate in multiple THREADs.

A single stitch may affect multiple THREADs.

THREADs may intersect when separate subjects depend upon shared knowledge.

## Pulling a THREAD

To **pull a thread** means to trace knowledge through its provenance and dependencies.

Pulling a thread may proceed backward:

- Where did this claim originate?
- What evidence supported it?
- Under what authority was it accepted?
- What decision established it?
- What did it supersede?

It may also proceed forward:

- What other claims depend upon it?
- Which authoritative pages express it?
- Which decisions assumed it?
- Which unresolved questions would change if it changed?
- What downstream material may need reconsideration?

The existing targeted and repository-wide semantic consistency workflows are mechanisms for pulling affected THREADs during integration.

Pulling a THREAD is not itself authority to alter knowledge. It is a method of discovering provenance, dependencies, and consequences.

## Loose and broken THREADs

A **loose thread** is knowledge requiring attention because its relationship to the coherent current state is unresolved.

Examples may include:

- an unresolved contradiction
- an unanswered question
- a provisional claim awaiting a decision
- potentially stale knowledge
- a dependency whose current validity requires review
- information whose downstream consequences have not yet been resolved

A **broken thread** is a traceability failure.

Examples may include:

- authoritative knowledge with missing provenance
- a decision whose source cannot be identified
- a downstream claim no longer connected to the authority that supposedly supports it
- a change whose effects cannot be reconciled with its recorded intake history

Do not automatically classify every open question as an error. Loose threads can be legitimate, explicitly represented states of knowledge.

Broken threads indicate deficiencies in provenance or traceability and should normally be repaired or explicitly documented.

## Stitch

A **stitch** is the author-facing unit of intentional semantic change to a CLOTH.

Typical language may include:

- "prepare a stitch"
- "review this stitch"
- "weave this stitch into the CLOTH"
- "this stitch affects three THREADs"
- "this stitch supersedes an earlier decision"

A stitch expresses a proposed or authorized delta to durable knowledge or repository governance.

A stitch may:

- add knowledge
- clarify existing knowledge
- change authority
- supersede earlier knowledge
- resolve or create an open question
- resolve or expose a contradiction
- establish or change repository policy
- change taxonomy or terminology
- retire knowledge
- establish relationships among existing claims

### Stitch does not collapse repository records

"Stitch" is a conceptual and author-facing change unit. It does **not** erase the existing provenance boundary between source material and reviewer interpretation.

When a stitch enters the repository workflow, continue to preserve distinct records for:

1. the immutable submitted source or author instruction
2. the intake/integration review containing claim classification, dispositions, impact analysis, and reviewer conclusions
3. resulting current-state repository changes
4. exception records where required
5. Git and pull-request publication history

The repository may continue to use technical record types such as `intake-submission` and `intake-review` where those names clearly describe implementation artifacts.

A stitch therefore corresponds to the semantic change being processed, while the submission and review are records used to process and audit that stitch.

Do not rename distinct records to "stitch" merely for thematic consistency.

## Relationship to the former "seed" terminology

Use **stitch** as the preferred general author-facing term for a prepared unit of knowledge intended for repository integration.

"Seed" may remain where required to describe:

- immutable historical submissions
- literal legacy completion markers
- compatibility behavior
- documentation referring specifically to artifacts created under the earlier terminology

Do not rewrite immutable historical submissions merely to replace the word "seed."

Do not break existing completeness validation merely to change terminology.

New documentation should prefer terminology such as:

- stitch
- submission
- source
- author instruction
- addendum

rather than using "seed" as the generic name for all new information.

## Stitch completion marker

The preferred completion marker for all new stitches is:

```text
<!-- END OF STITCH -->
```

This replaces `<!-- END OF SEED -->` as the current author-facing completion marker.

The completeness guarantee itself does not change.

A stitch or addendum must still be demonstrably complete before repository mutation begins.

### Compatibility requirements

The repository must support both completion markers:

```text
<!-- END OF STITCH -->
<!-- END OF SEED -->
```

`<!-- END OF STITCH -->` is the current standard.

`<!-- END OF SEED -->` is a legacy-compatible marker and remains valid for historical submissions and any material created under the earlier convention.

Do not modify immutable historical submissions to replace `<!-- END OF SEED -->`.

Validators, templates, workflow documentation, and agent instructions should be updated so that:

- new stitches use `<!-- END OF STITCH -->`
- `<!-- END OF SEED -->` remains accepted indefinitely for compatibility
- existing `completion_basis: end-marker` semantics remain valid
- the presence of either recognized marker can satisfy an end-marker completeness basis
- no transmission-completeness guarantee is weakened by this terminology migration

If validator constants or tests currently assume only a single literal marker, update them to recognize the current and legacy markers explicitly.

Do not replace the marker with a generic `<!-- END -->`; the marker should remain semantically specific to the submitted change unit.

### Transition boundary

This stitch itself uses the legacy:

```text
<!-- END OF SEED -->
```

marker because that is the repository rule in force at the time this stitch is submitted.

Integration of this stitch authorizes the new `<!-- END OF STITCH -->` convention.

The next newly prepared stitch should therefore use:

```text
<!-- END OF STITCH -->
```

This stitch forms the explicit historical transition between the seed and stitch terminology.

## Weave

To **weave** a stitch into a CLOTH means to integrate an accepted semantic change into the coherent repository state.

Weaving is broader than editing the most obvious target file.

The weave must determine what the accepted delta means for the existing knowledge system.

This includes, as applicable:

- locating existing representation of each substantive claim
- identifying confirmation, contradiction, or duplication
- identifying superseded knowledge
- finding dependent or related THREADs
- finding authoritative pages that become stale
- preserving narrower historical or scoped truths where appropriate
- creating or updating contradiction, question, proposal, decision, or retired records
- updating authoritative locations
- updating provenance relationships
- determining whether additional semantic audit scope is required
- recording deliberately unchanged material where relevant

The existing intake review, impact manifest, controlled claim dispositions, consistency tiers, and semantic audits are mechanisms used to govern the weave.

## Integration ordering

Semantic repository mutation follows this conceptual order:

**Stitch → review and authority determination → weave → integration review/current-state changes → validation → publication**

A semantic change should not normally be made first and justified afterward.

The accepted delta authorizes the weave.

The weave determines the consequences.

The resulting diff records the current-state changes.

The review records how and why those consequences were derived.

Git and the pull request provide publication history.

## CLOTH is not pure event sourcing

The repository's immutable submissions and supersession history preserve a durable sequence of knowledge changes, but CLOTH does not require the current repository to be mechanically regenerated byte-for-byte by replaying every historical stitch.

The authoritative repository remains a maintained current-state knowledge representation.

The governing invariant is:

> No semantic change to the maintained knowledge state should occur without traceable authority for that change.

Mechanical maintenance that does not change meaning may continue under the repository's maintenance rules.

## Semantic versus mechanical change

A **semantic change** alters what the CLOTH says, believes, records as authoritative, leaves unresolved, or requires future agents to do.

Examples include:

- changing canon or story truth
- changing a claim's authority
- resolving a contradiction
- changing repository governance
- changing how integration must operate
- changing a controlled taxonomy
- changing which source owns an authoritative fact

Semantic changes require appropriate governed integration.

A **mechanical change** preserves semantic meaning.

Examples may include:

- typo correction
- formatting repair
- broken-link repair where the intended target is unambiguous
- equivalent path maintenance
- generated-file refresh
- other explicitly allowed repository maintenance

Mechanical maintenance does not acquire semantic authority merely because it modifies files.

## Coherence

"Coherent" in CLOTH does not mean that the repository must pretend all recorded statements agree.

A coherent CLOTH may explicitly contain:

- conflicting claims
- uncertain claims
- provisional claims
- rejected proposals
- historical claims that are no longer current
- different beliefs held by different actors
- unresolved questions

Coherence means these states are represented without accidentally collapsing their distinctions.

A contradiction that is explicitly represented as a contradiction is coherent.

A provisional claim represented as established fact is not.

A historical claim represented as current truth is not.

A character belief represented as objective setting truth is not.

The goal is therefore not universal agreement among all records. The goal is a coherent representation of what each record means, what authority it has, where it came from, and how it relates to the current state.

## Authority, confidence, and truth-kind remain distinct

CLOTH terminology must not collapse the repository's existing distinctions among:

- what kind of truth or perspective a claim represents
- what authority or lifecycle status it holds
- how strongly it is supported or believed

Reviewer confidence does not create authority.

Repository presence does not create authority.

A source may authoritatively establish that a person or institution believes something without establishing that the belief is objectively true.

These distinctions remain fundamental to semantic integration.

## Repository self-governance

The CLOTH's own operating rules are part of the governed knowledge system.

Changes to:

- intake or stitch processing
- integration/weaving requirements
- consistency tiers
- claim dispositions
- authority rules
- templates
- validation requirements
- repository terminology
- agent instructions
- semantic governance

are themselves semantic changes to the CLOTH and should use the same governed change process when the process is available.

The system may therefore weave stitches that change how future stitches are woven.

Such self-modification must remain explicit, attributable, reviewable, and auditable.

## Preferred terminology

Use the following terminology going forward where natural:

**CLOTH**  
Coherent Library of Ongoing Thought and History. The governed knowledge system as a whole.

**THREAD**  
Traceable History of Requirements, Evidence, Authority, and Decisions. A provenance/dependency chain connecting related knowledge through time.

**stitch**  
An author-facing unit of intentional semantic change prepared for integration.

**weave**  
The governed integration of a stitch into the coherent current knowledge state.

**pull a thread**  
Trace provenance backward or semantic dependencies forward.

**loose thread**  
An explicitly unresolved, stale, provisional, contradictory, or otherwise attention-requiring knowledge relationship.

**broken thread**  
A provenance or traceability failure.

These terms supplement precise technical terms rather than replacing them where the technical distinction is important.

## Integration guidance

Review the repository for places where it currently describes itself only as a worldbuilding knowledge repository, intake pipeline, canon repository, or collection of Markdown documentation.

Update appropriate high-level documentation so that the CLOTH model is visible and understandable without requiring a reader to infer it from individual workflows.

Likely areas of impact include, but are not limited to:

- repository overview / README
- repository standards
- intake workflow
- consistency workflow
- Git workflow where semantic integration is discussed
- agent instructions
- intake quickstart documentation
- templates where author-facing "seed" terminology appears
- validation scripts and tests related to completion markers
- glossaries or terminology references, if present

Do not assume every occurrence of "seed" should be replaced.

Inspect each occurrence and preserve historical, compatibility, and technical meanings where appropriate.

The integration review should explicitly report:

- where CLOTH was defined
- where THREAD was defined
- where stitch/weave terminology was adopted
- which legacy "seed" terminology was deliberately retained and why
- how `<!-- END OF STITCH -->` compatibility was implemented
- whether validator or automation changes were required
- whether any terminology created ambiguity with existing repository concepts
- which THREADs of repository governance were affected
- any remaining terminology migration that should be deferred rather than silently inferred

## Non-goals

This stitch does not:

- change Highwall lore
- change story canon
- alter existing lore authority merely because terminology changes
- require conversion to a graph database or other storage technology
- require pure event sourcing
- require renaming every existing technical artifact
- authorize rewriting immutable historical submissions
- authorize weakening validation or provenance requirements
- make every repository record authoritative
- require metaphorical terminology where a precise technical term is clearer

The purpose is to give an explicit name and conceptual vocabulary to the architecture the repository already uses, while allowing that vocabulary to guide future evolution.

<!-- END OF SEED -->
