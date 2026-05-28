# Governed Lifecycle Filming Script

## Opening script

This demo is about governed execution lifecycle, not autonomous software
development.

The value is the governed boundary around execution: Control Plane owns the
workflow and finalization, Execution Substrate owns admission and runtime
handoff evidence, and runtime systems execute after submit. The proof we are
showing is Codex-reported, bounded, serial, and based on two happy-path
rehearsals. It is not independently audited and is not public/demo readiness by
itself.

## Architecture narration

Start with the authority map.

Control Plane owns Temporal workflow state, task progression, review,
checkpointing, materialization, finalization, and operator semantics.

Execution Substrate owns admission, prepare, submit handoff, runtime-profile
compatibility, lifecycle projection, outcome evidence, retained opaque result
bundles, and runtime handoff boundaries.

Nomad and Docker own runtime execution after submit.

Infrastructure Manager owns readiness, profile, provenance, diagnostics, and
support evidence only. Generated artifacts are evidence/projection/diagnostics
only.

## Deterministic workload narration

The workload is intentionally small and deterministic. That keeps attention on
the governed lifecycle rather than on autonomous software development.

We are not trying to prove that a model can build a product. We are proving that
the governed execution path records the right boundaries: contract checks,
prepare/admission, submit handoff, provider lifecycle evidence, retained-result
materialization, and CP-owned review/finalization.

## Submit intent narration

Control Plane starts from an explicit `temporal-basic` intent. It packages the
normal-shell task attempt for the `control-plane-normal-shell/v1` runtime
profile and uses the configured profile as proof-local provenance.

The important point is that intent does not become runtime truth. It has to pass
the producer contract gate, prepare/admission, submit handoff, lifecycle
observation, retained-result fetch, and CP finalization.

## ES prepare/admission narration

Before submit, CP checks the ES producer contract and records compatibility by
safe metadata.

ES prepare is an admission/preflight boundary. It can show that a package and
runtime profile are acceptable for the governed runtime path. Prepare is not
execution, not CP finalization, and not production readiness.

## ES submit/Nomad handoff narration

After prepare, CP submits through ES. ES owns the submit handoff and provider
run reference by safe metadata.

After submit, runtime execution belongs to the runtime boundary. Nomad and
Docker own execution mechanics; ES projects provider lifecycle and outcome
evidence back as evidence, not CP write authority.

## Lifecycle projection narration

The lifecycle projection is useful because it shows what ES observed about the
provider-side runtime path.

It remains projection/evidence. CP does not use ES lifecycle fields as
intervention write coordination or semantic finalization. The demo should call
out that separation explicitly.

## Logs/result narration

Logs and result surfaces are shown only by metadata or redacted presence fields.

The retained result remains an opaque ES-retained bundle until CP fetches,
materializes, reviews, and finalizes it. We do not show raw logs, retained
payloads, workspaces, prompts, or model outputs.

## Audit/outcome evidence narration

The outcome is CP-owned. The proof summary reports final result,
Temporal history, workflow start/completion, ES metadata, retained-result refs,
materialization refs, and CP review/finalization refs.

The happy-path-twice checklist is complete because two bounded serial happy-path
rehearsals reported `proof_passed`, and the second run also corrected the
Temporal DB placement lesson by keeping the DB outside the validation run root.

## Honest limitation close

This proves the governed execution lifecycle boundary for the recorded
`temporal-basic` path. It does not prove production readiness, HA,
multi-tenancy, autonomous software development, cancel/failure/intervention,
Proof 0 concurrency, IM support-bundle behavior, or public/demo readiness by
itself.

The next gate is the final demo-readiness audit.

## Screen plan

Use three panes:

1. Architecture text or diagram.
2. Proof terminal with stage progress and final result.
3. Sanitized summary projections.

Keep the terminal pane focused on stage labels and final result. Keep the
summary pane focused on selected fields, booleans, and metadata presence. Avoid
opening raw generated files directly on screen. If a summary projection is
shown, show only the selected fields listed below and collapse or hide all raw
payload-bearing sections.

## Safe fields to show

Safe fields:

- run id;
- `final_result`;
- `requested_mode`;
- stage statuses;
- Temporal readiness/history booleans;
- workflow start/completion booleans;
- producer contract compatible;
- prepare/admission status;
- submit/status/result evidence present;
- retained-result refs present by metadata only;
- materialization refs present by metadata only;
- finalization refs present by metadata only;
- CP review/finalization status.

## Fields/classes to hide

Hide:

- raw JSON or Markdown generated files;
- raw logs;
- traces;
- prompts and model outputs;
- workspaces;
- retained bundle payloads;
- DBs and DB contents;
- endpoint values;
- certificate, key, TLS, SPIFFE, Vault, WebAuthn, passkey, API-key, bearer, or
  credential material;
- local process records.

## Pre-filming checklist

- Confirm the ledger says the evidence is Codex-reported and not independently
  audited.
- Confirm the happy-path-twice checklist is complete in the ledger.
- Confirm the script says this is governed execution lifecycle, not autonomous
  software development.
- Confirm the Temporal dev-server DB/state prerequisite: use a path like
  `.out/temporal/<run-id-or-timestamp>-dev-server.db`, not
  `.out/<run_id>/temporal/dev-server.db`.
- Confirm the screen plan uses only the safe fields listed above.
- Confirm raw generated artifacts are not opened.
- Confirm no proof, validation, bringup, Temporal, Docker, Nomad, Vault, SPIRE,
  supported-local, Remote Alpha, or Linux-host command is planned.
- Confirm cancel/failure/intervention remains excluded.
- Confirm IM support-bundle generation remains deferred.
- Confirm the final demo-readiness audit remains a separate gate.

## During-filming checklist

- Keep the architecture pane visible while narrating authority boundaries.
- Show the proof terminal only at stage/final-result level.
- Show sanitized summary projections only.
- Say prepare is admission/preflight, not execution.
- Say lifecycle projection is ES evidence/projection, not CP finalization.
- Say retained-result refs are metadata until CP materialization and review.
- Avoid scrolling into raw generated files or secret-adjacent material.

## After-filming notes

- Re-run the proof-repo doc checks and redaction scan after any script edits.
- Review the recording for accidental raw artifacts, endpoint values,
  credentials, prompts, model outputs, traces, logs, workspaces, or DB contents.
- Keep any public wording attached to the supported claims and non-claims in
  `.docs/governed-lifecycle-proof-2026-05-28.md`.
- Do not claim public/demo readiness until the final demo-readiness audit
  passes.
