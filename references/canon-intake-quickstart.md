# Canon Intake Quick Start

This guide is the entry point for starting a new Highwall patch case in a
fresh Codex chat.

## Before starting

- Merge or close unrelated work first.
- Open the repository from a clean, synchronized `main` checkout.
- Use one Codex chat and working directory per active case.
- Decide whether the patch is established canon, working canon, or a proposal.
- End pasted patches with the literal `<!-- END OF PATCH -->` marker. The
  legacy `<!-- END OF STITCH -->` and `<!-- END OF SEED -->` markers remain
  valid for compatibility.
  Without the marker or an explicit confirmation that transmission is complete,
  Codex must wait rather than begin repository work.

If the material is still in notes or conversational form, first use the
author-facing [`lore patch template`](../templates/lore-seed.md) to have
ChatGPT or another assistant organize it without inventing or assigning
repository metadata. This preparation step does not grant canon authority.

## Recommended fresh-chat prompts

### Established canon

```text
Treat the attached patch as established canon in direct-integration mode.
Do not begin until the patch ends with `<!-- END OF PATCH -->` or I explicitly
confirm that transmission is complete.
Preserve it verbatim as a new intake case, inventory every substantive
claim, place each accepted fact in its single authoritative location,
record every disposition and rationale, run repository validation, and
open a draft PR. Do not invent anything not stated in the patch.
```

### Working canon

```text
Treat the attached patch as working canon in direct-integration mode.
Do not begin until the patch ends with `<!-- END OF PATCH -->` or I explicitly
confirm that transmission is complete.
Preserve it verbatim as a new intake case, identify every substantive
claim, integrate it without promoting anything to established canon,
record every decision, run validation, and open a draft PR. Do not fill
gaps or resolve ambiguity without asking.
```

### Exploration

```text
Treat the attached patch as proposal-only material in exploration mode.
Do not begin until the patch ends with `<!-- END OF PATCH -->` or I explicitly
confirm that transmission is complete.
Preserve it as a new intake case and help me develop it, but keep all
ideas in development and do not update canon until I explicitly approve
specific decisions.
```

## Expected processing sequence

The agent should:

1. Read [`../AGENTS.md`](../AGENTS.md) and the linked repository standards.
2. Confirm the transmission is complete; otherwise request the remainder and
   make no repository changes.
3. Confirm authority and session mode when they are not explicit.
4. Synchronize `main` and create a case branch.
5. Save the patch source verbatim from [`../templates/intake-submission.md`](../templates/intake-submission.md).
6. Create a claim-level review from [`../templates/intake-review.md`](../templates/intake-review.md).
7. Record the latest applicable semantic-audit baseline, examine the Git range
   since it, generate incremental context, and evaluate mandatory Tier 3
   triggers using Git history and completed review records.
8. Search existing canon, story, development, aliases, and terminology.
9. Assign every claim a controlled disposition before integration.
10. Create or update authoritative pages using the relevant templates.
11. Record contradictions and unresolved questions instead of choosing answers.
12. Validate locally, push, and open a draft PR for review.

## Continuing the conversation

Brainstorming does not become canon automatically. At a natural checkpoint, confirm which outcomes are approved. The agent should preserve those outcomes in a conversation addendum before applying them.

Corrections never rewrite an already reviewed submission. Create another
submission or addendum in the same case and identify the earlier claim being
clarified or superseded.

## Reviewing the result

Before approving the PR, verify:

- the patch source is preserved accurately
- every substantive claim appears in the review
- the review records its audit baseline, Git range, prior relationship outcomes,
  consistency tier, Tier 3 triggers, and completed-case count
- authority and session mode match the instruction
- facts are stored once and linked elsewhere
- beliefs, story knowledge, and objective truth remain distinct
- all deliberate non-changes have reasons
- every exception links to a development record
- local validation and both GitHub checks pass
- the PR contains no unrelated changes
