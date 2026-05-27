# Evidence Map

This map ties the static proof statements to repo evidence. The proof module
itself is not validation output. Tests were not run during module creation. Line
references are source-inspection anchors and should be re-audited after repo
changes.

## Documentation posture

- `Execution Substrate: AGENTS.md:54-63` requires agents to consult `PLANS.md`
  and the relevant `.docs/` pages, identify affected contracts, invariants,
  boundaries, lifecycle rules, and seam classifications, and surface conflicts.
- `Execution Substrate: AGENTS.md:102-111` requires implementation work to prefer
  documented contracts, keep compatibility edges explicit, and avoid bypassing
  governance, storage, policy, or lifecycle authority boundaries.
- `Execution Substrate: PLANS.md:54-60` records the current bounded slice posture:
  ES owns governed Docker/Nomad runtime realization and runtime handoff
  boundaries, while CP owns orchestration, review, checkpoint, and finalization
  semantics.
- `Execution Substrate: PLANS.md:67-86` keeps Remote Alpha operator/support
  helpers as bounded workflow/evidence surfaces rather than authority sources,
  token brokers, deployment systems, or reconciliation systems.
- `Execution Substrate: .docs/mvp.md:44-60` freezes the current MVP ownership
  split: ES owns admission, submission, lifecycle projection, retained opaque
  result bundles, runtime-profile compatibility, and runtime handoff; CP owns
  orchestration, Temporal workflow state, review, checkpoint, finalization,
  intervention, and operator-facing control semantics.
- `Execution Substrate: .docs/mvp.md:62-78` keeps IM evidence/projection
  diagnostic-only, keeps presentation surfaces from becoming run truth, and
  bounds Remote Alpha as pre-live/support posture rather than production, HA,
  multi-tenant, or general deployment architecture.
- `Execution Substrate: .docs/mvp.md:80-101` records non-claims for production
  readiness, general remote deployment, generated artifacts as authority, and
  proof harnesses as ES contract definitions.

## ES envelope surface classification

- `Execution Substrate: .docs/mvp.md:120-138` classifies ES admission,
  submission, lifecycle projection, retained results, and runtime handoff
  boundaries; specifically, producer contract is a compatibility edge, prepare
  is bounded preflight, submit is the MVP execution handoff, status is
  Nomad-backed projection, `outcome_evidence` is evidence vocabulary, and
  retained result bundles are opaque ES-owned output artifacts whose contents
  CP may interpret semantically.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:111-123`
  inventories the current endpoints and their high-level ownership labels:
  producer contract, prepare, submit, status, logs, result, and cancel.
- `Execution Substrate: .docs/system_overview/boundaries.md:415-431` records
  `:prepare` and `:submit` as bounded current surfaces, with submit as the
  primary public execution handoff and status exposing only bounded projection
  facts.
- `Execution Substrate: .docs/system_overview/boundaries.md:539-559` labels
  `:prepare`, `:contract`, current runtime paths, `authority_handoff`,
  `outcome_evidence`, result route, normal-shell profile, and CP compatibility
  as temporary compatibility edges that must not widen by drift.

## Producer contract as compatibility declaration

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:171-180` says
  `GET /v1/executions:contract` returns a non-secret, non-run-specific
  declaration for the current governed-execution producer compatibility surface,
  not health, submit readiness, run authority, or a general capability registry.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:224-233`
  says the declaration is read-only and non-secret, is not health, readiness,
  admission proof, lifecycle state, lifecycle write coordination, credential
  possession, policy approval, or scheduler API, and must not expose scheduler,
  host-path, result-path, Vault, Codex, JWT-SVID, lease, or approval details.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:242-248`
  describes it as a narrow compatibility-gate surface that does not create a
  broad capability registry or replace submit-ready checks.
- `Execution Substrate: es/admission/producercontract.go:23-50` implements the
  producer declaration with explicit `non_authority` labels including
  `not_service_health`, `not_submit_readiness`, `not_run_authority`,
  `not_lifecycle_truth`, `not_lifecycle_write_coordination`,
  `not_credential_truth`, `not_policy_truth`, and `not_scheduler_api`.

