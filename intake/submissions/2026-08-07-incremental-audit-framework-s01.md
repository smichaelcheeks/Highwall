---
title: Establish an Incremental Audit Framework
type: intake-submission
case_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK
submission_id: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-S01
sequence: 1
submitted_on: 2026-08-07
submitted_by: Shawn
authority: establish-policy
session_mode: direct-integration
transmission_status: complete
completion_basis: end-marker
parent_submission: null
supersedes_claims: []
related:
  - "../../references/incremental-audit-workflow.md"
---

# Establish an Incremental Audit Framework

Implement a reusable incremental-audit workflow for the Highwall repository.

Use GPT-5.6 Sol at `high` reasoning effort.

## Authority and session

- **Authority:** `establish-policy`
- **Session mode:** `direct-integration`
- **Transmission status:** Complete
- **Completion basis:** The literal end marker below

This request establishes repository process and tooling only. It grants no authority to add, alter, reinterpret, promote, or remove lore.

## Context

The following work is complete and merged:

- Regional Tier 3 semantic audit: `723d457`
- Claim-to-canon provenance audit: `a6a24d2`
- Provenance remediation through: `312e7a1`
- Repository-integrity regression suite: `856f0d4`

The audits established reusable baselines, but future reviews need a formal way to determine which earlier conclusions remain valid after later changes.

The existing 113-test regression suite should protect any new tooling.

## Repository workflow

Follow `AGENTS.md` and all referenced repository instructions.

Because this task establishes significant process policy, use the full intake workflow.

Use:

```text
Case ID: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK
Submission: CASE-2026-08-07-INCREMENTAL-AUDIT-FRAMEWORK-S01
Branch: agent/incremental-audit-framework
```

Preserve this complete request verbatim as the seed submission. Create the matching intake review, impact manifest, administrative claim inventory, and policy provenance.

Before mutation:

1. Read the required repository documents.
2. Read both completed audit reports.
3. Read the repository-integrity test-suite maintenance review.
4. Inspect all scripts and tests.
5. Synchronize clean `main`.
6. Confirm the branch name has never been used.
7. Create the dedicated branch.

Do not merge without explicit author instruction.

## Objective

Create a documented and tested process that lets a future audit:

1. Start from a prior audited commit.
2. Inspect the complete Git change set to a new commit.
3. Identify changed claims, authority records, canon, development records, and tooling.
4. Determine which previously audited relationships require renewed semantic review.
5. Carry forward unaffected conclusions with explicit evidence.
6. Widen to Tier 2 or Tier 3 when incremental review is insufficient.

The framework must reduce repeated work without treating semantic consistency as mechanically provable.

## Required policy

Establish these principles:

- Audit conclusions belong to an exact Git baseline.
- Git history is the authoritative record of changed files.
- Intake impact manifests and the canon change log assist interpretation but cannot replace the Git diff.
- Reuse applies to audited relationships and authority chains, not merely files.
- An unchanged file may be invalidated by a changed dependency.
- A changed file does not automatically invalidate every relationship involving it.
- A conclusion may be carried forward only after all recorded invalidation conditions are checked.
- Generated context is navigation-only and cannot declare canon coherent.
- Semantic review remains required for meaning, contradiction, authority, ownership, and narrative-boundary judgments.
- Unexpected dependencies require widening the review.
- Existing Tier 3 triggers remain in force.
- Missing, ambiguous, or unauditable baseline information requires a fresh review rather than guessed reuse.

## Deliverables

Implement the smallest maintainable set of artifacts needed to support the workflow. Expected deliverables are:

- A reference document defining the incremental-audit workflow.
- A reusable incremental-audit review template.
- A script that builds deterministic change context between Git commits.
- Automated tests for the new script.
- Updates linking the workflow from existing consistency guidance.
- The required intake submission and intake review.
- Any generated index updates required by the intake workflow.

A likely script name is:

```text
scripts/build_incremental_audit_context.py
```

A likely reference path is:

```text
references/incremental-audit-workflow.md
```

A likely template path is:

```text
templates/incremental-audit-review.md
```

Inspect repository conventions before finalizing paths.

## Incremental audit record

Define a reusable audit record containing at least:

- Audit ID
- Prior audit or baseline
- Baseline commit
- Head commit
- Confirmation that the baseline is an ancestor
- Git range examined
- Changed files by repository domain
- Claims added, removed, or changed
- Authority, disposition, target, and lifecycle changes
- Prior findings or verified relationships considered
- Invalidation conditions checked
- Results carried forward
- Results invalidated
- Semantic review performed
- Review widening
- New findings
- Coverage limitations
- Validation and publication state

Do not require historical audit reports to be rewritten. Preserve them as immutable historical snapshots and reference them from later incremental records.

## Context-builder behavior

The tool should accept a baseline and head, for example:

```powershell
python scripts/build_incremental_audit_context.py `
  --baseline 027d0e3 `
  --head HEAD
```

It should produce deterministic Markdown suitable for review.

At minimum, report:

- Resolved baseline and head commits
- Whether the baseline is an ancestor of the head
- Changed repository paths
- Changed canon, story, design, intake, review, development, reference, template, script, test, and workflow files
- Claims added or removed
- Existing claims whose indexed fields changed
- Changes to:
  - classification
  - authority basis
  - review authority
  - disposition
  - target
  - supersession relationships
  - exceptional-record status
