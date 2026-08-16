from __future__ import annotations

import contextlib
import io
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_repository import Validator
from fixtures import CASE_ID, CLAIM_ID, SUBMISSION_ID, FixtureRepository


UPDATE_CLAIM_ID = f"{SUBMISSION_ID}-C002"
RETIRE_CLAIM_ID = f"{SUBMISSION_ID}-C003"


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

    def bind_transition_hashes(self, base_ref: str) -> None:
        """Insert validator-calculated bindings into new fixture history events."""
        expected: dict[str, str] = {}
        for error in self.validate(base_ref):
            match = re.search(
                r"history (history-[a-z0-9-]+) transition_sha256 must equal "
                r"([0-9a-f]{64})",
                error,
            )
            if match:
                expected[match.group(1)] = match.group(2)
        self.assertTrue(expected, "fixture produced no transition hashes to bind")
        remaining = set(expected)
        for path in self.fixture.root.rglob("*.md"):
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
            output: list[str] = []
            current_history = ""
            changed = False
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("- history_id: "):
                    current_history = stripped.partition(":")[2].strip()
                output.append(line)
                if (
                    current_history in expected
                    and stripped.startswith("change_type: ")
                ):
                    newline = "\r\n" if line.endswith("\r\n") else "\n"
                    output.append(
                        f"    transition_sha256: {expected[current_history]}{newline}"
                    )
                    remaining.discard(current_history)
                    current_history = ""
                    changed = True
            if changed:
                path.write_text("".join(output), encoding="utf-8")
        self.assertEqual(set(), remaining)

    def install_schema_v2_objects(self) -> Path:
        relationship_id = "relationship-example-related-to-second"
        maintained_claim_id = "claim-example-place-exists"
        target = f"entity-example-place {relationship_id} {maintained_claim_id}"
        self.fixture.development_record(
            "development/retired/example-retired.md",
            status="retired",
            record_type="retired",
        )
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="canon", disposition="create", target=target
                ),
                self.fixture.claim_row(
                    claim_id=UPDATE_CLAIM_ID,
                    classification="canon",
                    disposition="update",
                    target=target,
                ),
                self.fixture.claim_row(
                    claim_id=RETIRE_CLAIM_ID,
                    classification="canon",
                    disposition="retire",
                    target=(
                        f"{target} "
                        "[Retired record](../retired/example-retired.md)"
                    ),
                ),
            ],
        )
        self.fixture.canon_page("canon/places/second-place.md", title="Second Place")
        second = self.fixture.root / "canon/places/second-place.md"
        second.write_text(
            second.read_text(encoding="utf-8").replace(
                "entity-example-place", "entity-second-place"
            ),
            encoding="utf-8",
        )
        page = self.fixture.root / "canon/places/example-place.md"
        block = f"""graph_status: active
history_coverage: complete
supersedes: []
superseded_by: []
relationships:
  - relationship_id: {relationship_id}
    relationship_type: related-to
    source: entity-example-place
    target: entity-second-place
    graph_status: active
    history_coverage: complete
    supersedes: []
    superseded_by: []
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - {CLAIM_ID}
claims:
  - claim_id: {maintained_claim_id}
    content_id: {maintained_claim_id}
    truth_kind: objective
    authority_level: established
    lifecycle: active
    history_coverage: complete
    about:
      - entity-example-place
    supersedes: []
    superseded_by: []
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - {CLAIM_ID}
history:
  - history_id: history-example-entity-001
    sequence: 1
    object_id: entity-example-place
    change_type: established
    review_claims:
      - {CLAIM_ID}
    summary: Established the fixture entity state.
  - history_id: history-example-relationship-001
    sequence: 1
    object_id: {relationship_id}
    change_type: relationship-added
    review_claims:
      - {CLAIM_ID}
    summary: Added the fixture relationship.
  - history_id: history-example-claim-001
    sequence: 1
    object_id: {maintained_claim_id}
    change_type: claim-added
    review_claims:
      - {CLAIM_ID}
    summary: Added the fixture claim.
"""
        body = """<!-- claim:claim-example-place-exists:start -->
The wall is red.
<!-- claim:claim-example-place-exists:end -->

Entity-owned context remains outside the maintained claim."""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("relationships: []\n", block)
            .replace("Synthetic administrative fixture.", body),
            encoding="utf-8",
        )
        return page

    def install_policy_registered_entity(self) -> Path:
        self.fixture.review(
            authority="establish-policy",
            claims=[
                self.fixture.claim_row(
                    disposition="update", target="entity-example-place"
                )
            ],
        )
        page = self.fixture.root / "canon/places/example-place.md"
        schema = f"""graph_status: active
history_coverage: prospective
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-policy-entity-001
    sequence: 1
    object_id: entity-example-place
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Registered the fixture entity without changing its content.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        return page

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

    def test_changed_entity_requires_schema_v2_lifecycle_and_history(self) -> None:
        baseline = self.fixture.initialize_git()
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "Synthetic administrative fixture.",
                "Synthetic administrative fixture updated.",
            ),
            encoding="utf-8",
        )
        errors = self.validate(baseline)
        self.assertTrue(any("lacks graph_status" in error for error in errors))
        self.assertTrue(any("did not append local history" in error for error in errors))

    def test_published_relationship_endpoints_are_immutable(self) -> None:
        self.fixture.canon_page("canon/places/second-place.md", title="Second Place")
        second = self.fixture.root / "canon/places/second-place.md"
        second.write_text(
            second.read_text(encoding="utf-8").replace(
                "entity-example-place", "entity-second-place"
            ),
            encoding="utf-8",
        )
        self.fixture.canon_page("canon/places/third-place.md", title="Third Place")
        third = self.fixture.root / "canon/places/third-place.md"
        third.write_text(
            third.read_text(encoding="utf-8").replace(
                "entity-example-place", "entity-third-place"
            ),
            encoding="utf-8",
        )
        page = self.fixture.root / "canon/places/example-place.md"
        relationship = """relationships:
  - relationship_id: relationship-example-related-to-second
    relationship_type: related-to
    source: entity-example-place
    target: entity-second-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "relationships: []\n", relationship
            ),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "target: entity-second-place", "target: entity-third-place"
            ),
            encoding="utf-8",
        )
        self.assert_error("changed immutable target", baseline)

    def test_published_history_event_is_append_only(self) -> None:
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="update", target="entity-example-place"
                )
            ]
        )
        page = self.fixture.root / "canon/places/example-place.md"
        history = f"""graph_status: active
history_coverage: complete
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-place-001
    sequence: 1
    object_id: entity-example-place
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Registered the fixture entity.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "relationships: []\n", history
            ),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "Registered the fixture entity.", "Rewrote the fixture history."
            ),
            encoding="utf-8",
        )
        self.assert_error("published history event history-example-place-001 was rewritten", baseline)

    def test_claim_content_change_requires_appended_claim_history(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "The wall is red.", "The wall is blue."
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "changed claim claim-example-place-exists did not append local history",
            baseline,
        )

    def test_claim_content_change_with_compatible_history_passes(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "The wall is red.", "The wall is crimson."
        )
        event = f"""  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: claim-clarified
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Clarified the bounded fixture wording.
"""
        page.write_text(
            text.replace("    summary: Added the fixture claim.\n", "    summary: Added the fixture claim.\n" + event),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_claim_content_change_rejects_generic_history_type(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "The wall is red.", "The wall is crimson."
        )
        event = f"""  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Mislabeled the bounded fixture wording change.
