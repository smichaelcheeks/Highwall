# Repository Integrity Tests

The suite exercises the repository validator, claim parser and index, and
targeted-context generator against deterministic synthetic repositories. It
never writes to the real canon, intake records, reviews, or generated index.

Run the complete suite from the repository root:

```powershell
python -m unittest discover -s tests -v
```

Tests use only the Python standard library. Cases that require Git initialize
an isolated temporary repository with local identity configuration.

Some tests deliberately characterize behavior that is not established as
repository policy. Their names begin with `test_characterizes_` and the
maintenance review records the corresponding limitation or successor task.
