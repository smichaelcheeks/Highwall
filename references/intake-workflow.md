# Intake Workflow

This workflow turns batches of new information into traceable repository changes while preserving the original source and every material processing decision.

## Records and responsibilities

The workflow maintains distinct records:

1. **Submission:** immutable source material under [`../intake/submissions/`](../intake/submissions/README.md).
2. **Intake review:** claim-level classifications and dispositions under [`../development/intake-reviews/`](../development/intake-reviews/README.md).
3. **Authoritative pages:** resulting world or story information under `canon/` or `story/`.
4. **Exception records:** open questions, proposals, contradictions, decisions, or retired ideas under `development/`.
5. **Canon change log:** concise index of significant canon effects.
6. **Git history:** durable record of the exact file changes associated with the review.

Do not combine these records. In particular, never append reviewer conclusions to the original submission.

## Transmission completeness gate

Confirm that a seed or addendum is complete before creating a branch, intake
record, review, or authoritative change. Completeness requires one of:

- the literal `<!-- END OF SEED -->` marker in the submitted document
- an explicit author statement that the transmission is complete
- a complete attachment whose boundaries are available for inspection

If none is present, ask whether more material is coming and wait. Also wait when
the source ends mid-sentence, omits a section it says will follow, leaves a code
fence or delimiter unclosed, ends abruptly within a list, or otherwise appears
truncated. Do not preserve a suspected partial transmission as `S01` and do not
begin partial integration.

Every new submission or addendum records:

```yaml
transmission_status: complete
completion_basis: end-marker
```

Controlled `completion_basis` values are `end-marker`,
`explicit-confirmation`, and `complete-attachment`. When `end-marker` is used,
the immutable submission must contain the literal marker. The validator applies
these requirements to submissions newly added relative to the supplied base
ref, preserving compatibility with historical merged intake records.

## Cases, submissions, and claim IDs

A case groups one seed submission with every conversational addendum, correction, and review that develops from it. Create a stable case ID from the seed date and topic:

```text
CASE-YYYY-MM-DD-SLUG
```

Within the case, identify the seed as `S01` and conversational addenda as `A01`, `A02`, and so on:

```text
CASE-YYYY-MM-DD-SLUG-S01
CASE-YYYY-MM-DD-SLUG-A01
CASE-YYYY-MM-DD-SLUG-A01-C001
```

If a case requires another independently supplied seed, increment the seed sequence. IDs remain stable even if prose is later quoted, summarized, corrected, or superseded elsewhere.

Every addendum records its parent submission, its sequence within the case, and any earlier claim IDs it supersedes. Supersession changes authority going forward but does not erase the earlier claim or review.

## Conversation session modes

Declare a session mode before or at the beginning of conversational refinement:

| Mode | Default treatment of conversation |
| --- | --- |
| `exploration` | Discussion is non-canonical unless the author explicitly approves a decision. |
| `canon-authoring` | Definite author statements are working canon unless marked speculative; ambiguity is held for confirmation. |
| `direct-integration` | Explicit instructions may be applied as established canon as work proceeds. Questions, hypotheticals, and alternatives remain non-canonical. |

If no mode is declared, use `exploration`. Changing modes affects only later conversation unless the author explicitly applies the change retroactively.

## Authority declaration

Before processing claims, the reviewer records the authority conveyed by the author's instruction:

- `establish-canon`: explicit instruction to make supplied setting facts canonical
- `working-canon`: explicit instruction to record supplied facts provisionally
- `establish-policy`: explicit instruction to establish repository structure, governance, or workflow without granting lore authority
- `proposal-only`: material is offered for consideration and cannot update canon
- `classify`: authority varies by claim or is not explicit; ambiguous canon effects must be held for clarification

An intake file's presence never grants authority by itself.

For conversational claims, also record the authority basis:

- `explicit`: the author directly approved or instructed the claim
- `session-mode`: the declared mode authorizes the definite statement
- `source-authority`: the parent seed already authorizes the claim and the conversation only clarifies wording
- `pending`: the discussion does not yet authorize repository integration

Reviewer inference is never an authority basis.

## Review lifecycle

Use these review statuses consistently:

