# Validation Plan

## Current evidence status

Current proof evidence:

- Codex-reported deterministic CP stale-action tests passed.
- Optional live/supported-local guarded-intervention commands remain not run.
- No provider-side cancel or intervention effect is claimed.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status. The deterministic record below is separate from the static example and
is not live proof output.

## Deterministic validation record (2026-05-27)

Type: Codex-reported deterministic validation.

Reference ledger: `.docs/deterministic-validation-2026-05-27.md`.

Reported commands:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_mismatched_actionability_fingerprint_rejects_before_mutation_and_valid_action_remains
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_actionability_fingerprint_rejects_request_copied_from_stale_snapshot
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_guarded_current_attempt_cancel_uses_snapshot_fingerprint_and_durable_context
```

Reported summarized results:

- `1 passed in 1.09s`
- `1 passed in 0.35s`
- `1 passed in 0.34s`

Claims supported by this Codex-reported deterministic validation:

- stale or mismatched actionability fingerprints reject before mutation;
- stale snapshot requests fail closed;
- valid guarded cancel uses snapshot fingerprint and durable CP context;
- CP workflow/query state remains guarded-action authority.

Claims not supported by this Codex-reported deterministic validation:

- live Temporal behavior;
- supported-local behavior;
- ES runtime behavior;
- browser or WebAuthn behavior;
- Remote Alpha behavior;
- Linux-host behavior;
- Docker, Nomad, Vault, or SPIRE behavior.

No live, supported-local, Remote Alpha, Linux-host, Docker, Nomad, Vault, SPIRE,
or Temporal server validation was run for this record.

## Tier 1: static/example fixture

Purpose: document the intended proof shape without importing product code or
ingesting generated artifacts.

Allowed material:

- static narrative in this directory;
- synthetic IDs and fingerprints;
- the static `proof-summary.example.yaml`;
- repo-relative evidence references.

Pass interpretation:

- The example clearly says stale `expected_actionability_fingerprint` rejects
  before mutation.
- The example labels CP workflow/query state and current fingerprint as
  authority.
- The example labels UI/report/channel/proof, ES, and IM facts as evidence,
  projection, presentation, or diagnostics only.

Fail interpretation:

- The example includes real run data, real hashes, raw logs, raw traces, raw
  prompts, raw model output, retained bundles, support bundles, credentials, or
  local process data.
- The example implies live validation passed.
- The example treats a generated artifact as authority.

## Tier 2: deterministic CP test-backed validation

Purpose: bound deterministic confirmation of the CP guarded route and
stale/fresh behavior using existing deterministic CP tests.

Codex-reported deterministic validation for this tier is recorded above and in
`.docs/deterministic-validation-2026-05-27.md`. The originally identified
deterministic command scope was:

```bash
pytest tests/test_monitoring_interventions.py::test_mismatched_actionability_fingerprint_rejects_before_mutation_and_valid_action_remains
pytest tests/test_monitoring_interventions.py::test_actionability_fingerprint_rejects_request_copied_from_stale_snapshot
pytest tests/test_monitoring_interventions.py::test_guarded_current_attempt_cancel_uses_snapshot_fingerprint_and_durable_context
```

Expected support for a bounded deterministic validation record:

- stale or mismatched fingerprints reject with `effect_status=none`;
- no provider request is produced by the stale request;
- no pending run-control action is created by the stale request;
- no durable accepted intervention record is created by the stale request;
- a valid current-fingerprint cancel request remains acceptable in the same
  action family;
- request context can carry the expected actionability fingerprint.

Non-claims for this tier:

- no live ES execution claim;
- no provider-side cancellation success claim;
- no terminal runtime outcome claim;
- no WebAuthn/passkey/browser delivery claim;
- no Remote Alpha or IM readiness claim.

## Tier 3: optional later supported-local/live validation

Purpose: optional future validation of the live `temporal-cancel` proof path.
This tier is not needed for the first proof and requires explicit operator
authorization before any command is run.

Commands found but not run:

```bash
python ../supported_local_validation_driver.py --mode temporal-cancel --config config.execution-substrate-supported-local.yaml --project-root . --supported-local-profile supported-local-client-profile.yaml
python ../execution_substrate_temporal_normal_shell_smoke.py --config config.execution-substrate-supported-local.yaml --project-root . --cancel-current-attempt
python ../supported_local_golden_path_capture.py --config config.execution-substrate-supported-local.yaml --project-root . --supported-local-profile supported-local-client-profile.yaml
```

Expected support if later explicitly authorized, run, and passing:

- guarded `temporal-cancel` fetches `ExecutionFlowSnapshot v1`;
- stale fingerprint rejection is observed before valid guarded cancel;
- valid guarded cancel records request context and durable history;
- later outcome is recorded separately from immediate receipt.

Non-claims for this tier:

- not production readiness;
- not high availability;
- not multi-tenancy;
- not general remote deployment;
- not proof harness architecture;
- not all intervention verbs;
- not ES or IM ownership of CP run-control authority;
- not runtime identity or Vault credential success unless separately proven by
  the owning contracts.

## Optional live commands found but not run

The deterministic commands with their Codex-reported deterministic validation
summaries are recorded above. Optional live commands remain not run:

- `python ../supported_local_validation_driver.py --mode temporal-cancel --config config.execution-substrate-supported-local.yaml --project-root . --supported-local-profile supported-local-client-profile.yaml`
- `python ../execution_substrate_temporal_normal_shell_smoke.py --config config.execution-substrate-supported-local.yaml --project-root . --cancel-current-attempt`
- `python ../supported_local_golden_path_capture.py --config config.execution-substrate-supported-local.yaml --project-root . --supported-local-profile supported-local-client-profile.yaml`

## Prerequisites

Tier 1:

- no runtime prerequisites;
- proof files must remain static and synthetic.

Tier 2:

- Control Plane development/test environment;
- explicit decision to run deterministic tests;
- no expectation of live ES, IM, Remote Alpha, browser, WebAuthn, or provider
  effect.

Tier 3:

- explicit operator authorization;
- supported-local prerequisites;
- configured CP/ES/Temporal environment;
- careful artifact exclusion and redaction review.

## Risks

- Static examples can be mistaken for live output unless labels remain explicit.
- Deterministic tests can be mistaken for live provider or supported-local
  validation unless tier labels remain explicit.
- Live validation can produce generated artifacts that must not become authority.
- Optional live validation can widen public claims if non-claims are not carried
  forward.
- Proof-only runner holds and helper behavior must remain proof scaffolding, not
  product runtime guarantees.

## Pass/fail interpretation

Pass means the tier's own stated claim is supported. It does not automatically
promote evidence from one tier into another tier.

Failure means the proof should stop and report the failed tier without
reinterpreting generated artifacts as authority or expanding product semantics.

## Non-claims by tier

- Tier 1 does not claim any command passed.
- Tier 2 does not claim live ES, IM, Remote Alpha, Temporal service, browser, or
  WebAuthn behavior.
- Tier 3 does not claim production readiness, HA, multi-tenancy, general remote
  deployment, all intervention verbs, proof harness architecture, or token
  brokerage.
