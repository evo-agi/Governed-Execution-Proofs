from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.check_proof_docs import parse_simple_yaml, validate_summary


REPO_ROOT = Path(__file__).resolve().parents[1]
PROOF_SUMMARY_SCHEMA = REPO_ROOT / "schemas" / "proof-summary.schema.json"
VALIDATION_RECORD_SCHEMA = REPO_ROOT / "schemas" / "validation-record.schema.json"


def validation_record_schema() -> dict[str, object]:
    return json.loads(VALIDATION_RECORD_SCHEMA.read_text(encoding="utf-8"))


def proof_summary_schema() -> dict[str, object]:
    return json.loads(PROOF_SUMMARY_SCHEMA.read_text(encoding="utf-8"))


def proof_summary_errors(summary: dict[str, object]) -> list[str]:
    validator = Draft202012Validator(proof_summary_schema())
    return sorted(error.message for error in validator.iter_errors(summary))


def validation_record_errors(record: dict[str, object]) -> list[str]:
    validator = Draft202012Validator(validation_record_schema())
    return sorted(error.message for error in validator.iter_errors(record))


def base_codex_deterministic_pass_record() -> dict[str, object]:
    return {
        "validation_id": "phase-c-deterministic-2026-05-27",
        "validation_type": "codex_reported_deterministic",
        "validation_status": "codex_reported_deterministic_passed",
        "date": "2026-05-27",
        "baseline_commit": "abcdef0",
        "module_ids": [
            "example-proof",
        ],
        "commands_run_summary": [
            "python3 -m pytest reported local proof-tooling checks only",
        ],
        "claims_supported": [
            "local proof-tooling checks completed under the recorded scope",
        ],
        "claims_not_supported": [
            "independent inspection",
        ],
        "artifact_classes": [
            {
                "class": "pytest summary",
                "classification": "diagnostic summary only",
                "raw_committed": False,
            }
        ],
        "raw_artifacts_committed": False,
        "independent_audit": False,
        "redaction_review": {
            "status": "reviewed",
            "raw_payloads_reviewed": False,
            "sensitive_payloads_committed": False,
        },
        "live_host_contact": False,
        "support_bundle_generated": False,
    }


def test_proof_summary_schema_requires_governance_fields() -> None:
    schema = json.loads(PROOF_SUMMARY_SCHEMA.read_text(encoding="utf-8"))
    required = set(schema["required"])

    assert {
        "schema_version",
        "scenario_id",
        "proof_mode",
        "source_material",
        "id_classification",
        "validation_status",
        "claims_supported",
        "claims_not_supported",
        "excluded_artifact_classes",
    } <= required
    assert schema["properties"]["validation_status"]["enum"] == ["not_run"]


def test_proof_summary_schema_rejects_non_static_statuses() -> None:
    summary = {
        "schema_version": "governed-execution-proof-summary.v1",
        "scenario_id": "example-proof",
        "proof_mode": "static_example",
        "source_material": "static_example_not_runtime_output",
        "id_classification": "synthetic_example",
        "validation_status": "codex_reported_live",
        "claims_supported": [
            "authored proof package shape is explicit",
        ],
        "claims_not_supported": [
            "runtime truth",
        ],
        "excluded_artifact_classes": [
            ".out contents",
        ],
        "non_authority_labels": {
            "proof_summary": "static_example_only",
        },
    }

    errors = proof_summary_errors(summary)
    assert errors
    assert any("'codex_reported_live' is not one of" in error for error in errors)


def test_validation_record_schema_requires_boundary_booleans() -> None:
    schema = validation_record_schema()
    required = set(schema["required"])

    assert {
        "validation_id",
        "validation_type",
        "validation_status",
        "date",
        "baseline_commit",
        "module_ids",
        "commands_run_summary",
        "claims_supported",
        "claims_not_supported",
        "artifact_classes",
        "raw_artifacts_committed",
        "independent_audit",
        "redaction_review",
        "live_host_contact",
        "support_bundle_generated",
    } <= required
    for field in (
        "raw_artifacts_committed",
        "independent_audit",
        "live_host_contact",
        "support_bundle_generated",
    ):
        assert schema["properties"][field]["type"] == "boolean"


def test_validation_record_schema_rejects_generic_passed_status() -> None:
    record = base_codex_deterministic_pass_record()
    record["validation_status"] = "passed"

    errors = validation_record_errors(record)
    assert errors
    assert any("'passed' is not one of" in error for error in errors)


def test_validation_record_schema_accepts_scoped_codex_pass_with_required_context() -> None:
    record = base_codex_deterministic_pass_record()

    assert validation_record_errors(record) == []


def test_validation_record_schema_rejects_scoped_codex_pass_without_context() -> None:
    required_context_fields = (
        "commands_run_summary",
        "claims_not_supported",
        "artifact_classes",
        "independent_audit",
        "redaction_review",
    )
    for field in required_context_fields:
        record = base_codex_deterministic_pass_record()
        record.pop(field)

        errors = validation_record_errors(record)
        assert errors, field

    for field in ("commands_run_summary", "claims_supported", "artifact_classes"):
        record = base_codex_deterministic_pass_record()
        record[field] = []

        errors = validation_record_errors(record)
        assert errors, field


def test_validation_record_schema_rejects_codex_record_claiming_independent_audit() -> None:
    record = deepcopy(base_codex_deterministic_pass_record())
    record["independent_audit"] = True

    errors = validation_record_errors(record)
    assert errors
    assert any("False was expected" in error for error in errors)


def test_current_static_examples_match_summary_schema_shape() -> None:
    for summary_path in sorted((REPO_ROOT / "proofs").glob("*/proof-summary.example.yaml")):
        text = summary_path.read_text(encoding="utf-8")
        data = parse_simple_yaml(text)
        diagnostics = validate_summary(summary_path.parent, data, text)
        assert diagnostics == []
