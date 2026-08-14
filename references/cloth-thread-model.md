# CLOTH / THREAD Model

Highwall is an instance of a **CLOTH**: a **Coherent Library of Ongoing
Thought and History**. A CLOTH is a governed knowledge system that maintains a
coherent, traceable body of evolving knowledge over time. Highwall is this
CLOTH's subject matter; the architecture is domain-independent.

The CLOTH contains more than authoritative current-state knowledge. It may
also preserve working knowledge, unresolved questions, contradictions,
proposals, retired knowledge, sources, decisions, claim relationships, and the
recorded consequences of accepted changes. Its purpose is to preserve
coherence, provenance, history, uncertainty, authority, and change
relationships so future human or machine work can identify both the current
knowledge state and how it arose.

## THREADs

A **THREAD** is a **Traceable History of Requirements, Evidence, Authority,
and Decisions**: a provenance and dependency chain through knowledge in the
CLOTH. The expansion identifies information a THREAD may connect; every THREAD
need not contain every category.

A THREAD may connect an intended outcome, source evidence, assumptions,
claims, authority decisions, open questions, contradictions, clarifications,
supersessions, authoritative knowledge, and downstream effects. A claim may
participate in multiple THREADs, a stitch may affect multiple THREADs, and
THREADs may intersect through shared knowledge. THREAD names the relationship,
not every claim or document participating in it.

To **pull a thread** is to trace provenance backward or dependencies forward.
Backward tracing asks where a claim originated, what supported and authorized
it, and what it superseded. Forward tracing asks what depends on it, where it is
expressed, and what would require reconsideration if it changed. Targeted and
repository-wide semantic consistency review are mechanisms for pulling
affected THREADs. Discovery alone grants no authority to alter knowledge.

A **loose thread** is an explicitly unresolved or attention-requiring
relationship, such as a contradiction, unanswered question, provisional or
potentially stale claim, or dependency awaiting review. Loose threads can be
legitimate coherent states and are not automatically errors.

A **broken thread** is a provenance or traceability failure, such as
authoritative knowledge without identifiable authority or a downstream claim
disconnected from its supporting decision. Repair a broken thread when
possible; otherwise document the deficiency explicitly.

## Stitches and weaving

A **stitch** is the author-facing unit of intentional semantic change prepared
for integration into a CLOTH. It may add, clarify, supersede, retire, relate, or
change knowledge or governance. **Weaving** is the governed integration that
determines the accepted stitch's consequences across the coherent current
state, not merely an edit to the most obvious target.

The conceptual order is:

**Stitch → review and authority determination → weave → integration review and
current-state changes → validation → publication**

The accepted delta authorizes the weave. The weave locates existing
representations and dependencies, identifies confirmation, contradiction,
duplication, and supersession, creates exception records where needed, updates
authoritative locations and provenance, and determines semantic audit scope.
The resulting diff records current-state changes; the review records how and
why they were derived; Git and the pull request record publication.

Stitch is a conceptual change unit, not a replacement for the distinct
technical records used to process it. Continue to preserve separately:

1. the immutable submission or author instruction;
2. the intake or integration review and its claim dispositions;
3. resulting current-state changes;
4. required exception records; and
5. Git and pull-request publication history.

Technical names such as `intake-submission` and `intake-review` remain correct.
Do not rename every participating record to “stitch.”

## Coherence and authority

Coherence does not require every recorded statement to agree. A coherent CLOTH
may explicitly represent conflicting, uncertain, provisional, rejected,
historical, perspectival, and unresolved claims. A represented contradiction
is coherent; a provisional claim presented as established fact, or a character
belief presented as objective truth, is not.

Truth kind, lifecycle authority, and confidence remain distinct. Reviewer
confidence and repository presence do not create authority. A source may
authoritatively establish that an actor believes a claim without establishing
the claim as objective truth.

The repository is maintained current state with durable source and
supersession history, not a pure event-sourced system that must be mechanically
replayed byte for byte. Its governing invariant is:

> No semantic change to the maintained knowledge state should occur without
> traceable authority for that change.

## Semantic and mechanical change

A **semantic change** alters what the CLOTH says, treats as authoritative,
leaves unresolved, or requires future contributors to do. Lore, story truth,
authority, contradiction resolution, governance, taxonomy, and ownership
changes therefore require governed integration.

A **mechanical change** preserves meaning, as with an unambiguous typo,
formatting or broken-link repair, equivalent path maintenance, or generated
file refresh. Mechanical maintenance does not acquire semantic authority merely
because it changes files.

The CLOTH's operating rules are themselves governed knowledge. Changes to
intake, weaving, consistency tiers, dispositions, authority, templates,
validation, terminology, agent instructions, or semantic governance must use
the governed process when available. The CLOTH may weave stitches that change
how later stitches are woven, but that self-modification must remain explicit,
attributable, reviewable, and auditable.

## Terminology compatibility

Use **stitch** as the preferred general author-facing term for newly prepared
semantic change. Retain **seed** where it identifies immutable historical
submissions, specifically named legacy artifacts, legacy completion markers,
or compatibility behavior. Never rewrite immutable submissions for
terminology alone.

New stitches use the completion marker:

```text
<!-- END OF STITCH -->
```

The legacy marker remains accepted indefinitely:

```text
<!-- END OF SEED -->
```

Either recognized literal marker satisfies `completion_basis: end-marker`.
The transmission-completeness guarantee and all distinct source, review,
authority, provenance, and publication boundaries remain unchanged.
