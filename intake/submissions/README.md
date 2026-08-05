# Intake Submissions

Store each new batch of information as a separate Markdown file in this directory. Start from [`../../templates/intake-submission.md`](../../templates/intake-submission.md).

Begin each topic as a case. Use a filename containing the seed date, descriptive slug, and submission sequence:

```text
YYYY-MM-DD-topic-s01.md
```

Capture later conversational decisions with [`../../templates/conversation-addendum.md`](../../templates/conversation-addendum.md):

```text
YYYY-MM-DD-topic-a01.md
YYYY-MM-DD-topic-a02.md
```

All files in the series share a `case_id`. Once review begins, do not edit a submission. Provide corrections or additions through a new submission or addendum that links to its parent and identifies superseded claim IDs.

Every newly added seed and addendum must declare
`transmission_status: complete` and a controlled `completion_basis` of
`end-marker`, `explicit-confirmation`, or `complete-attachment`. If
`end-marker` is used, preserve the literal `<!-- END OF SEED -->` marker in the
immutable submission. Do not create an intake record from a suspected partial
transmission.

Repository navigation files such as this README are not submissions.