"""
        page.write_text(
            text.replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + event,
            ),
            encoding="utf-8",
        )
        self.assert_error("bounded claim-content change", baseline)

    def test_relationship_lifecycle_change_requires_appended_history(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    graph_status: active\n    history_coverage: complete\n",
                "    graph_status: retired\n    history_coverage: complete\n",
                1,
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "changed relationship relationship-example-related-to-second did not append local history",
            baseline,
        )

    def test_relationship_lifecycle_change_rejects_generic_history_type(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "    graph_status: active\n    history_coverage: complete\n",
            "    graph_status: retired\n    history_coverage: complete\n",
            1,
        )
        event = f"""  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Mislabeled the relationship retirement.
"""
        page.write_text(
            text.replace(
                "    summary: Added the fixture relationship.\n",
                "    summary: Added the fixture relationship.\n" + event,
            ),
            encoding="utf-8",
        )
        self.assert_error("retired lifecycle transition", baseline)

    def test_relationship_retirement_with_retire_disposition_passes(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "    graph_status: active\n    history_coverage: complete\n",
            "    graph_status: retired\n    history_coverage: complete\n",
            1,
        )
        event = f"""  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: retired
    review_claims:
      - {RETIRE_CLAIM_ID}
    summary: Retired the fixture relationship.
