from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from tools.scan_redaction_risk import default_scan_files


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPO_ROOT / "tools" / "check_proof_docs.py"
SCANNER = REPO_ROOT / "tools" / "scan_redaction_risk.py"


def run_tool(script: Path, target: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), str(target)],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_minimal_repo(
    tmp_path: Path,
    module_id: str = "example-proof",
    include_public_writing_map: bool = True,
) -> Path:
    repo = tmp_path / "repo"
    module = repo / "proofs" / module_id
    docs = repo / ".docs"
    module.mkdir(parents=True)
    docs.mkdir()

    (docs / "conventions.md").write_text("# Conventions\n\nAuthored docs only.\n", encoding="utf-8")
    (module / "scenario.md").write_text(
        """# Scenario

## Current evidence status

Current proof evidence:

- Static fixture evidence only.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

## Authority boundaries

CP authority, ES evidence/projection, and IM diagnostics remain separate.

## Generated artifacts

Generated artifacts are evidence-only and excluded from committed proof docs.
""",
        encoding="utf-8",
    )
    (module / "claims.md").write_text(
        """# Claims

Validation status: static example only.

## Supported claims

- Authored proof package shape is explicit.

## Explicit non-claims

- production readiness.

## Authority, evidence, and projection labels

Generated evidence remains evidence-only.

## Sensitive/generated classes excluded

- `.out` contents.
""",
        encoding="utf-8",
    )
    (module / "evidence-map.md").write_text(
        """# Evidence Map

## Authority boundaries

Evidence references are authored and repo-relative.

## Evidence quality notes

Generated artifacts are diagnostics only.
""",
        encoding="utf-8",
    )
    (module / "validation-plan.md").write_text(
        """# Validation Plan

## Current status

Validation status: `not_run`.

## Claims not supported

- live validation.
""",
        encoding="utf-8",
    )
    if include_public_writing_map:
        (module / "public-writing-map.md").write_text(
            """# Public Writing Map

## What the proof demonstrates

- The authored package is shaped for review.

## What the proof does not demonstrate

- runtime truth.

## Wording to avoid

- The proof is production ready.
""",
            encoding="utf-8",
        )
    (module / "proof-summary.example.yaml").write_text(
        f"""schema_version: "governed-execution-proof-summary.v1"
scenario_id: "{module_id}"
proof_mode: "static_example"
source_material: "static_example_not_runtime_output"
id_classification: "synthetic_example"
validation_status: "not_run"
claims_supported:
  - "authored proof package shape is explicit"
claims_not_supported:
  - "production readiness"
excluded_artifact_classes:
  - ".out contents"
non_authority_labels:
  proof_summary: "static_example_only"
""",
        encoding="utf-8",
    )
    return repo


def test_current_proof_modules_pass_checker() -> None:
    result = run_tool(CHECKER, REPO_ROOT)
    assert result.returncode == 0, result.stdout + result.stderr


def test_public_writing_map_is_optional(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path, include_public_writing_map=False)

    result = run_tool(CHECKER, repo)
    assert result.returncode == 0, result.stdout + result.stderr


def test_current_scenarios_have_evidence_and_static_summary_status_headings() -> None:
    for scenario in sorted((REPO_ROOT / "proofs").glob("*/scenario.md")):
        text = scenario.read_text(encoding="utf-8")
        assert "## Current evidence status" in text, scenario
        assert "## Static example summary status" in text, scenario


def test_current_authored_docs_pass_redaction_scan() -> None:
    result = run_tool(SCANNER, REPO_ROOT)
    assert result.returncode == 0, result.stdout + result.stderr


def test_missing_claims_not_supported_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    summary = repo / "proofs" / "example-proof" / "proof-summary.example.yaml"
    summary.write_text(summary.read_text(encoding="utf-8").replace("claims_not_supported:\n  - \"production readiness\"\n", ""), encoding="utf-8")

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "claims_not_supported" in result.stdout


def test_static_yaml_with_passed_status_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    summary = repo / "proofs" / "example-proof" / "proof-summary.example.yaml"
    summary.write_text(summary.read_text(encoding="utf-8").replace('validation_status: "not_run"', 'validation_status: "passed"'), encoding="utf-8")

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "validation_status" in result.stdout


