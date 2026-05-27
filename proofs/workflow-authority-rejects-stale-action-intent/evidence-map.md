# Evidence Map

This map ties the proof statements to repo evidence. The proof module itself is
not validation output. Tests were not run during module creation. Line
references are source-inspection anchors and should be re-audited after repo
changes.

## CP workflow/actionability authority

- `Control Plane: .docs/long-running-operator-mode-contract.md:282-286`
  freezes Temporal workflow query state as owner of Control Plane status,
  current-attempt pointer, pending action, and durable intervention history.
- `Control Plane: .docs/long-running-operator-mode-contract.md:290-306`
  allows matching ES producer/runtime/lifecycle/authority/identity facts as
  evidence only and says they do not override workflow run-control truth.
- `Control Plane: .docs/long-running-operator-mode-contract.md:319-327`
  keeps workflow-backed current state as the actionability source, prevents
  projection fallback from re-enabling actions, and keeps unavailable workflow
  authority disabled for operator writes.
- `Control Plane: .docs/long-running-operator-mode-contract.md:388-402`
  says rendered guidance is not write authority, `actions.allowed` drives
  enabled controls, and operator narrative summaries are derived read-model copy.
- `Control Plane: .docs/long-running-operator-mode-contract.md:404-425`
  defines `actions.write_coordination` as a narrow
  actionability-fingerprint guard rather than snapshot-wide versioning, with ES
  lifecycle, authority-path, identity-handoff, and raw observation metadata
  outside the fingerprint.
- `Control Plane: .docs/long-running-operator-mode-contract.md:436-444`
  requires write requests to copy current expected-state guards from the latest
  snapshot and reject stale supplied fingerprints without inventing a global
  version.
- `Control Plane: src/control_plane/snapshots/execution_flow.py:30-66`
  lists the actionability fingerprint fields, including CP identity, status,
  pending action, current-attempt identity/state, cancel capability, allowed
  actions, and wrapper provenance.
- `Control Plane: src/control_plane/snapshots/execution_flow.py:2659-2675`
  builds the write-coordination payload and emits the fingerprint only when
  authority is available.

## CP guarded intervention mechanics

- `Control Plane: src/control_plane/monitoring/app.py:690-715` defines the
  guarded `POST /api/runs/{run_id}/interventions/cancel-current-attempt` route
  and delegates to `handle_intervention`.
- `Control Plane: src/control_plane/monitoring/interventions.py:250-280`
  validates workflow authority, route ownership, actionability fingerprint,
  expected status, pending action, and route target before mutation.
- `Control Plane: src/control_plane/monitoring/interventions.py:379-420`
  validates current-attempt guards: visible nonterminal attempt,
  `execution_substrate` provider, task id, attempt, provider-run id, and cancel
  capability.
- `Control Plane: src/control_plane/monitoring/interventions.py:624-642`
  compares the submitted `expected_actionability_fingerprint` to the current
  snapshot actionability fingerprint and tells callers to refresh the run
  snapshot on mismatch.
- `Control Plane: .docs/long-running-operator-mode-contract.md:480-500`
  requires stale or mismatched fingerprint rejections to be before-mutation
  receipts with no Temporal update, provider cancel call, attempt manifest,
  pending run-control action, or durable accepted intervention record.

## CP stale rejection and fresh action tests

- `Control Plane: tests/test_monitoring_interventions.py:426-460` covers a
  request copied from a stale snapshot: stale fingerprint, HTTP 409, rejected
  decision, `effect_status=none`, and `not_observed` effect observation.
- `Control Plane: tests/test_monitoring_interventions.py:463-523` covers a
  mismatched fingerprint rejected before mutation: no provider request, no
  executor call, no substrate directory, no last intervention receipt, no
  pending action, valid cancel remains available, and a later current-fingerprint
  request is accepted.
- `Control Plane: tests/test_monitoring_interventions.py:210-304` covers a
  fresh guarded cancel using the snapshot fingerprint and durable request
  context.
- `Control Plane: tests/test_execution_flow_snapshot.py:301-390` freezes the
  fingerprint surface by ignoring read-metadata churn and changing on decisive
  actionability fields.
- `Control Plane: tests/test_monitoring_run_console.py:722-757` shows console
  templates include current-attempt guards and the expected actionability
  fingerprint for cancel and running reject.

## CP presentation/channel/artifact boundaries

- `Control Plane: .docs/invariants.md:112-113` classifies report/artifact
  serving boundaries and browser state-changing route protections.
