from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_graph_index import render
from graph_common import GraphValidationError, build_graph_data
from fixtures import FixtureRepository


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
        self.assertEqual(1, graph["schema_version"])
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
    source: entity-second-place
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


if __name__ == "__main__":
    unittest.main()
