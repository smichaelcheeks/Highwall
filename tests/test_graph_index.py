from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_graph_index import render
from graph_common import GraphValidationError, build_graph_data
from fixtures import FixtureRepository
from fixtures import CLAIM_ID, SUBMISSION_ID


class GraphIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = FixtureRepository().build_valid()

    def tearDown(self) -> None:
        self.fixture.cleanup()

    def relationship_page(
        self,
        *,
        relationship_id: str = "relationship-example-related-to-second",
        relationship_type: str = "related-to",
        source: str = "entity-example-place",
        target: str = "entity-second-place",
        provenance: str = (
            '      - "../../development/intake-reviews/example-review.md"'
        ),
    ) -> None:
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        relationship = (
            "relationships:\n"
            f"  - relationship_id: {relationship_id}\n"
            f"    relationship_type: {relationship_type}\n"
            f"    source: {source}\n"
            f"    target: {target}\n"
            "    provenance:\n"
            f"{provenance}\n"
        )
        page.write_text(
            text.replace("relationships: []\n", relationship), encoding="utf-8"
        )

    def second_entity(self, entity_id: str = "entity-second-place") -> None:
        self.fixture.canon_page(
            "canon/places/second-place.md", title="Second Place"
        )
        page = self.fixture.root / "canon/places/second-place.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "entity-example-place", entity_id
            ),
            encoding="utf-8",
        )

    def test_builds_navigation_only_graph(self) -> None:
        self.second_entity()
        self.relationship_page()
        graph = build_graph_data(self.fixture.root)
        self.assertEqual(2, graph["schema_version"])
        self.assertEqual("navigation-only", graph["authority"])
        self.assertEqual(2, len(graph["entities"]))
        self.assertEqual(1, len(graph["relationships"]))

    def test_render_is_deterministic(self) -> None:
        self.second_entity()
        self.relationship_page()
        first = render(build_graph_data(self.fixture.root))
        second = render(build_graph_data(self.fixture.root))
        self.assertEqual(first, second)

    def test_duplicate_entity_id_is_rejected(self) -> None:
        self.second_entity("entity-example-place")
        with self.assertRaisesRegex(GraphValidationError, "duplicate entity_id"):
            build_graph_data(self.fixture.root)

    def test_uncontrolled_relationship_type_is_rejected(self) -> None:
        self.second_entity()
        self.relationship_page(relationship_type="invented-type")
        with self.assertRaisesRegex(GraphValidationError, "uncontrolled type"):
            build_graph_data(self.fixture.root)

    def test_duplicate_relationship_id_is_rejected(self) -> None:
        self.second_entity()
        self.relationship_page()
        second = self.fixture.root / "canon/places/second-place.md"
        text = second.read_text(encoding="utf-8")
        duplicate = """relationships:
  - relationship_id: relationship-example-related-to-second
    relationship_type: related-to
    source: entity-second-place
    target: entity-example-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
"""
        second.write_text(
            text.replace("relationships: []\n", duplicate), encoding="utf-8"
        )
        with self.assertRaisesRegex(GraphValidationError, "duplicate relationship_id"):
            build_graph_data(self.fixture.root)

    def test_unsupported_relationship_field_is_rejected(self) -> None:
        self.second_entity()
        self.relationship_page()
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "    source: entity-example-place\n",
                "    source: entity-example-place\n    confidence: certain\n",
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "unsupported relationship field"):
            build_graph_data(self.fixture.root)

    def test_unresolved_endpoint_is_rejected(self) -> None:
        self.relationship_page(target="entity-missing")
        with self.assertRaisesRegex(GraphValidationError, "unresolved target"):
            build_graph_data(self.fixture.root)

    def test_relationship_requires_provenance(self) -> None:
        self.second_entity()
        self.relationship_page(provenance="")
        with self.assertRaisesRegex(GraphValidationError, "has no provenance"):
            build_graph_data(self.fixture.root)

    def test_relationship_can_address_relationship(self) -> None:
        self.second_entity()
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        relationships = """relationships:
  - relationship_id: relationship-example-related-to-second
    relationship_type: related-to
    source: entity-example-place
    target: entity-second-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
  - relationship_id: relationship-second-related-to-first-relationship
    relationship_type: related-to
    source: entity-example-place
    target: relationship-example-related-to-second
    provenance:
      - "../../development/intake-reviews/example-review.md"
"""
        page.write_text(
            text.replace("relationships: []\n", relationships), encoding="utf-8"
        )
        graph = build_graph_data(self.fixture.root)
        self.assertEqual(2, len(graph["relationships"]))

    def test_explicit_related_to_marks_legacy_link_migrated(self) -> None:
        self.second_entity()
        self.relationship_page()
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "related: []", 'related:\n  - "second-place.md"'
            ),
            encoding="utf-8",
        )
        graph = build_graph_data(self.fixture.root)
        self.assertEqual([], graph["unmigrated_related_links"])

    def test_duplicate_symmetric_pair_with_distinct_ids_is_rejected(self) -> None:
        self.second_entity()
        self.relationship_page()
        second = self.fixture.root / "canon/places/second-place.md"
        text = second.read_text(encoding="utf-8")
        duplicate = """relationships:
  - relationship_id: relationship-second-related-to-example
    relationship_type: related-to
    source: entity-second-place
    target: entity-example-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
"""
        second.write_text(text.replace("relationships: []\n", duplicate), encoding="utf-8")
        with self.assertRaisesRegex(GraphValidationError, "duplicates symmetric pair"):
            build_graph_data(self.fixture.root)

    def test_registry_forbidden_self_link_is_rejected(self) -> None:
        self.relationship_page(target="entity-example-place")
        with self.assertRaisesRegex(GraphValidationError, "forbidden self-link"):
            build_graph_data(self.fixture.root)

    def test_symmetric_relationship_owner_must_be_endpoint(self) -> None:
        self.second_entity()
        self.fixture.canon_page(
            "canon/places/third-place.md", title="Third Place"
        )
        third = self.fixture.root / "canon/places/third-place.md"
        third.write_text(
            third.read_text(encoding="utf-8").replace(
                "entity-example-place", "entity-third-place"
            ),
            encoding="utf-8",
        )
        self.relationship_page(source="entity-second-place", target="entity-third-place")
        with self.assertRaisesRegex(
            GraphValidationError, "not stored on a symmetric endpoint's authoritative record"
        ):
            build_graph_data(self.fixture.root)

    def test_maintained_claim_has_bounded_content_and_exact_provenance(self) -> None:
        self.fixture.review(
            authority="establish-canon",
            claims=[
                self.fixture.claim_row(
                    disposition="create",
                    target="entity-example-place claim-example-place-exists",
                )
            ],
        )
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        claims = f"""graph_status: active
history_coverage: complete
supersedes: []
superseded_by: []
relationships:
  - relationship_id: relationship-example-related-to-claim
    relationship_type: related-to
    source: entity-example-place
    target: claim-example-place-exists
    provenance:
      - "../../development/intake-reviews/example-review.md"
claims:
  - claim_id: claim-example-place-exists
    content_id: claim-example-place-exists
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
  - history_id: history-example-place-001
    sequence: 1
    object_id: entity-example-place
    change_type: graph-registered
    review_claims:
      - {CLAIM_ID}
    summary: Registered the fixture entity.
  - history_id: history-example-place-claim-001
    sequence: 1
    object_id: claim-example-place-exists
    change_type: claim-added
    review_claims:
      - {CLAIM_ID}
    summary: Added the maintained fixture claim.
"""
        body = """<!-- claim:claim-example-place-exists:start -->
Synthetic maintained assertion.
<!-- claim:claim-example-place-exists:end -->"""
        page.write_text(
            text.replace("relationships: []\n", claims).replace(
                "Synthetic administrative fixture.", body
            ),
            encoding="utf-8",
        )
        graph = build_graph_data(self.fixture.root)
        self.assertEqual(1, len(graph["knowledge_claims"]))
        self.assertEqual(
            "claim-example-place-exists", graph["relationships"][0]["target"]
        )
        self.assertEqual(64, len(graph["knowledge_claims"][0]["content_sha256"]))
        self.assertNotIn(
            "entity-example-place",
            graph["migration_inventory"]["entities_without_history"],
        )

    def test_maintained_claim_requires_exact_content_boundaries(self) -> None:
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        claims = f"""claims:
  - claim_id: claim-example-place-exists
    content_id: claim-example-place-exists
    truth_kind: objective
    authority_level: established
    lifecycle: active
    history_coverage: complete
    about:
      - entity-example-place
    provenance:
      reviews:
        - "../../development/intake-reviews/example-review.md"
      review_claims:
        - {CLAIM_ID}
"""
        page.write_text(
            text.replace("relationships: []\n", "relationships: []\n" + claims),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "matching claim boundary"):
            build_graph_data(self.fixture.root)

    def test_active_claim_rejects_retire_disposition(self) -> None:
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
                        "claim-example-place-retired "
                        "[Retired record](../retired/example-retired.md)"
                    ),
                )
            ],
        )
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        metadata = f"""relationships: []
claims:
  - claim_id: claim-example-place-retired
    content_id: claim-example-place-retired
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
  - history_id: history-example-retired-claim-001
    sequence: 1
    object_id: claim-example-place-retired
    change_type: claim-added
    review_claims:
      - {CLAIM_ID}
    summary: Deliberately misused a retirement decision for an active claim.
"""
        body = """<!-- claim:claim-example-place-retired:start -->
Synthetic assertion that must not be activated by retirement authority.
<!-- claim:claim-example-place-retired:end -->"""
        page.write_text(
            text.replace("relationships: []\n", metadata).replace(
                "Synthetic administrative fixture.", body
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "non-authorizing disposition"):
            build_graph_data(self.fixture.root)

    def test_established_claim_rejects_policy_review_authority(self) -> None:
        self.fixture.review(
            authority="establish-policy",
            claims=[
                self.fixture.claim_row(
                    disposition="create", target="claim-example-place-policy-backed"
                )
            ],
        )
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        metadata = f"""relationships: []
claims:
  - claim_id: claim-example-place-policy-backed
    content_id: claim-example-place-policy-backed
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
  - history_id: history-example-policy-backed-claim-001
    sequence: 1
    object_id: claim-example-place-policy-backed
    change_type: claim-added
    review_claims:
      - {CLAIM_ID}
    summary: Added a deliberately unauthorized fixture claim.
"""
        body = """<!-- claim:claim-example-place-policy-backed:start -->
Synthetic policy-backed assertion.
<!-- claim:claim-example-place-policy-backed:end -->"""
        page.write_text(
            text.replace("relationships: []\n", metadata).replace(
                "Synthetic administrative fixture.", body
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "unauthorized review authority"):
            build_graph_data(self.fixture.root)

    def test_projection_contains_full_intake_and_development_objects(self) -> None:
        self.fixture.development_record(
            "development/decisions/example-decision.md", status="accepted"
        )
        self.fixture.development_record(
            "development/open-questions/example-question.md", status="open"
        )
        graph = build_graph_data(self.fixture.root)
        self.assertIsInstance(graph["intake_claims"], list)
        self.assertEqual("no-change", graph["intake_claims"][0]["disposition"])
        self.assertEqual("Synthetic fixture.", graph["intake_claims"][0]["existing_authority_or_evidence"])
        self.assertEqual("decision", graph["decisions"][0]["record_type"])
        self.assertEqual("open-question", graph["exceptions"][0]["record_type"])
        self.assertEqual(CLAIM_ID, graph["evidence_references"][0]["claim_id"])

    def test_registry_requires_controlled_provenance_policy(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "| `navigation` |", "| `invalid-policy` |"
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "invalid provenance policy"):
            build_graph_data(self.fixture.root)

    def test_semantic_relationship_history_rejects_link_only(self) -> None:
        link_claim_id = f"{SUBMISSION_ID}-C002"
        self.fixture.review(
            authority="establish-canon",
            lore_review="true",
            include_audit=True,
            claims=[
                self.fixture.claim_row(
                    classification="canon",
                    disposition="create",
                    target="relationship-example-located-in-second",
                ),
                self.fixture.claim_row(
                    claim_id=link_claim_id,
                    classification="canon",
                    disposition="link-only",
                    target="relationship-example-located-in-second",
                ),
            ],
        )
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8")
            + "| `located-in` | `directed` | `semantic` | `entity` | `entity` | "
            "`forbidden` | `none` | `semantic-canon` | Synthetic location. |\n",
            encoding="utf-8",
        )
        self.second_entity()
        page = self.fixture.root / "canon/places/example-place.md"
        schema = f"""relationships:
  - relationship_id: relationship-example-located-in-second
    relationship_type: located-in
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
history:
  - history_id: history-example-located-in-second-001
    sequence: 1
    object_id: relationship-example-located-in-second
    change_type: relationship-added
    review_claims:
      - {link_claim_id}
    summary: Deliberately used navigation-only authority for a semantic edge.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(
            GraphValidationError,
            "cites disposition 'link-only' incompatible with 'relationship-added'",
        ):
            build_graph_data(self.fixture.root)

    def test_relationship_pair_can_be_owned_by_shared_object_record(self) -> None:
        self.second_entity()
        self.fixture.canon_page("canon/places/third-place.md", title="Third Place")
        third = self.fixture.root / "canon/places/third-place.md"
        third.write_text(
            third.read_text(encoding="utf-8").replace(
                "entity-example-place", "entity-third-place"
            ),
            encoding="utf-8",
        )
        page = self.fixture.root / "canon/places/example-place.md"
        relationships = """relationships:
  - relationship_id: relationship-example-to-second
    relationship_type: related-to
    source: entity-example-place
    target: entity-second-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
  - relationship_id: relationship-example-to-third
    relationship_type: related-to
    source: entity-example-place
    target: entity-third-place
    provenance:
      - "../../development/intake-reviews/example-review.md"
  - relationship_id: relationship-first-related-to-second-relationship
    relationship_type: related-to
    source: relationship-example-to-second
    target: relationship-example-to-third
    provenance:
      - "../../development/intake-reviews/example-review.md"
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "relationships: []\n", relationships
            ),
            encoding="utf-8",
        )
        graph = build_graph_data(self.fixture.root)
        self.assertEqual(3, len(graph["relationships"]))

    def test_superseded_entity_requires_replacement(self) -> None:
        self.fixture.review(
            claims=[
                self.fixture.claim_row(
                    disposition="update", target="entity-example-place"
                )
            ]
        )
        page = self.fixture.root / "canon/places/example-place.md"
        schema = f"""graph_status: superseded
history_coverage: complete
supersedes: []
superseded_by: []
relationships: []
claims: []
history:
  - history_id: history-example-superseded-entity-001
    sequence: 1
    object_id: entity-example-place
    change_type: superseded
    review_claims:
      - {CLAIM_ID}
    summary: Superseded the fixture entity.
"""
        page.write_text(
            page.read_text(encoding="utf-8").replace("relationships: []\n", schema),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "superseded without a replacement"):
            build_graph_data(self.fixture.root)

    def test_undeclared_claim_boundary_is_rejected(self) -> None:
        page = self.fixture.root / "canon/places/example-place.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "Synthetic administrative fixture.",
                "<!-- claim:claim-undeclared:start -->\n"
                "Text that must remain entity-owned.\n"
                "<!-- claim:claim-undeclared:end -->",
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "undeclared claim boundary"):
            build_graph_data(self.fixture.root)

    def test_nested_claim_boundaries_are_rejected(self) -> None:
        page = self.fixture.root / "canon/places/example-place.md"
        text = page.read_text(encoding="utf-8")
        claims = """claims:
  - claim_id: claim-outer
    content_id: claim-outer
  - claim_id: claim-inner
    content_id: claim-inner
"""
        body = """<!-- claim:claim-outer:start -->
Outer content.
<!-- claim:claim-inner:start -->
Inner content.
<!-- claim:claim-inner:end -->
<!-- claim:claim-outer:end -->"""
        page.write_text(
            text.replace("relationships: []\n", "relationships: []\n" + claims).replace(
                "Synthetic administrative fixture.", body
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "nested claim boundary"):
            build_graph_data(self.fixture.root)

    def test_registry_requires_nonempty_definition(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "Synthetic generic association.", ""
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "empty definition"):
            build_graph_data(self.fixture.root)

    def test_registry_requires_reciprocal_directed_inverse(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8")
            + "| `parent-of` | `directed` | `semantic` | `entity` | `claim` | `forbidden` | `child-of` | `semantic-canon` | Synthetic parent relation. |\n"
            + "| `child-of` | `directed` | `semantic` | `claim` | `entity` | `forbidden` | `related-to` | `semantic-canon` | Synthetic child relation. |\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "inverse is not reciprocal"):
            build_graph_data(self.fixture.root)

    def test_registry_requires_inverse_endpoint_reversal(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8")
            + "| `parent-of` | `directed` | `semantic` | `entity` | `claim` | `forbidden` | `child-of` | `semantic-canon` | Synthetic parent relation. |\n"
            + "| `child-of` | `directed` | `semantic` | `entity` | `claim` | `forbidden` | `parent-of` | `semantic-canon` | Synthetic child relation. |\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "inverse endpoint kinds"):
            build_graph_data(self.fixture.root)

    def test_claim_boundary_malformed_forms_fail_closed(self) -> None:
        cases = (
            (
                "Inline <!-- claim:claim-inline:start --> marker.",
                "malformed claim boundary",
            ),
            (
                "<!-- claim:claim-ended:end -->",
                "end marker before its start",
            ),
            (
                "<!-- claim:claim-first:start -->\nText.\n"
                "<!-- claim:claim-second:end -->",
                "mismatched end marker",
            ),
            (
                "<!-- claim:claim-repeat:start -->\nOne.\n"
                "<!-- claim:claim-repeat:end -->\n"
                "<!-- claim:claim-repeat:start -->\nTwo.\n"
                "<!-- claim:claim-repeat:end -->",
                "duplicate claim boundary",
            ),
        )
        for body, expected in cases:
            with self.subTest(expected=expected):
                fixture = FixtureRepository().build_valid()
                try:
                    page = fixture.root / "canon/places/example-place.md"
                    page.write_text(
                        page.read_text(encoding="utf-8").replace(
                            "Synthetic administrative fixture.", body
                        ),
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(GraphValidationError, expected):
                        build_graph_data(fixture.root)
                finally:
                    fixture.cleanup()

    def test_symmetric_registry_requires_matching_endpoint_kinds(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "`entity, relationship, claim` | `entity, relationship, claim`",
                "`entity` | `claim`",
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "same source and target kinds"):
            build_graph_data(self.fixture.root)

    def test_navigation_registry_requires_navigation_provenance(self) -> None:
        registry = self.fixture.root / "references/relationship-types.md"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "| `navigation` |", "| `administrative` |"
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(GraphValidationError, "requires navigation provenance"):
            build_graph_data(self.fixture.root)


if __name__ == "__main__":
    unittest.main()
