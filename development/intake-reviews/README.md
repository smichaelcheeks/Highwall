# Intake Reviews

This directory contains auditable, claim-level reports for submissions under [`../../intake/submissions/`](../../intake/submissions/README.md).

Create one review per submission or addendum from [`../../templates/intake-review.md`](../../templates/intake-review.md). Use the source basename with `-review` appended:

```text
intake/submissions/2026-08-03-topic-s01.md
development/intake-reviews/2026-08-03-topic-s01-review.md

intake/submissions/2026-08-03-topic-a01.md
development/intake-reviews/2026-08-03-topic-a01-review.md
```

A review is complete only when every substantive claim has a disposition and the verification section reflects the resulting repository state. Reviews in the same case collectively preserve the seed-to-conversation history. Later corrections belong in a new addendum and review; corrections to the review record itself use a dated amendment. Do not rewrite history invisibly.
