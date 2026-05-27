# Validation Plan

## Current status

Static example status: `not_run`.

This module is static proof-planning material. It was created without running
tests, scripts, servers, bringup commands, proof commands, validation commands,
Docker, Nomad, Vault, SPIRE, Temporal, supported-local commands, Remote Alpha
commands, live host commands, or support-bundle commands.

The static example remains `not_run`. The deterministic record below captures
Codex-reported deterministic validation separately from the static example and
is not live proof output.

## Deterministic validation record (2026-05-27)

Type: Codex-reported deterministic validation.

Reference ledger: `.docs/deterministic-validation-2026-05-27.md`.

Initial import-path collection issue:

- `ModuleNotFoundError: No module named 'infra_manager'`

Rerun posture:

- `PYTHONPATH=src`
- no installs

Reported summarized passing batches:

- `6 passed`
- `32 passed`
- `72 passed`

Claims supported by this Codex-reported deterministic validation:

- IM outputs remain diagnostics/provenance/evidence only;
- Remote Alpha readiness and support artifacts preserve non-authority labels;
- support bundles do not become CP or ES authority;
- malformed, stale, secret-like, or overclaiming evidence fails closed;
- no-contact support-bundle boundary behavior is covered.

Claims not supported by this Codex-reported deterministic validation:

- live host contact;
- Remote Alpha live proof;
- Linux-host behavior;
- Docker, Nomad, Vault, SPIRE, or Temporal behavior;
- production readiness;
- CP authority;
- ES runtime behavior.

The bare invocation issue is recorded as an import-path collection issue, not a
proof failure. The later Codex-reported deterministic validation is not
packaging/install validation and not live host validation.

## Phase A/B limited provenance note (2026-05-27)

Reference: `.docs/live-validation-phase-a-2026-05-27.md`.

Phase A and Phase B provide limited Codex-reported profile/config/preflight
provenance for the bounded `temporal-basic` CP Temporal normal-shell path. No
support bundle was generated.

IM support-bundle claims remain unvalidated. IM profile/config/preflight
provenance remains diagnostics/provenance only and does not become CP
run-control authority or ES runtime authority.

## Tier 1: static/example review

Purpose: document the intended proof shape without importing product code,
ingesting generated artifacts, or claiming validation.

Allowed material:

- static narrative in this directory;
- the static `proof-summary.example.yaml`;
- synthetic ids and example digest text;
- repo-relative evidence references;
- source-inspection notes grounded in IM, CP, and ES docs/source/tests.

Pass interpretation:

- The module says IM support outputs are evidence, projection, provenance,
  diagnostics, or packaging only.
- The module labels CP workflow/query state and guarded writes as CP authority.
- The module labels ES runtime boundaries as ES-owned and not transferred to IM.
- The module includes `validation_status: "not_run"`.
- The module uses only synthetic/example ids.
- The module excludes raw generated and sensitive artifact classes.

Fail interpretation:

- The module includes real run data, real hashes, raw logs, raw traces, raw
  reports, raw prompts, raw model output, retained bundles, support bundles,
  credentials, local absolute paths, or local process data.
- The module implies that live validation passed.
- The module treats IM support packets, redaction reports, digest manifests, or
  generated artifacts as CP run-control authority or ES runtime authority.

## Tier 2: future source-only audit

Purpose: let a parent reviewer re-audit the cited source and docs without
running validation commands.

Expected support if the anchors still match:

- IM profile and doctor outputs keep CP run-control and ES runtime authority
  false.
- IM readiness reports remain pre-live evidence and not governed execution
  proof by themselves.
- IM support bundles preserve CP/ES section ownership and remain diagnostics,
  repeatability, shareability, and evidence packaging.
- Support-bundle digest identity remains primary for copied summary artifacts,
  with source-path identity secondary.
- Redaction and deny scans exclude sensitive classes and fail closed when
  uncertain.

This tier must not claim these happened or became true:

- live support bundle generation;
- raw support bundle copying;
- live host contact;
- Remote Alpha production readiness;
- CP run-control authority from IM evidence;
- ES runtime authority from IM evidence;
- remote provisioning/reconciler behavior;
- support-bundle authority.

## Tier 3: optional later validation

Purpose: optional future validation by an explicitly authorized parent or owner.
This worker did not run or prescribe live validation. Any later validation must
record its own scope, command provenance, generated artifacts, redaction review,
and non-claims outside this static module.

Required controls before any later validation:

- explicit operator authorization;
- owner selection for CP, ES, or IM validation scope;
- artifact exclusion and redaction review before any public writing;
- no promotion of generated summaries into authority;
- no support-bundle collection treated as proof, refresh, provisioning, renewal,
  or reconciliation authority.

Non-claims for this tier:

- a passing IM bundle or readiness check would not by itself prove CP
  run-control behavior;
- a passing CP proof would not by itself make IM support output authority;
- a passing ES check would not by itself prove Remote Alpha production
  readiness;
- support-bundle collection would remain diagnostics and shareability support.

## Forbidden in this module

Do not add or imply:

- generated bundle contents;
- raw support-bundle payloads;
- real run ids, provider ids, hashes, or local absolute paths;
- live host contact;
- support-bundle command output;
- CP proof pass output;
- ES proof pass output;
- provisioning or reconciler behavior;
- production-readiness claims.

## Pass/fail interpretation

Pass means the tier's own stated claim is supported. It does not promote
evidence from one tier into another tier.

Failure means the proof should stop and report the failed tier without
reinterpreting generated artifacts as authority or expanding product semantics.
