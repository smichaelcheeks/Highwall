# Codex Repository Instructions

These instructions apply to the entire Highwall repository. Treat them as mandatory for every fresh Codex session.

## Read before changing files

Read these documents in order:

1. [`README.md`](README.md)
2. [`CONTRIBUTING.md`](CONTRIBUTING.md)
3. [`references/repository-standards.md`](references/repository-standards.md)
4. [`references/intake-workflow.md`](references/intake-workflow.md)
5. [`references/front-matter.md`](references/front-matter.md)
6. [`references/git-workflow.md`](references/git-workflow.md)

For a new batch of setting information, also read [`references/canon-intake-quickstart.md`](references/canon-intake-quickstart.md) and the relevant templates.

## Canon safety

- Never invent lore, fill gaps creatively, or strengthen a claim beyond its source unless explicitly instructed.
- Nothing becomes canon merely because it appears in conversation, intake, story, development, research, or retired material.
- Keep objective setting truth, in-world belief, historical claim, character knowledge, reader reveal, and development proposal distinct.
- Never silently resolve a contradiction. Preserve both claims, link their sources, create or update a contradiction report, and await a decision.
- Prefer an explicit TODO, open question, or clarification request over guessing.
- Preserve ambiguity when instructed.
- Give each fact one authoritative home and link to it elsewhere.

## New information workflow

Before changing authoritative content:

1. Confirm the requested authority: `establish-canon`, `working-canon`, `establish-policy`, `proposal-only`, or `classify`.
2. Confirm the session mode: `exploration`, `canon-authoring`, or `direct-integration`. Default to `exploration` when unspecified.
3. Create a stable case ID and a short-lived `agent/<case-topic>` branch from synchronized `main`.
4. Preserve the seed verbatim in `intake/submissions/`; do not replace it with a summary.
5. Create the matching review in `development/intake-reviews/` and inventory every substantive claim before changing authoritative pages.
6. Give every claim a controlled disposition and concise, evidence-based rationale, including claims that cause no file change.
7. Create required open-question, proposal, contradiction, decision, or retired records before applying dependent changes.
8. Apply authorized changes to their single authoritative locations and add provenance links.
9. Capture later confirmed conversational decisions in immutable, sequenced addenda before integrating them.
10. Complete validation, push the branch, and open a draft PR. Never merge without explicit author instruction.

If the user says only “put this where it goes,” do not infer whether the material is established canon, working canon, or a proposal. Ask unless the surrounding instruction makes that authority explicit.

## Git and concurrent work

- Start substantial work from a clean, synchronized `main`.
- Do not mix a new intake case into an unrelated branch or pull request.
- Do not run concurrent Codex chats against the same working directory. Use separate Git worktrees or clones for truly parallel cases.
- Keep overlapping canon changes sequential even when Git could merge them textually.
- Do not delete open or unmerged branches.
- Do not reuse branch names.

## Required verification

Run before pushing:

```powershell
python scripts/validate_repository.py --base-ref origin/main
```

Also run `git diff --check` and inspect the complete diff for invented lore, duplicated authority, unrecorded decisions, broken narrative boundaries, and unrelated changes.

After pushing, require both GitHub checks to pass:

- `Canon and intake integrity`
- `Markdown style`

If local Python is unavailable, report that limitation and rely on the draft PR check rather than claiming local validation passed.

## Completion report

Summarize the case ID, authority, session mode, submissions and addenda, claim dispositions, files changed and deliberately unchanged, exceptions, validation, commit, and PR. Call out every unresolved decision. Do not describe a review as complete while required claims or checks remain pending.