## Prepare as preflight

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:257-263` says
  `POST /v1/executions:prepare` returns bounded preflight success and creates
  no run object or scheduler handoff.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:318-341`
  records prepare's artifact evidence, runtime-trust, runtime-config, and
  bounded evidence checks, and says prepare does not surface internal
  composition details, does not treat CP review/checkpoint/finalization or
  proof-harness metadata as shared admission facts, and returns preflight
  success only.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:343-350`
  lists explicit non-effects: no run id, no Nomad job or eval id, no scheduler
  handoff, no proto-execution state or durable ES execution record, and no
  workload-vault or identity details returned.
- `Execution Substrate: es/admission/types.go:44-50` documents `PrepareResult`
  as proving admission and preparation facts only, without run ids, scheduler
  metadata, or proto-execution state.

## Submit as runtime handoff

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:386-392` says
  `POST /v1/executions:submit` performs real execution submission and remains
  the MVP execution handoff surface: async, bounded receipt, and Nomad
  submission through ES.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:422-439`
  defines the successful response as a bounded receipt with run id, status, and
  non-secret `authority_handoff`; the receipt confirms handoff, not durable ES
  lifecycle ownership.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:441-447`
  states submit creates no durable ES lifecycle record, no sync execution
  result, no retry/reschedule policy, no richer scheduler abstraction, and no
  live Vault, Codex, SPIRE, lease, token-expiry, or approval state.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:467-475`
  says submit is real but intentionally narrow, async-only, and not an ES-owned
  orchestration, review, checkpoint, or finalization contract.
- `Execution Substrate: es/admission/types.go:52-62` documents `SubmitResult`
  as an async receipt for a real Nomad handoff that intentionally avoids a
  durable execution record or broader lifecycle surface.

## Status, outcome evidence, and authority handoff

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:523-533` defines
  status as a Nomad-backed projection with an opaque same-run
  `lifecycle_projection.revision`, not a scheduler id, lifecycle store, or write
  guard.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:537-543` says
  the status JSON envelope must not add CP run-control grammar or live
  credential/security fields.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:549-550` labels
  `outcome_evidence` as bounded evidence/projection.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:600-613`
  defines `authority_handoff` as additive, read-only, non-secret runtime
  handoff evidence. It is not scheduler truth, credential authority, proof of
  live JWT-SVID/Vault token/secret/lease possession, or CP review, approval,
  checkpoint, or finalization state.
- `Execution Substrate: es/admission/types.go:64-101` documents status,
  lifecycle projection, outcome evidence, and authority handoff as bounded
  read/evidence surfaces rather than durable lifecycle or credential surfaces.

## Result and retained output opacity

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:734-750` says
  result returns a retained terminal result bundle for the bounded slice, ES
  packages retained content opaquely, and ES does not parse CP semantics,
  checkpoint decisions, review outcomes, or finalization metadata from result
  files.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:756-769`
  states retained bundles are stored outside staging under the ES results root,
  keyed by run id, packaged as tar.gz archives, and retained idempotently.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:771-794`
  labels successful result responses as `application/gzip` with
  `es_retained_result_store`, `retained_result_bundle`, and
  `opaque_result_bundle`; the endpoint is not a lifecycle-state registry and
  must not promote bundle contents into CP checkpoint, finalization, review,
  scheduler, credential, or policy authority.
- `Execution Substrate: es/admission/results_test.go:62-147` covers the
  retained-result guardrail that CP-like semantic files remain opaque bundle
  entries and that ES does not synthesize authority sidecars such as workflow,
  checkpoint, scheduler-truth, or authority-handoff metadata.

## Cancel and runtime evidence non-finality

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:817-852` says
  ES cancel is a bounded Nomad stop request with `outcome_evidence`, not CP
  intervention, approval, Temporal, workflow, review, checkpoint, finalization,
  scheduler authority, or live credential/security state.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:864-869` says
  cancel does not create a richer cancellation state model, durable ES
  cancellation record, or proof that the workload has stopped.

## Runtime identity and token exclusions

- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:80-94`
  classifies runtime identity handoff as ES-selected and platform-delivered,
  keeps `authority_handoff` and `outcome_evidence` as non-authority
  evidence/projection, and keeps retained bundles, support bundles, reports,
  traces, logs, profiles, and `.out` artifacts out of runtime identity or
  credential authority.
- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:111-127`
  says ES does not broker Vault tokens, Vault secrets, JWT-SVID payloads,
  leases, Codex credential material, or credential payloads, and that ES
  retained bundles, `outcome_evidence`, `authority_handoff`, IM profiles,
  support bundles, logs, traces, reports, `.out` artifacts, and CP governance
  state are evidence/projection only.
- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:160-176`
  repeats the required evidence exclusions for runtime identity and credential
  authority.

## CP finalization and semantic ownership

- `Execution Substrate: .docs/mvp.md:53-60` assigns orchestration, Temporal
  workflow state, review, checkpoint, finalization, intervention, and
  operator-facing control semantics to Control Plane.
- `Execution Substrate: .docs/mvp.md:144-145` classifies CP workflow state,
  task ledger, run-control semantics, review, policy gates, checkpoints,
  quarantine/restore, escalation, and finalization as CP-owned stable
  contracts.
- `Control Plane: .docs/architecture.md:19-45` describes CP runtime flow with
  task attempts finalized only after terminal observation, OpenAI review,
  checkpoint creation, policy checks, and final audit sequencing.
- `Control Plane: .docs/architecture.md:160-161` says remote finalize is
  CP-owned: CP fetches the ES result bundle, validates and materializes the
  retained workspace, syncs it into CP-owned workspace state, and then runs the
  normal CP review path locally.
- `Control Plane: .docs/execution-substrate-integration.md:19-24` places
  remote start, observe, cancel, retained-result materialization,
  static-script finalize, and normal-shell finalize behind the CP substrate
  adapter, with retained-result bundle schema validation and materialization
  owned on the CP side.
- `Control Plane: .docs/execution-substrate-integration.md:140-150` keeps ES
  producer compatibility, status, outcome evidence, lifecycle projection,
  authority, identity handoff, and retained-result reads as evidence/provenance
  that do not become CP write guards or terminal semantics.
- `Control Plane: .docs/execution-substrate-integration.md:158-160` says ES
  retains the runtime output directory as an opaque tar.gz, while the contents
  are owned and validated by CP.

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
  ES or CP repo changes.
- This module does not claim that any tests or validation commands passed.
- This module does not include live run data, retained bundles, support
  bundles, raw logs, raw reports, raw traces, raw prompts, raw model outputs,
  credentials, local absolute paths, or generated artifact payloads.
