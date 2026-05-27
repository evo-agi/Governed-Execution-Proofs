# Validation Plan

## Current status

Static example status: `not_run`.

This module is static proof-planning material. It was created without running
tests, scripts, servers, setup commands, bringup commands, proof commands,
validation commands, supported-local commands, Remote Alpha commands, Docker,
Nomad, Vault, SPIRE, or Temporal.

The static example remains `not_run`. The deterministic record below captures
Codex-reported deterministic validation separately from the static example and
is not live proof output.

## Deterministic validation record (2026-05-27)

Type: Codex-reported deterministic validation.

Reference ledger: `.docs/deterministic-validation-2026-05-27.md`.

Reported commands:

```bash
go test -run TestPrimaryMilestoneRealignmentPreservesESOwnership -count=1 .
go test ./...
```

Reported summarized results:

- targeted test: `ok execution-substrate 0.242s`
- full `go test ./...` reported as passing across packages

Claims supported by this Codex-reported deterministic validation:

- ES owns admission and runtime boundaries;
- prepare, submit, status, result, cancel, and log surfaces stay bounded ES
  envelope or evidence surfaces;
- lifecycle projection remains evidence/projection;
- retained results remain opaque ES artifacts;
- `authority_handoff` is non-secret handoff evidence, not credential or CP
  authority.

Claims not supported by this Codex-reported deterministic validation:

- live runtime proof;
- Nomad, Docker, Vault, SPIRE, or Temporal live behavior;
- Remote Alpha or Linux-host behavior;
- CP semantic finalization;
- live retained-result availability.

No live runtime, supported-local, Remote Alpha, Linux-host, Docker, Nomad,
Vault, SPIRE, or Temporal server validation was run for this record.

## Tier 1: static/example fixture

Purpose: document the intended proof shape without importing product code,
running product paths, or ingesting generated artifacts.

Allowed material:

- static narrative in this module directory;
- synthetic/example IDs only;
- the static `proof-summary.example.yaml`;
- repo-relative evidence references;
- source-inspection anchors from ES and CP docs/source/tests.

Pass interpretation:

- The example labels producer contract as ES compatibility declaration.
- The example labels prepare as preflight only.
- The example labels submit as runtime handoff only.
- The example labels status/result/cancel/log facts as runtime evidence or
  projection only.
- The example labels retained bundles as opaque output artifacts.
- The example labels CP as the semantic review/finalization owner.
- The example keeps `validation_status: "not_run"` and makes no validation pass
  claim.

Fail interpretation:

- The example includes real run IDs, provider IDs, hashes, retained bundle refs,
  local absolute paths, raw logs, raw traces, raw reports, raw prompts, raw model
  output, retained bundle payloads, support bundle payloads, credentials, or
  local process data.
- The example implies a command passed.
- The example treats an ES evidence/projection surface as CP finalization.
- The example treats retained bundle bytes as semantically interpreted by ES.
- The example treats `authority_handoff` as credential or token brokerage proof.
- The example treats Remote Alpha, production readiness, service health, submit
  readiness, or provider/runtime success as proven.

## Tier 2: deterministic source validation

Purpose: confirm that existing source-level tests and docs still support the
static labels before publication or promotion.

Codex-reported deterministic validation for this tier is recorded above and in
`.docs/deterministic-validation-2026-05-27.md`. Any future promotion beyond this
record requires explicit parent authorization and must remain bounded to
existing deterministic source checks. It must not create proof outputs, support
bundles, retained bundles, shared frameworks, schemas, or generated artifacts in
this proof module.

Expected support for a bounded deterministic validation record:

- producer contract still emits explicit `non_authority` classifications;
- prepare still creates no run id, scheduler handoff, proto-execution state, or
  CP semantic state;
- submit still returns a bounded async handoff receipt rather than a durable ES
  lifecycle or CP finalization model;
- status still exposes projection/evidence labels without CP run-control grammar
  or live credential fields;
- result still serves retained opaque bundles without ES semantic
  interpretation or synthesized CP authority sidecars.

Non-claims for this tier:

- no live ES validation;
- no provider/runtime success;
- no CP finalization proof;
- no retained-bundle semantic interpretation;
- no credential/token brokerage proof;
- no Remote Alpha proof;
- no production readiness.

## Tier 3: live or supported-local validation

Live validation is out of scope for this module.

Any later live validation would need a separate owner decision, explicit
authorization, artifact hygiene review, and clear separation between generated
evidence and authority. It must not be backfilled into this static module as if
it had already run.

Non-claims for this tier:

- not production readiness;
- not high availability;
- not multi-tenancy;
- not general remote deployment;
- not Remote Alpha proof unless a separate Remote Alpha proof explicitly owns
  that claim;
- not proof harness architecture;
- not ES token brokerage;
- not CP ownership of ES contracts;
- not IM ownership of CP run-control truth or ES runtime truth.

## Sensitive artifact handling

Validation must exclude:

- raw `.out` contents;
- raw logs, traces, and reports;
- retained bundle and support bundle payloads;
- archives;
- database files;
- environment files;
- key, certificate, token, secret, API key, and bearer material;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, and private-key material;
- raw prompts;
- raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoint directories, quarantine directories, and restore
  directories;
- local process records;
- real run ids, provider ids, hashes, retained bundle refs, and local absolute
  paths.

## Risks

- Static examples can be mistaken for live output unless labels remain explicit.
- ES compatibility declarations can be overread as health or readiness.
- Prepare can be overread as execution unless its non-effects are repeated.
- Submit receipts can be overread as durable lifecycle or CP finalization.
- Status projection can be overread as CP workflow truth or a write guard.
- Retained bundle references can be overread as semantic interpretation.
- `authority_handoff` can be overread as live credential or token proof.
- Generated evidence can be promoted into architecture by drift.

## Pass/fail interpretation

Pass means the relevant tier supports only its own stated claim. It does not
promote a static example into live validation, and it does not promote generated
artifacts into authority.

Failure means the proof should stop and report the failed tier without
expanding product semantics or treating a lower-authority surface as a higher
authority surface.
