from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_case_context import build_context
from build_claim_index import build_index
from fixtures import CLAIM_ID, SUBMISSION_ID, FixtureRepository


class CaseContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository().build_valid()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def context(self, **criteria) -> str:
        return build_context(self.fixture.root, build_index(self.fixture.root), **criteria)

    def test_requires_at_least_one_filter(self) -> None:
        with self.assertRaisesRegex(ValueError, "provide at least one"):
            self.context()

    def test_subject_filter_matches_claim(self) -> None:
        report = self.context(subjects=["example-place"])
        self.assertIn(CLAIM_ID, report)
        self.assertIn("Subjects:** example-place", report)

    def test_domain_filter_matches_claim(self) -> None:
        report = self.context(domains=["administration"])
        self.assertIn(CLAIM_ID, report)

    def test_search_term_matches_summary(self) -> None:
        report = self.context(terms=["administrative claim"])
        self.assertIn(CLAIM_ID, report)

    def test_authoritative_target_matches_claim(self) -> None:
        report = self.context(targets=["canon/places/example-place.md"])
        self.assertIn(CLAIM_ID, report)
        self.assertIn("canon/places/example-place.md` (score 1000)", report)

    def test_backlink_content_is_discovered(self) -> None:
        self.fixture.write(
            "story/backlink.md",
            "# Backlink\n\nSee [Example](../canon/places/example-place.md).\n",
        )
        report = self.context(terms=["example-place"])
        self.assertIn("story/backlink.md", report)

    def test_multiple_filters_use_documented_discovery_union(self) -> None:
        report = self.context(subjects=["missing-subject"], domains=["administration"])
        self.assertIn(CLAIM_ID, report)

    def test_no_match_behavior_is_explicit(self) -> None:
        report = self.context(terms=["no-such-synthetic-token"])
        self.assertEqual(2, report.count("- None found."))

    def test_files_have_stable_score_then_path_order(self) -> None:
        self.fixture.write("story/b.md", "# B\n\nneedle\n")
        self.fixture.write("story/a.md", "# A\n\nneedle\n")
        report = self.context(terms=["needle"])
        self.assertLess(report.index("story/a.md"), report.index("story/b.md"))

    def test_max_results_limits_files_and_claims(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[self.fixture.claim_row(), self.fixture.claim_row(claim_id=second)]
        )
        report = self.context(terms=["synthetic"], max_results=1)
        indexed = report.split("## Indexed claims", 1)[1]
        self.assertEqual(1, indexed.count("CASE-"))

    def test_review_authority_is_displayed(self) -> None:
        self.fixture.review(authority="working-canon")
        report = self.context(terms=["synthetic"])
        self.assertIn("authority: `working-canon`", report)

    def test_working_and_established_authority_remain_distinct(self) -> None:
        later_case = "CASE-2000-01-02-EXAMPLE"
        later_submission = f"{later_case}-S01"
        later_claim = f"{later_submission}-C001"
        self.fixture.review(authority="establish-canon")
        self.fixture.review(
            relative="development/intake-reviews/working-review.md",
            case_id=later_case,
            submission_id=later_submission,
            authority="working-canon",
            claims=[self.fixture.claim_row(claim_id=later_claim)],
        )
        report = self.context(terms=["synthetic"])
        self.assertIn("authority: `establish-canon`", report)
        self.assertIn("authority: `working-canon`", report)

    def test_supersedes_and_superseded_by_are_displayed(self) -> None:
        later = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(),
                self.fixture.claim_row(claim_id=later, supersedes=CLAIM_ID),
            ]
        )
        report = self.context(terms=["synthetic"])
        self.assertIn(f"supersedes: {CLAIM_ID}", report)
        self.assertIn(f"superseded by: {later}", report)

    def test_exception_record_status_is_displayed(self) -> None:
        self.fixture.development_record(status="open")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        report = self.context(terms=["synthetic"])
        self.assertIn("development/open-questions/example-question.md [open]", report)

    def test_resolved_lifecycle_does_not_rewrite_original_disposition(self) -> None:
        self.fixture.development_record(status="resolved")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        report = self.context(terms=["synthetic"])
        self.assertIn("disposition: `defer`", report)
        self.assertIn("[resolved]", report)

    def test_normalization_deduplicates_and_sorts_filters(self) -> None:
        report = self.context(terms=["Synthetic", "synthetic", " administrative "])
        self.assertIn("Terms:** administrative, synthetic", report)


if __name__ == "__main__":
    unittest.main()
