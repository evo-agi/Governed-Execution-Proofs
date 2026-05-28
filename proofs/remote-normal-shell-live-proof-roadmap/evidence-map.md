# Evidence Map

This map ties the roadmap statements to repo documentation evidence. The proof
module itself is not validation output. The broader roadmap remains
future-facing, while bounded Codex-reported Phase A live evidence and Phase B
post-run audit status are recorded in
`.docs/live-validation-phase-a-2026-05-27.md`.

## Cross-repo MVP boundary freeze

- `Execution Substrate: .docs/mvp.md:44-68` freezes the current MVP ownership story:
  ES owns admission, submission handoff, runtime-profile compatibility,
  Nomad-backed lifecycle projection, retained opaque result bundles, and
  bounded runtime identity/workload credential handoff boundaries. CP owns
  orchestration, Temporal workflow state, review, checkpoint, intervention, and
  finalization semantics. IM owns bootstrap, readiness, provenance, diagnostics,
  and support-bundle assembly only.
- `Execution Substrate: .docs/mvp.md:69-78` also records the Remote Alpha
  non-claim:
  Remote Alpha is not production, not HA, not multi-tenant, not a general remote
  deployment architecture, not remote CP deployment, and not remote
  provisioning or reconciliation.

## ES execution and runtime contract evidence

- `Execution Substrate: PLANS.md:54-60` records the bounded status of
  `control-plane-normal-shell/v1`, the supported-local proof realization, the
  useful credential-flow slice, and Remote Alpha helper/support posture without
  promoting those surfaces into production architecture.
- `Execution Substrate: PLANS.md:67-86` keeps the current Remote Alpha operator
  helper/support posture bounded to workflow/evidence support rather than
  authority, token brokerage, deployment, or reconciliation.
- `Execution Substrate: .docs/system_overview/boundaries.md:415-448` records ES as the
  composition boundary for admission, submission, Nomad lifecycle projection,
  retained opaque bundles, runtime-profile compatibility, and runtime identity
  handoff. It also says generated evidence, reports, traces, logs, support
  bundles, retained bundles, and proof artifacts are non-authoritative
  evidence/projection.
- `Execution Substrate: .docs/system_overview/boundaries.md:452-480` keeps
  runtime identity and Vault handoff workload-side and non-secret, with ES
  excluded from token or credential brokerage and IM limited to diagnostics.
- `Execution Substrate: .docs/system_overview/boundaries.md:539-559` preserves
  `:prepare`, `:contract`, current runtime paths, `authority_handoff`,
  `outcome_evidence`, result retrieval, and `control-plane-normal-shell/v1` as
  bounded compatibility edges that must not widen by drift.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:257-263` keeps
  `:prepare` as bounded preflight with no run object or scheduler handoff.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:386-392` keeps
  `:submit` as the async MVP execution handoff through ES and Nomad.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:523-550` keeps
  status as Nomad-backed projection and outcome evidence as bounded
  evidence/projection.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:600-613` keeps
  `authority_handoff` as non-secret handoff evidence, not scheduler,
  credential, approval, or CP finalization truth.
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:734-794` keeps
  retained results as opaque ES output bundles whose contents are not promoted
  into CP checkpoint, review, finalization, scheduler, credential, or policy
  authority.
- `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:80-102` describes
  the CP consumer path over AGS publish plus ES contract, prepare, submit,
  status, logs, result, and cancel. It preserves the rule that ES facts are
  runtime evidence and CP owns semantic review, checkpoint, hold/resume/reject,
  and terminal run decisions.
- `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:107-137`
  assigns ES admission, runtime-profile, lifecycle projection, retained bundles,
  runtime handoff, and identity/workload-credential handoff to ES while keeping
  CP semantic validation and terminal decisions CP-owned.
- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:29-42`
  records runtime identity handoff ownership: ES selects and delivers the
  bounded workload-visible endpoint, the helper implements the in-task endpoint,
  SPIRE owns identity issuance, Vault owns token/secret/lease issuance after
  workload-side login, and ES does not broker credential payloads.
- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:111-127`
  keeps ES retained bundles, `outcome_evidence`, `authority_handoff`, IM
  profiles, support bundles, logs, traces, reports, `.out` artifacts, and CP
  governance state as evidence/projection only.

## CP integration and profile evidence

- `Control Plane: .docs/execution-substrate-integration.md:3-18` records the current
  CP HTTP client surface for AGS/ES, the producer-declaration compatibility
  gate, the `control-plane-normal-shell/v1` runtime-profile requirement, outcome
  evidence requirements, retained-result materialization, and CP-owned normal
  shell finalization through review.
- `Control Plane: .docs/execution-substrate-integration.md:140-156` records that
  ES producer compatibility, status, outcome evidence, lifecycle projection,
  authority/identity handoff, and retained-result reads remain evidence and do
  not become CP write guards or terminal semantics.
- `Control Plane: .docs/execution-substrate-integration.md:187-190` records that
  CP finalization owns semantic review of retained ES result contents.
- `Control Plane: .docs/invariants.md:12-18` records that ES integration is an
  explicit bounded provider path and that opt-in normal-shell uses
  `control-plane-normal-shell/v1`.
- `Control Plane: .docs/invariants.md:15-16` records that ES producer compatibility,
  outcome evidence, lifecycle projection, and authority/identity handoff facts
  are read evidence only. They must not become intervention preconditions or
  `actions.write_coordination` inputs.
- `Control Plane: .docs/supported-local-operator-runbook.md:9-16` records the
  accepted supported-local remote normal-shell path as bounded and opt-in. It
  keeps the default shell path local, preserves CP Temporal/review/finalization
  authority, and treats generated acceptance reports as evidence rather than
  product architecture.
- `Control Plane: .docs/supported-local-operator-runbook.md:137-142` treats the
  generated golden-path artifact as CP-owned interpretation over evidence CP
  already owns or consumes, not production certification.
- `Control Plane: .docs/remote-supported-host-profile.md:5-15` records the Remote
  Alpha profile contract: CP remains Mac-local, ES/AGS/runtime services run on
  one remote Linux host, direct HTTPS/mTLS is the accepted alpha posture, no
  shared filesystem is assumed, `control-plane-normal-shell/v1` is required,
  and IM readiness cannot become CP run-control authority.
- `Control Plane: .docs/remote-supported-host-profile.md:33-54` records the
  Alpha acceptance invariants, including direct HTTPS/mTLS, required runtime
  profile, Mac-local Temporal, no shared filesystem, and IM readiness as
  provenance only.
- `Control Plane: .docs/remote-supported-host-profile.md:65-75` records that the
  remote profile must not bootstrap or provision a host, imply SSH install
  automation, make IM readiness CP run-control input, or change CP/ES/default
  local-shell semantics.

## IM readiness and support evidence

- `Infrastructure Manager: .docs/architecture.md:5-26` records that IM owns
  supported-local environment bootstrap, readiness checks, profile emission, and
  provenance, but not CP orchestration semantics, ES execution/runtime
  semantics, retained-result contracts, or general infrastructure orchestration.
- `Infrastructure Manager: .docs/architecture.md:49-71` keeps IM out of CP
  orchestration semantics, ES runtime semantics, and general orchestration, and
  keeps generated profiles, doctor output, readiness reports, and support
  bundles as evidence/projection/diagnostics.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:5-35` records Remote
  Alpha 0.3 as a pre-live alpha. It may emit profiles, doctor output, readiness
  reports, live-refresh evidence, and support bundles, but it does not install
  or provision remote hosts, run a governed live job by itself, or claim CP
  run-control or ES runtime authority.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:81-103` keeps
  doctor output environment-provenance-only and authority flags false for CP
  run-control, ES runtime authority, remote SSH install automation, and remote
  host provisioning.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:147-173` keeps
  copied CP proof artifacts bounded to fixed-stage evidence and profile-lineage
  compatibility checks, not replacement proof lineage.
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:6-25`
  records support-bundle ownership and redaction boundaries. IM owns top-level
  assembly UX and final deny scan, CP and ES own their sections, and the bundle
  remains diagnostics/provenance rather than run-control or runtime authority.
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:221-246`
  keeps live support-bundle collection as copying repo-local evidence with
  digest and byte-count provenance, not live mutation, proof, or readiness by
  itself.

## Roadmap validation evidence classes

Future validation should collect only summarized, redacted, non-secret evidence
classes:

- remote profile diagnostics and proof-profile lineage;
- IM doctor and readiness stage summaries;
- ES producer-declaration compatibility summary;
- AGS publish digest facts;
- ES prepare result and submit receipt summary;
- ES status/outcome/lifecycle/authority-handoff summary;
- retained-result fetch and CP materialization summary;
- CP workflow history summary, review/finalization summary, and terminal
  `ExecutionFlowSnapshot v1` summary;
- operator narrative and machine-readable proof summary.

Future validation must not copy raw generated payloads into this proof module.

## Proof repo convention

- `Governed Execution Proofs: .docs/proof-module-conventions.md:11-38`
  records isolated module layout and the static/example-first validation
  default.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:40-60`
  records CP, ES, IM, generated-output, and presentation-surface authority and
  evidence labels.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:111-119`
  says the convention doc does not create product architecture and keeps Remote
  Alpha bounded, pre-live, and not production, HA, multi-tenant, provisioning,
  reconciliation, or general deployment architecture.

## Evidence quality notes

- Evidence references above are repo-relative labels, not local absolute paths.
- The evidence was inspected as safe authored documentation.
- This module does not include live run data, retained bundles, support bundles,
  raw logs, raw reports, raw traces, raw prompts, raw model outputs,
  credentials, local absolute paths, or generated artifact payloads.
- If CP, ES, or IM docs disagree during future validation, stop and surface the
  conflict rather than working around it in the proof narrative.
