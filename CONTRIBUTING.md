# Contributing to Highwall

This repository is a governed CLOTH and controlled canon system. Contributions
should improve clarity and consistency without expanding the setting beyond
explicit instructions. See the
[`CLOTH / THREAD model`](references/cloth-thread-model.md).

## Non-negotiable rules

- Never invent canon or fill gaps creatively unless explicitly instructed.
- Never silently resolve contradictions. Document each claim, cite its repository location, and request a decision.
- Ask for clarification rather than guessing when an answer would affect meaning or canon.
- Prefer links to the authoritative page over duplicated explanations.
- Keep brainstorming, alternatives, and speculative material in `development/`, not `canon/`.
- Keep setting truth in `canon/` and narrative state in `story/`.
- Keep authorial intent in `design/`; never cite it as evidence of an in-world
  fact or infer missing lore from it.
- Preserve narrative ambiguity when instructed. Do not convert implication, rumor, belief, or reader inference into fact.
- Record significant canon changes and the decision authorizing them.
- Keep maintained knowledge-claim IDs distinct from immutable intake-claim
  IDs, and append local object history when schema-v2 objects change.
- Do not treat external research, prior drafts, or retired ideas as canon.

## Contribution workflow

For a new patch, follow [`references/intake-workflow.md`](references/intake-workflow.md):

1. **Confirm completeness.** Require the current `<!-- END OF PATCH -->`
   marker, the legacy `<!-- END OF STITCH -->` or `<!-- END OF SEED -->`
   marker, explicit author confirmation, or a complete attachment. If the
   source appears partial, wait for the remainder before changing the
   repository.
2. **Preserve the submission.** Store it in `intake/submissions/` with a stable ID and do not alter it after review begins.
3. **Establish authority.** Record whether the author's instruction establishes canon, proposes possibilities, or supplies material for classification.
4. **Inventory claims.** Give every substantive claim a stable ID in a separate intake review.
5. **Map the impact.** Record subjects, domains, search terms, and expected
   authoritative targets, then generate targeted context.
6. **Evaluate the audit baseline.** For every lore review, examine Git history
   from the latest applicable semantic baseline, record prior relationship
   outcomes and Tier 3 triggers, and determine the completed canon-case count
   from Git and review records.
7. **Assign a disposition.** Record what will or will not change, the target, evidence, and rationale for every claim.
8. **Stitch approved patches.** Pull affected THREADs, use the appropriate
   content templates, and link rather than duplicate.
9. **Expose uncertainty.** Create an open question, proposal, or contradiction report instead of selecting an unsupported answer.
10. **Verify the result.** Apply the consistency tier required by
   [`references/consistency-workflow.md`](references/consistency-workflow.md),
   then check the diff, links, provenance, accidental canon changes, and leaked
   story spoilers.
11. **Close the audit.** List every changed file, verification result, unresolved item, and resulting canon-change entry.

For conversational refinement, declare a session mode and maintain a review checkpoint separating decisions, proposals, corrections, and questions. Before integrating new conversational facts, preserve the confirmed outcome in an immutable addendum from [`templates/conversation-addendum.md`](templates/conversation-addendum.md). Follow the detailed rules in [`references/intake-workflow.md`](references/intake-workflow.md).

For routine process-only maintenance that contains no lore or significant
governance decision, use [`templates/maintenance-review.md`](templates/maintenance-review.md).
Use the full intake workflow when maintenance changes authority, resolves a
contradiction, or establishes significant repository policy.

## Working with canon pages

All canon pages must contain YAML front matter conforming to [`references/front-matter.md`](references/front-matter.md). New canon material should not be marked `established` unless the author explicitly approves that status.

Do not move a development document into `canon/` as a shortcut. Create or update the appropriate canon page, link the approving decision, and retain the development record when it explains important history.

## Contradictions

If two statements conflict:

1. Do not edit either statement merely to make them agree.
2. Create a report from [`templates/contradiction-report.md`](templates/contradiction-report.md).
3. Quote or neutrally summarize both claims and link to each source.
4. Describe the scope and downstream pages affected.
5. Leave the report open until the author decides.
6. Apply the decision consistently and record the resulting canon change.

## AI collaboration checklist

Before completing a task, an AI contributor must verify:

- Every new factual claim came from the user's instruction or an existing authoritative page.
- Placeholders remain visibly marked as TODO or unknown.
- No proposal, belief, draft, or discarded idea was promoted to canon.
- No contradiction was hidden by rewording or deletion.
- Relative links identify the authoritative pages.
- Significant changes are traceable to a request or decision record.
- Every substantive intake claim has a disposition, including claims that caused no repository change.
- The original submission remains unchanged and the review report distinguishes source text from reviewer conclusions.

When asked to brainstorm, write only in `development/` unless the user explicitly requests canon changes. When instructions are ambiguous about canon impact, pause and ask.

## File conventions

Use plain Markdown, lowercase kebab-case filenames, and relative links. Do not introduce generator-specific syntax into content unless the repository formally adopts that tool. Follow [`references/repository-standards.md`](references/repository-standards.md) for naming, headings, TODOs, and change records.

## Branches and pull requests

Use one short-lived branch per intake case or other coherent maintenance task. Keep overlapping canon changes sequential unless their independence has been established. See [`references/git-workflow.md`](references/git-workflow.md) for naming, draft PRs, validation, and merge boundaries.

Before pushing, run the same deterministic integrity check used by CI:

```powershell
python -m pip install --requirement requirements.txt
python scripts/validate_repository.py --base-ref origin/main
python scripts/build_claim_index.py --check
python scripts/build_graph_index.py --check
```

The base-ref argument enforces immutability for submissions that have already merged. Omit it only when validating a standalone checkout without a comparison ref.
