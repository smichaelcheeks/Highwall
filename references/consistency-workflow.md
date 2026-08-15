# Consistency Workflow

Use this workflow to keep semantic review proportional to a case's likely
effects while retaining full deterministic repository validation.

In CLOTH terminology, consistency review **pulls affected THREADs**: it traces
authority and provenance backward and semantic dependencies forward. This
discovery determines the scope of an integration but does not itself authorize a
change. See the [`CLOTH / THREAD model`](cloth-thread-model.md).

Follow explicit graph relationships when they are available. Use semantic
search, manifests, backlinks, and indexed claims to discover missing, implicit,
or unmodeled relationships and widen the review when those discoveries expose
additional effects. An explicit relationship assists traversal but never grants
authority by itself.

## Impact manifests

Every new intake review declares four nonempty front-matter lists:

```yaml
subjects:
  - highwall
domains:
  - places
search_terms:
  - corridor
authoritative_targets:
  - canon/places/highwall.md
```

Subject IDs use lowercase kebab case and remain stable across aliases. Domains
use this controlled vocabulary: `administration`, `characters`, `culture`,
`design`, `economy`, `government`, `history`, `institutions`, `law`,
`organizations`, `places`, `religion`, `story`, `technology`, and
`terminology`.

Search terms include names, aliases, distinctive phrases, and relationship
terms needed to find earlier coverage. Authoritative targets use
repository-relative paths and identify the pages expected to own approved
changes. Update the manifest when review discovers additional impact.

## Consistency tiers

### Tier 1: deterministic repository validation

Run for every change. It checks links, metadata, intake structure, controlled
dispositions, transmission completeness, impact manifests, generated-index
freshness, and submission immutability. Tier 1 is repository-wide because its
cost is deterministic and bounded.

### Tier 2: targeted semantic review

Run for every lore case. Build context from the impact manifest:

```powershell
python scripts/build_case_context.py `
  --subject highwall `
  --domain places `
  --term corridor `
  --target canon/places/highwall.md
```

Inspect the returned authoritative targets, prior indexed claims, matching
canon and development pages, and backlinks. Widen the manifest and rerun when a
new dependency, alias, or affected subject appears. Ordinary cases stop after
the complete affected neighborhood is reviewed.

This is the ordinary mechanism for pulling the THREADs named by an impact
manifest.

### Tier 3: repository-wide semantic audit

Review the complete canon and claim set when a change alters shared taxonomy,
naming, chronology, geography, political structure, repository boundaries,
paths, aliases, or ownership; affects three or more domains; or exposes
unexpected cross-domain effects.

Tier 3 pulls THREADs repository-wide when targeted tracing cannot reliably
bound the consequences.

## Knowledge graph index

`development/indexes/knowledge-graph.json` is generated from explicit graph
metadata on maintained Markdown records:

```powershell
python scripts/build_graph_index.py
python scripts/build_graph_index.py --check
```

The graph index is navigation-only. Validation rejects duplicate identities,
uncontrolled relationship types, unresolved endpoints, and missing relationship
provenance. Its unmigrated-link inventory supports incremental conversion of
legacy `related` links without changing their meaning.

## Claim index

`development/indexes/claim-index.json` is generated from intake-review claim
tables:

```powershell
python scripts/build_claim_index.py
python scripts/build_claim_index.py --check
```

The index is navigation-only. It cannot establish canon, replace reviews, or
resolve contradictions. Each row surfaces the source review's declared
`review_authority` so working and established claims can be distinguished
during discovery. It also derives `supersedes` and `superseded_by` claim links
and the current status of development records required by `defer`, `conflict`,
and `retire` dispositions. These lifecycle fields are discovery aids; the
linked review and development records remain authoritative. Targeted case
context displays the same fields. CI rejects a stale index, a missing
supersession target, or an exceptional disposition without a linked status
record.

## Mandatory fresh Tier 3 audits

A fresh Tier 3 audit is required:

- after every ten completed canon cases since the latest comprehensive Tier 3
  baseline;
- before a tagged canon snapshot;
- before sustained story drafting;
- after major regional, chronological, political, taxonomy, ownership, path,
  or alias changes;
- when one change affects three or more semantic domains;
- when incremental or targeted reviews repeatedly expose unexpected
  dependencies; or
- when the prior baseline is missing, incomplete, or unreliable.

Evaluate these triggers during every lore intake review, not as an optional
later maintenance activity. Identify the latest applicable baseline, examine
the full Git range since it, and record the required and performed tier. Count
unique completed canon cases from Git history and completed review records;
multiple submissions or addenda in one case count once. The canon change log
and impact manifests may corroborate the evaluation but cannot determine it by
themselves. Semantic judgment remains required when deciding applicability,
whether a change is major, and whether unexpected dependencies are repeated.
Ambiguity makes the baseline unreliable and therefore activates a fresh Tier 3
review.

## Incremental audits

After an audit establishes an exact Git baseline, use the
[`incremental audit workflow`](incremental-audit-workflow.md) to determine which
recorded relationships require renewed semantic review after later commits.
The complete Git diff is the changed-path authority. Impact manifests, the
canon change log, claim indexes, and generated context assist discovery but do
not prove semantic consistency.

For every lore intake review, apply this baseline evaluation within the regular
intake record. The standalone incremental-audit template remains available for
dedicated maintenance audits and rebaselines, but it is not a substitute for
the intake-review fields.

Incremental reuse applies only after every recorded dependency and invalidation
condition has been checked. An unchanged file may be affected by a changed
dependency, and a changed file does not invalidate all of its relationships.
Widen to Tier 2 or Tier 3 when the incremental record exposes the triggers in
that workflow; the existing Tier 3 triggers above remain controlling.

## Maintenance boundary

Routine process-only maintenance may use
[`../templates/maintenance-review.md`](../templates/maintenance-review.md)
without an intake submission or claim inventory. Use full intake when work adds
lore, changes authority, resolves a contradiction, or establishes significant
repository governance. A lightweight record never grants lore authority.

## Publication boundary

Complete an intake review after claims, authorized changes, local validation,
and diff inspection are complete. Record publication as `pending` and publish
the final content once. GitHub owns check history and the eventual merge commit;
do not create audit-only commits merely to copy passing check results or a
commit hash into the review. The completion report must still state the PR,
checks, merge state, and unresolved decisions.
