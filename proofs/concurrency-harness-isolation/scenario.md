# Scenario

## Validation status

Static example status: `not_run`.

This module describes Proof 0 concurrency and harness-isolation groundwork. It
does not record a local no-network run, a live Temporal run, a supported-local
run, a Remote Alpha run, or Linux-host contact.

## Scenario shape

Proof 0 prepares the proof track so a later authorized validation can run either
two local no-network harness-isolation configurations or two live Remote Alpha
`temporal-basic` validations without sharing harness-owned state.

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

## Authority boundaries

Control Plane owns workflow/run-control state, Temporal shell state, review,
checkpoint, escalation, finalization, and operator semantics.

Execution Substrate owns admission, submission handoff, lifecycle projection,
retained opaque results, and runtime handoff boundaries.

Infrastructure Manager owns readiness, profile, provenance, diagnostics, and
support evidence. IM support-bundle generation is outside Proof 0 core.

Generated artifacts, `.out`, reports, traces, logs, support bundles, retained
bundles, profiles, local proof outputs, and validation outputs remain
evidence/projection/diagnostics only. They are not authority.

## Generated artifacts

This module commits no generated proof output. Any later harness-isolation plan
or validation summary must remain evidence-only and must not be treated as a
runtime authority source.
