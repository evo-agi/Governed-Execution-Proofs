# Public Writing Map

## Article title

The Button Was Stale: Why Governed Execution Treats UI Actions as Requests, Not Truth

## Precise thesis

Governed Execution should not let a stale UI, report, channel, or proof snapshot
authorize mutation. Control Plane must re-read workflow-authoritative state,
compare the submitted actionability fingerprint with the current actionability
fingerprint, and reject stale action intent before mutation.

## What the proof demonstrates

- A stale `cancel-current-attempt` request can carry an old
  `expected_actionability_fingerprint`.
- Control Plane workflow/query state and the current actionability fingerprint
  are the guarded write authority.
- A mismatched fingerprint is rejected before mutation.
- UI, report, channel, dashboard, notification, and proof outputs can inform an
  operator, but they are not run-control truth.
- A fresh accepted cancel request is a guarded Control Plane receipt, not proof
  of provider-side effect or terminal runtime outcome.

## What the proof does not demonstrate

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
- proof harness architecture.

## Safe public diagram

Use a simple diagram with four labeled areas:

1. Stale surface: UI/report/channel/proof snapshot with an old fingerprint.
2. Guarded CP route: `cancel-current-attempt` request with expected-state guards.
3. Workflow authority: current CP workflow/query state and current fingerprint.
4. Result: rejected before mutation, with no provider request or pending action.

Show ES and IM facts as side panels labeled "evidence/projection only" and
"provenance/diagnostics only." Do not include real run IDs, real hashes, real
paths, raw logs, screenshots, retained bundle contents, support bundle contents,
credentials, or local environment details.

## Safe wording

- "The stale action intent was rejected before mutation."
- "The current CP workflow state and actionability fingerprint decide the
  guarded action."
- "Presentation and evidence surfaces can inform an operator, but they do not
  authorize mutation."
- "A fresh accepted cancel request is a CP receipt, not a terminal runtime
  outcome."
- "ES lifecycle and cancel facts may be useful evidence, but they do not
  override CP workflow state."
- "IM readiness and support facts are diagnostics/provenance, not run-control
  authority."

## Wording to avoid

- "The UI prevented the mutation."
- "The proof output is the source of truth."
- "The stale report canceled the run."
- "The accepted cancel proves the provider stopped."
- "The run was terminally canceled."
- "ES lifecycle projection authorizes CP intervention."
- "IM readiness proves governed execution truth."
- "Remote Alpha is production-ready."
- "Prepare proves execution."
- "Runtime identity handoff proves token brokerage."
- "This proves every intervention verb."
- "The harness defines the architecture."

## Sensitive details to omit

Omit:

- raw `.out` contents;
- raw logs, traces, and reports;
- retained bundles and support bundles;
- archives;
- DB/SQLite files;
- env files;
- keys, certs, tokens, secrets, API keys, bearer material;
- TLS, SPIFFE, Vault, WebAuthn, or passkey material;
- raw prompts and raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoints, quarantines, and restores;
- local process records;
- real run IDs, real provider IDs, real hashes, and local absolute paths.

## Evidence labels for publication

Use these labels consistently:

- "CP authority": workflow/query state, current actionability fingerprint, and
  guarded intervention decision.
- "Presentation/evidence": UI, report, dashboard, notification, channel, and
  proof outputs.
- "ES evidence/projection": lifecycle projection, outcome evidence, cancel
  evidence, retained-result references, and non-secret `authority_handoff`
  metadata.
- "IM provenance/diagnostics": profiles, readiness, doctor output, support
  bundles, redaction summaries, and instance state.
- "Static example": the proof-summary example in this module.
- "Not run": validation commands listed in this module unless a later validation
  pass explicitly runs and records them.

## Theory vs repo-grounded evidence vs Codex-reported validation vs inference

- Theory: why stale action intent should not be authority.
- Repo-grounded evidence: cited CP, ES, and IM docs/source/tests in
  `evidence-map.md`.
- Codex-reported validation: planning and inspection reports only; no tests were
  run during module creation.
- Inference: this scenario is the smallest first proof because
  `cancel-current-attempt` has direct stale rejection plus fresh guarded cancel
  evidence without proving all intervention verbs.
