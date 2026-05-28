# Scenario

## Current evidence status

Current proof evidence:

- Codex-reported 0B no-network plan-only harness-isolation evidence: passed.
- Codex-reported 0C bounded live Remote Alpha `temporal-basic` evidence: passed.
- Confirmed class: CP to ES `temporal-basic` with explicit isolation leases,
  generated runtime config as live `--config`, and no supported-local profile
  re-forwarding.
- Other proof classes require a Proof 0 continuation before parallel live
  execution.
- Support bundle: not part of the Proof 0 ledger.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

This module describes Proof 0 as a generic parallel-proof execution and
harness-isolation policy. Bounded Codex-reported 0B and 0C status is recorded
separately in `.docs/proof0-concurrency-2026-05-27.md`.

This module does not import generated proof output and does not record
Linux-host contact.

## Scenario shape

Proof 0 prepares the proof track for future parallel proof execution, not only
for the next proof. It defines the proof isolation lease that a parent
coordinator must allocate before parallel live proof writers may run.

Read-only planning, inspection, docs, proof-package updates, and post-run audits
may use subagents freely because they do not compete for live runtime
resources. Live proof subagents may run in parallel only when the parent
allocates explicit isolation leases and the proof class has either been
confirmed or is being deliberately tested as a Proof 0 continuation.

Codex-reported 0B covered two no-network plan-only harness-isolation
configurations. Codex-reported 0C covered only two overlapping live Remote
Alpha `temporal-basic` validations under the hardened generated-config/no-profile
invocation shape.

The intended isolation surfaces are:

- proof run id;
- validation output root;
- Control Plane execution run root;
- report root and report index;
- SQLite mirror path;
- Temporal target, namespace, workflow task queue, workspace task queue, and
  dev-server database path;
- fake-model provider URL;
- attempt-manifest and finalization artifact paths.

Other proof classes, including direct ES proofs, runtime identity/Vault proofs,
cancel/failure proofs, IM support-bundle proofs, IM live-refresh proofs, and
destructive/recovery proofs, require a separate Proof 0 continuation before
parallel live execution.

## Authority boundaries

Control Plane owns workflow/run-control state, Temporal shell state, review,
checkpoint, escalation, finalization, and operator semantics.

Execution Substrate owns admission, submission handoff, lifecycle projection,
retained opaque results, and runtime handoff boundaries.

Infrastructure Manager owns readiness, profile, provenance, diagnostics, and
support evidence. IM support-bundle generation is outside Proof 0 core.
Support-bundle generation should snapshot completed evidence and should not run
concurrently with live proof writers unless that class is separately proved.

Generated artifacts, `.out`, reports, traces, logs, support bundles, retained
bundles, profiles, local proof outputs, and validation outputs remain
evidence/projection/diagnostics only. They are not authority.

## Generated artifacts

This module commits no generated proof output. Any later harness-isolation plan
or validation summary must remain evidence-only and must not be treated as a
runtime authority source.