"""
        page.write_text(
            text.replace(
                "    summary: Added the fixture relationship.\n",
                "    summary: Added the fixture relationship.\n" + event,
            ),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_entity_prose_change_requires_appended_history(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "Entity-owned context remains", "Changed entity-owned context remains"
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "changed entity entity-example-place did not append local history",
            baseline,
        )

    def test_established_entity_content_rejects_policy_authority(self) -> None:
        page = self.install_policy_registered_entity()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "Synthetic administrative fixture.",
            "Synthetic administrative fixture changed by policy.",
        )
        event = f"""  - history_id: history-example-policy-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately attempted a content change under policy authority.
"""
        page.write_text(
            text.replace(
                "    summary: Registered the fixture entity without changing its content.\n",
                "    summary: Registered the fixture entity without changing its content.\n"
                + event,
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "uses authority 'establish-policy' for entity content change",
            baseline,
        )

    def test_entity_graph_metadata_accepts_policy_authority(self) -> None:
        page = self.install_policy_registered_entity()
        baseline = self.fixture.initialize_git()
        text = page.read_text(encoding="utf-8").replace(
            "history_coverage: prospective", "history_coverage: complete"
        )
        event = f"""  - history_id: history-example-policy-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {CLAIM_ID}
    summary: Completed graph-history coverage without changing entity content.
"""
        page.write_text(
            text.replace(
                "    summary: Registered the fixture entity without changing its content.\n",
                "    summary: Registered the fixture entity without changing its content.\n"
                + event,
            ),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_existing_record_registration_accepts_policy_authority(self) -> None:
        page = self.fixture.write(
            "story/example-story.md",
            "---\n"
            "title: Example Story\n"
            "type: story\n"
            "status: active\n"
            "---\n\n"
            "# Example Story\n\n"
            "Synthetic narrative fixture.\n",
        )
        self.fixture.review(
            authority="establish-policy",
            claims=[
                self.fixture.claim_row(
                    disposition="update", target="entity-example-story"
                )
            ],
        )
        baseline = self.fixture.initialize_git()
        schema = f"""entity_id: entity-example-story
