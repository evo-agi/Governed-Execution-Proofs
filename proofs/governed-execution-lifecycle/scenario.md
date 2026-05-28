# Governed Execution Lifecycle

## Current evidence status

Current proof evidence:

- Codex-reported two-pass lifecycle evidence is recorded in
  `.docs/governed-lifecycle-proof-2026-05-28.md`.
- The recorded run ids are
  `governed-lifecycle-temporal-basic-20260527T213519Z` and
  `governed-lifecycle-temporal-basic-20260528T000846Z`.
- Happy-path-twice is complete for the bounded serial `temporal-basic`
  governed execution lifecycle story.
- Independent audit is not claimed.
- Public/demo readiness is not claimed; it requires a final demo-readiness
  audit.
- Cancel/failure/intervention behavior was not run.
- IM support-bundle generation was not run.
- Runtime identity/Vault credential behavior was not run as a dedicated proof.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

## Scenario summary

This module turns the governed execution lifecycle proof from top-level authored
documentation into a first-class proof package. It points to the lifecycle
ledger in `.docs/governed-lifecycle-proof-2026-05-28.md` and the filming
posture in `.docs/governed-lifecycle-filming-script.md` without importing raw
generated artifacts.

The scenario is the CP/Temporal -> ES -> Nomad/Linux lifecycle narrative for one
bounded `temporal-basic` normal-shell path:

1. Control Plane owns the Temporal workflow, run-control state, review,
   materialization, and finalization.
2. Control Plane packages a normal-shell attempt for
   `control-plane-normal-shell/v1`.
3. Control Plane checks the ES producer contract before runtime handoff.
4. ES owns prepare/admission, submit handoff, lifecycle projection,
   result/retained-result evidence, and runtime handoff metadata.
5. Nomad/Linux runtime execution happens after ES submit.
6. CP consumes ES evidence, materializes retained results by safe metadata, and
   performs CP-owned review/finalization.

The proof is about the governed lifecycle boundary, not autonomous software
development and not general deployment architecture. It records that two bounded
serial happy-path rehearsals completed, while preserving the distinction between
CP authority, ES evidence/projection, runtime execution, and IM diagnostics.

## Authority boundaries

- **CP authority**: Temporal workflow state, guarded run-control, review,
  materialization, checkpoint/finalization semantics, and operator-facing
  decisions.
- **ES authority**: producer compatibility, prepare/admission, submit handoff,
  lifecycle projection, outcome/result evidence, retained opaque result refs,
  and runtime handoff boundaries.
- **Runtime authority**: Nomad/Linux execution after submit.
- **IM diagnostics**: profile, readiness, provenance, and support-bundle
  material when separately run; no IM support-bundle proof is claimed here.

ES lifecycle/status/result facts do not become CP finalization. IM diagnostics
do not become CP run-control truth or ES runtime authority.

## Generated artifact posture

Generated outputs, reports, traces, logs, retained bundles, Temporal DB files,
and validation outputs are evidence/projection/diagnostics only. This module
records authored references, run ids from the ledger, and path classes only; it
does not copy raw summaries, raw reports, raw logs, retained payloads, prompts,
model outputs, workspaces, databases, credentials, endpoint values, or local
process records.
