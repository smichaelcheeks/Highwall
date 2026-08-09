# Maintenance Review: Ignore Codex Attachments

## Scope

- **Maintenance ID:** `MAINT-2026-08-08-IGNORE-CODEX-ATTACHMENTS`
- **Objective:** Prevent Codex-managed transient attachment storage from
  making the repository working tree appear dirty.
- **Why this is maintenance:** The change introduces no lore, authority,
  contradiction resolution, claim disposition, or significant governance
  policy.
- **Branch:** `agent/ignore-codex-attachments` from synchronized `main`.
- **Impact:** Git ignores only the repository-root transient attachment
  directory at `.codex-remote-attachments/`.

## Files inspected

- `.gitignore`
- Repository tracking metadata for `.codex-remote-attachments/`
- The maintenance-review template and required repository workflow documents

The attachment directory itself and the files inside it were not inspected.
`git ls-files -- .codex-remote-attachments` returned no paths, confirming that
the directory contained no tracked repository files.

## Changes

Added this exact repository-root ignore rule to `.gitignore`:

```gitignore
# Codex-managed transient attachments
/.codex-remote-attachments/
```

Created this maintenance review to record the cleanup boundary and
verification.

## Deliberate non-changes

- No attachment was deleted, moved, inspected, staged, or committed.
- No broader `.codex/`, attachment, image, or temporary-file ignore pattern
  was added.
- No canon, story, design, intake, intake review, claim, authority,
  contradiction, proposal, decision, or retired record changed.
- No semantic audit was performed and no incremental-context output was
  written to the repository.

## Verification

- [x] `git status --short` omits `.codex-remote-attachments/`.
- [x] The incremental-context smoke test accepts live `HEAD` with transient
  attachment storage present and emits context to stdout only.
- [x] All 149 unit tests pass under the installed Python 3.13.14 runtime;
  `python` is not available on `PATH`.
- [x] Repository validation passes against `origin/main` under the installed
  Python 3.13.14 runtime.
- [x] The generated claim index is current under the installed Python 3.13.14
  runtime.
- [x] `git diff --check` passes.
- [x] The complete diff contains only the `.gitignore` rule and this review.
- [x] No setting, story, belief, historical, or design claim was introduced.
- [x] No authority or contradiction decision was made.
- [x] No attachment was deleted, moved, inspected, staged, or committed.
- [x] Publication status will be reported from GitHub rather than copied into
  an audit-only commit.

## Publication

Pending. The branch has not yet been pushed, and the draft pull request and
required GitHub checks have not yet been created or run.
