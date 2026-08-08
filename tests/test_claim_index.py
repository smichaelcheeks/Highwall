from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_claim_index import build_index, render
from fixtures import CASE_ID, CLAIM_ID, SUBMISSION_ID, FixtureRepository


class ClaimIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository().build_valid()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def claims(self):
        return build_index(self.fixture.root)["claims"]

    def test_valid_fixture_builds_navigation_only_index(self) -> None:
        index = build_index(self.fixture.root)
        self.assertEqual(3, index["schema_version"])
        self.assertEqual("navigation-only", index["authority"])
        self.assertEqual(CLAIM_ID, index["claims"][0]["claim_id"])

    def test_claim_fields_are_preserved(self) -> None:
        row = self.fixture.claim_row(
            summary="Synthetic summary.",
            classification="question",
            disposition="out-of-scope",
            target="No change",
            rationale="A rationale that is not indexed.",
        )
        self.fixture.review(claims=[row])
        claim = self.claims()[0]
        self.assertEqual("Synthetic summary.", claim["summary"])
        self.assertEqual("question", claim["classification"])
        self.assertEqual("out-of-scope", claim["disposition"])
        self.assertEqual("No change", claim["target"])

    def test_characterizes_rationale_as_review_only(self) -> None:
        self.fixture.review(
            claims=[self.fixture.claim_row(rationale="Review-owned rationale.")]
        )
        self.assertNotIn("rationale", self.claims()[0])

    def test_review_authority_propagates(self) -> None:
        self.fixture.review(authority="working-canon")
        self.assertEqual("working-canon", self.claims()[0]["review_authority"])

    def test_manifest_fields_propagate(self) -> None:
        claim = self.claims()[0]
        self.assertEqual(["example-place"], claim["subjects"])
        self.assertEqual(["administration"], claim["domains"])
        self.assertEqual(
            ["canon/places/example-place.md"], claim["authoritative_targets"]
        )

    def test_multiple_claims_are_sorted_by_id(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(claim_id=second),
                self.fixture.claim_row(claim_id=CLAIM_ID),
            ]
        )
        self.assertEqual([CLAIM_ID, second], [claim["claim_id"] for claim in self.claims()])

    def test_duplicate_claim_ids_across_reviews_raise(self) -> None:
        self.fixture.review(relative="development/intake-reviews/duplicate.md")
        with self.assertRaisesRegex(ValueError, "Duplicate claim ID"):
            build_index(self.fixture.root)

    def test_claim_without_lifecycle_relationship_has_empty_fields(self) -> None:
        claim = self.claims()[0]
        self.assertEqual([], claim["supersedes"])
        self.assertEqual([], claim["superseded_by"])
        self.assertEqual([], claim["exception_records"])

    def test_supersession_derives_reverse_relationship(self) -> None:
        later = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(),
                self.fixture.claim_row(claim_id=later, supersedes=f"`{CLAIM_ID}`"),
            ]
        )
        claims = {claim["claim_id"]: claim for claim in self.claims()}
        self.assertEqual([CLAIM_ID], claims[later]["supersedes"])
        self.assertEqual([later], claims[CLAIM_ID]["superseded_by"])

    def test_multiple_later_claims_have_stable_reverse_order(self) -> None:
        later_two = f"{SUBMISSION_ID}-C003"
        later_one = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(),
                self.fixture.claim_row(claim_id=later_two, supersedes=CLAIM_ID),
                self.fixture.claim_row(claim_id=later_one, supersedes=CLAIM_ID),
            ]
        )
        claims = {claim["claim_id"]: claim for claim in self.claims()}
        self.assertEqual([later_one, later_two], claims[CLAIM_ID]["superseded_by"])

    def test_missing_supersession_target_raises(self) -> None:
        missing = "CASE-2000-01-01-MISSING-S01-C001"
        self.fixture.review(claims=[self.fixture.claim_row(supersedes=missing)])
        with self.assertRaisesRegex(ValueError, "supersedes missing claim"):
            build_index(self.fixture.root)

    def test_supersession_across_independent_reviews_preserves_authority(self) -> None:
        later_case = "CASE-2000-01-02-EXAMPLE"
        later_submission = f"{later_case}-S01"
        later_claim = f"{later_submission}-C001"
        self.fixture.review(
            relative="development/intake-reviews/later-review.md",
            case_id=later_case,
            submission_id=later_submission,
            authority="working-canon",
            claims=[self.fixture.claim_row(claim_id=later_claim, supersedes=CLAIM_ID)],
        )
        claims = {claim["claim_id"]: claim for claim in self.claims()}
        self.assertEqual("establish-policy", claims[CLAIM_ID]["review_authority"])
        self.assertEqual("working-canon", claims[later_claim]["review_authority"])
        self.assertEqual([later_claim], claims[CLAIM_ID]["superseded_by"])

    def test_supersession_across_addendum(self) -> None:
        addendum_id = f"{CASE_ID}-A01"
        addendum_claim = f"{addendum_id}-C001"
        self.fixture.review(
            relative="development/intake-reviews/addendum-review.md",
            submission_id=addendum_id,
            claims=[self.fixture.claim_row(claim_id=addendum_claim, supersedes=CLAIM_ID)],
        )
        claims = {claim["claim_id"]: claim for claim in self.claims()}
        self.assertEqual([addendum_claim], claims[CLAIM_ID]["superseded_by"])

    def test_characterizes_circular_supersession_as_navigation(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(supersedes=second),
                self.fixture.claim_row(claim_id=second, supersedes=CLAIM_ID),
            ]
        )
        claims = {claim["claim_id"]: claim for claim in self.claims()}
        self.assertEqual([second], claims[CLAIM_ID]["supersedes"])
        self.assertEqual([second], claims[CLAIM_ID]["superseded_by"])

    def test_exception_record_open_status_is_derived(self) -> None:
        self.fixture.development_record(status="open")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        self.assertEqual("open", self.claims()[0]["exception_records"][0]["status"])

    def test_exception_record_resolved_status_is_derived(self) -> None:
        self.fixture.development_record(
            "development/contradictions/example-conflict.md", status="resolved"
        )
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="conflict",
                    target="[Conflict](../contradictions/example-conflict.md)",
                )
            ]
        )
        self.assertEqual("resolved", self.claims()[0]["exception_records"][0]["status"])

    def test_exceptional_claim_without_link_raises(self) -> None:
        self.fixture.review(claims=[self.fixture.claim_row(disposition="retire")])
        with self.assertRaisesRegex(ValueError, "no linked development record"):
            build_index(self.fixture.root)

    def test_missing_exception_record_raises(self) -> None:
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer", target="[Missing](../open-questions/missing.md)"
                )
            ]
        )
        with self.assertRaisesRegex(ValueError, "Missing exception record"):
            build_index(self.fixture.root)

    def test_exception_record_without_status_raises(self) -> None:
        self.fixture.write(
            "development/open-questions/example-question.md",
            "---\ntitle: Example\ntype: open-question\n---\n\n# Example\n",
        )
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        with self.assertRaisesRegex(ValueError, "has no status"):
            build_index(self.fixture.root)

    def test_wrong_exception_record_type_raises(self) -> None:
        self.fixture.development_record()
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="conflict",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        with self.assertRaisesRegex(ValueError, "Wrong exception record type"):
            build_index(self.fixture.root)

    def test_render_is_deterministic(self) -> None:
        self.assertEqual(
            render(build_index(self.fixture.root)), render(build_index(self.fixture.root))
        )

    def test_render_preserves_utf8_and_has_trailing_newline(self) -> None:
        self.fixture.review(
            claims=[self.fixture.claim_row(summary="Synthetic café — navigation.")]
        )
        rendered = render(build_index(self.fixture.root))
        self.assertIn("café — navigation", rendered)
        self.assertTrue(rendered.endswith("\n"))

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "build_claim_index.py"),
                "--root",
                str(self.fixture.root),
                *args,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_cli_writes_and_repeated_generation_is_identical(self) -> None:
        first = self.run_cli()
        self.assertEqual(0, first.returncode, first.stderr)
        output = self.fixture.root / "development/indexes/claim-index.json"
        content = output.read_bytes()
        second = self.run_cli()
        self.assertEqual(0, second.returncode, second.stderr)
        self.assertEqual(content, output.read_bytes())

    def test_cli_check_accepts_current_index(self) -> None:
        self.assertEqual(0, self.run_cli().returncode)
        result = self.run_cli("--check")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("current", result.stdout)

    def test_cli_check_rejects_missing_index(self) -> None:
        result = self.run_cli("--check")
        self.assertEqual(1, result.returncode)
        self.assertIn("stale", result.stderr)

    def test_cli_check_rejects_stale_index(self) -> None:
        output = self.fixture.write("development/indexes/claim-index.json", "{}\n")
        before = output.read_text(encoding="utf-8")
        result = self.run_cli("--check")
        self.assertEqual(1, result.returncode)
        self.assertEqual(before, output.read_text(encoding="utf-8"))

    def test_staleness_detects_lifecycle_only_change(self) -> None:
        self.fixture.development_record(status="open")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        self.assertEqual(0, self.run_cli().returncode)
        record = self.fixture.root / "development/open-questions/example-question.md"
        record.write_text(
            record.read_text(encoding="utf-8").replace("status: open", "status: resolved"),
            encoding="utf-8",
        )
        self.assertEqual(1, self.run_cli("--check").returncode)


if __name__ == "__main__":
    unittest.main()
