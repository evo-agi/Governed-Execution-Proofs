# Public Writing Map

## Article title

The Support Packet Is Not the Control Plane

## Precise thesis

Infrastructure Manager support packets are useful because they make environment
provenance, readiness posture, redaction, and digest identity inspectable. They
are dangerous if read as authority. In Governed Execution, CP workflow state
still decides run control, ES still owns runtime boundaries, and the support
packet remains evidence.

## What the proof demonstrates

- IM profiles, doctor output, readiness reports, support bundles, redaction
  reports, and digest manifests should be labeled as evidence, projection,
  provenance, diagnostics, or packaging.
- Support-bundle assembly can preserve CP and ES ownership boundaries.
- Digest-first provenance can identify copied summary artifacts without
  turning those artifacts into live truth.
- Redaction and deny scans are shareability guardrails, not authority.
- Codex-reported deterministic IM validation supports the non-authority boundary.
- No IM support bundle was generated; support-bundle claims remain unvalidated.
- Static proof examples must remain synthetic and clearly marked `not_run`.

## What the proof does not demonstrate

- live support bundle generated;
- raw support bundle copied;
- Remote Alpha production readiness;
- CP run-control authority;
- ES runtime authority;
- provisioning/reconciler behavior;
- live host contact;
- support-bundle authority;
- live readiness refresh;
- governed live job proof;
- CP proof pass;
- ES proof pass;
- live ES execution;
- runtime identity or Vault credential success;
- retained-bundle semantics;
- browser, WebAuthn, or passkey proof.

## Safe public diagram

Use four labeled areas:

1. IM support packet: profile, doctor, readiness, redaction, digest manifest.
2. CP authority: workflow/query state and guarded operator writes.
3. ES runtime boundary: admission, prepare/submit, lifecycle projection,
   runtime-profile compatibility, cancel/result/log evidence, retained bundles.
4. Exclusions: raw logs, raw bundles, credentials, local paths, workspaces, and
   real ids.

Show arrows from IM to CP and ES as "evidence/projection only." Do not draw the
support packet as a command path, approval gate, scheduler, reconciler, or
runtime owner.

## Safe wording

- "The packet explains environment provenance; it does not authorize mutation."
- "Digest identity helps audit copied summary evidence, not live truth."
- "Redaction is a shareability guardrail, not a proof of authority."
- "CP workflow state remains the run-control authority."
- "ES runtime facts remain under ES-owned contracts."
- "Remote Alpha readiness evidence is pre-live unless a separate owner records a
  narrower validation result."

## Wording to avoid

- "The support bundle proves the run was allowed."
- "The readiness report is the source of truth."
- "The digest proves the host is live."
- "The bundle generated CP authority."
- "IM approved the ES runtime."
- "Remote Alpha is production-ready."
- "The support packet reconciled the host."
- "Redaction made raw logs safe to publish."
- "This static proof ran validation."

## Sensitive details to omit

Omit:

- raw `.out` contents;
- raw support bundles and retained bundles;
- raw logs, traces, and reports;
- archives;
- databases;
- env files;
- keys, certificates, tokens, secrets, API keys, and bearer material;
- TLS, SPIFFE, Vault, WebAuthn, and passkey material;
- raw prompts and raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoints, quarantines, and restores;
- local process records;
- real run ids, real provider ids, real hashes, and local absolute paths.

## Evidence labels for publication

Use these labels consistently:

- `CP authority`: workflow/query state and guarded operator writes.
- `ES runtime boundary`: admission, runtime profile, lifecycle projection,
  runtime handoff, cancel/result/log evidence, and retained opaque bundles.
- `IM provenance/diagnostics`: profile, doctor, readiness, support-bundle
  assembly, redaction, and digest manifesting.
- `Support packet evidence`: copied summary artifacts and non-authority labels.
- `Static example`: the example YAML in this module, which remains
  `validation_status: "not_run"`.
- `Support-bundle status`: no IM support bundle was generated; support-bundle
  claims remain unvalidated unless a later owner records a separate validation
  pass.

## Theory vs repo-grounded evidence vs validation

- Theory: operational support packets are useful only when they are kept out of
  authority paths.
- Repo-grounded evidence: cited IM, CP, and ES docs/source/tests in
  `evidence-map.md`.
- Codex-reported validation: deterministic IM validation is recorded in
  `.docs/deterministic-validation-2026-05-27.md`; the static example remains
  `validation_status: "not_run"`.
- Inference: this scenario is a safe static proof because the IM docs and source
  already require non-authority labels, digest-first provenance, and redaction
  boundaries.
