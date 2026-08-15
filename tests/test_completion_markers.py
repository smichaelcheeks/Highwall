from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from fixtures import FixtureRepository
from validate_repository import Validator


class CompletionMarkerTests(unittest.TestCase):
    def validate_marker(self, marker: str) -> list[str]:
        fixture = FixtureRepository().build_valid()
        try:
            fixture.submission(marker=marker)
            validator = Validator(None, fixture.root)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                validator.run()
            return validator.errors
        finally:
            fixture.cleanup()

    def test_current_patch_marker_is_accepted(self) -> None:
        self.assertEqual([], self.validate_marker("<!-- END OF PATCH -->"))

    def test_legacy_stitch_marker_is_accepted(self) -> None:
        self.assertEqual([], self.validate_marker("<!-- END OF STITCH -->"))

    def test_legacy_seed_marker_is_accepted(self) -> None:
        self.assertEqual([], self.validate_marker("<!-- END OF SEED -->"))


if __name__ == "__main__":
    unittest.main()
