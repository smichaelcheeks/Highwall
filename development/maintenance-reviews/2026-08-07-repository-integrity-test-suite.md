# Maintenance Review: Repository Integrity Test Suite

## Scope

- **Maintenance ID:** `MAINT-2026-08-07-REPOSITORY-INTEGRITY-TEST-SUITE`
- **Objective:** Protect the documented behavior of the repository validator,
  claim parser and index, and targeted-context generator with isolated,
  repeatable regression tests before further audit automation is added.
- **Authority:** Explicitly authorized routine process-only maintenance. This
  record and its tests grant no lore, story, design, claim-disposition, or
  repository-policy authority.
- **Session handling:** Direct implementation of the supplied maintenance
  request. No intake case, submission, addendum, or claim inventory is
  required because the change introduces no lore or significant governance.
- **Branch:** `agent/repository-integrity-tests` from synchronized `main` at
  `312e7a13d79c9feb5dd1d51a0eca1b409484fe9d`.
- **Impact:** A standard-library test harness, testability-focused script
  seams, focused fixes for documented invariants, and CI execution of the
  suite before existing repository validation.

## Maintenance boundary

The task tests and enforces existing requirements only. It does not modify
canon, story, design, submissions, intake reviews, claim dispositions,
authority declarations, exceptional-record state, or the generated claim
index. Cases whose correct behavior would require a new policy interpretation
are characterized or deferred below.

## Files and behavior inspected

- All four Python tools under `scripts/` and the repository-integrity GitHub
  Actions workflow.
- Repository, intake, front-matter, Git, and consistency standards.
- The regional Tier 3 and claim-to-canon provenance audits.
- The authority-discovery and claim-lifecycle maintenance records.
- Representative submissions, reviews, exceptional records, and generated
  claim-index rows, including working authority and resolved lifecycle state.
- The maintenance-review template and current repository layout.

## Test architecture

`tests/fixtures.py` builds a minimal deterministic temporary repository with a
synthetic canon page, complete submission, matching review, actionable claim,
optional exceptional record, generated index location, and required search
roots. Tests add only the records relevant to each case. Git-specific tests
initialize a temporary repository with explicit local identity configuration.

The harness uses `unittest`, `tempfile`, and other standard-library modules.
It has no network, credential, branch-name, execution-order, or third-party
dependency. Production functions accept an explicit repository root, while
the existing command-line defaults and output remain unchanged.

The canonical local command is:

```powershell
python -m unittest discover -s tests -v
```

## Coverage matrix summary

