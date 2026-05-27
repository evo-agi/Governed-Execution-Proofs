#!/usr/bin/env python3
"""Scan authored proof-repo surfaces for redaction-risk markers.

The scanner reports file/category/count only. It never prints matching source
lines or values, and it refuses generated artifact paths.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable


SCAN_SUFFIXES = {".json", ".md", ".py", ".toml", ".yaml", ".yml"}
DEFAULT_SCAN_DIRS = (".docs", "proofs", "tools", "schemas", "tests")
DEFAULT_SCAN_FILES = ("pyproject.toml", "README.md")
REFUSED_SUFFIXES = {
    ".log",
    ".trace",
    ".zip",
    ".tar",
    ".gz",
    ".tgz",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".env",
    ".pem",
    ".key",
    ".crt",
    ".cer",
}
REFUSED_PART_RE = re.compile(
    r"(^|[-_/\.])(\.out|logs?|traces?|archives?|retained[-_]?bundles?|support[-_]?bundles?|raw[-_]?generated[-_]?payloads?|workspaces?|checkpoints?|quarantines?|restores?)([-_/\.]|$)",
    re.I,
)
TOKENISH_NAME_RE = re.compile(r"(api[-_]?key|token|secret|password|credential|private[-_]?key)", re.I)

CATEGORY_PATTERNS = {
    "absolute local path": re.compile(r"(?<![\w.-])/(?:Users/[^`\s)]+|mnt/data(?:/[^`\s)]*)?)"),
    "token/secret/password/credential/api-key/bearer/private-key": re.compile(
        r"api[_-]?key|token|secret|password|credential|Bearer\s+\S+|BEGIN [A-Z ]*PRIVATE KEY",
        re.I,
    ),
    "TLS/SPIFFE/Vault/WebAuthn/passkey": re.compile(r"\bTLS\b|\bSPIFFE\b|\bVault\b|\bWebAuthn\b|\bpasskey\b", re.I),
    "raw prompt/model-output marker": re.compile(r"\braw prompts?\b|\braw model outputs?\b|\bprompt:\b|\bmodel_output\b", re.I),
    ".out raw artifact reference": re.compile(r"(^|[^\w])\.out(?:/|\b)"),
    "production/HA/multi-tenant overclaim marker": re.compile(
        r"\bproduction[- ]ready\b|\bproduction readiness\b|\bHA\b|\bhigh availability\b|\bmulti[- ]tenant\w*|\bmulti-tenancy\b",
        re.I,
    ),
}

VALUE_LIKE_SECRET_RE = re.compile(
    r"(api[_-]?key|token|secret|password|credential)\s*[:=]\s*[^`'\"\s][^,\s]*|Bearer\s+(?!material\b)[A-Za-z0-9._~+/-]{10,}|BEGIN [A-Z ]*PRIVATE KEY",
    re.I,
)

SAFE_HEADINGS = (
    "claims not supported",
    "explicit non-claims",
    "does not demonstrate",
    "what this roadmap does not demonstrate",
    "sensitive",
    "excluded",
    "exclusion",
    "omit",
    "wording to avoid",
    "non-goals",
    "security/redaction",
    "artifact inventory",
    "artifact and evidence classification",
    "command inventory",
    "phase a command/result summary",
    "phase b post-run audit summary",
    "support-bundle status",
    "public-writing implications",
    "follow-up",
    "risk",
    "stop condition",
    "pass/fail",
    "fail interpretation",
    "claim-review checklist",
    "evidence quality notes",
    "documentation posture",
    "explicit exclusions",
    "does not happen",
    "must not claim",
    "not claim",
    "does not prove",
    "does not support",
)

SAFE_LINE_MARKERS = (
    " not ",
    "not_",
    "does not",
    "do not",
    "must not",
    " no ",
    "without",
    "exclude",
    "excluded",
    "omit",
    "unclaimed",
    "deferred",
    "redaction",
    "metadata only",
    "path class",
    "example reference",
    "expected artifacts",
    "generated proof outputs",
    "non-authority",
    "evidence/projection",
    "evidence, projection",
    "diagnostics",
    "not committed",
    "rather than",
    "separate from",
    "distinct from",
    "non-claims",
    "non-authority",
    "guardrail",
    "keep ",
    "remain",
    "false",
)

SAFE_YAML_KEYS = {
    "claims_not_supported",
    "excluded_artifact_classes",
    "sensitive_exclusion_summary",
    "non_authority",
    "non_authority_labels",
}


def has_path_traversal(raw: str) -> bool:
    return any(part == ".." for part in Path(raw).parts)


def is_hidden_env_file_name(name: str) -> bool:
    return name == ".env" or name.startswith(".env.")


def refused_path(path: Path) -> str | None:
    if path.is_symlink():
        return "symlink paths are refused"
    if is_hidden_env_file_name(path.name):
        return "env files are refused"
    if path.suffix.lower() in REFUSED_SUFFIXES:
        return f"{path.suffix} files are refused"
    parts = "/".join(path.parts)
    if REFUSED_PART_RE.search(parts):
        return "generated/raw artifact paths are refused"
    if TOKENISH_NAME_RE.search(path.name):
        return "token/secret-like file names are refused"
    return None


def current_yaml_key(line: str, previous: str | None) -> str | None:
    if line and not line.startswith(" ") and ":" in line:
        return line.split(":", 1)[0].strip()
    return previous


def is_allowed_context(line: str, heading: str, yaml_key: str | None) -> bool:
    lower_line = f" {line.lower()} "
    lower_heading = heading.lower()
    if yaml_key in SAFE_YAML_KEYS:
        return True
    if any(marker in lower_heading for marker in SAFE_HEADINGS):
        return True
    if any(marker in lower_line for marker in SAFE_LINE_MARKERS):
        return True
    return False


def is_high_risk(category: str, line: str, heading: str, yaml_key: str | None) -> bool:
    if is_allowed_context(line, heading, yaml_key):
        return False
    if category == "absolute local path":
        return True
    if category == "token/secret/password/credential/api-key/bearer/private-key":
        return bool(VALUE_LIKE_SECRET_RE.search(line))
    if category == "TLS/SPIFFE/Vault/WebAuthn/passkey":
        return bool(re.search(r"BEGIN [A-Z ]*PRIVATE KEY", line, re.I))
    if category == "raw prompt/model-output marker":
        return bool(re.search(r"\bprompt:\b|\bmodel_output\s*[:=]", line, re.I))
    if category == ".out raw artifact reference":
        return bool(re.search(r"\b(proves?|authority|source of truth|passed|success|truth)\b", line, re.I))
    if category == "production/HA/multi-tenant overclaim marker":
        return bool(
            re.search(
                r"\b(?:is|are|now|fully)\s+production[- ]ready\b|\bproduction[- ]ready\b|\bHA\s+ready\b|\bmulti[- ]tenant\s+ready\b",
                line,
                re.I,
            )
        )
    return False


def default_scan_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for directory_name in DEFAULT_SCAN_DIRS:
        directory = root / directory_name
        if directory.exists():
            files.extend(
                path
                for path in directory.rglob("*")
                if path.is_file() and path.suffix.lower() in SCAN_SUFFIXES
            )
    for file_name in DEFAULT_SCAN_FILES:
        path = root / file_name
        if path.exists() and path.is_file() and path.suffix.lower() in SCAN_SUFFIXES:
            files.append(path)
    return sorted(files)


def explicit_scan_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() in SCAN_SUFFIXES else []
    return sorted(
        child
        for child in path.rglob("*")
        if child.is_file() and child.suffix.lower() in SCAN_SUFFIXES
    )


def collect_files(raw_args: list[str]) -> tuple[Path, list[Path], list[str]]:
    diagnostics: list[str] = []
    files: list[Path] = []
    root = Path.cwd().resolve()

    for raw in raw_args:
        if has_path_traversal(raw):
            diagnostics.append(f"{raw}: path traversal inputs are refused")
            continue
        path = Path(raw)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            diagnostics.append(f"{raw}: path does not exist")
            continue
        if path.is_symlink():
            diagnostics.append(f"{path}: symlink paths are refused")
            continue
        path = path.resolve()
        reason = refused_path(path)
        if reason:
            diagnostics.append(f"{path}: {reason}")
            continue

        if (path / "proofs").is_dir() and (path / ".docs").is_dir():
            root = path
            files.extend(default_scan_files(path))
        else:
            files.extend(explicit_scan_files(path))

    clean_files: list[Path] = []
    for file_path in files:
        reason = refused_path(file_path)
        if reason:
            diagnostics.append(f"{file_path}: {reason}")
            continue
        clean_files.append(file_path)

    return root, sorted(set(clean_files)), diagnostics


def scan_file(path: Path) -> tuple[Counter[str], Counter[str]]:
    counts: Counter[str] = Counter()
    high_risk: Counter[str] = Counter()
    heading = ""
    yaml_key: str | None = None
    text = path.read_text(encoding="utf-8")
    previous_context_allowed = False

    for line in text.splitlines():
        stripped = line.strip()
        if path.suffix.lower() in {".yaml", ".yml"}:
            yaml_key = current_yaml_key(line, yaml_key)
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
        elif stripped.endswith(":") and not stripped.startswith(("-", "|")):
            heading = stripped[:-1]
        base_allowed = is_allowed_context(line, heading, yaml_key)
        paragraph_continuation = (
            previous_context_allowed
            and bool(stripped)
            and not stripped.startswith(("#", "- ", "|"))
        )
        line_allowed = base_allowed or (line.startswith((" ", "\t")) and previous_context_allowed) or paragraph_continuation
        for category, pattern in CATEGORY_PATTERNS.items():
            matches = pattern.findall(line)
            if not matches:
                continue
            count = len(matches)
            counts[category] += count
            if not line_allowed and is_high_risk(category, line, heading, yaml_key):
                high_risk[category] += count
        previous_context_allowed = bool(stripped) and (base_allowed or paragraph_continuation)

    return counts, high_risk


def run(paths: list[str]) -> int:
    root, files, diagnostics = collect_files(paths)
    by_file: dict[Path, Counter[str]] = {}
    high_by_file: dict[Path, Counter[str]] = {}

    for path in files:
        counts, high = scan_file(path)
        if counts:
            by_file[path] = counts
        if high:
            high_by_file[path] = high

    if diagnostics:
        print("Redaction-risk scan refused input:")
        for item in diagnostics:
            print(f"- {item}")
        return 2

    if by_file:
        print("Redaction-risk markers by file/category:")
        for path in sorted(by_file):
            rel = path.relative_to(root) if path.is_relative_to(root) else path
            for category, count in sorted(by_file[path].items()):
                high_count = high_by_file.get(path, Counter()).get(category, 0)
                suffix = f", high_risk={high_count}" if high_count else ""
                print(f"- {rel}: {category}: count={count}{suffix}")
    else:
        print("No redaction-risk markers found.")

    if high_by_file:
        print("High-risk redaction markers found outside allowed contexts.")
        return 1

    print("Redaction-risk scan passed for authored proof-repo surfaces.")
    return 0


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scan authored proof-repo surfaces for redaction-risk markers.")
    parser.add_argument("paths", nargs="+", help="Repo root, authored directory, or authored file.")
    args = parser.parse_args(list(argv) if argv is not None else None)
    return run(args.paths)


if __name__ == "__main__":
    sys.exit(main())