graph_status: active
history_coverage: prospective
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-story-001
    sequence: 1
    object_id: entity-example-story
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Registered the existing story record without changing its content.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "status: active\n", "status: active\n" + schema
            ),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_retired_entity_cannot_be_reactivated(self) -> None:
        self.fixture.development_record(
            "development/retired/example-retired.md",
            status="retired",
            record_type="retired",
        )
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="canon",
                    disposition="retire",
                    target=(
                        "entity-example-place "
                        "[Retired record](../retired/example-retired.md)"
                    ),
                ),
                self.fixture.claim_row(
                    claim_id=UPDATE_CLAIM_ID,
                    classification="canon",
                    disposition="update",
                    target="entity-example-place",
                ),
            ],
        )
        page = self.fixture.root / "canon/places/example-place.md"
        schema = f"""graph_status: retired
history_coverage: complete
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-retired-entity-001
    sequence: 1
    object_id: entity-example-place
    change_type: retired
    review_claims:
      - {CLAIM_ID}
    summary: Retired the fixture entity.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-retired-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Deliberately attempted to reactivate a tombstone.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("graph_status: retired", "graph_status: active", 1)
            .replace(
                "    summary: Retired the fixture entity.\n",
                "    summary: Retired the fixture entity.\n" + event,
            ),
            encoding="utf-8",
        )
        self.assert_error("cannot transition from tombstone lifecycle", baseline)

    def test_owner_path_move_with_move_histories_passes(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        events = f"""  - history_id: history-example-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the owning record.
  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the relationship with its owning record.
  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the claim with its owning record.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + events,
            ),
            encoding="utf-8",
        )
        moved = page.with_name("renamed-example-place.md")
        page.rename(moved)
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_policy_authority_can_record_content_neutral_owner_move(self) -> None:
        page = self.install_schema_v2_objects()
        move_case = "CASE-2000-01-02-MOVE"
        move_submission = f"{move_case}-S01"
        move_claim = f"{move_submission}-C001"
        self.fixture.submission(
            relative="intake/submissions/move-submission.md",
            case_id=move_case,
            submission_id=move_submission,
        )
        self.fixture.review(
            relative="development/intake-reviews/move-review.md",
            submission_relative="intake/submissions/move-submission.md",
            case_id=move_case,
            submission_id=move_submission,
            authority="establish-policy",
            claims=[
                self.fixture.claim_row(
                    claim_id=move_claim,
                    disposition="update",
                    target=(
                        "entity-example-place "
                        "relationship-example-related-to-second "
                        "claim-example-place-exists"
                    ),
                )
            ],
        )
        baseline = self.fixture.initialize_git()
        events = f"""  - history_id: history-example-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: moved
    review_claims:
      - {move_claim}
    summary: Recorded the content-neutral owner move.
  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: moved
    review_claims:
      - {move_claim}
    summary: Moved the relationship with its owner.
  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: moved
    review_claims:
      - {move_claim}
    summary: Moved the claim with its owner.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + events,
            ),
            encoding="utf-8",
        )
        page.rename(page.with_name("renamed-example-place.md"))
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_owner_path_move_rejects_generic_history_types(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        events = f"""  - history_id: history-example-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Mislabeled the entity move.
  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Mislabeled the relationship move.
  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Mislabeled the claim move.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + events,
            ),
            encoding="utf-8",
        )
        page.rename(page.with_name("renamed-example-place.md"))
        self.assert_error("change_type for owner-path move", baseline)

    def test_move_and_content_change_require_both_event_classes(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        events = f"""  - history_id: history-example-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the owning record.
  - history_id: history-example-relationship-002
    sequence: 2
    object_id: relationship-example-related-to-second
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the relationship with its owning record.
  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: moved
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Moved the claim with its owning record.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace(
                "Entity-owned context remains",
                "Changed entity-owned context remains",
            )
            .replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + events,
            ),
            encoding="utf-8",
        )
        page.rename(page.with_name("renamed-example-place.md"))
        self.assert_error("change_type for entity content change", baseline)

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
        self.assert_error(
            "requires <!-- END OF PATCH --> or <!-- END OF STITCH --> or "
            "<!-- END OF SEED -->"
        )

    def test_current_end_of_patch_marker_is_accepted(self) -> None:
        self.fixture.submission(marker="<!-- END OF PATCH -->")
        self.assertEqual([], self.validate())

    def test_legacy_end_of_stitch_marker_remains_accepted(self) -> None:
        self.fixture.submission(marker="<!-- END OF STITCH -->")
        self.assertEqual([], self.validate())

    def test_legacy_end_of_seed_marker_remains_accepted(self) -> None:
        self.fixture.submission(marker="<!-- END OF SEED -->")
        self.assertEqual([], self.validate())

    def test_marker_mentioned_only_in_prose_does_not_satisfy_literal_rule(self) -> None:
        self.fixture.submission(
            include_marker=False,
            body=(
                "# Example\n\nThe phrases END OF PATCH, END OF STITCH, and "
                "END OF SEED are discussed administratively."
            ),
        )
        self.assert_error(
            "requires <!-- END OF PATCH --> or <!-- END OF STITCH --> or "
            "<!-- END OF SEED -->"
        )

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

    def test_working_authority_cannot_downgrade_established_entity(self) -> None:
        page = self.install_policy_registered_entity()
        review = self.fixture.root / "development/intake-reviews/example-review.md"
        review.write_text(
            review.read_text(encoding="utf-8").replace(
                "authority: establish-policy", "authority: working-canon"
            ),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-policy-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately attempted to lower established entity authority.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("canon_level: established", "canon_level: working")
            .replace(
                "    summary: Registered the fixture entity without changing its content.\n",
                "    summary: Registered the fixture entity without changing its content.\n"
                + event,
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "uses authority 'working-canon' for entity content change",
            baseline,
        )

    def test_classify_authority_cannot_downgrade_established_claim(self) -> None:
        claim_id = "claim-example-established"
        page = self.fixture.root / "canon/places/example-place.md"
        self.fixture.development_record(
            "development/retired/example-retired.md",
            status="retired",
            record_type="retired",
        )
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    disposition="create", target=claim_id
                ),
                self.fixture.claim_row(
                    claim_id=UPDATE_CLAIM_ID,
                    disposition="update",
                    target=claim_id,
                ),
                self.fixture.claim_row(
                    claim_id=RETIRE_CLAIM_ID,
                    disposition="retire",
                    target=(
                        f"{claim_id} "
                        "[Retired record](../retired/example-retired.md)"
                    ),
                ),
            ],
        )
        schema = f"""relationships: []
claims:
  - claim_id: {claim_id}
    content_id: {claim_id}
    truth_kind: objective
    authority_level: established
    lifecycle: active
    history_coverage: complete
    about:
      - entity-example-place
    supersedes: []
    superseded_by: []
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - {CLAIM_ID}
history:
  - history_id: history-example-established-claim-001
    sequence: 1
    object_id: {claim_id}
    change_type: claim-added
    review_claims:
      - {CLAIM_ID}
    summary: Added the established fixture claim.
"""
        body = f"""<!-- claim:{claim_id}:start -->
The fixture assertion is established.
<!-- claim:{claim_id}:end -->"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("relationships: []\n", schema)
            .replace("Synthetic administrative fixture.", body),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        review = self.fixture.root / "development/intake-reviews/example-review.md"
        review.write_text(
            review.read_text(encoding="utf-8").replace(
                "authority: establish-canon", "authority: classify"
            ),
            encoding="utf-8",
        )
        events = f"""  - history_id: history-example-established-claim-002
    sequence: 2
    object_id: {claim_id}
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Deliberately attempted to lower established claim authority.
  - history_id: history-example-established-claim-003
    sequence: 3
    object_id: {claim_id}
    change_type: retired
    review_claims:
      - {RETIRE_CLAIM_ID}
    summary: Deliberately attempted to retire established content under classify authority.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("authority_level: established", "authority_level: unresolved")
            .replace("lifecycle: active", "lifecycle: retired")
            .replace(
                "    summary: Added the established fixture claim.\n",
                "    summary: Added the established fixture claim.\n" + events,
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "uses authority 'classify' for claim metadata change",
            baseline,
        )

    def test_new_entity_requires_established_initial_event(self) -> None:
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="canon",
                    disposition="create",
                    target="entity-new-place",
                )
            ],
        )
        baseline = self.fixture.initialize_git()
        page = self.fixture.canon_page(
            "canon/places/new-place.md", title="New Place"
        )
        schema = f"""graph_status: active
history_coverage: prospective
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-new-place-001
    sequence: 1
    object_id: entity-new-place
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately mislabeled a new entity as a registration.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("entity-example-place", "entity-new-place")
            .replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        self.assert_error("initial publication; expected one of ['established']", baseline)

    def test_new_entity_with_established_transition_passes(self) -> None:
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="canon",
                    disposition="create",
                    target="entity-new-place",
                )
            ],
        )
        baseline = self.fixture.initialize_git()
        page = self.fixture.canon_page(
            "canon/places/new-place.md", title="New Place"
        )
        schema = f"""graph_status: active
history_coverage: complete
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-new-place-001
    sequence: 1
    object_id: entity-new-place
    change_type: established
    review_claims:
      - {CLAIM_ID}
    summary: Established the new fixture entity.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("entity-example-place", "entity-new-place")
            .replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_existing_record_requires_graph_registered_initial_event(self) -> None:
        page = self.fixture.write(
            "story/example-story.md",
            "---\ntitle: Example Story\ntype: story\nstatus: active\n---\n\n"
            "# Example Story\n\nSynthetic narrative fixture.\n",
        )
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="story",
                    disposition="create",
                    target="entity-example-story",
                )
            ],
            target="story/example-story.md",
        )
        baseline = self.fixture.initialize_git()
        schema = f"""entity_id: entity-example-story