| Requirement | Implementation | Positive coverage | Negative or boundary coverage | Fixture and expected result |
| --- | --- | --- | --- | --- |
| Local links and anchors | `Validator.validate_links`, `anchors_for` | Relative links, anchors, duplicate headings, UTF-8, POSIX and Windows separators | Missing targets and anchors, repository escape | Temporary Markdown tree; valid links pass and focused defects identify their source |
| Canon metadata | `validate_canon_front_matter` | Complete metadata, index exemption, block and inline lists | Missing fields, invalid status/level, scalar in a list field | Synthetic canon page; schema violations fail without touching real canon |
| Intake relationships and IDs | `validate_intake`, `validate_review_claims` | Matched submission/review and controlled dispositions | Orphans, mismatches, duplicate submission and claim IDs, malformed rows | Synthetic submission/review pairs; each invalid relationship produces a focused error |
| Transmission completeness | `validate_transmission_completeness`, `is_new_path` | End marker, explicit confirmation, complete attachment, historical compatibility | Missing or invalid metadata and absent literal marker | New and historical synthetic submissions; only documented deterministic cases are enforced |
| Impact manifests | `validate_impact_manifest` | Nonempty controlled fields and existing target | Missing/empty fields, bad subject/domain, missing/escaping target | Synthetic review metadata; invalid manifest fails at the relevant field |
| Submission immutability | `validate_submission_immutability` | Unchanged baseline and newly added submission | Modified, whitespace-only, renamed, deleted, and invalid base ref | Isolated Git repository; merged-source mutations fail without real history changes |
| Claim parsing | `parse_claim_rows`, `split_markdown_row` | Multiple rows, optional cells, escaped pipes, whitespace, UTF-8 | Short and extra-column rows | Static synthetic table rows; well-formed data is preserved and malformed data is skipped by the parser and rejected by validation |
| Claim index and authority | `build_index`, `render` | Field preservation, authority propagation, manifests, deterministic order | Duplicate IDs, missing exceptional records/status | Temporary reviews and records; index remains navigation-only |
| Supersession lifecycle | `build_index` | Forward and reverse links, multiple successors, addenda, independent reviews | Missing target; circular relation characterized | Multi-review fixture; derived links are stable and never replace review authority |
| Generated-index freshness | `main`, `render` | Current index and repeatable generation | Missing, stale, and lifecycle-only stale index | Temporary tracked-output path; check mode never rewrites stale content |
| Targeted semantic context | `build_context` | Subject, domain, term, target, backlink, authority, lifecycle, and stable order | No filters, no match, result limit | Temporary index and search corpus; semantic fields are asserted without broad snapshots |
| CI integration | `.github/workflows/repository-integrity.yml` | Standard local command runs under existing Python setup | Test failures stop the integrity job | Existing pinned actions and later validation steps remain unchanged |

## Tests added

- `test_validate_repository.py`: 56 validator and isolated-Git tests.
- `test_claim_index.py`: 27 index, freshness, authority, and lifecycle tests.
- `test_case_context.py`: 16 targeted-context and discovery tests.
- `test_consistency_common.py`: 14 front-matter and claim-parser tests.
- Total: 113 tests.

## Adversarial cases

The suite includes duplicate claim IDs within and across reviews, a claim ID
belonging to another submission, incomplete and extra-column claim rows,
exceptional dispositions without valid or correctly typed development records,
missing supersession targets, circular supersession characterization, stale
lifecycle fields, malformed front-matter list values, path escape attempts,
Windows separators, UTF-8 text, duplicate headings,
working-versus-established authority, and open-versus-resolved exceptional
records.

The validator now reports a complete review's malformed claim row instead of
allowing a valid neighboring row to hide it. The parser alone still omits
malformed rows by design; repository validation is the enforcement surface.

## Production refactors

- `Validator` accepts an explicit repository root and consistently uses it for
  traversal, link resolution, Git comparison, and displayed paths.
- Claim-index construction accepts a root, builds once per command, separates
  rendering from writing, and deterministically sorts reverse lifecycle links.
- Targeted-context rendering is available as a pure `build_context` function;
  CLI parsing and file output remain in `main`.
- All three CLIs retain their existing defaults. A hidden `--root` option
  permits isolated CLI regression tests without advertising a new workflow.
- Shared claim-table splitting now preserves escaped Markdown pipes and
  requires the documented nine-column schema.
- Shared front-matter parsing recognizes the repository's block lists and
  simple inline YAML list form.

## Unambiguous implementation defects fixed

1. Claim IDs were checked only within one review. Repository-wide duplicate
   IDs now fail both validation and index construction.
2. Claim rows were split at every pipe, so an escaped pipe shifted columns.
   Escaped Markdown pipes are now preserved and covered directly.
3. Submission immutability compared `base_ref` only with `HEAD`, missing
   staged and unstaged source mutations. It now compares the base with the
   working tree, covering modifications, whitespace, renames, and deletions.
4. An invalid comparison ref raised a subprocess exception instead of a
   repository validation error. It now produces a focused diagnostic.
5. Required canon list fields were checked only for presence, so scalar values
   passed. The validator now requires list syntax while accepting empty,
   block, and simple inline lists.
6. Backslash-based relative paths resolved differently on Windows and Linux.
   Local-link and authoritative-target resolution now normalize separators.
