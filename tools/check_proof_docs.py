#!/usr/bin/env python3
"""Local linting for authored proof modules.

This tool intentionally validates only local proof-document shape and wording.
It does not run product systems, inspect generated artifacts, or contact hosts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable


REQUIRED_MODULE_FILES = {
    "scenario.md",
    "claims.md",
    "evidence-map.md",
    "proof-summary.example.yaml",
    "validation-plan.md",
}

OPTIONAL_MODULE_FILES = {
    "public-writing-map.md",
}

REQUIRED_SUMMARY_FIELDS = {
    "schema_version",
    "scenario_id",
    "proof_mode",
    "source_material",
    "id_classification",
    "validation_status",
    "claims_supported",
    "claims_not_supported",
    "excluded_artifact_classes",
}

VALIDATION_STATUS_ENUM = {
    "not_run",
}

AUTHORITY_LABEL_FIELDS = {
    "non_authority_labels",
    "authority_labels",
    "evidence_projection_labels",
    "evidence_projection_facts",
}

REQUIRED_SCENARIO_STATUS_HEADINGS = (
    "## Current evidence status",
    "## Static example summary status",
)

HEADLINE_NOT_RUN_STATUS_RE = re.compile(
    r"(?im)^\s*(?:Static example status|Current status|Validation status):\s*`?not_run`?\.?\s*$"
)

ABSOLUTE_LOCAL_PATH_RE = re.compile(r"(?<![\w.-])/(?:Users/[^`\s)]+|mnt/data(?:/[^`\s)]*)?)")
ADJACENT_ABSOLUTE_REF_RE = re.compile(
    r"(Control Plane|Execution Substrate|Infrastructure Manager):\s*/"
)

FORBIDDEN_PATTERNS = [
    ("production readiness overclaim", re.compile(r"\bproduction[- ]ready\b|\bproduction readiness\b", re.I)),
    ("high availability overclaim", re.compile(r"\bhigh availability\b|\bHA\b")),
    ("multi-tenancy overclaim", re.compile(r"\bmulti[- ]tenant\w*|\bmulti-tenancy\b", re.I)),
    ("source-of-truth overclaim", re.compile(r"\bsource of truth\b", re.I)),
    ("provider-side success overclaim", re.compile(r"\bprovider-side success\b", re.I)),
    ("token brokerage overclaim", re.compile(r"\btoken brokerage\b|\bbrokers? (?:Vault|Codex )?tokens?\b", re.I)),
    ("independent audit overclaim", re.compile(r"\bindependent audit\b|\bindependently audited\b", re.I)),
    ("public/demo readiness overclaim", re.compile(r"\bpublic/demo readiness\b|\bpublic demo readiness\b", re.I)),
    (
        "support-bundle authority overclaim",
        re.compile(r"\bsupport[- ]bundle authority\b|support_bundle_authority:\s*true", re.I),
    ),
    (
        "retained bundle finalization overclaim",
        re.compile(r"\bretained[- ]bundle\b.*\b(?:CP )?(?:semantic )?finalization\b", re.I),
    ),
]

ALLOWING_HEADINGS = (
    "non-claim",
    "claims not supported",
    "not supported",
    "does not demonstrate",
    "wording to avoid",
    "avoid",
    "sensitive",
    "excluded",
    "exclusion",
    "omit",
    "forbidden",
    "risk",
    "stop condition",
    "non-goal",
    "claim-review checklist",
    "evidence quality notes",
    "documentation posture",
    "explicit exclusions",
    "does not happen",
    "must not claim",
    "not claim",
    "does not prove",
    "does not support",
    "public-writing implications",
    "support-bundle status",
    "pass/fail",
    "fail interpretation",
    "follow-up",
)

ALLOWING_LINE_MARKERS = (
    " not ",
    "not_",
    "does not",
    "do not",
    "must not",
    "no ",
    "without",
    "exclude",
    "excluded",
    "unclaimed",
    "deferred",
    "unsupported",
    "not support",
    "not prove",
    "not claim",
    "not validated",
    "remains unvalidated",
    "until ",
    "unless ",
    "avoid",
    "rather than",
    "separate from",
    "distinct from",
    "non-claims",
    "non-authority",
    "guardrail",
    "keep ",
    "keeps",
    "remain",
    "false",
)

ALLOWING_YAML_KEYS = {
    "claims_not_supported",
    "excluded_artifact_classes",
    "sensitive_exclusion_summary",
    "non_authority",
    "non_authority_labels",
}


class ProofDocError(Exception):
    """Raised for invalid invocation shape."""


def is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def has_path_traversal(raw: str) -> bool:
    return any(part == ".." for part in Path(raw).parts)


def has_symlink_component(path: Path, stop_at: Path | None = None) -> bool:
    current = path
    stop = stop_at.resolve() if stop_at is not None else None
    while True:
        if current.exists() and current.is_symlink():
            return True
        if stop is not None and current == stop:
            return False
        parent = current.parent
        if parent == current:
            return False
        current = parent


def derive_root_and_modules(raw_args: list[str]) -> tuple[Path | None, list[Path], list[str]]:
    diagnostics: list[str] = []
    roots: list[Path] = []
    modules: list[Path] = []

    for raw in raw_args:
        if has_path_traversal(raw):
            diagnostics.append(f"{raw}: path traversal inputs are rejected")
            continue
        path = Path(raw)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            diagnostics.append(f"{raw}: path does not exist")
            continue
        if path.is_symlink():
            diagnostics.append(f"{raw}: symlink inputs are rejected")
            continue

        resolved = path.resolve()
        if (resolved / "proofs").is_dir():
            root = resolved
            roots.append(root)
            modules.extend(sorted(p for p in (root / "proofs").iterdir() if p.is_dir()))
        elif (resolved / "proof-summary.example.yaml").is_file():
            if resolved.parent.name != "proofs":
                diagnostics.append(f"{raw}: module directory must live under proofs/")
                continue
            root = resolved.parent.parent
            roots.append(root)
            modules.append(resolved)
        else:
            diagnostics.append(f"{raw}: expected repo root or proof module directory")

    unique_roots = {root.resolve() for root in roots}
    if len(unique_roots) > 1:
        diagnostics.append("all inputs must belong to the same proof repo")
    root = next(iter(unique_roots), None)

    if root is not None:
        clean_modules: list[Path] = []
        for module in modules:
            if module.is_symlink():
                diagnostics.append(f"{module}: symlink proof modules are rejected")
                continue
            resolved = module.resolve()
            if not is_relative_to(resolved, root):
                diagnostics.append(f"{module}: resolved outside proof repo")
                continue
            if has_symlink_component(resolved, root):
                diagnostics.append(f"{module}: symlink path components are rejected")
                continue
            clean_modules.append(resolved)
        modules = sorted(set(clean_modules))

    return root, modules, diagnostics


def unquote_scalar(value: str) -> object:
    value = value.strip()
    if value in {"[]", ""}:
        return [] if value == "[]" else ""
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict[str, object]:
    """Parse the small top-level YAML subset used by proof examples."""

    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if indent == 0 and ":" in stripped:
            key, raw_value = stripped.split(":", 1)
            current_key = key.strip()
            value = raw_value.strip()
            if value == "":
                data[current_key] = []
            else:
                data[current_key] = unquote_scalar(value)
            continue

        if indent > 0 and current_key and stripped.startswith("- "):
            existing = data.setdefault(current_key, [])
            if not isinstance(existing, list):
                data[current_key] = existing = []
            existing.append(str(unquote_scalar(stripped[2:].strip())))

    return data


def current_yaml_key(line: str, previous: str | None) -> str | None:
    if line and not line.startswith(" ") and ":" in line:
        return line.split(":", 1)[0].strip()
    return previous


def validate_summary(module: Path, data: dict[str, object], text: str) -> list[str]:
    diagnostics: list[str] = []
    missing = sorted(REQUIRED_SUMMARY_FIELDS - set(data))
    for field in missing:
        diagnostics.append(f"{module}/proof-summary.example.yaml: missing required field {field}")

    if not (AUTHORITY_LABEL_FIELDS & set(data)):
        diagnostics.append(
            f"{module}/proof-summary.example.yaml: missing non_authority_labels or equivalent authority/evidence labels"
        )

    scenario_id = data.get("scenario_id")
    if scenario_id != module.name:
        diagnostics.append(
            f"{module}/proof-summary.example.yaml: scenario_id {scenario_id!r} does not match directory {module.name!r}"
        )

    validation_status = data.get("validation_status")
    if validation_status not in VALIDATION_STATUS_ENUM:
        diagnostics.append(
            f"{module}/proof-summary.example.yaml: validation_status {validation_status!r} is not an allowed schema value"
        )
    if validation_status != "not_run":
        diagnostics.append(
            f"{module}/proof-summary.example.yaml: static examples must use validation_status \"not_run\""
        )
    if re.search(r"validation_status:\s*[\"']?passed[\"']?\b", text, re.I):
        diagnostics.append(
            f"{module}/proof-summary.example.yaml: static example must not claim passed validation"
        )

    for list_field in ("claims_supported", "claims_not_supported"):
        value = data.get(list_field)
        if not isinstance(value, list) or not value:
            diagnostics.append(f"{module}/proof-summary.example.yaml: {list_field} must be a non-empty list")

    return diagnostics


def validate_markdown_shape(module: Path, texts: dict[str, str]) -> list[str]:
    diagnostics: list[str] = []
    combined = "\n".join(texts.values()).lower()

    checks = [
        ("supported claims", r"\bsupported claims\b|\bclaims supported\b|\bwhat the proof demonstrates\b"),
        (
            "non-claims / claims not supported",
            r"\bexplicit non-claims\b|\bnon-claims\b|\bclaims not supported\b|\bdoes not demonstrate\b",
        ),
        (
            "authority boundaries",
            r"\bauthority boundary\b|\bauthority boundaries\b|\bauthority owners\b|\bauthority labels\b|\bauthority, evidence\b",
        ),
        ("validation status or validation plan", r"\bvalidation status\b|\bvalidation plan\b|\bcurrent status\b"),
        (
            "generated artifacts/evidence-only language",
            r"\bgenerated\b(?s:.){0,120}\b(evidence|artifact|projection|diagnostics|excluded|only)\b",
        ),
    ]

    for label, pattern in checks:
        if not re.search(pattern, combined, re.I):
            diagnostics.append(f"{module}: markdown corpus missing {label}")

    return diagnostics


def validate_scenario_status(module: Path, text: str) -> list[str]:
    diagnostics: list[str] = []

    for heading in REQUIRED_SCENARIO_STATUS_HEADINGS:
        if heading not in text:
            diagnostics.append(f"{module}/scenario.md: missing {heading}")

    for match in HEADLINE_NOT_RUN_STATUS_RE.finditer(text):
        window = text[max(0, match.start() - 800) : min(len(text), match.end() + 800)]
        if "## Current evidence status" not in window:
            line_no = text.count("\n", 0, match.start()) + 1
            diagnostics.append(
                f"{module}/scenario.md:{line_no}: headline not_run status must be separated from current proof evidence status"
            )

    return diagnostics


def line_allows_forbidden_phrase(line: str, heading: str, yaml_key: str | None) -> bool:
    lower_line = f" {line.lower()} "
    lower_heading = heading.lower()
    if yaml_key in ALLOWING_YAML_KEYS:
        return True
    if any(marker in lower_heading for marker in ALLOWING_HEADINGS):
        return True
    if any(marker in lower_line for marker in ALLOWING_LINE_MARKERS):
        return True
    return False


def validate_text_hygiene(module: Path, file_name: str, text: str) -> list[str]:
    diagnostics: list[str] = []
    heading = ""
    yaml_key: str | None = None
    previous_context_allowed = False

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if file_name.endswith((".yaml", ".yml")):
            yaml_key = current_yaml_key(line, yaml_key)
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
        elif stripped.endswith(":") and not stripped.startswith(("-", "|")):
            heading = stripped[:-1]

        base_allowed = line_allows_forbidden_phrase(line, heading, yaml_key)
        paragraph_continuation = (
            previous_context_allowed
            and bool(stripped)
            and not stripped.startswith(("#", "- ", "|"))
        )
        allowed = base_allowed or (line.startswith((" ", "\t")) and previous_context_allowed) or paragraph_continuation

        if ABSOLUTE_LOCAL_PATH_RE.search(line):
            diagnostics.append(f"{module}/{file_name}:{line_no}: absolute local path is not allowed")
        if ADJACENT_ABSOLUTE_REF_RE.search(line):
            diagnostics.append(f"{module}/{file_name}:{line_no}: adjacent repo evidence refs must be repo-relative")

        for label, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(line) and not allowed:
                diagnostics.append(f"{module}/{file_name}:{line_no}: forbidden {label}")

        if re.search(r"\bretained[- ]bundle\b.*\bCP finalization\b", line, re.I) and not allowed:
            diagnostics.append(f"{module}/{file_name}:{line_no}: ES retained bundle cannot be labeled as CP finalization")
        if re.search(r"\bIM\b.*\bsupport[- ]bundle\b.*\bauthority\b", line, re.I) and not allowed:
            diagnostics.append(f"{module}/{file_name}:{line_no}: IM support bundle cannot be labeled as authority")

        previous_context_allowed = bool(stripped) and (base_allowed or paragraph_continuation)

    return diagnostics


def validate_module(root: Path, module: Path) -> list[str]:
    diagnostics: list[str] = []
    if module.is_symlink():
        return [f"{module}: symlink proof modules are rejected"]
    if not is_relative_to(module.resolve(), root.resolve()):
        return [f"{module}: proof module resolved outside repo"]

    entries = [entry for entry in module.iterdir() if entry.name != ".DS_Store"]
    symlink_entries = []
    for entry in entries:
        if entry.is_symlink():
            symlink_entries.append(entry)
            diagnostics.append(f"{entry}: symlink entries are rejected")
    if symlink_entries:
        return diagnostics

    names = {entry.name for entry in entries}
    permitted = REQUIRED_MODULE_FILES | OPTIONAL_MODULE_FILES
    missing = sorted(REQUIRED_MODULE_FILES - names)
    extra = sorted(names - permitted)
    for name in missing:
        diagnostics.append(f"{module}: missing required file {name}")
    for name in extra:
        diagnostics.append(f"{module}: unexpected file or directory {name}")
    if missing:
        return diagnostics

    texts: dict[str, str] = {}
    for name in sorted(REQUIRED_MODULE_FILES | (OPTIONAL_MODULE_FILES & names)):
        path = module / name
        if not path.is_file():
            continue
        if not is_relative_to(path.resolve(), root.resolve()):
            diagnostics.append(f"{path}: file resolved outside repo")
            continue
        texts[name] = path.read_text(encoding="utf-8")

    summary_text = texts.get("proof-summary.example.yaml", "")
    diagnostics.extend(validate_summary(module, parse_simple_yaml(summary_text), summary_text))

    markdown_texts = {name: text for name, text in texts.items() if name.endswith(".md")}
    diagnostics.extend(validate_markdown_shape(module, markdown_texts))
    diagnostics.extend(validate_scenario_status(module, texts.get("scenario.md", "")))

    for name, text in texts.items():
        diagnostics.extend(validate_text_hygiene(module, name, text))

    return diagnostics


def run(paths: list[str]) -> int:
    root, modules, diagnostics = derive_root_and_modules(paths)
    if root is None:
        diagnostics.append("could not determine proof repo root")
    elif not modules:
        diagnostics.append(f"{root}: no proof modules found")
    else:
        for module in modules:
            diagnostics.extend(validate_module(root, module))

    if diagnostics:
        print("Proof document check failed:")
        for item in diagnostics:
            print(f"- {item}")
        return 1

    print(f"Proof document check passed for {len(modules)} module(s).")
    return 0


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint authored proof module docs.")
    parser.add_argument("paths", nargs="+", help="Proof repo root or proof module directories.")
    args = parser.parse_args(list(argv) if argv is not None else None)
    return run(args.paths)


if __name__ == "__main__":
    sys.exit(main())
