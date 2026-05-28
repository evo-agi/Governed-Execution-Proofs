# Workflow Authority Rejects Stale Action Intent

## Current evidence status

Current proof evidence:

- Codex-reported deterministic CP stale-action tests passed in
  `.docs/deterministic-validation-2026-05-27.md`.
- Optional live/supported-local guarded-intervention commands remain not run.
- No provider-side cancel or intervention effect is claimed.
- No live Temporal, supported-local, Remote Alpha, ES runtime, browser/WebAuthn,
  Docker, Nomad, Vault, or SPIRE behavior is claimed.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

## Scenario summary

This proof documents the smallest governed-execution actionability boundary:
a stale `cancel-current-attempt` intent copied from a UI, report, channel, or
proof snapshot cannot mutate a governed run. Control Plane re-reads
workflow-authoritative state, compares the submitted
`expected_actionability_fingerprint` with the current actionability fingerprint,
and rejects stale intent before mutation.

This module is static proof-planning material. It is not live validation output,
not a generated proof artifact, and not product architecture.

## Operator story

An operator sees an older snapshot showing that the current attempt can be
canceled. Before the operator submits the action, the governed run changes. The
operator's stale request still carries the old
`expected_actionability_fingerprint`. When the request reaches the guarded
Control Plane route, Control Plane re-reads workflow-authoritative state and
rejects the request because the current actionability fingerprint no longer
matches the submitted one.

## What the stale operator saw

- A presentation or evidence surface that appeared to allow
  `cancel-current-attempt`.
- A request body copied from that older surface, including expected run status,
  current-attempt guards, provider-run guard, and stale
  `expected_actionability_fingerprint`.
- Potentially helpful evidence such as UI text, report fields, channel action
  cards, or proof examples.

Those surfaces may inform the operator, but they are not run-control truth.

## What CP re-read as authoritative

Control Plane re-reads the current `ExecutionFlowSnapshot v1` backed by workflow
authority. The authoritative decision inputs are:

- workflow/query state for status and run-control actionability;
- the current actionability fingerprint;
- expected status and pending-action guards;
- current-attempt task, attempt, provider-run id, terminal state, and cancel
  capability;
- the existing guarded `cancel-current-attempt` intervention route.

Supporting anchors:

- `Control Plane: .docs/long-running-operator-mode-contract.md:282-327`
- `Control Plane: .docs/long-running-operator-mode-contract.md:388-444`
- `Control Plane: src/control_plane/snapshots/execution_flow.py:30-66`
- `Control Plane: src/control_plane/snapshots/execution_flow.py:2659-2675`

## Why the stale request was rejected

The request is rejected because the submitted
`expected_actionability_fingerprint` does not match the current snapshot's
actionability fingerprint. The rejection is a before-mutation result: it must
not start Temporal updates, provider cancel calls, attempt manifests, pending
run-control actions, or durable accepted intervention records.

Supporting anchors:

- `Control Plane: .docs/long-running-operator-mode-contract.md:436-444`
- `Control Plane: .docs/long-running-operator-mode-contract.md:480-500`
- `Control Plane: src/control_plane/monitoring/interventions.py:250-280`
- `Control Plane: src/control_plane/monitoring/interventions.py:624-642`
- `Control Plane: tests/test_monitoring_interventions.py:426-523`

## What did not mutate

For the stale request, this scenario expects:

- no provider request;
- no Temporal update started by the stale request;
- no attempt manifest created by the stale request;
- no pending run-control action;
- no durable accepted intervention receipt;
- no proof-generated artifact becoming authority;
- no ES or IM evidence overriding CP workflow state.

The static proof summary represents those facts as example fields only. It does
not claim that any live command passed.

## Optional fresh-request contrast

The scenario may include a fresh-request comparison. If a later request is copied
from the current snapshot and accepted, that accepted result is a guarded Control
Plane receipt. It is not proof that the provider canceled the workload, not proof
of a terminal runtime outcome, and not proof that ES or IM became action
authority.

Supporting anchors:

- `Control Plane: tests/test_monitoring_interventions.py:210-285`
- `Control Plane: tests/test_monitoring_interventions.py:512-523`
- `Control Plane: .docs/architecture.md:104-115`
- `Control Plane: .docs/execution-substrate-integration.md:140-156`

## Authority boundary map

- Control Plane owns workflow state, actionability, guarded intervention
  semantics, intervention receipts, durable intervention history, checkpoints,
  quarantine/restore, escalation, and finalization.
- Execution Substrate owns admission, submit handoff, runtime-profile
  compatibility, lifecycle projection, cancel/result/log evidence, retained
  opaque bundles, and non-secret runtime identity handoff boundaries. ES facts do
  not override CP workflow run-control truth.
- Infrastructure Manager owns bootstrap, readiness, profile emission,
  provenance, support-bundle assembly, and diagnostics. IM outputs do not become
  CP run-control authority or ES runtime authority.
- UI, browser, CLI, report, dashboard, notification, channel, and proof-repo
  surfaces are presentation, guarded-action adapters, or evidence only.

Supporting anchors:

- `Execution Substrate: .docs/mvp.md:40-111`
- `Execution Substrate: .docs/mvp.md:142-170`
- `Execution Substrate: .docs/system_overview/boundaries.md:417-448`
- `Execution Substrate: .docs/system_overview/boundaries.md:482-497`
- `Infrastructure Manager: .docs/architecture.md:5-26`
- `Infrastructure Manager: .docs/architecture.md:58-71`

## Evidence-only artifacts

The following classes may be named only as evidence, projection, diagnostics, or
explicit non-claims:

- UI snapshots, report snippets, dashboard views, channel cards, notification
  records, and proof examples;
- ES producer compatibility, lifecycle projection, outcome evidence, cancel
  evidence, logs evidence, retained result references, and `authority_handoff`
  metadata;
- IM profiles, instance state, bridge records, doctor output, readiness reports,
  support bundles, and redaction summaries;
- local proof outputs, generated summaries, validation summaries, and `.out`
  paths.

## Explicit exclusions

This proof does not prove:

- production readiness;
- high availability or multi-tenancy;
- Remote Alpha readiness;
- live ES execution;
- provider-side cancellation success;
- terminal runtime outcome;
- runtime identity or Vault credential success;
- retained-bundle semantics;
- support-bundle authority;
- WebAuthn, passkey, or browser delivery;
- all intervention verbs;
- proof harness architecture.

It also does not treat preflight or prepare as execution, and it does not treat
runtime identity handoff as token brokerage.
