# IM Support Packet Is Evidence, Not Authority

## Scenario summary

This proof documents the Infrastructure Manager support-packet boundary:
readiness, profile, doctor, support-bundle, redaction, and digest outputs help
explain environment provenance and diagnostics, but they do not become Control
Plane run-control truth or Execution Substrate runtime authority.

This module is static proof-planning material. It is not live validation output,
not a generated support bundle, not copied bundle content, and not product
architecture.

## Operator story

An operator receives an IM support packet for a Remote Supported-Host Alpha
environment. The packet can show profile identity, readiness posture, doctor
stage status, copied summary evidence, redaction results, and digest-first
provenance. Those facts may help triage why an environment looks usable,
blocked, or not proven yet.

The operator must not treat that packet as permission to mutate a governed run,
as proof that a live host was contacted by this proof module, as a provisioning
or reconciliation instruction, or as proof that ES runtime behavior occurred.

## What the support packet may explain

- IM provenance: emitted profile shape, doctor vocabulary, readiness report
  posture, bundle assembly layout, redaction policy, and digest manifest.
- CP evidence: profile diagnostic summaries and copied proof-lineage references
  when a separate CP-owned artifact has already supplied them.
- ES evidence/projection: producer-contract summaries, health/readiness
  summaries, lifecycle/status/result/cancel evidence, hardening check-only
  evidence, and helper staging provenance when separately emitted by ES-owned
  surfaces.
- Shareability guardrails: deny scans, redaction counts, byte counts, and
  digest-first identity for copied summary artifacts.

These are evidence, projection, diagnostics, or packaging facts. They are not
run-control or runtime authority.

## Authority boundary map

- Control Plane authority: workflow/query state, guarded operator writes,
  actionability, request guards, intervention receipts, durable workflow-owned
  history, review, checkpoints, escalation, and finalization.
- Execution Substrate authority: admission, prepare/submit handoff, runtime
  profile compatibility, Nomad-backed lifecycle projection, runtime handoff
  boundaries, cancel/result/log evidence, and retained opaque output bundles.
- Infrastructure Manager ownership: bootstrap, readiness, profile emission,
  doctor vocabulary, environment provenance, support-bundle assembly, redaction,
  digest manifesting, and diagnostics.
- Support packet classification: evidence packet only. It can summarize and
  label copied evidence, but it does not re-own the semantics of CP or ES facts.

Supporting anchors:

- `Infrastructure Manager: README.md`
- `Infrastructure Manager: .docs/architecture.md`
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md`
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md`
- `Execution Substrate: .docs/mvp.md`
- `Execution Substrate: .docs/system_overview/boundaries.md`
- `Control Plane: .docs/long-running-operator-mode-contract.md`

## What does not happen in this static module

This module does not generate a live support bundle, copy a raw support bundle,
contact a live host, run a readiness refresh, run a CP proof, run ES workload
execution, run provisioning, run reconciliation, or validate Remote Alpha
production readiness.

The example summary uses synthetic ids only and carries
`validation_status: "not_run"`.

## Evidence-only packet result

The support packet can support a narrow statement:

IM support outputs are useful evidence and diagnostics for environment lineage,
but they remain outside CP run-control authority and outside ES runtime
authority unless a separate explicit contract says otherwise.

The packet can make copied artifact identity easier to audit through digests and
redaction reports. A digest proves identity of copied bytes in the packet
context; it does not prove live host truth, CP actionability, ES runtime success,
or production readiness.

## Explicit exclusions

This proof excludes raw or sensitive generated artifact classes:

- raw support bundles and retained bundles;
- raw logs, traces, reports, prompts, model outputs, and review/audit payloads;
- `.out` payloads, archives, databases, environment files, and local process
  records;
- keys, certificates, tokens, bearer material, API keys, TLS, SPIFFE, Vault,
  WebAuthn, and passkey material;
- workspaces, checkpoints, quarantines, and restores;
- real run ids, real provider ids, real hashes, and local absolute paths.

## Validation status

Current status: `not_run`.

No tests, scripts, servers, bringup commands, proof commands, validation
commands, Docker, Nomad, Vault, SPIRE, Temporal, supported-local commands,
remote-alpha commands, live host commands, or support-bundle commands were run
to create this module.