- `Control Plane: .docs/invariants.md:123-126` freezes single-run intervention
  route guards and keeps channel action-adapter payloads as deterministic
  presentation-only projections over `ExecutionFlowSnapshot v1`.
  This proof uses those artifact, route, and channel boundary rules only; it
  does not rely on WebAuthn/passkey validation statements in neighboring lines.
- `Control Plane: .docs/invariants.md:151-157` keeps monitoring pages and
  metrics read-only over workflow authority and evidence, and says channel/app
  delivery evidence must not become actionability truth or intervention truth.
- `Control Plane: src/control_plane/channels/action_adapter.py:120-199` renders
  channel actionability and action intents as read-model-only payloads, with
  stale writes rejected by the existing guarded intervention API and delivery
  classified as non-authoritative notification only.

## ES boundary and non-authority evidence

- `Execution Substrate: .docs/mvp.md:44-60` freezes ES as the core admission,
  submit, lifecycle-projection, retained-result, runtime-profile, and
  runtime-handoff owner while CP owns orchestration, workflow state, review,
  checkpoint, finalization, intervention, and operator-facing control semantics.
- `Execution Substrate: .docs/mvp.md:62-78` keeps IM as bootstrap, readiness,
  provenance, and diagnostics only; keeps UI/report/channel surfaces from
  becoming run truth; and bounds Remote Alpha as pre-live/support posture.
- `Execution Substrate: .docs/mvp.md:82-101` records non-claims for production
  readiness, general remote deployment, generated artifacts as authority, app or
  channel surfaces as run truth, remote provisioning/reconciliation, and proof
  harnesses as ES contract definitions.
- `Execution Substrate: .docs/mvp.md:142-170` classifies CP workflow state and
  intervention fingerprinting as stable contracts, CP/ES integration edges as
  bounded compatibility, and IM profiles/support outputs as
  evidence/projection.
- `Execution Substrate: .docs/mvp.md:237-244` asks whether proof scaffolding is
  clearly labeled so the MVP does not become whatever the proof harness happens
  to do.
- `Execution Substrate: .docs/system_overview/boundaries.md:417-424` keeps
  `:prepare` as preflight, `:submit` as execution handoff, and lifecycle
  projection as an opaque Nomad-backed read projection.
- `Execution Substrate: .docs/system_overview/boundaries.md:432-448` keeps
  retained bundles as opaque output artifacts, `authority_handoff` as non-secret
  evidence only, and runtime identity/Vault handoff workload-side rather than ES
  token or credential brokerage.
- `Execution Substrate: .docs/system_overview/boundaries.md:482-497` states ES
  status/log/result/cancel are evidence or compatibility surfaces, not CP
  workflow truth or intervention authority.
- `Execution Substrate: .docs/system_overview/boundaries.md:541-553` keeps
  prepare/contract/runtime identity and outcome-evidence vocabulary bounded and
  explicitly not token brokerage, durable lifecycle architecture, or broad
  result/log/cancel architecture.

## IM provenance/diagnostics non-authority evidence

- `Infrastructure Manager: .docs/architecture.md:5-26` says Remote Alpha
  readiness is diagnostic and fail-closed, and does not make IM a remote
  reconciler, CP run-control authority, or ES runtime authority.
- `Infrastructure Manager: .docs/architecture.md:58-71` says generated profiles,
  instance state, bridge records, doctor output, readiness reports, and support
  bundles remain evidence/projection/diagnostics unless an explicit contract says
  otherwise.
- `Infrastructure Manager: .docs/architecture.md:126-135` says successful
  preflight and contract probes are not live execution, retained-result,
  Temporal history, Codex, Vault, or workload-identity proof.

## Proof repo convention

- `Governed Execution Proofs: .docs/proof-module-conventions.md:11-38`
  records isolated module layout and the static/example-first validation
  default.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:74-96`
  records repo-relative evidence-reference rules and sensitive/generated
  artifact exclusions.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:111-119`
  says the convention doc does not create a shared proof framework, product
  schema, validation runner, generated artifact contract, or product
  architecture.

## Evidence quality notes

- Repo evidence above was inspected as safe text/source/test material.
- The line references are anchors, not immutable citations. Re-audit them after
  CP, ES, IM, or proof-repo changes.
- This module does not claim that any tests or validation commands passed.
- This module does not include live run data, retained bundles, support bundles,
  raw logs, raw reports, raw traces, raw prompts, raw model outputs, credentials,
  or `.out` payloads.
