"""Deterministic synthetic repositories used by the integrity tests."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


CASE_ID = "CASE-2000-01-01-EXAMPLE"
SUBMISSION_ID = f"{CASE_ID}-S01"
CLAIM_ID = f"{SUBMISSION_ID}-C001"


class FixtureRepository:
    """Build the smallest repository tree needed by the production tools."""

    def __init__(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(prefix="highwall-tests-")
        self.root = Path(self._temporary.name).resolve()
        for directory in (
            "canon/places",
            "intake/submissions",
            "development/intake-reviews",
            "development/indexes",
            "development/open-questions",
            "development/contradictions",
            "development/retired",
            "story",
            "design",
        ):
            (self.root / directory).mkdir(parents=True, exist_ok=True)

    def cleanup(self) -> None:
        self._temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def canon_page(
        self,
        relative: str = "canon/places/example-place.md",
        *,
        status: str = "active",
        canon_level: str = "established",
        title: str = "Example Place",
        list_fields: str = "aliases: []\ntags: []\nrelated: []\nprovenance: []",
        body: str = "# Example Place\n\nSynthetic administrative fixture.\n",
    ) -> Path:
        return self.write(
            relative,
            "\n".join(
                [
                    "---",
                    f"title: {title}",
                    "type: place",
                    f"status: {status}",
                    f"canon_level: {canon_level}",
                    list_fields,
                    "---",
                    "",
                    body.rstrip(),
                    "",
                ]
            ),
        )

    def submission(
        self,
        *,
        relative: str = "intake/submissions/example-submission.md",
        case_id: str = CASE_ID,
        submission_id: str = SUBMISSION_ID,
        completion_basis: str | None = "end-marker",
        transmission_status: str | None = "complete",
        include_marker: bool = True,
        marker: str = "<!-- END OF STITCH -->",
        body: str = "# Example Submission\n\nSynthetic administrative input.",
    ) -> Path:
        metadata = [
            "---",
            "title: Example Submission",
            "type: intake-submission",
            f"case_id: {case_id}",
            f"submission_id: {submission_id}",
        ]
        if transmission_status is not None:
            metadata.append(f"transmission_status: {transmission_status}")
        if completion_basis is not None:
            metadata.append(f"completion_basis: {completion_basis}")
        metadata.extend(["---", "", body])
        if include_marker:
            metadata.extend(["", marker])
        metadata.append("")
        return self.write(relative, "\n".join(metadata))

    @staticmethod
    def claim_row(
        *,
        claim_id: str = CLAIM_ID,
        summary: str = "Synthetic administrative claim.",
        classification: str = "administrative",
        authority_basis: str = "explicit",
        supersedes: str = "None",
        evidence: str = "Synthetic fixture.",
        disposition: str = "no-change",
        target: str = "No repository change",
        rationale: str = "The fixture records current behavior.",
    ) -> str:
        return (
            f"| {claim_id} | {summary} | {classification} | `{authority_basis}` | "
            f"{supersedes} | {evidence} | `{disposition}` | {target} | {rationale} |"
        )

    def review(
        self,
        *,
        relative: str = "development/intake-reviews/example-review.md",
        case_id: str = CASE_ID,
        submission_id: str = SUBMISSION_ID,
        authority: str = "establish-policy",
        status: str = "complete",
        lore_review: str | None = "false",
        include_audit: bool = False,
        claims: list[str] | None = None,
        include_impact: bool = True,
        target: str = "canon/places/example-place.md",
    ) -> Path:
        metadata = [
            "---",
            "title: Example Review",
            "type: intake-review",
            f"status: {status}",
            'submission: "../../intake/submissions/example-submission.md"',
            f"case_id: {case_id}",
            f"submission_id: {submission_id}",
            f"authority: {authority}",
        ]
        if lore_review is not None:
            metadata.append(f"lore_review: {lore_review}")
        if include_audit:
            baseline = "0" * 40
            head = "1" * 40
            metadata.extend(
                [
                    f"semantic_audit_baseline: {baseline}",
                    f'audit_git_range: "{baseline}..{head}"',
                    "incremental_context_generated: yes",
                    "consistency_tier_required: tier-2",
                    "consistency_tier_performed: tier-2",
                    "tier_three_trigger_active: no",
                    "completed_canon_cases_since_tier_three: 0",
                    "prior_audited_relationships: []",
                    "audit_results_carried_forward: []",
                    "audit_results_revalidated: []",
                    "audit_results_invalidated: []",
                    "audit_results_widened: []",
                    "tier_three_triggers: []",
                ]
            )
        if include_impact:
            metadata.extend(
                [
                    "subjects:",
                    "  - example-place",
                    "domains:",
                    "  - administration",
                    "search_terms:",
                    "  - synthetic",
                    "authoritative_targets:",
                    f"  - {target}",
                ]
            )
        metadata.extend(
            [
                "---",
                "",
                "# Example Review",
                "",
                "## Claim decisions",
                "",
                "| Claim ID | Submitted claim | Classification | Authority basis | Supersedes | Existing authority or evidence | Disposition | Target or resulting record | Rationale |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        metadata.extend(claims if claims is not None else [self.claim_row()])
        metadata.append("")
        return self.write(relative, "\n".join(metadata))

    def development_record(
        self,
        relative: str = "development/open-questions/example-question.md",
        *,
        status: str = "open",
    ) -> Path:
        return self.write(
            relative,
            f"---\ntitle: Example Question\ntype: open-question\nstatus: {status}\n---\n\n"
            "# Example Question\n\nSynthetic administrative fixture.\n",
        )

    def build_valid(self) -> "FixtureRepository":
        self.canon_page()
        self.submission()
        self.review()
        return self

    def git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            check=check,
            capture_output=True,
            text=True,
        )

    def initialize_git(self) -> str:
        self.git("init", "-q")
        self.git("config", "user.email", "tests@example.invalid")
        self.git("config", "user.name", "Highwall Tests")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "fixture baseline")
        return self.git("rev-parse", "HEAD").stdout.strip()
