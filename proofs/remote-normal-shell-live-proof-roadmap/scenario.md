# Remote Normal-Shell Live Proof Roadmap

## Current evidence status

Current proof evidence:

- The roadmap remains broader and future-facing.
- Phase A Codex-reported live evidence exists for one bounded Remote Alpha
  `temporal-basic` CP Temporal normal-shell path.
- Phase B post-run audit is recorded separately.
- Codex-reported two-pass governed lifecycle evidence is recorded in
  `.docs/governed-lifecycle-proof-2026-05-28.md`.
- Support bundle: deferred.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

## Scenario summary

This module defines the broader future capstone proof package for the remote
Linux host path. It is a roadmap and validation contract with bounded Phase A
live evidence and a Codex-reported two-pass lifecycle ledger recorded
separately; it does not claim that the full roadmap proof has already run.

The future proof is expected to cover one bounded, opt-in Control Plane
normal-shell task attempt through the remote governed-execution path:

1. Control Plane starts and owns the Temporal shell workflow.
2. Control Plane packages a normal-shell task attempt for the explicit
   `control-plane-normal-shell/v1` runtime profile.
3. Control Plane gates the attempt on the ES producer declaration.
4. Control Plane publishes the runtime package through AGS.
5. Control Plane calls ES `prepare` and then ES `submit`.
6. ES submits the governed execution to Nomad.
7. Nomad places the task and Docker runs the workload on the remote Linux host.
8. ES delivers the bounded runtime identity handoff surface to the workload.
9. The workload performs any Vault credential access through workload-side
   runtime identity behavior, not through ES token brokerage.
10. ES retains the opaque result bundle.
11. Control Plane fetches and materializes the retained result, then performs
    CP-owned review, checkpointing, and finalization semantics.
12. Operator evidence, a machine-readable proof summary, and a human-readable
    narrative are produced with explicit authority and non-authority labels.

The proof package must remain honest about which parts are authority, which
parts are evidence or projection, and which parts were not validated.

## Remote posture

The target posture is Remote Supported-Host Alpha, not production deployment.
Control Plane API, UI, workers, run root, review/finalization, run-control
decisions, and Temporal remain Mac-local for the alpha posture. Execution
Substrate services, AGS, Nomad, Docker, SPIRE, Vault, and runtime support run on
one remote Linux host. Control Plane reaches AGS and ES over direct HTTPS with
mTLS. No shared filesystem is assumed between Control Plane and the remote host.

Supporting anchors:

- `Control Plane: .docs/remote-supported-host-profile.md`
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md`
- `Execution Substrate: .docs/mvp.md`

## Future operator story

An operator selects the opt-in remote normal-shell path for a governed run. The
run starts as a Control Plane Temporal shell workflow. The workflow packages one
task attempt, confirms that the pointed-at ES instance declares the expected
current governed-execution producer contract, publishes the package through AGS,
calls ES `prepare`, and then calls ES `submit`.

ES admits and realizes the execution through its governed runtime boundary. ES
hands the task to Nomad, Nomad places it, Docker runs it, the platform-owned
runtime identity endpoint is exposed through the bounded
`EXEC_WORKLOAD_IDENTITY_ENDPOINT` contract, and the workload uses workload-side
Vault login/read behavior when credential material is required. ES does not
broker Vault tokens or Codex credentials.

When the provider reaches a terminal state, Control Plane observes ES lifecycle
projection and outcome evidence, fetches the retained opaque result bundle,
materializes it under CP-owned semantics, and performs review, checkpoint, and
finalization. Any operator-facing report then separates the immediate provider
evidence from the CP-owned terminal run decision.

## Authority labels

- **CP authority**: Temporal workflow state, task progression, review,
  checkpoints, hold/resume/reject/cancel intervention semantics,
  operator-facing run-control decisions, retained-result semantic
  interpretation, and finalization.
- **AGS authority**: publication assembly and publication response facts for
  the submitted artifact package.
- **ES authority**: admission, prepare, submit handoff, runtime-profile
  compatibility, Nomad-backed lifecycle projection, outcome-evidence
  envelopes, retained opaque result bundles, and bounded runtime identity
  handoff boundaries.
- **Nomad authority**: scheduler placement and task lifecycle observed by ES.
- **Docker authority**: container execution mechanics observed through the
  governed runtime path.
- **SPIRE authority**: identity issuance and SVID material.
- **Vault authority**: token, secret, and lease issuance after workload-side
  login.
- **IM provenance/diagnostics**: profile emission, doctor stages, readiness
  reports, support-bundle assembly, redaction, and provenance.

## Evidence and projection labels

The future proof may use these only as evidence, projection, diagnostics, or
bounded compatibility facts:

- ES producer declaration compatibility;
- AGS publish response digest facts;
- ES prepare success;
- ES submit receipt;
- ES lifecycle projection and opaque projection revision;
- ES outcome evidence on status, cancel, logs, and result;
- ES non-secret `authority_handoff` metadata;
- retained-result references and retained opaque bundle fetch status;
- Control Plane attempt manifests and read-model summaries;
- IM remote profile, doctor output, readiness report, support-bundle metadata,
  and proof-profile lineage;
- operator narrative, diagrams, and proof summaries.

These surfaces may inform the proof. They must not become CP run-control truth,
ES runtime authority beyond the owning ES contract, Vault credential truth, or
support-bundle authority.

## Future validation success shape

A future passing proof must show, with fresh same-run evidence, that:

- the remote profile and readiness posture matched the Remote Alpha contract;
- CP selected the explicit `execution_substrate` plus `normal_shell` path;
- `control-plane-normal-shell/v1` was required before the real attempt;
- CP accepted the producer declaration before AGS publish, ES prepare, ES
  submit, or real attempt-manifest creation;
- AGS publish, ES prepare, ES submit, Nomad/Docker execution, and ES lifecycle
  observation happened in order;
- runtime identity and Vault credential behavior was validated only through the
  workload-side contract, with no ES token brokerage;
- retained-result fetch and materialization happened before CP semantic
  finalization;
- CP review/finalization, not ES retained-bundle existence, decided the terminal
  Control Plane outcome;
- generated artifacts were summarized with redaction and non-authority labels;
- machine-readable and human-readable summaries remained free of raw sensitive
  payloads.

## Explicit exclusions

This roadmap excludes:

- live validation claims;
- generated artifact contents;
- raw logs, traces, reports, prompts, model outputs, retained bundles, support
  bundles, archives, databases, workspaces, checkpoints, quarantines, restores,
  and local process records;
- env files, key material, certificate bodies, TLS material, SPIFFE material,
  Vault tokens, root tokens, unseal keys, API keys, bearer material, WebAuthn or
  passkey material, JWT-SVID bodies, secret payloads, leases, and Codex
  credential material;
- real run ids, real provider ids, real hashes, real bundle references, local
  absolute paths, or remote filesystem paths as proof payload.
