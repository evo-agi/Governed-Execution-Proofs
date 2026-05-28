# Public Writing Map

## What the proof demonstrates

With the current evidence status, Proof 0 demonstrates that the proof track has
an authored generic parallel-proof execution and harness-isolation policy plus
bounded Codex-reported 0B and 0C evidence.

Public writing may also describe bounded Codex-reported 0B and 0C status from
`.docs/proof0-concurrency-2026-05-27.md`: 0B as no-network plan-only
harness-isolation evidence, and 0C as the CP to ES `temporal-basic` class under
the hardened generated-config/no-profile invocation. That wording must remain
bounded, non-independent, and evidence-only.

## What the proof does not demonstrate

Proof 0 does not demonstrate live Temporal behavior beyond the bounded
Codex-reported 0C path, supported-local behavior beyond that path, Remote Alpha
behavior beyond that path, Linux-host behavior, Docker, Nomad, Vault, SPIRE,
fake-model service behavior, ES runtime success, provider success, production
readiness, high availability, multi-tenancy, public/demo readiness,
independent audit, default shared-config safety, all interleavings, or general
parallel proof coverage.

Direct ES proofs, runtime identity/Vault proofs, cancel/failure proofs, IM
support-bundle proofs, IM live-refresh proofs, and destructive/recovery proofs
are not automatically covered.

## Authority boundaries

Public writing must preserve these labels:

- CP workflow/run-control state remains Control Plane authority.
- ES admission, submission handoff, lifecycle projection, retained opaque
  result, and runtime handoff remain Execution Substrate boundaries.
- IM readiness, profile, provenance, diagnostics, and support evidence remain
  Infrastructure Manager diagnostics/provenance/evidence.
- Generated `.out`, reports, traces, profiles, retained bundles, support
  bundles, local proof outputs, and validation outputs remain
  evidence/projection/diagnostics only.
- Support bundles should snapshot completed evidence and should not overlap
  live proof writers unless separately proved.

## Wording to avoid

Avoid saying that Proof 0 has an independently inspected pass, that Proof 0
parallelism covers all future proofs, that Remote Alpha is production ready,
that the proof harness is product architecture, that support bundles can run
concurrently with live proof writers, or that generated outputs are authority.

## Documentation posture

Public writing should describe the static example as `validation_status:
"not_run"` and the 0B/0C ledger as Codex-reported bounded evidence. Claims must
stay tied to the proof class that was actually recorded.
