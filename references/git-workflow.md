# Git Workflow

Git history and pull requests provide the publication layer for the CLOTH's
intake audit trail. They do not replace submissions, reviews, decisions, or the
canon change log. In the semantic integration sequence, publication follows
the authorized patch, review and authority determination, stitching,
current-state changes, and validation. See the
[`CLOTH / THREAD model`](cloth-thread-model.md).

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

Mark the PR ready only when every included review is complete or the PR clearly documents why an unresolved administrative item does not block the proposed changes. A completed review may still record publication as pending while GitHub checks run.

The `Repository integrity` workflow validates pull requests and pushes to `main`. It checks internal links, canon metadata, graph structure and index freshness, intake and review relationships, controlled claim dispositions, development records for exceptional dispositions, and the immutability of submissions already present on the base branch. A separate restrained Markdown job checks repository-maintained prose while excluding immutable author submissions.

All third-party and GitHub-maintained Actions must be pinned to full commit SHAs. Keep the corresponding major-version comment beside each SHA for readability. Dependabot checks monthly for GitHub Actions updates and opens reviewable PRs rather than moving action versions implicitly.

### Windows credential-backed GitHub CLI

On Windows, sandboxed processes may be unable to read GitHub credentials stored
in Windows Credential Manager even when `gh auth status` succeeds in the user's
own terminal. For authenticated `gh` operations, request narrowly scoped
escalation on the first attempt when the keyring is the configured credential
source. Prefer reusable approvals for only the required operations, such as
`gh pr create`, `gh pr view`, `gh pr checks`, `gh pr ready`, and `gh pr merge`.

Do not disable the sandbox, request unrestricted shell access, expose a token,
or store a token in repository files. `git push` is not a `gh` operation and
retains its own scoped approval and authentication path. Connector-backed
GitHub operations remain preferred when they can access the repository.

## Parallel branches

Parallel branches are appropriate only when their semantic effects are independent. Different files alone do not prove independence.

Avoid parallel canon-changing branches when they affect the same subject, rely on one another's decisions, change shared terminology, reorganize paths used by the other branch, or could produce incompatible facts despite a clean textual merge.

When relevant canon changes merge while another branch remains open, update the open branch from `main` and repeat its contradiction and duplication checks.

## Commits and merge strategy

Keep commits coherent and attributable to the intake case or maintenance task.
Finalize the review, generated index, and locally verified content before the
publication commit when practical. Git history and the PR record exact commit
provenance; do not create follow-up commits solely to copy a commit hash,
check result, PR URL, or merge state into a review.

Squash merging is the default for a completed case because it gives `main` one understandable change unit. Regular merge commits remain available for exceptional cases where individual commits carry meaningful independent provenance. Rebase merging is disabled.

GitHub automatically deletes merged remote head branches. After updating local `main` and confirming a clean working tree, delete the corresponding local branch as well. Do not delete open or unmerged branches, and preserve abandoned work through a closed PR or development record before deleting it. Never reuse a deleted branch name.

Do not merge merely because Git reports no conflicts. Confirm that:

- every substantive claim has a reviewed disposition
- authoritative pages match the review
- unresolved conflicts remain documented rather than silently selected
- links and required metadata validate
- the diff contains no unrelated changes
- the repository-integrity and Markdown checks pass

## Remote policy

The repository allows squash and regular merge commits, disables rebase merging, and automatically deletes merged remote head branches. Squash commits use the PR title and body so accepted history reflects the reviewed change description.

GitHub Projects, Wiki, and Discussions are disabled; Issues remain available for work tracking. Actions have read-only default token permissions, cannot approve pull requests, and must use immutable SHA references.

Required reviews, required status checks, and protection against direct pushes remain unresolved and must not be enabled or altered without explicit author approval. They are unavailable for this private repository under its current GitHub plan.