7. Exceptional dispositions accepted any development link even though the
   controlled meanings require questions/proposals for `defer`, contradiction
   reports for `conflict`, and retired records for `retire`. Validation and
   index construction now enforce those existing record boundaries.

Each change has direct positive and negative regression coverage.

## Characterized but unchanged behavior

- TODO placeholder links are excluded when their target contains `TODO`.
- Historical submissions and reviews without newer completeness or impact
  metadata retain compatibility when no base comparison identifies them as
  new.
- Explicit-confirmation and complete-attachment bases rely on recorded
  metadata; deterministic validation cannot independently prove the human
  event.
- Targeted-context filters form a discovery union, and subject filters also
  contribute a normalized search term.
- Circular supersession currently renders as bidirectional navigation. No
  existing rule declares such a relationship invalid, so the test does not
  grant or recommend authority to the cycle.
- The standalone claim parser skips malformed rows; the validator detects a
  claim-shaped row with the wrong number of columns.
- Claim rationale remains authoritative in the linked review and is not
  copied into the navigation-only index. No current index policy requires
  that duplication, so the suite characterizes the boundary rather than
  expanding the generated schema.

## Policy ambiguities deliberately not resolved

- Deprecated canon pages must link to a replacement or retirement record, but
  current policy does not specify whether that link must be in `related`,
  `provenance`, or prose. The suite characterizes the current lack of a
  structured check instead of selecting one location.
- No rule defines whether supersession cycles are prohibited or how they
  should be resolved. The index remains navigation-only and no cycle policy is
  encoded.
- Semantic truncation indicators such as an abrupt sentence or promised
  omitted section require judgment. Only existing deterministic completeness
  metadata and literal-marker rules are tested.
- The lightweight front-matter parser supports documented repository forms,
  not arbitrary YAML features such as nested mappings or commas inside quoted
  inline-list values. Adopting a general YAML parser would require a separate
  dependency and policy decision.

## Files deliberately unchanged

- All files under `canon/`, `story/`, `design/`, and `intake/`.
- All intake reviews and all authority, disposition, supersession, and
  rationale records.
- All open questions, contradictions, proposals, decisions, and retired
  records.
- `development/indexes/claim-index.json`; its generated content remains
  current and no schema change was required.
- Repository standards and templates; the task tests existing rules rather
  than establishing new ones.

## CI integration

The existing `Canon and intake integrity` job now runs the canonical test
command after the already-pinned Python setup and before repository validation
and index freshness checks. No action, permission, dependency, network call,
or existing check was added, removed, or weakened. The separate `Markdown
style` job is unchanged.

## Local verification

- [x] All 113 tests pass using the bundled Codex Python runtime because
  `python` is not available on `PATH`.
- [x] The suite passes on repeated runs with deterministic fixture output.
- [x] Repository validation passes against `origin/main`.
- [x] The generated claim index is current.
- [x] `git diff --check` passes.
- [x] The complete diff was inspected for unintended content and authority
  effects.
- [x] No immutable submission changed.
- [x] No canon, story, belief, historical, or design claim changed.
- [x] No authority, disposition, contradiction, or development-record status
  changed.
- [x] No unrelated generated output changed.
- [ ] Draft pull request opened.
- [ ] `Canon and intake integrity` passes on GitHub.
- [ ] `Markdown style` passes on GitHub.

## Recommended successor tasks

1. Establish a deterministic location rule for deprecated-page replacement or
   retirement links, then add the corresponding validator tests.
2. Decide whether supersession cycles are forbidden, merely suspicious, or
   valid in a bounded correction model before adding cycle validation.
3. Evaluate a general YAML parser only if front matter begins using structures
   beyond the deliberately small documented subset.

## Publication

Pending. GitHub owns the final commit, draft-PR, and check history; those states
will be reported externally and will not be copied into this completed review
through an audit-only follow-up commit.
