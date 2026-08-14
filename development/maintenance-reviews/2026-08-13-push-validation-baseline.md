# Maintenance Review: Push Validation Baseline

## Scope

- **Maintenance ID:** `MAINT-2026-08-13-PUSH-VALIDATION-BASELINE`
- **Objective:** Make repository-integrity validation on pushes to `main` use
  the pre-push commit as its comparison baseline while preserving pull-request
  baseline behavior.
- **Why this is maintenance:** The change modifies CI configuration and test
  coverage only. It introduces no lore, authority, contradiction resolution,
  claim disposition, or significant repository-governance decision.
- **Branch:** `agent/fix-push-validation-baseline` from synchronized `main`.
- **Impact:** Post-merge validation checks the newly merged change instead of
  applying current prospective review requirements retroactively to all
  historical records.

## Files inspected

- `.github/workflows/repository-integrity.yml`
- `scripts/validate_repository.py` behavior as exercised by the existing test
  suite and prior failing GitHub Actions logs
- `tests/`
- `AGENTS.md`
- `README.md`
- `CONTRIBUTING.md`
- `references/repository-standards.md`
- `references/intake-workflow.md`
- `references/front-matter.md`
- `references/git-workflow.md`
- `references/consistency-workflow.md`
- `templates/maintenance-review.md`

## Changes

Updated the `Validate repository` step so `BASE_SHA` resolves to the pull
request base SHA for pull-request events and otherwise to `github.event.before`
for pushes:

```yaml
BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}
```

This preserves the existing standalone fallback for events without either
value, including manual workflow dispatch.

Added `tests/test_workflow_configuration.py` to assert that the workflow keeps
both event-specific baseline selection and the validator's `--base-ref` call.

Created this maintenance review to record the diagnosis, scope, and
verification boundary.

## Deliberate non-changes

- No historical intake review was edited to satisfy newer prospective metadata
  requirements.
- No validator rule or compatibility behavior was weakened.
- No claim index, canon, story, design, intake submission, intake review,
  authority, contradiction, proposal, decision, or retired record changed.
- No workflow triggers, token permissions, pinned action versions, Markdown
  lint configuration, or concurrency behavior changed.

## Verification

- [ ] Full unit test suite passes.
- [ ] Repository validation passes against `main` as the branch baseline.
- [ ] Generated claim index is current.
- [ ] The complete diff contains only the workflow fix, regression test, and
  this maintenance review.
- [x] No setting, story, belief, historical, or design claim was introduced.
- [x] No authority or contradiction decision was made.
- [x] Historical records were left unchanged.
- [x] Publication status will be reported from GitHub rather than copied into
  an audit-only commit.

## Publication

Pending.
