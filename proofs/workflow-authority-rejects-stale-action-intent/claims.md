# Claims

Validation status: this module is currently static/example-first. No pytest,
supported-local, ES, IM, Temporal, Docker, Nomad, Vault, SPIRE, browser, or
WebAuthn validation commands have been run for this proof module yet.

## Supported claims

This proof module may make these narrow claims:

- A stale `expected_actionability_fingerprint` on a
  `cancel-current-attempt` request is rejected before mutation.
- Control Plane workflow/query state and the current actionability fingerprint
  are the authority for the guarded action decision.
- `ExecutionFlowSnapshot v1` is a read contract for actionability, not a source
  of independent product architecture.
- UI, report, channel, dashboard, notification, and proof outputs are
  presentation or evidence surfaces. They are not run-control truth.
- A fresh accepted cancel request, if shown, is a guarded Control Plane receipt.
  It is not proof of provider-side cancel effect or terminal runtime outcome.
- ES facts may enrich the read model only as evidence or projection. They do not
  override CP workflow state.
- IM facts may explain environment provenance, readiness, or diagnostics only.
  They do not become CP run-control authority or ES runtime authority.

## Explicit non-claims

This proof module must not claim:

- production readiness;
- high availability;
- multi-tenancy;
- Remote Alpha readiness;
- live ES execution;
- provider-side cancellation success;
- terminal runtime outcome;
- runtime identity or Vault credential success;
- retained-bundle semantics;
- support-bundle authority;
- WebAuthn, passkey, or browser delivery;
- all intervention verbs;
- ES ownership of CP intervention authority;
- IM ownership of CP run-control truth or ES runtime truth;
- preflight or prepare as execution;
- runtime identity handoff as token brokerage;
- proof harness behavior as product architecture.

## Authority owners

### CP authoritative facts

Control Plane authoritative facts for this proof are:

- workflow/query status;
- current actionability fingerprint;
- route-level guarded intervention decision;
- expected status, pending-action, current-attempt, provider-run, and cancel
  capability guards;
- immediate intervention receipt;
- durable intervention history when present.

Evidence anchors:

- `Control Plane: .docs/long-running-operator-mode-contract.md:282-327`
- `Control Plane: .docs/long-running-operator-mode-contract.md:388-444`
- `Control Plane: .docs/long-running-operator-mode-contract.md:480-500`
- `Control Plane: .docs/invariants.md:123-126`
- `Control Plane: src/control_plane/monitoring/interventions.py:250-280`
- `Control Plane: src/control_plane/monitoring/interventions.py:624-642`

### ES evidence/projection facts

Execution Substrate facts may appear only as evidence, projection, compatibility
edge, or non-claim:

- producer compatibility;
- lifecycle projection;
- outcome evidence;
- logs/result/cancel evidence;
- retained opaque result references;
- bounded non-secret `authority_handoff` metadata;
- runtime-profile compatibility labels.

Evidence anchors:

- `Execution Substrate: .docs/mvp.md:40-111`
- `Execution Substrate: .docs/system_overview/boundaries.md:417-448`
- `Execution Substrate: .docs/system_overview/boundaries.md:482-497`
- `Execution Substrate: .docs/system_overview/boundaries.md:541-553`

### IM evidence/projection facts

Infrastructure Manager facts may appear only as provenance, readiness evidence,
support diagnostics, or explicit non-claims:

- profiles;
- instance state;
- bridge records;
- doctor output;
- readiness reports;
- support bundles;
- redaction summaries.

Evidence anchors:

- `Infrastructure Manager: .docs/architecture.md:5-26`
- `Infrastructure Manager: .docs/architecture.md:58-71`
- `Infrastructure Manager: .docs/architecture.md:126-135`

### UI/report/channel/proof output facts

These surfaces may present or carry action intent, but they do not decide action
authority:

- browser console or API view;
- report/dashboard/export;
- notification, app, iMessage, or channel payload;
- proof-repo narrative or example summary;
- generated validation output.

Evidence anchors:

- `Control Plane: .docs/invariants.md:112-126`
- `Control Plane: .docs/invariants.md:151-157`
- `Control Plane: src/control_plane/channels/action_adapter.py:120-199`
- `Execution Substrate: .docs/mvp.md:69-101`

## Evidence/projection-only classes

The proof must label these as evidence or projection only:

- generated artifacts;
- logs;
- reports;
- traces;
- support bundles;
- retained bundles;
- profiles;
- `.out` paths;
- local proof outputs;
- validation outputs;
- ES lifecycle projections;
- ES outcome evidence;
- ES authority handoff metadata;
- IM readiness and support diagnostics;
- UI/report/channel summaries.

## Sensitive/generated classes excluded

The proof must exclude these classes:

- `.out` contents;
- raw logs, traces, and reports;
- retained bundles and support bundles;
- archives;
- DB/SQLite files;
- env files;
- keys, certificates, tokens, secrets, API keys, bearer material;
- TLS, SPIFFE, Vault, WebAuthn, and passkey material;
- raw prompts;
- raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoint directories, quarantine directories, and restore
  directories;
- local process records.

## Claim-review checklist

Before publication or validation, verify:

- Does the text say CP workflow state and current fingerprint decide the guarded
  write?
- Does the text keep stale UI/report/channel/proof snapshots out of authority?
- Does the text say stale rejection happens before mutation?
- Does the text avoid claiming provider-side cancellation success?
- Does the text keep accepted fresh cancel as a CP receipt only?
- Does the text keep ES facts as evidence/projection?
- Does the text keep IM facts as provenance/diagnostics?
- Does the text exclude raw generated and sensitive artifact classes?
- Does the text avoid all-verbs claims?
- Does the text avoid turning this module into shared product architecture?