- Impact-manifest subjects, domains, terms, and authoritative targets associated with changed reviews
- Changed canon provenance, authority level, aliases, and related metadata where deterministically discoverable
- Relevant backlinks and current targeted context
- A warning when semantic dependencies may extend beyond directly changed files
- Clear limitations stating that the output does not establish coherence

Prefer stdout output and avoid committing routine generated reports.

The tool must fail clearly when:

- A commit cannot be resolved.
- The baseline is not an ancestor of the head.
- Required historical index data cannot be read.
- The comparison would silently omit uncommitted working-tree changes.
- Repository structure is insufficient for a reliable comparison.

Do not add network or GitHub dependencies.

## Claim comparison

Use the generated claim index at each commit when available.

Compare claims by stable claim ID and distinguish:

- Added claim
- Removed claim
- Changed indexed fields
- Added supersession
- Removed supersession
- Changed exceptional-record status
- Changed review authority
- Unchanged claim

Do not interpret a removed or changed claim as authorized retirement. Report the historical difference and require semantic review.

The linked review remains authoritative; the generated index and incremental report remain navigation-only.

## Carry-forward decision vocabulary

Define controlled outcomes for prior audited results:

- `carried-forward`: All recorded dependencies and invalidation conditions were checked and remain semantically unaffected.
- `revalidated`: The relationship was affected but was reviewed again and remains valid.
- `invalidated`: A dependency changed and the prior conclusion cannot be reused.
- `superseded`: A later audit result explicitly replaces the earlier result.
- `not-assessed`: Available evidence was insufficient or the relationship was outside scope.
- `widened`: Review expanded to Tier 2 or Tier 3.

These outcomes describe audit coverage only. They do not change canon authority or claim disposition.

## Widening rules

Require widening when changes affect or expose:

- Shared terminology or aliases
- Geography or spatial identity
- Chronology or event equivalence
- Political structure
- Canon ownership
- Established versus working authority
- Story or reader-reveal boundaries
- Paths used by authoritative links
- Three or more semantic domains
- Unexpected dependencies outside the declared change scope
- A prior critical relationship
- An incomplete or unreliable baseline

A comprehensive Tier 3 rebaseline remains required under the triggers already documented in `references/consistency-workflow.md`.

## Historical acceptance exercise

Run the framework against a real historical range beginning with the provenance-audit baseline:

```text
Baseline: 027d0e3
Head: 856f0d4
```

The generated context should make it possible for a reviewer to identify that this range affected:

- Forge location
- Highwall information-flow scope
- Claim lifecycle discovery
- Working-wildfire ownership
- Repository validator and parser behavior

It should also avoid claiming that unrelated verified relationships are automatically invalid.

This exercise validates context discovery only. Do not create a new semantic finding or retroactively edit either completed audit.

## Testing

Extend the standard-library test suite.

Cover at least:

- Valid ancestor comparison
- Invalid commit
- Non-ancestor baseline
- Clean-tree requirement
- Changed-file classification
- Added and removed claims
- Changed authority or disposition
- Changed supersession relationships
- Changed exceptional-record status
- Deterministic output
- Windows path handling
- UTF-8 content
- Historical index retrieval
- Missing historical index
- Empty diff
- Tooling-only diff
- Canon change with unchanged dependent page
- Output limitations and navigation-only warning

Use isolated temporary Git repositories. Do not mutate real content or history.

The canonical test command should remain:

```powershell
python -m unittest discover -s tests -v
```

## Boundaries

Do not:

- Automate semantic approval.
- Declare unchanged canon coherent solely from a file diff.
- Treat impact manifests as exhaustive.
- Modify historical audit reports.
- Modify immutable submissions other than adding this new authorized submission.
- Change existing lore, story, design, authority, or claim dispositions.
- Resolve the deprecated-page, supersession-cycle, or general-YAML policy questions from the test-suite review.
- Add third-party dependencies without explicit approval.
- Expand the task into scheduled automation or external services.

Record any newly discovered policy ambiguity and stop that line of implementation rather than guessing.

## Verification

Before pushing, run:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_repository.py --base-ref origin/main
python scripts/build_claim_index.py --check
git diff --check
```

If `python` is unavailable on `PATH`, use the available Codex Python runtime and report that accurately.

Inspect the complete diff for:

- Invented lore
- Authority changes outside the approved process policy
- Submission mutation
- Silent contradiction resolution
- Unrelated changes
- Stale generated output
- Unpinned GitHub Actions

## Publication

Commit the coherent case, push the branch, and open a draft PR.

Require both GitHub checks to pass:

- `Canon and intake integrity`
- `Markdown style`

Do not mark the PR ready or merge it without explicit author instruction.

## Completion report

Report:

- Case ID
- Authority and session mode
- Submission and review
- Policy claims and dispositions
- Reference, template, script, and tests added or changed
- Historical acceptance-exercise result
- Files deliberately unchanged
- Policy ambiguities deferred
- Local test count and results
- Repository validation
- Claim-index check
- Diff inspection
- Commit
- Draft PR
- GitHub check status
- Recommended next maintenance task
- Every unresolved decision

<!-- END OF SEED -->
