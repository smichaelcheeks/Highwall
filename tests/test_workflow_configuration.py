import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "repository-integrity.yml"


class WorkflowConfigurationTests(unittest.TestCase):
    def test_repository_validation_uses_event_specific_base_sha(self):
        content = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(
            "BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}",
            content,
        )
        self.assertIn(
            'python scripts/validate_repository.py --base-ref "$BASE_SHA"',
            content,
        )


if __name__ == "__main__":
    unittest.main()