- `in-progress`: claims are still being inventoried, discussed, or applied
- `awaiting-confirmation`: conversational interpretation requires author confirmation before it can be integrated
- `awaiting-decision`: a documented question, proposal, or contradiction requires an authorial choice
- `complete`: every claim has a disposition, authorized changes are applied, and verification is recorded
- `blocked`: completion cannot proceed because required source material or external authority is unavailable

A review may move between the first three states as conversation continues. Do not mark it `complete` merely because a discussion session ended.

## Claim inventory

A substantive claim is any statement that could create, alter, contradict, retire, or materially contextualize repository knowledge. Break compound statements apart when their dispositions could differ. Minor wording, formatting, and connective prose need not receive separate IDs.

For every substantive claim, record:

- a stable claim ID
- a faithful summary or short quotation
- classification: canon, story, belief, historical claim, proposal, question, correction, or administrative
- existing authoritative or related pages inspected
- disposition
- target or resulting record
- concise rationale grounded in evidence and repository rules
- authority basis and, for corrections, superseded claim IDs

## Controlled dispositions

Use one of these values:

| Disposition | Meaning |
| --- | --- |
| `create` | Create a new authoritative page. |
| `update` | Change an existing authoritative page. |
| `no-change` | The claim is already represented accurately or is non-substantive. |
| `link-only` | Add a relationship without duplicating the claim. |
| `defer` | Preserve as an unresolved question or proposal. |
| `conflict` | Create or update a contradiction report and await a decision. |
| `retire` | Remove from active canon while preserving provenance. |
| `out-of-scope` | Take no repository action because the claim does not belong in this knowledge base or task. |

`no-change` and `out-of-scope` still require a reason. `conflict`, `defer`, and `retire` must link to the development record that preserves the unresolved or historical context.

## Processing sequence

1. Pass the transmission completeness gate.
2. Save the source using [`../templates/intake-submission.md`](../templates/intake-submission.md).
3. Create a review using [`../templates/intake-review.md`](../templates/intake-review.md).
4. Record the authority declaration and files inspected.
5. Inventory and classify every substantive claim.
6. Search canon, story, development records, aliases, and terminology for prior coverage.
7. Assign a disposition before modifying authoritative pages.
8. Apply authorized changes, creating exception records where required.
9. Record all changed and deliberately unchanged targets in the review.
10. Run link, metadata, contradiction, duplication, and diff checks.
11. Add a canon change-log entry for significant canon effects.
12. Mark the review complete only when no claim lacks a disposition.
13. When committed, record the Git commit hash in the review.

## Conversational refinement

Keep the seed immutable while its review remains open. During conversation, maintain a checkpoint that separates:

- established decisions
- proposals still under consideration
- corrections or supersessions
- unresolved questions
- expected repository effects

Create a conversational addendum from [`../templates/conversation-addendum.md`](../templates/conversation-addendum.md) at a natural integration boundary. Typical boundaries include an explicit instruction to apply the discussion, a topic change, the end of a working session, or a group of decisions ready to update authoritative pages.

The addendum preserves confirmed outcomes and enough context to understand their authority. It is not required to reproduce the entire transcript. Do not include exploratory alternatives as decisions; list them separately as proposals or open questions when their preservation is useful.

Create a new addendum when the conversation:

- adds a substantive fact not present in an existing submission
- corrects or supersedes an earlier claim
- explicitly approves or rejects a proposal
- resolves an open question or contradiction
- changes the authority or intended interpretation of prior material

The existing review may remain open without a new addendum while the conversation only explores possibilities, requests explanation, or makes non-substantive wording adjustments. Before applying repository changes derived from conversation, ensure the relevant confirmed claims exist in an immutable addendum.

## Amendments and corrections

Do not revise a processed submission. A correction is a new seed or conversational addendum in the same case that links to the original and names superseded claim IDs. If a review itself contains an error, append a dated amendment describing the correction, its reason, and any resulting file changes. Preserve the earlier entry so the audit trail remains intelligible.

## Review rationale

Rationale should be concise and reproducible. Identify the evidence reviewed, the applicable rule or authority, and why the recorded action follows. The purpose is to let a future contributor audit the decision, not to preserve an exhaustive transcript of exploratory reasoning.
