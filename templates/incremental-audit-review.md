# Incremental Audit: TODO

## Scope and authority boundary

- **Audit ID:** `TODO`
- **Objective:** TODO
- **Authority:** Audit-only. This record grants no lore, story, design,
  policy, claim-disposition, or contradiction-resolution authority.
- **Prior audit or baseline:** TODO
- **Baseline commit:** `TODO`
- **Head commit:** `TODO`
- **Baseline is ancestor of head:** TODO: `yes` or `no`
- **Git range examined:** `TODO..TODO`
- **Branch:** `TODO`

## Deterministic change context

- **Command:** `python scripts/build_incremental_audit_context.py --baseline TODO --head TODO`
- **Output handling:** TODO: state where temporary output was inspected; do
  not commit routine generated reports.
- **Changed files by repository domain:** TODO
- **Claims added, removed, or changed:** TODO
- **Authority, disposition, target, and lifecycle changes:** TODO
- **Changed review impact manifests:** TODO
- **Changed canon metadata:** TODO
- **Relevant backlinks and targeted context:** TODO

The generated context is navigation-only. Git owns the changed-path record;
linked reviews and authority-bearing records remain authoritative.

## Prior results considered

| Prior result ID | Relationship or finding | Dependencies and invalidation conditions | Evidence checked | Semantic effect | Outcome |
| --- | --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO | `TODO` |

Use only:

- `carried-forward`
- `revalidated`
- `invalidated`
- `superseded`
- `not-assessed`
- `widened`

These outcomes describe audit coverage only and do not change canon authority
or claim disposition.

## Invalidation conditions checked

TODO: Record every checked claim, review, authority record, canon or story
owner, development record, term, alias, link, and semantic dependency. An
unchanged path alone is insufficient evidence.

## Results

### Carried forward

TODO or `None`.

### Revalidated

TODO or `None`.

### Invalidated

TODO or `None`.

### Superseded

TODO or `None`.

### Not assessed

TODO or `None`.

### Widened

TODO or `None`.

## Semantic review performed

TODO: Describe the meaning, contradiction, authority, ownership, and
narrative-boundary judgments performed by a reviewer.

## Review widening

- **Tier reached:** TODO: Tier 1, Tier 2, or Tier 3
- **Trigger:** TODO or `None`
- **Additional scope inspected:** TODO or `None`
- **Unexpected dependencies:** TODO or `None`

Widen when required by
[`incremental-audit-workflow.md`](../references/incremental-audit-workflow.md)
and retain the existing Tier 3 triggers.

## New findings

TODO or `None`. A finding does not authorize remediation.

## Coverage limitations

TODO: Identify missing, ambiguous, out-of-scope, or unauditable evidence. Use a
fresh review instead of guessed reuse where the baseline is unreliable.

## Validation

- [ ] Baseline and head resolve to exact commits.
- [ ] Baseline ancestry is confirmed.
- [ ] The complete Git diff was inspected.
- [ ] Historical claim indexes were read at both commits.
- [ ] Every prior result in scope has one controlled coverage outcome.
- [ ] Every `carried-forward` result has all invalidation conditions checked.
- [ ] Changed dependencies received semantic review.
- [ ] Widening triggers were evaluated.
- [ ] Generated context was not treated as canon evidence or semantic proof.
- [ ] No claim change was interpreted as authorized retirement or promotion.
- [ ] Repository validation appropriate to resulting changes passed.
- [ ] The complete diff contains no unrelated changes.

## Publication

- **Commit:** Recorded by Git after publication.
- **Pull request:** Pending.
- **Required checks:** Pending.
- **Merge state:** Not merged without explicit author instruction.
