# Claims

Current evidence status: Codex-reported deterministic IM validation exists in
`.docs/deterministic-validation-2026-05-27.md`. No IM support bundle was
generated, support-bundle claims remain unvalidated, and Phase A/B adds limited
profile/config/preflight provenance only. The static example remains
`validation_status: "not_run"` because it is a template, not proof evidence
status. Independent audit and public/demo readiness are not claimed.

## Supported claims

This proof module may make these narrow claims:

- IM readiness, profile, doctor, support-bundle, redaction, and digest outputs
  are provenance, diagnostics, evidence, projection, or packaging surfaces.
- IM support-packet assembly can preserve CP-owned and ES-owned section
  boundaries without transferring their semantics to IM.
- A digest-first manifest can identify copied summary artifacts, with path
  identity treated as secondary context only.
- Redaction and deny-scan reports are shareability guardrails; they are not CP
  run-control truth and not ES runtime truth.
- Remote Alpha readiness reporting is pre-live operator UX evidence. It is not
  a governed execution proof by itself.
- CP workflow/query state and guarded write paths remain the run-control
  authority.
- ES-owned admission, runtime-profile, lifecycle projection, cancel, result,
  log, runtime handoff, and retained-bundle surfaces remain ES-owned evidence or
  runtime boundaries. IM support packets do not override them.

## Explicit non-claims

This proof module must not claim these happened or became true:

- live support bundle generation;
- raw support bundle copying;
- Remote Alpha production readiness;
- CP run-control authority from IM evidence;
- ES runtime authority from IM evidence;
- remote provisioning/reconciler behavior;
- live host contact;
- support-bundle authority;
- live readiness refresh;
- governed live job proof;
- CP proof pass;
- ES proof pass;
- live ES execution;
- provider-side cancellation success;
- terminal runtime outcome;
- runtime identity or Vault credential success;
- retained-bundle semantic finalization;
- all-routes or all-stage validation;
- browser, WebAuthn, or passkey proof;
- proof harness behavior as product architecture.

## Authority, evidence, and projection labels

Use these labels consistently:

- `CP authority`: workflow/query state, guarded operator writes, run-control
  actionability, receipts, durable intervention history, review, checkpoints,
  escalation, and finalization.
- `ES runtime boundary`: admission, prepare/submit handoff, runtime-profile
  compatibility, lifecycle projection, cancel/result/log evidence, runtime
  handoff, and retained opaque bundles.
- `IM provenance/diagnostics`: profile emission, doctor vocabulary, readiness
  summaries, environment lineage, bridge/process state, support-bundle assembly,
  redaction, and digest manifesting.
- `Support packet evidence`: copied summaries and manifests that preserve
  source ownership and non-authority labels.
- `Digest identity evidence`: SHA-style content identity for copied summary
  artifacts, never liveness, readiness, run-control, or runtime authority.
- `Redaction guardrail`: shareability and deny-scan status, never proof that
  excluded raw material was safe to publish.

## Evidence/projection-only classes

The proof must label these as evidence, projection, diagnostics, or explicit
non-claims:

- profiles;
- doctor output;
- readiness reports;
- support-bundle manifests;
- redaction reports;
- digest manifests;
- CP profile diagnostics;
- CP proof-lineage summaries when copied from separate CP-owned evidence;
- ES producer-contract summaries;
- ES health/readiness summaries;
- ES lifecycle, outcome, cancel, result, and log evidence;
- ES hardening check-only or apply summaries;
- helper staging provenance;
- local proof examples.

## Sensitive/generated classes excluded

The proof must exclude these classes:

- `.out` contents;
- raw support bundles;
- raw retained bundles;
- raw logs, traces, reports, prompts, model outputs, and review/audit payloads;
- archives;
- databases;
- environment files;
- keys, certificates, tokens, secrets, API keys, bearer material;
- TLS, SPIFFE, Vault, WebAuthn, and passkey material;
- workspaces, checkpoint directories, quarantine directories, and restore
  directories;
- local process records;
- real run ids, real provider ids, real hashes, and local absolute paths.

## Claim-review checklist

Before publication or validation, verify:

- Does the text keep CP workflow/query state as run-control authority?
- Does the text keep ES runtime semantics under ES-owned contracts?
- Does the text label IM outputs as provenance, diagnostics, evidence, or
  projection only?
- Does the text avoid claiming that a support bundle was generated or copied?
- Does the text avoid live host contact, provisioning, or reconciler claims?
- Does the text avoid Remote Alpha production-readiness claims?
- Does the text preserve digest identity as evidence only?
- Does the text exclude raw generated and sensitive artifact classes?
- Does the text keep the static example at `validation_status: "not_run"` while
  recording actual evidence status separately?
