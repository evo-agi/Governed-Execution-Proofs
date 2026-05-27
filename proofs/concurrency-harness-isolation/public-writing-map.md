# Public Writing Map

## What the proof demonstrates

At static status, Proof 0 demonstrates only that the proof track has an authored
concurrency/harness-isolation module and explicit non-live groundwork for later
isolated validation.

## What the proof does not demonstrate

Proof 0 does not demonstrate a passing local no-network run, a passing live
Remote Alpha run, live Temporal behavior, supported-local behavior, Linux-host
behavior, Docker, Nomad, Vault, SPIRE, fake-model service behavior, ES runtime
success, provider success, production readiness, high availability,
multi-tenancy, public/demo readiness, or independent audit.

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

## Wording to avoid

Avoid saying that Proof 0 passed, that two live runs were completed, that local
no-network validation ran, that Remote Alpha is production ready, that the
proof harness is product architecture, or that generated outputs are authority.

## Documentation posture

Until a later authorized validation records its own provenance, public writing
should describe this as static Proof 0 groundwork with `validation_status:
"not_run"`.
