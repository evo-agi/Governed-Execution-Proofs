# Claims

Validation status: this module is static/example-first. It defines a future
remote normal-shell live proof roadmap and validation contract. It does not
claim that the proof has run.

## Supported claims

This module may make these narrow claims:

- A future capstone proof package has a defined intended sequence for CP
  Temporal shell, AGS publish, ES prepare/submit, Nomad/Docker execution,
  runtime identity and Vault handoff, retained result, CP review/finalization,
  operator evidence, machine-readable summary, and public narrative.
- The future proof must keep Control Plane, Execution Substrate, Infrastructure
  Manager, AGS, Nomad, Docker, SPIRE, and Vault authority boundaries explicit.
- The future proof must label ES lifecycle, outcome, retained-result, and
  `authority_handoff` facts as ES evidence/projection unless an ES contract says
  otherwise.
- The future proof must label IM profile, readiness, doctor, and support-bundle
  surfaces as provenance/diagnostics only.
- The future proof must treat CP workflow state, review, checkpoint, guarded
  intervention, and finalization as CP-owned semantics.
- The future proof must require the `control-plane-normal-shell/v1` runtime
  profile for the governed normal-shell path.
- The future proof must require producer-declaration compatibility before real
  AGS publish, ES prepare, ES submit, or real attempt-manifest creation.
- The future proof must treat retained ES bundles as opaque until CP performs
  semantic materialization, review, and finalization.
- The future proof must exclude raw generated and sensitive artifact classes
  from committed proof material.
- The machine-readable example in this module is synthetic and may be used only
  as a schema-shaped planning example.

## Explicit non-claims

This module must not claim:

- live Linux validation yet;
- production readiness;
- high availability;
- multi-tenancy;
- a general deployment architecture;
- remote provisioning, remote SSH install automation, or a remote reconciler;
- remote Control Plane deployment;
- a default-path flip from local shell to remote normal shell;
- live governed execution success;
- AGS publish success;
- ES prepare or submit success;
- Nomad placement success;
- Docker workload success;
- runtime identity credential success until validated;
- Vault workload login, token, lease, secret-read, or Codex credential success
  until validated;
- ES Vault token brokerage;
- retained result semantic finalization until CP performs it;
- support-bundle authority;
- IM ownership of CP run-control truth or ES runtime truth;
- CP ownership of ES admission, runtime, lifecycle, or retained-result
  contracts;
- proof-harness behavior as product architecture;
- generated artifacts, reports, traces, logs, support bundles, retained bundles,
  or profiles as orchestration authority.

## Authority owners

### CP authority

Control Plane owns:

- Temporal workflow state;
- task progression and task-attempt state;
- review, revision, checkpoint, hold/resume/reject, escalation, and
  finalization semantics;
- guarded intervention write coordination;
- operator-facing run-control decisions;
- semantic interpretation of retained result contents.

Evidence anchors:

- `Control Plane: .docs/invariants.md`
- `Control Plane: .docs/execution-substrate-integration.md`
- `Control Plane: .docs/supported-local-operator-runbook.md`
- `Control Plane: .docs/remote-supported-host-profile.md`

### AGS and ES authority

AGS owns publication assembly and publication facts. ES owns:

- public admission, prepare, and submit handoff surfaces;
- runtime-profile compatibility for `control-plane-normal-shell/v1`;
- Nomad-backed lifecycle projection;
- outcome evidence on current lifecycle/log/result/cancel surfaces;
- retained opaque result bundles;
- bounded non-secret runtime identity and workload credential handoff
  boundaries.

Evidence anchors:

- `Execution Substrate: PLANS.md`
- `Execution Substrate: .docs/mvp.md`
- `Execution Substrate: .docs/system_overview/boundaries.md`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md`
- `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md`

### Runtime authority

Nomad owns scheduler placement and task lifecycle. Docker owns container
execution mechanics. SPIRE owns identity issuance and SVID material. Vault owns
token, secret, and lease issuance after workload-side login.

Evidence anchors:

- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md`

### IM provenance and diagnostics

Infrastructure Manager owns profile emission, doctor vocabulary, readiness
reporting, support-bundle assembly, redaction, and environment provenance. Those
outputs remain diagnostics/provenance unless a specific owning contract says
otherwise.

Evidence anchors:

- `Infrastructure Manager: .docs/architecture.md`
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md`
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md`

## Evidence/projection-only classes

The proof must label these as evidence, projection, diagnostics, compatibility,
or operator narrative only:

- generated artifacts;
- profiles and profile lineage;
- doctor output and readiness reports;
- support bundles and redaction summaries;
- logs, traces, reports, and summaries;
- retained result references and retained bundles;
- ES lifecycle projections and projection revisions;
- ES outcome evidence;
- ES `authority_handoff` metadata;
- CP attempt manifests and proof summaries;
- operator UI, dashboard, browser, notification, and public-writing surfaces.

## Sensitive/generated classes excluded

The proof must exclude these classes from committed module files:

- raw generated artifact contents;
- `.out` contents;
- raw logs, traces, reports, retained bundles, support bundles, and archives;
- databases and local process records;
- env files;
- keys, certificates, tokens, secrets, API keys, bearer material, and credential
  payloads;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, and private-key material;
- raw prompts and raw model outputs;
- raw Codex stdout, stderr, final, review, audit, or metadata payloads;
- workspaces, checkpoint directories, quarantine directories, and restore
  directories;
- real run ids, real provider ids, real hashes, real bundle references, local
  absolute paths, and remote filesystem paths.

## Claim-review checklist

Before publication or validation, verify:

- Does the text keep this module at `not_run` until a later validation pass is
  explicitly executed and recorded?
- Does the text preserve CP as workflow/review/finalization authority?
- Does the text preserve ES as admission/runtime/lifecycle/retained-bundle
  authority without giving ES CP finalization semantics?
- Does the text preserve IM outputs as provenance/diagnostics only?
- Does the text avoid claiming runtime identity or Vault credential success
  before same-run validation exists?
- Does the text avoid treating support bundles as authority?
- Does the text avoid real ids, real hashes, local absolute paths, raw artifact
  payloads, and sensitive material?
- Does the text stop and surface conflicts rather than widening governance
  boundaries?

