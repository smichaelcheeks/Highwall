---
title: Knowledge Object Schema V2 Migration
type: implementation-status
status: active
authority: navigation-only
case_id: CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2
review: "intake-reviews/2026-08-16-knowledge-object-schema-v2-s01-review.md"
related:
  - "../references/graph-structure.md"
  - "../references/cloth-thread-model.md"
  - "intake-reviews/2026-08-16-knowledge-object-schema-v2-a01-review.md"
  - "intake-reviews/2026-08-16-knowledge-object-schema-v2-a02-review.md"
  - "intake-reviews/2026-08-16-knowledge-object-schema-v2-a03-review.md"
---

# Knowledge Object Schema V2 Migration

This is the public completion ledger for the schema-v2 knowledge-object
program. It reports implementation state and grants no lore, story, or graph
semantic authority. The governing policy remains in `references/` and the
authorizing review is linked above.

The program is **not complete** while any required stage below is incomplete.
An infrastructure stage, a passing test suite, or a fresh generated index is
not equivalent to a completed knowledge migration.

## Completion stages

| Stage | Required outcome | Status |
| --- | --- | --- |
| Policy and schema | Knowledge claims, intake claims, histories, lifecycle, provenance, and completion invariants are authoritative policy. | Complete in foundation case with A01 and A02 corrections |
| Parser and projection | Maintained metadata and governance records are parsed structurally and emitted in a unified navigation-only projection. | Complete in foundation case with A01 and A02 corrections |
| Prospective validation | New and changed objects enforce identity, per-change history, lifecycle, ownership, authorized provenance, and content-boundary rules. | Reopened by A03 after the second audit found boundary, transition, authority, supersession, event-truth, and registry bypasses |
| Entity history migration | Every current entity has audited history coverage and an explicit migration disposition. | Pending |
| Relationship history migration | Every current relationship has audited history, lifecycle, provenance, ownership, and pair validation. | Pending |
| Intake-claim crosswalk | Every indexed intake claim maps to a maintained claim or an explicit non-current-state category. | Pending |
| Knowledge-claim migration | Every approved maintained claim in scope has a stable ID, bounded content, subjects, authority, lifecycle, and provenance. | Pending |
| THREAD traversal | Deterministic object-first traversal covers claims, histories, relations, reviews, decisions, and exceptions. | Pending |
| Final audit | Independent canon-equivalence, semantic relationship, provenance, story-boundary, and completion audit passes. | Pending |

## Fixed baseline inventory

The author authorized the program against commit
`9840884cfa5b534a448352c284734efe111115b7`, which contains:

- 20 opted-in graph entities;
- 51 explicit relationships;
- one controlled relationship type, navigation-only `related-to`; and
- 419 indexed intake-review claims.

These numbers are a migration baseline, not a frozen limit on later governed
repository growth.

## Completion invariants

The program may be marked complete only when:

1. every baseline entity and relationship has an explicit audited migration
   result, required local history, and honest controlled history coverage;
2. every baseline intake claim has one crosswalk disposition;
3. every maintained knowledge claim selected by that audit has a stable
   identity, bounded authoritative content, lifecycle, subjects, and exact
   provenance;
4. retired and superseded objects remain addressable and no durable ID is
   reused or reactivated;
5. every schema-v2 object change appends a compatible local history event and
   every exact provenance claim authorizes and names its resulting object;
   authority applies to the actual changed state, dispositions match actions,
   and compound changes record every applicable event class;
6. no semantic relationship was inferred from navigation links, prose, or
   co-occurrence;
7. generated projections contain no unexplained migration inventory;
8. deterministic validation and THREAD traversal checks pass; and
9. an independent read-only audit confirms canon equivalence and the story
   boundary.

## Publication log

| Stage publication | Case or PR | Result |
| --- | --- | --- |
| Schema-v2 foundation and completion corrections | `CASE-2026-08-16-KNOWLEDGE-OBJECT-SCHEMA-V2` | S01, A01, and A02 reviews complete; A03 remediation and independent reaudit in progress on draft PR #41 |
