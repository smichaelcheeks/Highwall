# Git Workflow

Git history and pull requests provide the publication layer for the repository's intake audit trail. They do not replace submissions, reviews, decisions, or the canon change log.

## Branch policy

Use a short-lived branch for each intake case or coherent maintenance task. Prefer these patterns:

```text
agent/case-topic
agent/fix-topic
agent/repository-maintenance
```

Start branches from the latest accepted `main`. Do not commit substantive work directly to `main` unless the author explicitly authorizes an emergency exception.

## Pull requests

Open a draft pull request while a case is still being refined. Its description should link or identify:

- the case ID
- all included submissions and addenda
- their intake reviews
- significant files created or changed
- contradictions, decisions, and open questions
- validation performed
- any canon change-log entry

Mark the PR ready only when every included review is complete or the PR clearly documents why an unresolved administrative item does not block the proposed changes.

The `Repository integrity` workflow validates pull requests and pushes to `main`. It checks internal links, canon metadata, intake and review relationships, controlled claim dispositions, development records for exceptional dispositions, and the immutability of submissions already present on the base branch. A separate restrained Markdown job checks repository-maintained prose while excluding immutable author submissions.

## Parallel branches

Parallel branches are appropriate only when their semantic effects are independent. Different files alone do not prove independence.

Avoid parallel canon-changing branches when they affect the same subject, rely on one another's decisions, change shared terminology, reorganize paths used by the other branch, or could produce incompatible facts despite a clean textual merge.

When relevant canon changes merge while another branch remains open, update the open branch from `main` and repeat its contradiction and duplication checks.

## Commits and merge strategy

Keep commits coherent and attributable to the intake case or maintenance task. Record relevant commit provenance in completed reviews.

Squash merging is the preferred default for a completed case because it gives `main` one understandable change unit. This remains a preference, not a mandatory repository rule, until the author explicitly decides whether exceptions or enforcement are desired.

Do not merge merely because Git reports no conflicts. Confirm that:

- every substantive claim has a reviewed disposition
- authoritative pages match the review
- unresolved conflicts remain documented rather than silently selected
- links and required metadata validate
- the diff contains no unrelated changes
- the repository-integrity and Markdown checks pass

## Remote policy

Branch protection, required reviews, status checks, and automatic deletion of merged branches are GitHub repository settings. Do not enable or alter them until the author selects the desired enforcement policy.
