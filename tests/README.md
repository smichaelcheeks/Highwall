# Repository Integrity Tests

The suite exercises the repository validator, claim parser and index,
targeted-context generator, and incremental-audit context builder against
deterministic synthetic repositories. It never writes to the real canon,
intake records, reviews, or generated index.

Validator fixtures also cover prospective lore-review audit-baseline fields,
deterministic Tier 3 trigger relationships, and the boundary that leaves
semantic trigger judgments to reviewers.

Run the complete suite from the repository root:

```powershell
python -m unittest discover -s tests -v
```

Tests use only the Python standard library. Cases that require Git initialize
an isolated temporary repository with local identity configuration.

Some tests deliberately characterize behavior that is not established as
repository policy. Their names begin with `test_characterizes_` and the
maintenance review records the corresponding limitation or successor task.
