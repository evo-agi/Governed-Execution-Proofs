# Evidence Map

This map ties the governed execution lifecycle proof claims to authored docs.
The module is not generated output and does not include raw generated artifact
content.

## Claim to evidence map

| Claim | Authored evidence references | Evidence posture |
| --- | --- | --- |
| Two bounded serial governed lifecycle rehearsals completed | `.docs/governed-lifecycle-proof-2026-05-28.md`; `proofs/remote-normal-shell-live-proof-roadmap/validation-plan.md` | Codex-reported lifecycle evidence, not independent audit. |
| CP Temporal workflow/history evidence exists | `.docs/governed-lifecycle-proof-2026-05-28.md`; `.docs/governed-lifecycle-filming-script.md` | CP-owned workflow/history metadata and filming-safe field list only. |
| ES prepare/submit/lifecycle/result metadata exists | `.docs/governed-lifecycle-proof-2026-05-28.md`; `.docs/governed-lifecycle-filming-script.md` | ES evidence/projection metadata only. |
| Retained-result materialization and CP finalization metadata exist | `.docs/governed-lifecycle-proof-2026-05-28.md`; `.docs/governed-lifecycle-filming-script.md` | Metadata refs only; retained bundles do not become semantic finalization. |
| Static module shape and example status | `.docs/proof-module-conventions.md` | Authored proof-module convention; example remains `not_run`. |
| Relationship to the broader remote normal-shell roadmap | `proofs/remote-normal-shell-live-proof-roadmap/validation-plan.md`; `.docs/remote-normal-shell-live-validation-plan.md` | The lifecycle ledger supports the roadmap but does not complete the full roadmap. |

## Authored docs referenced

- `.docs/governed-lifecycle-proof-2026-05-28.md`
- `.docs/governed-lifecycle-filming-script.md`
- `proofs/remote-normal-shell-live-proof-roadmap/validation-plan.md`
- `.docs/remote-normal-shell-live-validation-plan.md`
- `.docs/proof-module-conventions.md`

## Authority boundaries

- **Control Plane authority**: Temporal workflow state, run-control state,
  review, retained-result materialization, checkpoints, intervention semantics,
  and finalization.
- **Execution Substrate authority**: producer compatibility, prepare/admission,
  submit handoff, lifecycle projection, result metadata, retained opaque result
  references, and runtime handoff boundaries.
- **Infrastructure Manager diagnostics**: profile, readiness, provenance,
  redaction, and support-bundle surfaces when separately run. IM evidence does
  not become CP run-control truth or ES runtime authority.

CP facts decide CP finalization. ES lifecycle/status/result evidence informs
the lifecycle proof but does not override CP workflow state. IM diagnostics do
not authorize or finalize a governed run.

## Generated artifact handling

The ledger may mention path classes such as `.out/<run_id>/` and
`.out/temporal/<timestamp>-dev-server.db` only as metadata and redaction
guidance. This evidence map does not reference raw `.out` contents and does not
copy raw generated summaries, reports, logs, traces, retained payloads,
prompts, model outputs, workspaces, databases, credentials, endpoint values, or
local process records.

## Evidence quality notes

- Evidence references are repo-relative authored-doc references.
- The evidence status is Codex-reported, not independently inspected.
- Public/demo readiness is not claimed; a final demo-readiness audit remains
  required.
- If future CP, ES, or IM docs conflict with this module, stop and surface the
  conflict instead of widening the proof claims.
