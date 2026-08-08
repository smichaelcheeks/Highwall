from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from consistency_common import (
    parse_claim_rows,
    parse_front_matter,
    parse_inline_list,
    split_markdown_row,
)
from fixtures import CLAIM_ID, FixtureRepository


class ConsistencyCommonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def parse_rows(self, rows: list[str]):
        path = self.fixture.write("review.md", "\n".join(rows) + "\n")
        return parse_claim_rows(path)

    def test_parse_front_matter_preserves_scalars_and_lists(self) -> None:
        path = self.fixture.write(
            "metadata.md",
            "---\ntitle: Example\nsubjects:\n  - example-place\n  - other-place\n---\n",
        )
        scalars, lists = parse_front_matter(path)
        self.assertEqual("Example", scalars["title"])
        self.assertEqual(["example-place", "other-place"], lists["subjects"])

    def test_parse_front_matter_without_delimiters_is_empty(self) -> None:
        path = self.fixture.write("metadata.md", "# Example\n")
        self.assertEqual(({}, {}), parse_front_matter(path))

    def test_parse_inline_front_matter_list(self) -> None:
        path = self.fixture.write(
            "metadata.md", '---\nsubjects: [example-place, "other-place"]\n---\n'
        )
        _, lists = parse_front_matter(path)
        self.assertEqual(["example-place", "other-place"], lists["subjects"])

    def test_non_list_scalar_is_not_parsed_as_inline_list(self) -> None:
        self.assertIsNone(parse_inline_list("example-place"))

    def test_split_markdown_row_preserves_escaped_pipe_in_cell(self) -> None:
        cells = split_markdown_row("| one | compound \\| value | three |")
        self.assertEqual(["one", "compound \\| value", "three"], cells)

    def test_parse_valid_claim_row(self) -> None:
        claims = self.parse_rows([self.fixture.claim_row()])
        self.assertEqual(CLAIM_ID, claims[0]["claim_id"])
        self.assertEqual("no-change", claims[0]["disposition"])

    def test_parse_multiple_claims_in_source_order(self) -> None:
        second = CLAIM_ID[:-3] + "002"
        claims = self.parse_rows(
            [self.fixture.claim_row(), self.fixture.claim_row(claim_id=second)]
        )
        self.assertEqual([CLAIM_ID, second], [claim["claim_id"] for claim in claims])

    def test_parse_compound_markdown_cell(self) -> None:
        claims = self.parse_rows(
            [self.fixture.claim_row(summary="First clause \\| second clause")]
        )
        self.assertEqual("First clause \\| second clause", claims[0]["summary"])
        self.assertEqual("administrative", claims[0]["classification"])

    def test_parse_empty_optional_cells(self) -> None:
        claims = self.parse_rows(
            [self.fixture.claim_row(authority_basis="", supersedes="", target="")]
        )
        self.assertEqual("", claims[0]["authority_basis"])
        self.assertEqual([], claims[0]["supersedes"])
        self.assertEqual("", claims[0]["target"])

    def test_malformed_short_row_is_skipped(self) -> None:
        claims = self.parse_rows([f"| {CLAIM_ID} | Too short |"])
        self.assertEqual([], claims)

    def test_unexpected_additional_column_is_skipped(self) -> None:
        row = self.fixture.claim_row().rstrip("|") + "| extra |"
        self.assertEqual([], self.parse_rows([row]))

    def test_whitespace_is_normalized_around_cells(self) -> None:
        row = self.fixture.claim_row(summary="  Synthetic summary  ")
        claims = self.parse_rows([row])
        self.assertEqual("Synthetic summary", claims[0]["summary"])

    def test_supersedes_extracts_multiple_full_claim_ids(self) -> None:
        earlier = "CASE-2000-01-01-EXAMPLE-S01-C099"
        other = "CASE-2000-01-01-OTHER-S01-C001"
        claims = self.parse_rows(
            [self.fixture.claim_row(supersedes=f"`{earlier}` and `{other}`")]
        )
        self.assertEqual([earlier, other], claims[0]["supersedes"])

    def test_utf8_summary_is_preserved(self) -> None:
        claims = self.parse_rows(
            [self.fixture.claim_row(summary="Synthetic café — administrative only.")]
        )
        self.assertEqual("Synthetic café — administrative only.", claims[0]["summary"])


if __name__ == "__main__":
    unittest.main()