def test_scenario_static_example_status_without_current_evidence_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    scenario = repo / "proofs" / "example-proof" / "scenario.md"
    scenario.write_text(
        """# Scenario

## Validation status

Static example status: `not_run`.

## Authority boundaries

CP authority, ES evidence/projection, and IM diagnostics remain separate.

## Generated artifacts

Generated artifacts are evidence-only and excluded from committed proof docs.
""",
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "headline not_run status" in result.stdout
    assert "Current evidence status" in result.stdout


def test_scenario_current_status_not_run_without_current_evidence_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    scenario = repo / "proofs" / "example-proof" / "scenario.md"
    scenario.write_text(
        """# Scenario

## Validation status

Current status: `not_run`.

## Authority boundaries

CP authority, ES evidence/projection, and IM diagnostics remain separate.

## Generated artifacts

Generated artifacts are evidence-only and excluded from committed proof docs.
""",
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "headline not_run status" in result.stdout
    assert "Current evidence status" in result.stdout


def test_scenario_id_mismatch_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    summary = repo / "proofs" / "example-proof" / "proof-summary.example.yaml"
    summary.write_text(summary.read_text(encoding="utf-8").replace('scenario_id: "example-proof"', 'scenario_id: "other-proof"'), encoding="utf-8")

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "scenario_id" in result.stdout


def test_absolute_local_path_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    scenario = repo / "proofs" / "example-proof" / "scenario.md"
    scenario.write_text(
        scenario.read_text(encoding="utf-8")
        + "\nNegative test fixture: `/Users/example/project/output` is not allowed.\n",
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "absolute local path" in result.stdout


def test_es_retained_bundle_labeled_as_cp_finalization_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    claims = repo / "proofs" / "example-proof" / "claims.md"
    claims.write_text(
        claims.read_text(encoding="utf-8").replace(
            "- Authored proof package shape is explicit.",
            "- Authored proof package shape is explicit.\n- ES retained-bundle CP finalization is proven.",
        ),
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "retained bundle" in result.stdout


def test_im_support_bundle_labeled_as_authority_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    claims = repo / "proofs" / "example-proof" / "claims.md"
    claims.write_text(
        claims.read_text(encoding="utf-8").replace(
            "- Authored proof package shape is explicit.",
            "- Authored proof package shape is explicit.\n- IM support-bundle authority is proven.",
        ),
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "support-bundle authority" in result.stdout


def test_independently_audited_overclaim_fails(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    claims = repo / "proofs" / "example-proof" / "claims.md"
    claims.write_text(
        claims.read_text(encoding="utf-8").replace(
            "- Authored proof package shape is explicit.",
            "- Authored proof package shape is explicit.\n- This proof is independently audited.",
        ),
        encoding="utf-8",
    )

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "independent audit" in result.stdout


def test_raw_out_reference_without_exclusion_context_fails_scan(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    risky_doc = repo / ".docs" / "phase.md"
    risky_doc.write_text("# Evidence\n\nRaw `.out/run.json` proves the run.\n", encoding="utf-8")

    result = run_tool(SCANNER, repo)
    assert result.returncode != 0
    assert ".out raw artifact reference" in result.stdout


def test_scanner_rejects_out_input_path(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    out_dir = repo / ".out"
    out_dir.mkdir()

    result = run_tool(SCANNER, out_dir)
    assert result.returncode == 2
    assert "generated/raw artifact paths are refused" in result.stdout


def test_scanner_rejects_log_archive_and_support_bundle_input_paths(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    log_file = repo / "operator.log"
    archive_file = repo / "diagnostics.zip"
    support_bundle_dir = repo / "support-bundles"
    log_file.write_text("negative test fixture, not a retained log payload\n", encoding="utf-8")
    archive_file.write_text("negative test fixture, not an archive payload\n", encoding="utf-8")
    support_bundle_dir.mkdir()

    for target in (log_file, archive_file, support_bundle_dir):
        result = run_tool(SCANNER, target)
        assert result.returncode == 2
        assert "refused" in result.stdout


def test_scanner_rejects_explicit_hidden_env_input(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    env_file = repo / ".env"
    env_file.write_text("negative test fixture\n", encoding="utf-8")

    result = run_tool(SCANNER, env_file)
    assert result.returncode == 2
    assert "env files are refused" in result.stdout


def test_scanner_rejects_explicit_hidden_env_variant_input(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    env_file = repo / ".env.local"
    env_file.write_text("negative test fixture\n", encoding="utf-8")

    result = run_tool(SCANNER, env_file)
    assert result.returncode == 2
    assert "env files are refused" in result.stdout


def test_scanner_rejects_explicit_symlink_input(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    target = repo / ".docs"
    link = repo / "docs-link"
    try:
        os.symlink(target, link)
    except (OSError, NotImplementedError):
        return

    result = run_tool(SCANNER, link)
    assert result.returncode == 2
    assert "symlink paths are refused" in result.stdout


def test_scanner_default_scope_includes_authored_code_schema_tests_and_root_files(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    for directory in ("tools", "schemas", "tests"):
        (repo / directory).mkdir()
    (repo / "tools" / "tool.py").write_text("# tool\n", encoding="utf-8")
    (repo / "schemas" / "schema.json").write_text("{}\n", encoding="utf-8")
    (repo / "tests" / "test_tool.py").write_text("# test\n", encoding="utf-8")
    (repo / "pyproject.toml").write_text("[tool.pytest.ini_options]\n", encoding="utf-8")
    (repo / "README.md").write_text("# Readme\n", encoding="utf-8")

    scanned = {path.relative_to(repo).as_posix() for path in default_scan_files(repo)}
    assert {
        ".docs/conventions.md",
        "proofs/example-proof/claims.md",
        "tools/tool.py",
        "schemas/schema.json",
        "tests/test_tool.py",
        "pyproject.toml",
        "README.md",
    } <= scanned


def test_path_traversal_input_is_rejected(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    target = repo / "proofs" / ".." / "proofs" / "example-proof"

    result = run_tool(CHECKER, target)
    assert result.returncode != 0
    assert "path traversal" in result.stdout


def test_symlink_module_is_rejected(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    link = repo / "proofs" / "linked-proof"
    try:
        os.symlink(repo / "proofs" / "example-proof", link)
    except (OSError, NotImplementedError):
        return

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "symlink" in result.stdout


def test_symlink_expected_module_file_is_rejected_without_reading_target(tmp_path: Path) -> None:
    repo = write_minimal_repo(tmp_path)
    module = repo / "proofs" / "example-proof"
    claims = module / "claims.md"
    outside_target = repo / "linked-claims.md"
    outside_target.write_text("# Claims\n\n- This proof is independently audited.\n", encoding="utf-8")
    claims.unlink()
    try:
        os.symlink(outside_target, claims)
    except (OSError, NotImplementedError):
        claims.write_text(
            """# Claims

## Supported claims

- Authored proof package shape is explicit.

## Explicit non-claims

- production readiness.
""",
            encoding="utf-8",
        )
        return

    result = run_tool(CHECKER, repo)
    assert result.returncode != 0
    assert "symlink entries are rejected" in result.stdout
    assert "independent audit" not in result.stdout
