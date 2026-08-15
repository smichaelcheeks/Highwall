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
7. [`references/consistency-workflow.md`](references/consistency-workflow.md)

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

1. Confirm transmission completeness before any repository mutation. Require the
   current `<!-- END OF PATCH -->` marker, the legacy
   `<!-- END OF STITCH -->` or `<!-- END OF SEED -->` marker, an explicit
   author statement that the transmission is complete, or a complete
   attachment. If none is present, or the source appears truncated, stop and
   request the remainder. Do not create a branch, submission, review, or
   authoritative change from a partial source.
2. Confirm the requested authority: `establish-canon`, `working-canon`, `establish-policy`, `proposal-only`, or `classify`.
3. Confirm the session mode: `exploration`, `canon-authoring`, or `direct-integration`. Default to `exploration` when unspecified.
4. Create a stable case ID and a short-lived `agent/<case-topic>` branch from synchronized `main`.
5. Preserve the complete patch source verbatim in `intake/submissions/`; do not
   replace it with a summary. Retain legacy “stitch” or “seed” wording in
   historical artifacts where it identifies their original form.
6. Create the matching review in `development/intake-reviews/`, record its
   impact manifest, generate targeted context, and inventory every substantive
   claim before changing authoritative pages.
7. For every lore review, record the latest semantic-audit baseline, full Git
   range examined, incremental-context state, prior relationships and outcomes,
   required and performed consistency tier, Tier 3 triggers, and the completed
   canon-case count since the latest comprehensive Tier 3 baseline.
8. Give every claim a controlled disposition and concise, evidence-based rationale, including claims that cause no file change.
9. Create required open-question, proposal, contradiction, decision, or retired records before applying dependent changes.
10. Stitch authorized patches through every affected THREAD, update their
    single authoritative locations, and add provenance links. Follow explicit
    graph relationships where available and widen via semantic search when
    discovery exposes missing or implicit dependencies. Pulling a THREAD
    discovers dependencies but never supplies authority by itself.
11. Treat entities and relationships as addressable knowledge objects when
    applying the CLOTH graph model. A relationship may participate in another
    relationship when the second relation is specifically about that
    connection. Reify a relationship as an entity when it develops substantial
    independent identity, rules, history, or further structure. Do not silently
    mint new durable relationship types without authority.
12. Capture later confirmed conversational decisions in immutable, sequenced addenda before integrating them. Apply the same completeness gate to addenda.
13. Apply the required consistency tier. A fresh Tier 3 audit is mandatory
    after ten completed canon cases; before a tagged canon snapshot or sustained
    story drafting; after major regional, chronological, political, taxonomy,
    ownership, path, or alias changes; for three or more affected domains; for
    repeated unexpected dependencies; or when the baseline is missing,
    incomplete, or unreliable.
14. Complete validation, push the branch, and open a draft PR. Never merge without explicit author instruction.

Use the conceptual order: patch → review and authority determination →
stitch/integration → integration review/current-state changes → validation →
publication. Keep the submission, review, current-state changes, exception
records, and Git/PR history distinct; do not rename every technical record to
“patch.” The authoritative terminology and graph abstraction are in
[`references/cloth-thread-model.md`](references/cloth-thread-model.md).

Treat mid-sentence endings, missing promised sections, unclosed delimiters or
code fences, abrupt list endings, and references to omitted continuation as
possible truncation. Do not infer missing text. A short administrative request
may use explicit author confirmation instead of the marker when its complete
scope is unambiguous.

If the user says only “put this where it goes,” do not infer whether the material is established canon, working canon, or a proposal. Ask unless the surrounding instruction makes that authority explicit.

## Git and concurrent work

- Start substantial work from a clean, synchronized `main`.
- Do not mix a new intake case into an unrelated branch or pull request.
- Do not run concurrent Codex chats against the same working directory. Use separate Git worktrees or clones for truly parallel cases.
- Keep overlapping canon changes sequential even when Git could merge them textually.
- Do not delete open or unmerged branches.
- Do not reuse branch names.
- On Windows, authenticated `gh` operations that require credentials stored in
  Windows Credential Manager must request narrowly scoped escalation on the
  first attempt. Prefer reusable approvals limited to the required `gh pr`
  subcommand. Do not disable the sandbox or request unrestricted PowerShell or
  GitHub CLI access. `git push` remains a separate Git operation and approval.

## Required verification

Run before pushing:

```powershell
python scripts/validate_repository.py --base-ref origin/main
python scripts/build_claim_index.py --check
python scripts/build_graph_index.py --check
```

Also run `git diff --check` and inspect the complete diff for invented lore, duplicated authority, unrecorded decisions, broken narrative boundaries, and unrelated changes.

After pushing, require both GitHub checks to pass:

- `Canon and intake integrity`
- `Markdown style`

If local Python is unavailable, report that limitation and rely on the draft PR check rather than claiming local validation passed.

## Completion report

Summarize the case ID, authority, session mode, submissions and addenda, claim dispositions, files changed and deliberately unchanged, exceptions, validation, commit, PR, and GitHub checks. Call out every unresolved decision. A review may be complete after its claims, changes, local validation, and diff inspection are complete; do not describe publication or the case as finished while required GitHub checks remain pending. Do not create an audit-only commit to copy external publication state into the review.
