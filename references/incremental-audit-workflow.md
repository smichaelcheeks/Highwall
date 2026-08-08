# Incremental Audit Workflow

Use this workflow to reassess a previously audited repository state after later
changes. It reduces repeated coverage work while preserving semantic review as
the authority for consistency judgments.

## Policy authority and provenance

This process was established by
[`CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-S01`](../intake/submissions/2026-08-07-incremental-audit-framework-s01.md)
and its
[`intake review`](../development/intake-reviews/2026-08-07-incremental-audit-framework-s01-review.md).
It grants no lore, story, design, or claim-disposition authority.

Historical audit reports are immutable snapshots. Do not rewrite them to fit
this workflow. A later incremental record identifies the prior report and exact
audited commit, then records new coverage decisions separately.

## Governing principles

- Every audit conclusion belongs to an exact Git commit.
- Git history is the authoritative record of changed paths. Intake impact
  manifests and the canon change log assist interpretation but cannot replace
  the complete Git diff.
- Reuse applies to a previously audited relationship and its complete authority
  chain, not merely to the files that happened to contain it.
- An unchanged file may be invalidated by a changed dependency. A changed file
  does not automatically invalidate every relationship involving it.
- Carry a conclusion forward only after checking every recorded dependency and
  invalidation condition.
- Generated claim indexes, case context, and incremental context are
  navigation-only. They cannot declare canon coherent.
- Meaning, contradiction, authority, ownership, and narrative-boundary
  judgments require semantic review.
- Unexpected dependencies require a wider review.
- Existing Tier 3 triggers in
  [`consistency-workflow.md`](consistency-workflow.md) remain in force.
- Missing, ambiguous, or unauditable baseline evidence requires fresh review,
  not guessed reuse.

## Prerequisites

An incremental audit requires:

1. A prior audit or baseline record that names an exact Git commit.
2. The complete invalidation conditions or dependencies for each result being
   considered for reuse.
3. A new committed head state whose full Git range can be examined.
4. Readable generated claim indexes at both commits when claim comparison is
   part of the repository baseline.
5. A reliable repository structure and an ancestry relationship from baseline
   to head.

If a prior result lacks sufficient dependency or invalidation information,
record it as `not-assessed` and review it fresh. Do not infer its coverage from
an unchanged path.

## Workflow

### 1. Fix the comparison range

Record the prior audit, baseline commit, head commit, ancestry result, and exact
Git range. Use full resolved commit hashes in the audit record even when the
command accepts abbreviated hashes or symbolic refs.

For a live comparison to `HEAD`, use a clean working tree so the range cannot
silently omit uncommitted changes. A comparison explicitly pinned to two
historical commits examines only those committed snapshots.

### 2. Build deterministic change context

Run:

```powershell
python scripts/build_incremental_audit_context.py `
  --baseline BASELINE_COMMIT `
  --head HEAD
```

The tool writes deterministic Markdown to stdout. Redirect it only for a
temporary working artifact when useful; routine generated reports should not be
committed.

The report compares the complete Git path change set, historical claim indexes,
changed review manifests, discoverable canon metadata, backlinks, and current
targeted claim context. It reports historical differences without interpreting
them as authorization.

### 3. Map changes to audited relationships

For each prior finding or verified relationship in scope:

1. List its authority-bearing claims, review records, canon or story owners,
   development records, terminology, aliases, links, and narrative boundaries.
2. List every invalidation condition recorded by the prior audit.
3. Check the Git diff, claim changes, manifest context, changed metadata,
   backlinks, and semantic dependencies against that list.
4. Record the evidence for every checked condition, including unchanged
   dependencies that were inspected.

Impact manifests are starting points rather than exhaustive dependency maps.
The canon change log is a human-readable aid rather than a substitute for the
Git range.

### 4. Perform semantic review

The reviewer decides whether the relationship's meaning, authority, ownership,
contradiction state, or narrative boundary changed. Generated output cannot
make this decision.

Use one controlled coverage outcome:

| Outcome | Meaning |
| --- | --- |
| `carried-forward` | All recorded dependencies and invalidation conditions were checked and remain semantically unaffected. |
| `revalidated` | The relationship was affected, reviewed again, and remains valid. |
| `invalidated` | A dependency changed and the prior conclusion cannot be reused. |
| `superseded` | A later audit result explicitly replaces the earlier result. |
| `not-assessed` | Evidence was insufficient or the relationship was outside scope. |
| `widened` | Review expanded to Tier 2 or Tier 3. |

These outcomes describe audit coverage only. They do not change canon level,
review authority, claim disposition, development-record status, or lore.

### 5. Widen when required

Widen the review when changes affect or expose:

- shared terminology or aliases;
- geography or spatial identity;
- chronology or event equivalence;
- political structure;
- canon ownership;
- established-versus-working authority;
- story or reader-reveal boundaries;
- paths used by authoritative links;
- three or more semantic domains;
- unexpected dependencies outside the declared change scope;
- a prior critical relationship; or
- an incomplete or unreliable baseline.

Use Tier 2 for the complete affected semantic neighborhood. Use Tier 3 when the
repository-wide triggers in
[`consistency-workflow.md`](consistency-workflow.md#tier-3-repository-wide-semantic-audit)
apply. An incomplete baseline cannot be repaired by increasingly confident
automation; establish a fresh baseline.

### 6. Record and validate the audit

Create a new record from
[`incremental-audit-review.md`](../templates/incremental-audit-review.md).
Reference historical audit results rather than editing them. Run the repository
validation appropriate to any resulting changes and keep publication state in
Git and GitHub.

## Required incremental audit record

Every record includes:

- audit ID;
- prior audit or baseline;
- baseline and head commits;
- confirmation that the baseline is an ancestor;
- Git range examined;
- changed files by repository domain;
- claims added, removed, or changed;
- authority, disposition, target, and lifecycle changes;
- prior findings or verified relationships considered;
- invalidation conditions checked;
- results carried forward, revalidated, invalidated, superseded, not assessed,
  or widened;
- semantic review performed;
- review widening;
- new findings;
- coverage limitations; and
- validation and publication state.

Evidence must identify the relevant commit, path, claim, review, or dependency.
An outcome without recorded invalidation checks is not `carried-forward`.

## Context-builder guarantees and limits

[`build_incremental_audit_context.py`](../scripts/build_incremental_audit_context.py)
uses Git and the Python standard library only. It reports:

- resolved commits, ancestry, and range;
- changed paths classified as canon, story, design, intake, review,
  development, reference, template, script, test, workflow, or other;
- added, removed, changed, and unchanged indexed claims;
- changes to classification, authority basis, review authority, disposition,
  target, supersession, and exceptional-record status;
- changed review impact manifests;
- changed canon status, canon level, aliases, related links, and provenance when
  present in supported front matter;
- relevant backlinks, including unchanged source pages; and
- current targeted claim context derived from changed manifests and targets.

It fails when a commit cannot be resolved, the baseline is not an ancestor, a
required historical index cannot be read, `HEAD` would omit working-tree
changes, or the repository structure is insufficient. It has no network or
GitHub dependency.

The tool does not prove that a manifest is exhaustive, infer semantic
dependencies, authorize a removed claim's retirement, interpret a changed
claim as a correction, or establish coherence. The linked review remains the
claim-processing authority.
