from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_repository import Validator
from fixtures import CASE_ID, CLAIM_ID, SUBMISSION_ID, FixtureRepository


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository().build_valid()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def validate(self, base_ref: str | None = None) -> list[str]:
        validator = Validator(base_ref, self.fixture.root)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            validator.run()
        return validator.errors

    def assert_error(self, text: str, base_ref: str | None = None) -> None:
        self.assertTrue(
            any(text in error for error in self.validate(base_ref)),
            f"expected error containing {text!r}",
        )

    def test_minimal_fixture_passes(self) -> None:
        self.assertEqual([], self.validate())

    def test_valid_relative_link(self) -> None:
        self.fixture.write("story/target.md", "# Target\n")
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8") + "[Target](../../story/target.md)\n",
            encoding="utf-8",
        )
        self.assertEqual([], self.validate())

    def test_missing_link_target(self) -> None:
        self.fixture.write("story/link.md", "[Missing](missing.md)\n")
        self.assert_error("missing link target")

    def test_valid_heading_anchor(self) -> None:
        self.fixture.write("story/target.md", "# Target\n\n## Exact Heading\n")
        self.fixture.write("story/link.md", "[Heading](target.md#exact-heading)\n")
        self.assertEqual([], self.validate())

    def test_missing_heading_anchor(self) -> None:
        self.fixture.write("story/target.md", "# Target\n")
        self.fixture.write("story/link.md", "[Heading](target.md#missing)\n")
        self.assert_error("missing heading anchor")

    def test_external_url_fragment_is_excluded(self) -> None:
        self.fixture.write("story/link.md", "[External](https://example.invalid/page#part)\n")
        self.assertEqual([], self.validate())

    def test_mailto_link_is_excluded(self) -> None:
        self.fixture.write("story/link.md", "[Mail](mailto:test@example.invalid)\n")
        self.assertEqual([], self.validate())

    def test_todo_placeholder_link_is_currently_excluded(self) -> None:
        self.fixture.write("story/link.md", "[Pending](TODO-missing.md)\n")
        self.assertEqual([], self.validate())

    def test_windows_style_relative_link_is_normalized(self) -> None:
        self.fixture.write("story/nested/target.md", "# Target\n")
        self.fixture.write("story/link.md", "[Target](nested\\target.md)\n")
        self.assertEqual([], self.validate())

    def test_posix_style_relative_link_is_supported(self) -> None:
        self.fixture.write("story/nested/target.md", "# Target\n")
        self.fixture.write("story/link.md", "[Target](nested/target.md)\n")
        self.assertEqual([], self.validate())

    def test_relative_link_cannot_escape_repository(self) -> None:
        self.fixture.write("story/link.md", "[Escape](../../outside.md)\n")
        self.assert_error("link escapes repository")

    def test_duplicate_headings_receive_numbered_anchors(self) -> None:
        self.fixture.write("story/target.md", "# Target\n\n## Repeat\n\n## Repeat\n")
        self.fixture.write("story/link.md", "[Second](target.md#repeat-1)\n")
        self.assertEqual([], self.validate())

    def test_non_ascii_heading_anchor(self) -> None:
        self.fixture.write("story/target.md", "# Café Context\n")
        self.fixture.write("story/link.md", "[Café](target.md#café-context)\n")
        self.assertEqual([], self.validate())

    def test_canon_page_requires_front_matter(self) -> None:
        self.fixture.write("canon/places/no-metadata.md", "# No Metadata\n")
        self.assert_error("lacks valid YAML front matter")

    def test_canon_page_requires_all_fields(self) -> None:
        path = self.fixture.root / "canon/places/example-place.md"
        path.write_text(path.read_text(encoding="utf-8").replace("provenance: []\n", ""), encoding="utf-8")
        self.assert_error("missing front matter fields: provenance")

    def test_invalid_canon_status(self) -> None:
        self.fixture.canon_page(status="finished")
        self.assert_error("invalid canon status")

    def test_invalid_canon_level(self) -> None:
        self.fixture.canon_page(canon_level="official")
        self.assert_error("invalid canon level")

    def test_inline_empty_front_matter_lists_are_valid(self) -> None:
        self.assertEqual([], self.validate())

    def test_block_front_matter_lists_are_valid(self) -> None:
        self.fixture.canon_page(
            list_fields=(
                "aliases:\n  - Example Alias\ntags:\n  - synthetic\nrelated: []\nprovenance: []"
            )
        )
        self.assertEqual([], self.validate())

    def test_inline_nonempty_front_matter_lists_are_valid(self) -> None:
        self.fixture.canon_page(
            list_fields=(
                'aliases: ["Example Alias"]\ntags: [synthetic]\nrelated: []\nprovenance: []'
            )
        )
        self.assertEqual([], self.validate())

    def test_malformed_front_matter_list_is_rejected(self) -> None:
        self.fixture.canon_page(
            list_fields="aliases: Example Alias\ntags: []\nrelated: []\nprovenance: []"
        )
        self.assert_error("front matter field must be a list: aliases")

    def test_canon_readme_is_exempt_from_front_matter(self) -> None:
        self.fixture.write("canon/README.md", "# Canon\n")
        self.assertEqual([], self.validate())

    def test_characterizes_deprecated_page_without_structured_replacement(self) -> None:
        self.fixture.canon_page(status="deprecated")
        self.assertEqual([], self.validate())

    def test_submission_without_review_fails(self) -> None:
        (self.fixture.root / "development/intake-reviews/example-review.md").unlink()
        self.assert_error("no intake review found")

    def test_review_without_submission_fails(self) -> None:
        (self.fixture.root / "intake/submissions/example-submission.md").unlink()
        self.assert_error("review references unknown submission_id")

    def test_mismatched_submission_id_fails(self) -> None:
        self.fixture.submission(submission_id="CASE-2000-01-01-OTHER-S01")
        self.assert_error("submission_id does not belong to case")

    def test_duplicate_submission_id_fails(self) -> None:
        self.fixture.submission(relative="intake/submissions/duplicate.md")
        self.assert_error("duplicate submission_id")

    def test_claim_id_must_belong_to_review_submission(self) -> None:
        wrong = "CASE-2000-01-01-OTHER-S01-C001"
        self.fixture.review(claims=[self.fixture.claim_row(claim_id=wrong)])
        self.assert_error("claim ID does not belong to review submission")

    def test_duplicate_claim_id_within_review_fails(self) -> None:
        row = self.fixture.claim_row()
        self.fixture.review(claims=[row, row])
        self.assert_error("duplicate claim ID")

    def test_duplicate_claim_id_across_reviews_fails(self) -> None:
        self.fixture.review(relative="development/intake-reviews/duplicate-review.md")
        self.assert_error("duplicate claim ID also used by")

    def test_all_controlled_dispositions_are_recognized(self) -> None:
        rows = []
        for index, disposition in enumerate(
            ("create", "update", "no-change", "link-only", "out-of-scope"), start=1
        ):
            rows.append(
                self.fixture.claim_row(
                    claim_id=f"{SUBMISSION_ID}-C{index:03d}", disposition=disposition
                )
            )
        self.fixture.review(claims=rows)
        self.assertEqual([], self.validate())

    def test_invalid_disposition_fails(self) -> None:
        self.fixture.review(claims=[self.fixture.claim_row(disposition="accept")])
        self.assert_error("expected one controlled disposition")

    def test_exceptional_dispositions_require_development_record(self) -> None:
        for disposition in ("defer", "conflict", "retire"):
            with self.subTest(disposition=disposition):
                self.fixture.review(claims=[self.fixture.claim_row(disposition=disposition)])
                self.assert_error(f"{disposition} must link to a development record")

    def test_exceptional_dispositions_accept_linked_development_record(self) -> None:
        records = {
            "defer": "development/open-questions/example-question.md",
            "conflict": "development/contradictions/example-conflict.md",
            "retire": "development/retired/example-retired.md",
        }
        for disposition, record in records.items():
            with self.subTest(disposition=disposition):
                self.fixture.development_record(record)
                relative = Path(record).relative_to("development").as_posix()
                self.fixture.review(
                    claims=[
                        self.fixture.claim_row(
                            disposition=disposition,
                            target=f"[Example](../{relative})",
                        )
                    ]
                )
                self.assertEqual([], self.validate())

    def test_conflict_cannot_point_to_open_question(self) -> None:
        self.fixture.development_record()
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="conflict",
                    target="[Question](../open-questions/example-question.md)",
                )
            ]
        )
        self.assert_error("conflict must link to a development record under contradictions")

    def test_incomplete_claim_row_fails_with_column_count(self) -> None:
        self.fixture.review(claims=[f"| {CLAIM_ID} | incomplete |"])
        self.assert_error("expected 9 claim columns")

    def test_valid_explicit_confirmation_basis(self) -> None:
        self.fixture.submission(completion_basis="explicit-confirmation", include_marker=False)
        self.assertEqual([], self.validate())

    def test_valid_complete_attachment_basis(self) -> None:
        self.fixture.submission(completion_basis="complete-attachment", include_marker=False)
        self.assertEqual([], self.validate())

    def test_missing_completion_basis_fails(self) -> None:
        self.fixture.submission(completion_basis=None)
        self.assert_error("invalid or missing completion_basis")

    def test_invalid_completion_basis_fails(self) -> None:
        self.fixture.submission(completion_basis="assumed")
        self.assert_error("invalid or missing completion_basis")

    def test_end_marker_basis_requires_literal_marker(self) -> None:
        self.fixture.submission(include_marker=False)
        self.assert_error("requires <!-- END OF SEED -->")

    def test_marker_mentioned_only_in_prose_does_not_satisfy_literal_rule(self) -> None:
        self.fixture.submission(
            include_marker=False,
            body="# Example\n\nThe phrase END OF SEED is discussed administratively.",
        )
        self.assert_error("requires <!-- END OF SEED -->")

    def test_historical_submission_without_completeness_metadata_is_accepted(self) -> None:
        self.fixture.submission(
            completion_basis=None, transmission_status=None, include_marker=False
        )
        self.fixture.review(include_impact=False, lore_review=None)
        self.assertEqual([], self.validate())

    def test_new_review_requires_lore_review_classification(self) -> None:
        self.fixture.review(lore_review=None)
        self.assert_error("invalid or missing lore_review")

    def test_process_review_does_not_require_audit_baseline_fields(self) -> None:
        self.fixture.review(lore_review="false")
        self.assertEqual([], self.validate())

    def test_canon_authority_requires_lore_review_true(self) -> None:
        self.fixture.review(authority="establish-canon", lore_review="false")
        self.assert_error("requires lore_review: true")

    def test_valid_lore_review_audit_evaluation_passes(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        self.assertEqual([], self.validate())

    def test_lore_review_requires_audit_baseline_fields(self) -> None:
        self.fixture.review(authority="establish-canon", lore_review="true")
        self.assert_error("missing audit baseline fields")
        self.assert_error("missing audit baseline list fields")

    def test_semantic_baseline_requires_full_commit_hash(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            f"semantic_audit_baseline: {'0' * 40}",
            "semantic_audit_baseline: 027d0e3",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("must be a full commit hash or 'none'")

    def test_audit_range_must_start_at_baseline(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            f"{'0' * 40}..{'1' * 40}", f"{'2' * 40}..{'1' * 40}"
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("must start at semantic_audit_baseline")

    def test_missing_baseline_requires_fresh_tier_3(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            f"semantic_audit_baseline: {'0' * 40}",
            "semantic_audit_baseline: none",
        ).replace(
            f'audit_git_range: "{"0" * 40}..{"1" * 40}"',
            "audit_git_range: fresh-tier-3-required",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("deterministic Tier 3 triggers are missing: missing-baseline")

    def test_ten_completed_cases_requires_tier_3_trigger(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "completed_canon_cases_since_tier_three: 0",
            "completed_canon_cases_since_tier_three: 10",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error(
            "deterministic Tier 3 triggers are missing: ten-completed-canon-cases"
        )

    def test_unknown_case_count_requires_unreliable_baseline_trigger(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "completed_canon_cases_since_tier_three: 0",
            "completed_canon_cases_since_tier_three: unknown",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error(
            "deterministic Tier 3 triggers are missing: unreliable-baseline"
        )

    def test_three_domains_requires_tier_3_trigger(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "domains:\n  - administration",
            "domains:\n  - administration\n  - history\n  - places",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error(
            "deterministic Tier 3 triggers are missing: three-or-more-semantic-domains"
        )

    def test_active_tier_3_trigger_requires_tier_3_required(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "tier_three_trigger_active: no", "tier_three_trigger_active: yes"
        )
        text = text.replace(
            "tier_three_triggers: []",
            "tier_three_triggers:\n  - tagged-canon-snapshot",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("active Tier 3 trigger requires consistency_tier_required: tier-3")

    def test_complete_tier_3_review_requires_tier_3_performed(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("consistency_tier_required: tier-2", "consistency_tier_required: tier-3")
        text = text.replace(
            "tier_three_trigger_active: no", "tier_three_trigger_active: yes"
        )
        text = text.replace(
            "tier_three_triggers: []",
            "tier_three_triggers:\n  - tagged-canon-snapshot",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("must record consistency_tier_performed: tier-3")

    def test_prior_relationships_require_recorded_results(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "prior_audited_relationships: []",
            "prior_audited_relationships:\n  - AUDIT-V01",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("prior audited relationships lack recorded results: AUDIT-V01")

    def test_audit_results_must_name_considered_relationships(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "audit_results_carried_forward: []",
            "audit_results_carried_forward:\n  - AUDIT-V01",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("audit results name unconsidered relationships: AUDIT-V01")

    def test_complete_lore_review_cannot_leave_audit_fields_pending(self) -> None:
        self.fixture.review(
            authority="establish-canon", lore_review="true", include_audit=True
        )
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "incremental_context_generated: yes",
            "incremental_context_generated: pending",
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("complete lore review has pending audit fields")

    def test_missing_impact_manifest_field_fails(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("search_terms:\n  - synthetic\n", "")
        path.write_text(text, encoding="utf-8")
        self.assert_error("missing impact manifest fields: search_terms")

    def test_empty_impact_manifest_field_fails(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "search_terms:\n  - synthetic\n", "search_terms:\n"
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("impact manifest field must not be empty: search_terms")

    def test_invalid_subject_fails(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace("example-place", "Example Place", 1)
        path.write_text(text, encoding="utf-8")
        self.assert_error("invalid subject ID")

    def test_invalid_domain_fails(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace("  - administration", "  - unknown")
        path.write_text(text, encoding="utf-8")
        self.assert_error("invalid consistency domain")

    def test_missing_authoritative_target_fails(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "canon/places/example-place.md", "canon/places/missing.md"
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("missing authoritative target")

    def test_authoritative_target_cannot_escape_repository(self) -> None:
        path = self.fixture.root / "development/intake-reviews/example-review.md"
        text = path.read_text(encoding="utf-8").replace(
            "canon/places/example-place.md", "../outside.md"
        )
        path.write_text(text, encoding="utf-8")
        self.assert_error("authoritative target escapes repository")

    def test_unchanged_merged_submission_passes(self) -> None:
        base = self.fixture.initialize_git()
        self.assertEqual([], self.validate(base))

    def test_modified_merged_submission_fails(self) -> None:
        base = self.fixture.initialize_git()
        path = self.fixture.root / "intake/submissions/example-submission.md"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        self.assert_error("merged submissions are immutable", base)

    def test_whitespace_only_submission_modification_fails(self) -> None:
        base = self.fixture.initialize_git()
        path = self.fixture.root / "intake/submissions/example-submission.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        self.assert_error("merged submissions are immutable", base)

    def test_new_submission_is_not_an_immutability_violation(self) -> None:
        base = self.fixture.initialize_git()
        second_case = "CASE-2000-01-02-EXAMPLE"
        second_submission = f"{second_case}-S01"
        self.fixture.submission(
            relative="intake/submissions/new.md",
            case_id=second_case,
            submission_id=second_submission,
        )
        self.fixture.review(
            relative="development/intake-reviews/new-review.md",
            case_id=second_case,
            submission_id=second_submission,
            claims=[
                self.fixture.claim_row(claim_id=f"{second_submission}-C001")
            ],
        )
        self.assertEqual([], self.validate(base))

    def test_deleted_historical_submission_fails(self) -> None:
        base = self.fixture.initialize_git()
        (self.fixture.root / "intake/submissions/example-submission.md").unlink()
        self.assert_error("merged submissions are immutable", base)

    def test_renamed_historical_submission_fails(self) -> None:
        base = self.fixture.initialize_git()
        source = self.fixture.root / "intake/submissions/example-submission.md"
        source.rename(source.with_name("renamed-submission.md"))
        self.assert_error("merged submissions are immutable", base)

    def test_invalid_comparison_ref_reports_validation_error(self) -> None:
        self.fixture.initialize_git()
        self.assert_error("invalid comparison ref", "missing-ref")


if __name__ == "__main__":
    unittest.main()
