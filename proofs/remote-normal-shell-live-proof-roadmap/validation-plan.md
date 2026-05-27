# Validation Plan

## Current status

Status: `not_run`.

This module is static proof-planning material. It was created without running
tests, scripts, servers, bringup commands, setup commands, proof commands,
validation commands, Docker, Nomad, Vault, SPIRE, Temporal, supported-local,
remote-alpha, or Linux-host commands.

Future validation requires an explicit operator decision in the owning repos.
This module is not itself authorization to run validation.

## Deterministic validation status note (2026-05-27)

The Codex-reported deterministic validation pass recorded in
`.docs/deterministic-validation-2026-05-27.md` did not run this remote roadmap.
The roadmap remains future-facing, and Linux-host validation is deferred. No
supported-local, Remote Alpha, Linux-host, Docker, Nomad, Vault, SPIRE, or
Temporal server commands were run for this roadmap status note.

Milestone 3 and live proof claims remain unvalidated.

## Live validation planning record

Date: 2026-05-27.

Status: plan recorded, live proof not run.

The Linux/Remote Alpha live validation plan is recorded in
`.docs/remote-normal-shell-live-validation-plan.md`.

Linux-host validation is deferred until explicit authorization. This roadmap
remains future-facing. Generated live evidence will require post-run audit
before proof claims are updated.

## Tier 1: static roadmap review

Purpose: confirm that the proof package shape is clear before any live
validation is attempted.

Pass interpretation:

- The scenario says the proof has not run.
- The claims include explicit non-claims.
- Authority labels are present for CP, AGS, ES, Nomad, Docker, SPIRE, Vault,
  and IM.
- Evidence/projection labels are present for IM readiness, ES lifecycle and
  outcome facts, retained-result references, support bundles, and proof
  summaries.
- Sensitive/generated artifact exclusions are explicit.
- Evidence anchors are repo-relative labels.

Fail interpretation:

- The module implies live validation passed.
- The module includes real run ids, real hashes, raw generated artifact payloads,
  local absolute paths, remote filesystem paths, retained bundle contents,
  support-bundle contents, logs, traces, prompts, model outputs, or credentials.
- The module treats generated artifacts or support bundles as authority.

## Tier 2: profile and readiness contract gate

Purpose: later prove that the target remote profile and readiness posture match
the Remote Supported-Host Alpha contract before any governed run is attempted.

Expected future evidence classes:

- CP remote-profile diagnostic summary;
- IM remote doctor summary;
- IM alpha readiness report summary;
- proof-profile lineage summary when a compatibility proof profile is derived
  from a remote-supported-host profile;
- redaction/deny-scan summary for shareable evidence.

Required pass conditions:

- direct HTTPS/mTLS alpha posture is accepted;
- `control-plane-normal-shell/v1` is the runtime profile;
- Temporal and Control Plane remain Mac-local for the alpha posture;
- no shared filesystem is assumed;
- IM readiness remains provenance/diagnostics only;
- support bundles remain diagnostics only.

Non-claims for this tier:

- no live governed execution;
- no AGS publish;
- no ES prepare or submit;
- no retained result;
- no CP review/finalization;
- no runtime identity credential success;
- no remote provisioning or reconciler.

## Tier 3: producer, publish, and prepare gate

Purpose: later prove that Control Plane refuses to create a real attempt unless
the current ES producer declaration and pre-submit compatibility gates pass.

Expected future evidence classes:

- ES producer-declaration compatibility summary;
- AGS publish response digest summary;
- ES prepare result summary;
- CP attempt-manifest pre-submit summary.

Required pass conditions:

- CP requires the current governed-execution producer declaration before AGS
  publish, ES prepare, ES submit, or real attempt-manifest creation;
- the declaration includes the expected current producer contract and
  non-authority classifications;
- the `control-plane-normal-shell/v1` runtime profile is enabled;
- AGS publish and ES prepare are summarized as evidence, not run-control truth.

Non-claims for this tier:

- no execution;
- no Nomad placement;
- no Docker workload success;
- no retained result;
- no runtime identity or Vault credential success;
- no CP semantic finalization.

## Tier 4: submit, Nomad/Docker execution, and lifecycle observation

Purpose: later prove that the remote governed execution path actually submits
and reaches an honestly observed provider terminal condition.

Expected future evidence classes:

- ES submit receipt summary;
- provider run id summary;
- ES status/lifecycle projection summary;
- outcome-evidence summary;
- bounded logs metadata summary when logs are fetched;
- provider terminal observation summary.

Required pass conditions:

- ES submit happens only after the producer/publish/prepare gate;
- status is treated as Nomad-backed lifecycle projection;
- projection revision is treated as opaque read coordination, not scheduler id
  or CP write guard;
- outcome evidence remains evidence/projection;
- CP does not use ES lifecycle facts as intervention write authority.

Non-claims for this tier:

- no CP finalization until retained result is fetched and reviewed;
- no retained-result semantic success;
- no runtime identity credential success unless separately validated;
- no production readiness.

## Tier 5: runtime identity and Vault handoff

Purpose: later prove the bounded workload-side credential flow without turning
ES into a credential broker.

Expected future evidence classes:

- non-secret ES `authority_handoff` summary;
- workload-visible identity endpoint summary;
- workload-side Vault login/read success summary when validated;
- redacted credential-flow summary;
- absence-of-secret-persistence summary.

Required pass conditions:

- `EXEC_WORKLOAD_IDENTITY_ENDPOINT` is the bounded workload-visible discovery
  contract;
- raw SPIRE socket access is not exposed as public ES grammar;
- SPIRE owns identity issuance;
- Vault owns token, secret, and lease issuance after workload-side login;
- ES does not mint, fetch, broker, parse, store, rotate, or validate Vault
  tokens, JWT-SVID payloads, secrets, leases, API keys, or Codex credentials;
- proof outputs contain only safe metadata.

Non-claims for this tier:

- no production Vault readiness;
- no general runtime identity architecture;
- no support-bundle authority;
- no credential success unless the same validation run proves it.

## Tier 6: retained result, CP review, and finalization

Purpose: later prove that the retained output is fetched and then interpreted
under CP-owned semantics.

Expected future evidence classes:

- retained-result fetch summary;
- safe materialization summary;
- retained bundle correlation summary;
- CP review/finalization summary;
- terminal `ExecutionFlowSnapshot v1` summary;
- operator narrative and machine-readable proof summary.

Required pass conditions:

- retained result remains an opaque ES output until CP materializes and reviews
  it;
- CP owns semantic result validation, checkpointing, terminal outcome, and
  finalization;
- final proof summary separates provider evidence from CP terminal outcome;
- generated artifacts are summarized without raw payloads.

Non-claims for this tier:

- no support-bundle authority;
- no production readiness;
- no HA or multi-tenancy;
- no default remote runtime claim;
- no general deployment architecture.

## Stop conditions

Future validation must stop and surface a conflict if:

- CP docs require behavior that ES docs do not own;
- ES evidence is being used as CP write coordination or finalization authority;
- IM profile/readiness/support output is being used as CP run-control or ES
  runtime authority;
- support bundles are treated as proof authority;
- runtime identity evidence implies ES credential brokerage;
- generated artifacts contain raw secrets or raw sensitive payloads;
- the validation cannot distinguish preflight, prepare, submit, execution,
  retained-result fetch, and CP finalization.

## Pass/fail interpretation

Passing a tier supports only that tier's stated claim. Passing one tier does not
promote evidence from another tier and does not remove any explicit non-claim.

Failure means the proof should stop and report the failed tier without
reinterpreting generated artifacts as authority or widening product semantics.
