# Governed Lifecycle Proof Ledger: 2026-05-28

## Status

Status: Codex-reported two-pass lifecycle condition recorded.

This ledger records a bounded serial governed execution lifecycle proof with
two happy-path rehearsals. The record is not independently audited and is not
public/demo readiness by itself.

Happy-path-twice checklist: complete.

Raw generated artifacts are not committed here. Generated artifacts are
evidence/projection/diagnostics only.

No live proof, validation rerun, Linux-host contact, supported-local bringup,
Remote Alpha command, Docker, Nomad, Vault, SPIRE, Temporal, setup, proof, or
validation command was run while writing this ledger.

## Scope

This ledger records Codex-reported lifecycle evidence for one serial
`temporal-basic` Control Plane Temporal normal-shell path rehearsed twice.

The scope includes:

- CP workflow/run-control, Temporal shell state, review, materialization, and
  finalization evidence by safe metadata;
- ES producer contract, prepare/admission, submit handoff, lifecycle/status,
  result, retained-result, and runtime handoff evidence by safe metadata;
- local Temporal harness readiness/setup lessons from blocked rehearsals;
- filming readiness for a sanitized demo of the governed execution lifecycle.

The scope excludes cancel, failure, intervention, hold/resume/reject,
compare/experiment/wrapper modes, Proof 0 concurrency, IM support bundles,
runtime identity/Vault credential success, independent audit, public/demo
readiness, production readiness, HA, multi-tenancy, provisioning, reconciler
behavior, and general deployment architecture.

## Evidence Basis

Evidence basis: Codex-reported run summaries and post-run audit notes from the
Control Plane validation output. This ledger records run ids, path classes,
stage/result booleans, and presence/absence metadata only.

Raw generated artifacts are not committed here. This ledger does not copy raw
summary JSON, raw Markdown reports, logs, traces, retained bundle payloads,
prompts, model outputs, workspaces, database contents, credentials, certificate
or key material, endpoint values, or local process records.

## Two-Pass Summary

| Pass | Run id | Mode | Codex-reported result | Notes |
| --- | --- | --- | --- | --- |
| First | `governed-lifecycle-temporal-basic-20260527T213519Z` | `temporal-basic` | `proof_passed` | Internal first happy-path rehearsal audit passed. |
| Second | `governed-lifecycle-temporal-basic-20260528T000846Z` | `temporal-basic` | `proof_passed` | Fresh run used a Temporal DB path class outside the validation run root. |

The two runs are recorded as two happy-path rehearsals for the bounded serial
governed execution lifecycle condition.

Happy-path-twice checklist: complete.

## First Pass Summary

Run id: `governed-lifecycle-temporal-basic-20260527T213519Z`.

Codex-reported result: `proof_passed`.

Post-run audit status: passed for the internal first happy-path rehearsal.

This pass supports the first half of the two-pass lifecycle condition. It does
not by itself claim independent audit, public/demo readiness, production
readiness, all-mode validation, concurrency safety, or intervention behavior.

## Second Pass Summary

Run id: `governed-lifecycle-temporal-basic-20260528T000846Z`.

Codex-reported result: `proof_passed`.

Temporal DB path class: `.out/temporal/governed-lifecycle-20260528T000846Z-dev-server.db`.
The DB path was outside `.out/<run_id>/` and outside the CP driver validation
run-root lifecycle.

Codex-reported second-pass checks:

- all validation stages passed;
- Temporal readiness passed;
- Temporal history was exercised;
- workflow start and workflow completion were observed;
- ES producer contract was compatible;
- AGS publish was exercised;
- ES prepare succeeded;
- ES submit/status/result evidence was present by safe metadata;
- retained-result refs and materialization refs were present by metadata;
- CP review/finalization refs were present;
- services started by the rehearsal task were stopped;
- ports 18081, 7233, and 8233 were closed afterward.

This pass completes the second half of the two-pass lifecycle condition.

## Blocked Attempt Lessons

Blocked attempts are recorded as operational lessons, not ES runtime failures.

| Run id | Codex-reported blocker | Lesson |
| --- | --- | --- |
| `governed-lifecycle-temporal-basic-20260527T221648Z` | Temporal shard status unknown before workflow startup. | CP/local Temporal harness readiness must be established before invoking the driver. |
| `governed-lifecycle-temporal-basic-20260527T225230Z` | Temporal TCP preflight connection refused. | TCP reachability is a hard pre-driver gate for the local Temporal harness. |
| `governed-lifecycle-temporal-basic-20260527T235821Z` | Temporal DB path was under `.out/<run_id>`. | The Temporal dev-server DB must live outside the CP validation run directory because the driver owns that run-root lifecycle. |

These lessons belong to CP/local Temporal harness readiness and setup. They do
not indicate ES runtime admission, prepare, submit, lifecycle, or retained-result
failure.

