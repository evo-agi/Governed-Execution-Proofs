# Validation Plan

## Current status

Status: `not_run`.

This module is static proof-planning material. It was created without running
tests, scripts, servers, bringup commands, proof commands, validation commands,
Docker, Nomad, Vault, SPIRE, Temporal, supported-local commands, Remote Alpha
commands, live host commands, or support-bundle commands.

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