graph_status: active
history_coverage: prospective
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-story-001
    sequence: 1
    object_id: entity-example-story
    change_type: established
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately mislabeled registration as establishment.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "status: active\n", "status: active\n" + schema
            ),
            encoding="utf-8",
        )
        self.assert_error(
            "schema-v2 registration; expected one of ['graph-registered']",
            baseline,
        )

    def test_establish_canon_can_promote_working_entity(self) -> None:
        page = self.install_policy_registered_entity()
        review = self.fixture.root / "development/intake-reviews/example-review.md"
        review.write_text(
            review.read_text(encoding="utf-8").replace(
                "authority: establish-policy", "authority: establish-canon"
            ),
            encoding="utf-8",
        )
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "canon_level: established", "canon_level: working"
            ),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-policy-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {CLAIM_ID}
    summary: Promoted the working fixture entity to established authority.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("canon_level: working", "canon_level: established")
            .replace(
                "    summary: Registered the fixture entity without changing its content.\n",
                "    summary: Registered the fixture entity without changing its content.\n"
                + event,
            ),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        self.assertEqual([], self.validate(baseline))

    def test_policy_authority_cannot_rewire_established_supersession(self) -> None:
        self.fixture.review(
            authority="establish-policy",
            claims=[
                self.fixture.claim_row(
                    disposition="update",
                    target=(
                        "entity-example-place entity-replacement-one "
                        "entity-replacement-two"
                    ),
                )
            ],
        )

        def schema(
            entity_id: str,
            *,
            graph_status: str,
            supersedes: str = "[]",
            superseded_by: str = "[]",
            history_slug: str,
        ) -> str:
            return f"""graph_status: {graph_status}
history_coverage: prospective
supersedes: {supersedes}
superseded_by: {superseded_by}
relationships: []
claims: []
history:
  - history_id: history-{history_slug}-001
    sequence: 1
    object_id: {entity_id}
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Registered the existing fixture entity.
"""

        old = self.fixture.root / "canon/places/example-place.md"
        old.write_text(
            old.read_text(encoding="utf-8").replace(
                "relationships: []\n",
                schema(
                    "entity-example-place",
                    graph_status="superseded",
                    superseded_by="[entity-replacement-one]",
                    history_slug="example-place",
                ),
            ),
            encoding="utf-8",
        )
        replacement_one = self.fixture.canon_page(
            "canon/places/replacement-one.md", title="Replacement One"
        )
        replacement_one.write_text(
            replacement_one.read_text(encoding="utf-8")
            .replace("entity-example-place", "entity-replacement-one")
            .replace(
                "relationships: []\n",
                schema(
                    "entity-replacement-one",
                    graph_status="active",
                    supersedes="[entity-example-place]",
                    history_slug="replacement-one",
                ),
            ),
            encoding="utf-8",
        )
        replacement_two = self.fixture.canon_page(
            "canon/places/replacement-two.md", title="Replacement Two"
        )
        replacement_two.write_text(
            replacement_two.read_text(encoding="utf-8")
            .replace("entity-example-place", "entity-replacement-two")
            .replace(
                "relationships: []\n",
                schema(
                    "entity-replacement-two",
                    graph_status="active",
                    history_slug="replacement-two",
                ),
            ),
            encoding="utf-8",
        )
        baseline = self.fixture.initialize_git()

        def append_event(path: Path, slug: str, object_id: str) -> None:
            event = f"""  - history_id: history-{slug}-002
    sequence: 2
    object_id: {object_id}
    change_type: metadata-changed
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately attempted to rewire established supersession.
"""
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "    summary: Registered the existing fixture entity.\n",
                    "    summary: Registered the existing fixture entity.\n" + event,
                ),
                encoding="utf-8",
            )

        old.write_text(
            old.read_text(encoding="utf-8").replace(
                "superseded_by: [entity-replacement-one]",
                "superseded_by: [entity-replacement-two]",
            ),
            encoding="utf-8",
        )
        replacement_one.write_text(
            replacement_one.read_text(encoding="utf-8").replace(
                "supersedes: [entity-example-place]", "supersedes: []"
            ),
            encoding="utf-8",
        )
        replacement_two.write_text(
            replacement_two.read_text(encoding="utf-8").replace(
                "supersedes: []", "supersedes: [entity-example-place]"
            ),
            encoding="utf-8",
        )
        append_event(old, "example-place", "entity-example-place")
        append_event(replacement_one, "replacement-one", "entity-replacement-one")
        append_event(replacement_two, "replacement-two", "entity-replacement-two")

        self.assert_error(
            "uses authority 'establish-policy' for entity supersession change",
            baseline,
        )

    def test_changed_object_requires_exact_transition_hash(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: claim-clarified
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Clarified the bounded fixture wording without a transition binding.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("The wall is red.", "The wall is amber.")
            .replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + event,
            ),
            encoding="utf-8",
        )
        self.assert_error("transition_sha256 must equal", baseline)

    def test_incorrect_transition_hash_is_rejected(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-claim-002
    sequence: 2
    object_id: claim-example-place-exists
    change_type: claim-clarified
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Clarified the bounded fixture wording.
"""
        page.write_text(
            page.read_text(encoding="utf-8")
            .replace("The wall is red.", "The wall is amber.")
            .replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + event,
            ),
            encoding="utf-8",
        )
        self.bind_transition_hashes(baseline)
        page.write_text(
            re.sub(
                r"transition_sha256: [0-9a-f]{64}",
                "transition_sha256: " + "0" * 64,
                page.read_text(encoding="utf-8"),
                count=1,
            ),
            encoding="utf-8",
        )
        self.assert_error("transition_sha256 must equal", baseline)

    def test_appended_history_without_state_transition_is_rejected(self) -> None:
        page = self.install_schema_v2_objects()
        baseline = self.fixture.initialize_git()
        event = f"""  - history_id: history-example-entity-002
    sequence: 2
    object_id: entity-example-place
    change_type: metadata-changed
    review_claims:
      - {UPDATE_CLAIM_ID}
    summary: Deliberately recorded an event without changing the object.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    summary: Added the fixture claim.\n",
                "    summary: Added the fixture claim.\n" + event,
            ),
            encoding="utf-8",
        )
        self.assert_error("has no object transition", baseline)


if __name__ == "__main__":
    unittest.main()