## Temporal DB Placement Lesson

For governed lifecycle rehearsals, Temporal dev-server DB/state must live
outside the CP validation run directory.

Use:

- `.out/temporal/<run-id-or-timestamp>-dev-server.db`

Do not use:

- `.out/<run_id>/temporal/dev-server.db`

Reason: the CP validation driver owns and may delete/recreate `.out/<run_id>/`
as the run workspace. Placing Temporal dev-server state under that tree can
conflict with the driver's run-root lifecycle and produce harness readiness
failures.

## Artifact Classification

Generated `.out`, reports, traces, logs, retained bundles, profiles, local proof
outputs, validation outputs, proof summaries, and Temporal DB files are
evidence/projection/diagnostics only.

Proof-repo treatment:

- record run ids and path classes only when needed for traceability;
- keep raw generated artifacts out of the repo;
- treat generated summaries/manifests as redaction-needed unless separately
  cleared;
- treat retained-result references and materialization/finalization refs as
  metadata only;
- do not treat generated files as CP run-control authority, ES runtime
  authority, IM readiness authority, or public/demo readiness.

## Claims Supported

This Codex-reported ledger supports these bounded claims:

- two serial `temporal-basic` happy-path governed lifecycle rehearsals reported
  `proof_passed`;
- the second rehearsal used a Temporal DB path class outside the validation run
  root;
- the second rehearsal reported all stages passed with Temporal readiness,
  Temporal history, workflow start, and workflow completion evidence;
- the second rehearsal reported ES producer compatibility, AGS publish, ES
  prepare, submit/status/result evidence, retained-result reference evidence,
  materialization evidence, and CP review/finalization evidence by safe
  metadata;
- the two-pass checklist for the bounded serial governed execution lifecycle is
  complete for filming preparation.

## Claims Not Supported

This ledger does not support:

- independent audit;
- public/demo readiness by itself;
- production readiness;
- HA;
- multi-tenancy;
- general deployment architecture;
- Remote Alpha as production or a general deployment architecture;
- remote provisioning or reconciler behavior;
- Proof 0 concurrency or parallel proof execution safety;
- cancel/failure/intervention behavior;
- hold/resume/reject behavior;
- compare, experiment, wrapper, or child-run behavior;
- IM support-bundle generation or support-bundle authority;
- runtime identity/Vault credential success;
- hardening-checkpoint, destructive recovery, service-user migration/apply, or
  Vault reset behavior;
- raw retained-bundle, prompt, model-output, workspace, database, credential, or
  secret-adjacent content claims.

## Authority-Boundary Assessment

The reported evidence preserves the expected authority boundaries.

CP owns workflow/run-control state, Temporal shell state, review,
materialization, finalization, and operator semantics.

ES owns admission, prepare, submit handoff, runtime-profile compatibility,
lifecycle projection, retained opaque result bundles, and runtime handoff
boundaries.

Nomad and Docker own runtime execution after submit.

IM owns readiness/profile/provenance/diagnostics/support evidence only.

Generated artifacts are evidence/projection/diagnostics only and do not become
authority. ES lifecycle/status/result evidence does not become CP finalization.
IM profile/readiness material does not become CP run-control truth or ES runtime
truth.

## Filming Readiness Assessment

The two-pass lifecycle condition is complete for filming preparation.

Visible fields exist for a sanitized recording:

- run id;
- `final_result`;
- `requested_mode`;
- stage statuses;
- Temporal readiness/history booleans;
- workflow start/completion booleans;
- producer contract compatibility;
- prepare/admission status;
- submit/status/result evidence-present booleans;
- retained-result/materialization/finalization refs present by metadata only;
- CP review/finalization status.

This is not public/demo readiness by itself. Final public/demo readiness still
requires the final demo-readiness audit.

## Sensitive/Raw-Excluded Artifacts

Do not commit, quote, screen-share, or narrate these raw classes:

- raw JSON or Markdown generated summaries;
- raw logs;
- traces;
- raw retained bundles or payloads;
- raw prompts;
- raw model outputs;
- workspaces;
- DB contents;
- endpoint values;
- certificate, key, TLS, SPIFFE, Vault, WebAuthn, passkey, API-key, bearer, or
  credential material;
- local process records.

Use only safe metadata, boolean presence fields, classifications, and path
classes in proof documentation and filming material.

## Follow-Up Gates

Before publication or public demo:

- run the final demo-readiness audit;
- verify the filming script against this ledger's supported claims and
  non-claims;
- keep proof-summary examples at `validation_status: "not_run"`;
- keep raw generated artifacts out of the proof repo;
- repeat redaction and wording scans after any script or screen-plan changes;
- obtain independent audit before making any independent-audit claim.
