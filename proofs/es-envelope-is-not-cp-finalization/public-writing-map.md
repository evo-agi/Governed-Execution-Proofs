# Public Writing Map

## Article title

The Envelope Is Not the Final Say: Separating ES Runtime Evidence from CP Finalization

## Precise thesis

Execution Substrate can safely own the bounded execution envelope without
becoming the semantic finalizer. Producer contract, prepare, submit, status, and
retained-output references each have narrow labels; Control Plane alone owns
semantic review, checkpoint, intervention, and finalization.

## What the proof demonstrates

- ES producer contract is a compatibility declaration.
- ES prepare is preflight and creates no execution state.
- ES submit is bounded runtime handoff.
- ES status is runtime projection/evidence.
- ES result is an opaque retained-output envelope.
- ES `authority_handoff` is non-secret runtime handoff evidence only.
- CP owns semantic review and finalization above the ES boundary.

## What the proof does not demonstrate

- live ES validation;
- production readiness;
- provider or runtime success;
- CP finalization proof;
- retained-bundle semantic interpretation;
- credential or token brokerage proof;
- Remote Alpha proof;
- service health;
- submit readiness;
- terminal runtime outcome;
- live retained-result availability;
- Vault, SPIRE, JWT-SVID, Codex credential, lease, or secret success;
- WebAuthn, passkey, browser, channel, notification, or app delivery;
- high availability;
- multi-tenancy;
- proof harness architecture.

## Safe public diagram

Use a simple left-to-right diagram with two lanes:

1. ES envelope lane:
   `contract -> prepare -> submit -> status/result -> retained opaque output`
2. CP semantic lane:
   `materialize -> review -> checkpoint/intervention -> finalization`

Label arrows between lanes as "evidence/projection consumed by CP." Do not show
real run ids, provider ids, hashes, retained bundle references, local paths, raw
logs, screenshots, retained bundle payloads, support bundle payloads,
credentials, or local environment details.

## Safe wording

- "ES producer contract is compatibility metadata, not health or finalization."
- "Prepare proves preflight only."
- "Submit is a bounded runtime handoff."
- "Status is a projection/evidence surface."
- "The retained result bundle is opaque to ES."
- "CP materializes and interprets result contents semantically."
- "CP owns review, checkpoint, intervention, and finalization."
- "`authority_handoff` is non-secret handoff evidence, not credential proof."

## Wording to avoid

- "The ES envelope finalized the run."
- "Producer contract proves the service is ready."
- "Prepare executed the task."
- "Submit proves the provider succeeded."
- "Status is CP workflow truth."
- "The lifecycle projection is a write guard."
- "The retained bundle proves semantic acceptance."
- "ES interpreted the checkpoint or finalization files."
- "The result endpoint is a CP finalization API."
- "`authority_handoff` proves token delivery."
- "This proves Remote Alpha."
- "This is production-ready."
- "The proof harness defines the architecture."

## Evidence labels for publication

Use these labels consistently:

- "ES compatibility declaration": producer contract.
- "ES preflight": prepare.
- "ES runtime handoff": submit.
- "ES runtime projection": status and lifecycle projection.
- "ES runtime evidence": outcome evidence, logs, cancel, and result headers.
- "ES opaque retained output": retained bundle envelope and reference.
- "ES non-secret handoff evidence": `authority_handoff`.
- "CP semantic authority": review, checkpoint, intervention, and finalization.
- "Static example": the proof-summary example in this module.
- "Not run": every validation claim unless a later validation pass explicitly
  records otherwise outside this static module.

## Sensitive details to omit

Omit:

- raw `.out` contents;
- raw logs, traces, and reports;
- retained bundles and support bundles;
- archives;
- DB/SQLite files;
- env files;
- keys, certs, tokens, secrets, API keys, and bearer material;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, and private-key material;
- raw prompts and raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoints, quarantines, and restores;
- local process records;
- real run IDs, provider IDs, hashes, bundle refs, and local absolute paths.

## Theory vs repo-grounded evidence vs Codex-reported validation vs inference

- Theory: a runtime envelope should preserve provenance and handoff evidence
  without absorbing semantic governance.
- Repo-grounded evidence: cited ES and CP docs/source/tests in
  `evidence-map.md`.
- Codex-reported validation: source inspection only; no tests or live commands
  were run during module creation.
- Inference: this scenario is useful because it shows the whole ES envelope
  crossing CP consumption boundaries while keeping finalization semantics owned
  by CP.
