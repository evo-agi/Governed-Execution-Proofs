# Claims

Validation status: this module is static/example-first. No ES, CP, IM, pytest,
Go test, supported-local, Remote Alpha, Docker, Nomad, Vault, SPIRE, Temporal,
server, setup, bringup, proof, or validation commands have been run for this
proof module.

## Supported claims

This proof module may make these narrow claims:

- ES producer contract is a compatibility declaration, not health, readiness,
  run authority, scheduler API, policy truth, credential truth, or CP
  finalization.
- ES prepare is bounded preflight and creates no run id, scheduler handoff,
  proto-execution state, durable ES execution record, or CP semantic state.
- ES submit is a bounded async runtime handoff through ES and the scheduler; the
  receipt is not a durable ES lifecycle model or CP finalization record.
- ES status is runtime projection/evidence. `lifecycle_projection.revision` is
  opaque same-run read coordination and must not be used as a write guard.
- ES `outcome_evidence` is an additive evidence/projection label surface, not
  scheduler authority, lifecycle write coordination, policy truth, credential
  truth, or CP workflow truth.
- ES retained result bundles are opaque output artifacts owned by ES as retained
  envelopes; CP may materialize and interpret their contents semantically above
  the ES boundary.
- CP alone owns orchestration, workflow state, review, checkpoints,
  intervention semantics, semantic finalization, and operator-facing control
  semantics.
- `authority_handoff`, when present, is bounded non-secret runtime handoff
  evidence only.

## Explicit non-claims

This proof module must not claim:

- live ES validation;
- production readiness;
- provider or runtime success;
- CP finalization proof;
- retained-bundle semantic interpretation;
- credential or token brokerage proof;
- Remote Alpha proof;
- service health or submit readiness;
- artifact-specific admission proof beyond static prepare-label discussion;
- successful scheduler placement;
- terminal runtime outcome;
- live status/result/cancel behavior;
- live retained-result availability;
- Vault, SPIRE, JWT-SVID, Codex credential, lease, or secret success;
- WebAuthn, passkey, browser, channel, notification, or app delivery;
- high availability;
- multi-tenancy;
- proof harness behavior as product architecture;
- all ES endpoints as final architecture;
- all CP intervention verbs;
- IM ownership of CP run-control truth or ES runtime truth.

## Authority owners

### ES-owned envelope labels

Execution Substrate owns the bounded public execution envelope labels used by
this scenario:

- producer compatibility declaration;
- prepare preflight;
- async submit/runtime handoff;
- status lifecycle projection;
- outcome evidence;
- non-secret runtime `authority_handoff` evidence;
- retained opaque result bundle envelope.

Evidence anchors:

- `Execution Substrate: .docs/mvp.md:44-52`
- `Execution Substrate: .docs/mvp.md:120-138`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:111-123`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:171-248`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:257-376`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:386-475`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:485-650`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:734-815`

### CP-owned semantic authority

Control Plane owns semantic governance above ES:

- orchestration and Temporal workflow state;
- task progression and current-attempt control semantics;
- review, checkpoint, quarantine/restore, escalation, and finalization;
- materialization and semantic validation of retained result contents;
- guarded intervention semantics.

Evidence anchors:

- `Execution Substrate: .docs/mvp.md:53-60`
- `Execution Substrate: .docs/mvp.md:144-145`
- `Control Plane: .docs/architecture.md:19-45`
- `Control Plane: .docs/architecture.md:160-161`
- `Control Plane: .docs/execution-substrate-integration.md:19-24`
- `Control Plane: .docs/execution-substrate-integration.md:140-150`

### Evidence/projection-only classes

The proof must label these as evidence or projection only:

- ES lifecycle projection;
- ES outcome evidence;
- ES logs/result/cancel evidence;
- ES retained bundle references and retained bundle payload class;
- ES `authority_handoff`;
- generated proof summaries;
- validation summaries;
- reports and traces;
- support bundles;
- `.out` classes;
- IM readiness/profile/provenance/support outputs;
- UI, browser, CLI, app, notification, channel, dashboard, and report surfaces.

## Sensitive/generated classes excluded

The proof must exclude these classes:

- raw `.out` contents;
- raw logs, traces, and reports;
- retained bundles and support bundles;
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

## Claim-review checklist

Before publication or later validation, verify:

- Does the text keep ES envelope labels distinct from CP finalization?
- Does the text say producer contract is compatibility declaration only?
- Does the text say prepare is preflight only?
- Does the text say submit is runtime handoff only?
- Does the text label status/result/cancel/log facts as evidence or projection?
- Does the text keep retained bundle contents opaque to ES?
- Does the text make CP the semantic review/finalization owner?
- Does the text avoid claiming live validation, provider success, Remote Alpha,
  production readiness, token brokerage, or credential success?
- Does the text exclude raw generated and sensitive artifact classes?
- Does the text avoid turning the proof module into a shared framework or
  product schema?
