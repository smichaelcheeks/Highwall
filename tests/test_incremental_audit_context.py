from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_claim_index import build_index, render
from build_incremental_audit_context import (
    AuditContextError,
    build_report,
    classify_path,
)
from fixtures import CLAIM_ID, SUBMISSION_ID, FixtureRepository


class IncrementalAuditContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository().build_valid()
        self.write_index()
        self.baseline = self.fixture.initialize_git()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def write_index(self) -> None:
        self.fixture.write(
            "development/indexes/claim-index.json",
            render(build_index(self.fixture.root)),
        )

    def commit(self, message: str) -> str:
        self.fixture.git("add", ".")
        self.fixture.git("commit", "-q", "-m", message)
        return self.fixture.git("rev-parse", "HEAD").stdout.strip()

    def report(self, baseline: str | None = None, head: str | None = None) -> str:
        return build_report(
            self.fixture.root,
            baseline or self.baseline,
            head or self.fixture.git("rev-parse", "HEAD").stdout.strip(),
        )

    def test_valid_ancestor_comparison(self) -> None:
        self.fixture.write("references/change.md", "# Change\n")
        head = self.commit("add reference")
        report = self.report(head=head)
        self.assertIn(f"Resolved baseline:** `{self.baseline}`", report)
        self.assertIn(f"Resolved head:** `{head}`", report)
        self.assertIn("Baseline is ancestor of head:** Yes", report)

    def test_invalid_commit_fails_clearly(self) -> None:
        with self.assertRaisesRegex(AuditContextError, "Cannot resolve baseline commit"):
            self.report(baseline="not-a-commit")

    def test_non_ancestor_baseline_fails(self) -> None:
        self.fixture.write("references/main.md", "# Main\n")
        main_head = self.commit("main change")
        self.fixture.git("switch", "-q", "-c", "side", self.baseline)
        self.fixture.write("references/side.md", "# Side\n")
        side_head = self.commit("side change")
        with self.assertRaisesRegex(AuditContextError, "not an ancestor"):
            self.report(baseline=main_head, head=side_head)

    def test_clean_tree_required_when_head_is_HEAD(self) -> None:
        self.fixture.write("uncommitted.md", "# Uncommitted\n")
        with self.assertRaisesRegex(AuditContextError, "silently omit uncommitted"):
            build_report(self.fixture.root, self.baseline, "HEAD")

    def test_clean_tree_required_for_current_branch_ref(self) -> None:
        branch = self.fixture.git("branch", "--show-current").stdout.strip()
        self.fixture.write("uncommitted.md", "# Uncommitted\n")
        with self.assertRaisesRegex(AuditContextError, "silently omit uncommitted"):
            build_report(self.fixture.root, self.baseline, branch)

    def test_changed_file_classification(self) -> None:
        paths = {
            "canon/place.md": "canon",
            "story/reveal.md": "story",
            "design/principles.md": "design",
            "intake/submissions/seed.md": "intake",
            "development/intake-reviews/review.md": "review",
            "development/open-questions/question.md": "development",
            "references/workflow.md": "reference",
            "templates/review.md": "template",
            "scripts/tool.py": "script",
            "tests/test_tool.py": "test",
            ".github/workflows/check.yml": "workflow",
        }
        for path, expected in paths.items():
            self.assertEqual(expected, classify_path(path))

    def test_added_and_removed_claims(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[self.fixture.claim_row(), self.fixture.claim_row(claim_id=second)]
        )
        self.write_index()
        added_head = self.commit("add claim")
        added_report = self.report(head=added_head)
        self.assertIn("Added claims:** 1", added_report)
        self.assertIn(second, added_report)

        self.fixture.review(claims=[self.fixture.claim_row(claim_id=second)])
        self.write_index()
        removed_head = self.commit("remove claim")
        removed_report = self.report(baseline=added_head, head=removed_head)
        self.assertIn("Removed claims:** 1", removed_report)
        self.assertIn("historical difference only", removed_report)

    def test_changed_review_authority_and_disposition(self) -> None:
        self.fixture.review(
            authority="working-canon",
            claims=[self.fixture.claim_row(disposition="update")],
        )
        self.write_index()
        head = self.commit("change indexed authority")
        report = self.report(head=head)
        self.assertIn("review_authority:", report)
        self.assertIn("disposition:", report)
        self.assertIn("working-canon", report)

    def test_changed_supersession_relationships(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[self.fixture.claim_row(), self.fixture.claim_row(claim_id=second)]
        )
        self.write_index()
        before = self.commit("two claims")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(),
                self.fixture.claim_row(claim_id=second, supersedes=CLAIM_ID),
            ]
        )
        self.write_index()
        after = self.commit("add supersession")
        report = self.report(baseline=before, head=after)
        self.assertIn("supersedes: added", report)
        self.assertIn("superseded_by: added", report)

    def test_changed_exceptional_record_status(self) -> None:
        self.fixture.development_record(status="open")
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="defer",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        self.write_index()
        before = self.commit("open question")
        self.fixture.development_record(status="resolved")
        self.write_index()
        after = self.commit("resolve question")
        report = self.report(baseline=before, head=after)
        self.assertIn("exceptional-record status", report)
        self.assertIn('"open"', report)
        self.assertIn('"resolved"', report)

    def test_output_is_deterministic(self) -> None:
        self.fixture.write("scripts/tool.py", "print('stable')\n")
        head = self.commit("tooling")
        self.assertEqual(self.report(head=head), self.report(head=head))

    def test_windows_path_handling(self) -> None:
        self.assertEqual(
            "review",
            classify_path("development\\intake-reviews\\example-review.md"),
        )
        self.assertEqual("workflow", classify_path(".github\\workflows\\check.yml"))

    def test_utf8_content_is_preserved(self) -> None:
        second = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            claims=[
                self.fixture.claim_row(),
                self.fixture.claim_row(
                    claim_id=second, summary="Café authority — navigation only."
                ),
            ]
        )
        self.write_index()
        head = self.commit("utf8 claim")
        self.assertIn("Café authority — navigation only.", self.report(head=head))

    def test_historical_index_is_read_from_commit(self) -> None:
        self.fixture.write("references/change.md", "# Historical\n")
        head = self.commit("historical range")
        (self.fixture.root / "development/indexes/claim-index.json").unlink()
        report = self.report(head=head)
        self.assertIn("Unchanged claims:** 1", report)

    def test_schema_added_empty_lifecycle_field_is_explicit(self) -> None:
        data = build_index(self.fixture.root)
        data["claims"][0].pop("supersedes")
        self.fixture.write(
            "development/indexes/claim-index.json",
            json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        )
        before = self.commit("historical schema")
        self.write_index()
        after = self.commit("current schema")
        report = self.report(baseline=before, head=after)
        self.assertIn("supersedes: <missing> -> []", report)

    def test_missing_historical_index_fails(self) -> None:
        (self.fixture.root / "development/indexes/claim-index.json").unlink()
        missing = self.commit("remove index")
        with self.assertRaisesRegex(AuditContextError, "Required historical data"):
            self.report(baseline=missing, head=missing)

    def test_empty_diff_is_reported(self) -> None:
        report = self.report(head=self.baseline)
        self.assertIn("### Canon\n\n- None.", report)
        self.assertIn("Changed claims:** 0", report)

    def test_tooling_only_diff_is_classified_without_semantic_verdict(self) -> None:
        self.fixture.write("scripts/tool.py", "print('tooling only')\n")
        head = self.commit("tooling only")
        report = self.report(head=head)
        self.assertIn("`A` `scripts/tool.py`", report)
        self.assertIn("No canon files changed", report)
        self.assertNotIn("canon is coherent", report.lower())

    def test_canon_change_surfaces_unchanged_dependent_backlink(self) -> None:
        self.fixture.write(
            "story/dependent.md",
            "# Dependent\n\n[Example](../canon/places/example-place.md)\n",
        )
        before = self.commit("add dependent")
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8") + "Changed administrative wording.\n",
            encoding="utf-8",
        )
        after = self.commit("change canon")
        report = self.report(baseline=before, head=after)
        self.assertIn("story/dependent.md` -> `canon/places/example-place.md`", report)
        self.assertIn("source file unchanged", report)
        self.assertIn("unchanged file can be invalidated", report)

    def test_output_states_navigation_only_and_semantic_limitations(self) -> None:
        report = self.report(head=self.baseline)
        self.assertIn("Navigation-only change context", report)
        self.assertIn("does not establish canon coherence", report)
        self.assertIn("require semantic review", report)


if __name__ == "__main__":
    unittest.main()
