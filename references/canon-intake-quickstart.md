# Canon Intake Quick Start

This guide is the entry point for starting a new Highwall canon case in a fresh Codex chat.

## Before starting

- Merge or close unrelated work first.
- Open the repository from a clean, synchronized `main` checkout.
- Use one Codex chat and working directory per active case.
- Decide whether the seed is established canon, working canon, or a proposal.

## Recommended fresh-chat prompts

### Established canon

```text
Treat the attached seed as established canon in direct-integration mode.
Preserve it verbatim as a new intake case, inventory every substantive
claim, place each accepted fact in its single authoritative location,
record every disposition and rationale, run repository validation, and
open a draft PR. Do not invent anything not stated in the seed.
```

### Working canon

```text
Treat the attached seed as working canon in direct-integration mode.
Preserve it verbatim as a new intake case, identify every substantive
claim, integrate it without promoting anything to established canon,
record every decision, run validation, and open a draft PR. Do not fill
gaps or resolve ambiguity without asking.
```

### Exploration

```text
Treat the attached seed as proposal-only material in exploration mode.
Preserve it as a new intake case and help me develop it, but keep all
ideas in development and do not update canon until I explicitly approve
specific decisions.
```

## Expected processing sequence

The agent should:

1. Read [`../AGENTS.md`](../AGENTS.md) and the linked repository standards.
2. Confirm authority and session mode when they are not explicit.
3. Synchronize `main` and create a case branch.
4. Save the seed verbatim from [`../templates/intake-submission.md`](../templates/intake-submission.md).
5. Create a claim-level review from [`../templates/intake-review.md`](../templates/intake-review.md).
6. Search existing canon, story, development, aliases, and terminology.
7. Assign every claim a controlled disposition before integration.
8. Create or update authoritative pages using the relevant templates.
9. Record contradictions and unresolved questions instead of choosing answers.
10. Validate locally, push, and open a draft PR for review.

## Continuing the conversation

Brainstorming does not become canon automatically. At a natural checkpoint, confirm which outcomes are approved. The agent should preserve those outcomes in a conversation addendum before applying them.

Corrections never rewrite an already reviewed submission. Create another seed or addendum in the same case and identify the earlier claim being clarified or superseded.

## Reviewing the result

Before approving the PR, verify:

- the seed is preserved accurately
- every substantive claim appears in the review
- authority and session mode match the instruction
- facts are stored once and linked elsewhere
- beliefs, story knowledge, and objective truth remain distinct
- all deliberate non-changes have reasons
- every exception links to a development record
- local validation and both GitHub checks pass
- the PR contains no unrelated changes
