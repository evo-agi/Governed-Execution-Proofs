# Evidence Map

This map ties proof statements to repo evidence. The proof module itself is not
validation output. Current evidence status is recorded separately:
Codex-reported deterministic IM validation exists in
`.docs/deterministic-validation-2026-05-27.md`; no IM support bundle was
generated. The anchors below are source-inspection references and should be
re-audited after repo changes.

## IM ownership and non-authority boundary

- `Infrastructure Manager: README.md:3-9` states that IM owns environment
  bootstrap, readiness, profile emission, bounded compatibility checks, and
  teardown for the supported-local slice, while CP orchestration semantics and
  ES runtime semantics remain outside IM ownership.
- `Infrastructure Manager: .docs/architecture.md:49-71` says generated profiles,
  instance state, bridge records, checks, readiness reports, and support bundles
  are environment provenance, liveness evidence, diagnostics, or projection only
  unless an explicit contract says otherwise.
- `Infrastructure Manager: .docs/supported-local-operator-runbook.md:10-43` keeps IM
  profile/state lineage as environment provenance and never run-control
  authority, and routes CP and ES semantics back to their owning repos.

## Remote Alpha profile, doctor, and readiness

- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:5-11` names Remote
  Alpha 0.3 as pre-live, not a final deployment target, not host provisioning,
  and not a governed live job by itself.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:15-35` says IM is not
  CP run-control authority, not ES runtime authority, not a remote SSH
  installer, not a remote host provisioner, and not a long-lived reconciler.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:81-103` classifies
  doctor output as environment provenance and requires authority fields to keep
  CP run-control authority, ES runtime authority, remote SSH install automation,
  and remote host provisioning false.
- `Infrastructure Manager: .docs/remote-supported-host-alpha.md:147-173` says the
  combined readiness report may incorporate read-only evidence and supplied CP
  proof artifacts only as fixed-stage evidence, and is not a governed execution
  proof by itself.
- `Infrastructure Manager: src/infra_manager/emitters/remote_supported_host_profile.py:151-190`
  emits `readiness.run_control_authority = false` on the profile payload and
  emits doctor authority fields that keep CP run-control, ES runtime authority,
  long-lived reconciler, remote SSH install automation, and remote host
  provisioning false.
- `Infrastructure Manager: src/infra_manager/emitters/remote_alpha_readiness_report.py:213-223`
  emits a readiness-report authority block with CP run-control authority, ES
  runtime authority, remote SSH install automation, remote host provisioning,
  and shared filesystem required all false.
- `Infrastructure Manager: tests/test_remote_profile_emission.py:83-103` source checks
  the remote profile and doctor output for fixed vocabulary and non-authority
  fields.
- `Infrastructure Manager: tests/test_remote_alpha_readiness_report.py:64-67` source
  checks readiness posture, blocker handling, non-authority fields, and the
  statement that the report does not submit or run a live governed CP job.

## Support-bundle layout, digest, and redaction

- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:6-25`
  defines the support-bundle layout. It gives IM top-level assembly UX,
  redaction, and deny-scan ownership while keeping CP and ES section ownership
  separate.
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:49-63`
  defines the bundle as summary evidence only, with included classes such as CP
  profile diagnostics, IM readiness reports, ES summaries, byte counts,
  redaction counts, digest values, and non-authority labels.
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:221-246`
  says the live collector copies existing repo-local live-refresh/readiness
  artifacts without contacting or mutating the host, does not rewrite source
  artifacts, and treats support-bundle collection as diagnostics,
  repeatability, and shareability support.
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:609-639`
  requires deny-by-default redaction and excludes private keys, bearer tokens,
  Vault tokens, JWT-SVIDs, cookies, authorization headers, API keys, WebAuthn
  and passkey material, session material, raw env files, databases, workspaces,
  checkpoints, raw prompts, raw model responses, raw Codex outputs, raw logs,
  raw result bundles, and artifact payload bytes.
- `Infrastructure Manager: .docs/commands.md:224-279` documents
  `remote-alpha-live-support-bundle` as copying current repo-local artifacts,
  recording source paths, byte counts, and SHA-256 digests, with digest identity
  primary and path identity secondary.
- `Infrastructure Manager: .docs/commands.md:196-202` says support-bundle collection is
  not renewal authority, not run authority, not a remote reconciler, and not a
  trigger for proof, refresh, bootstrap, apply, or TLS renewal.
- `Infrastructure Manager: src/infra_manager/emitters/remote_support_bundle.py:181-210`
  defines non-authority labels such as `not_cp_run_control` and
  `not_es_runtime_authority`, live collector statements that it does not SSH,
  rerun refresh, install, provision, or mutate the live host, and guardrails for
  denied filenames, denied payloads, digest-first provenance, and redaction.
- `Infrastructure Manager: src/infra_manager/emitters/remote_support_bundle.py:4768-4781`
  records copied evidence refs with byte count, digest, owner, schema, evidence
  class, and path identity as secondary provenance context.
- `Infrastructure Manager: src/infra_manager/emitters/remote_support_bundle.py:4797-4814`
  builds live support-bundle guardrails with fail-closed deny classes and
  digest-primary, path-secondary policy.
- `Infrastructure Manager: src/infra_manager/emitters/remote_support_bundle.py:4933-4963`
  emits live support-bundle authority fields that keep bundle assembly,
  artifact copy, and digest manifesting separate from CP run-control and ES
  runtime authority.
- `Infrastructure Manager: tests/test_remote_support_bundle.py:126-132` source checks
  static support-bundle authority fields, non-authority labels, redaction
  output, denied material exclusion, and docs alignment.
- `Infrastructure Manager: tests/test_remote_alpha_live_support_bundle.py:211-214`
  source checks that live support-bundle collection is evidence collection only,
  does not call live refresh or command-runner paths, records missing optional
  artifacts as warnings, preserves digest/path provenance, and fails closed on
  mutating or overclaiming ES evidence.

## CP boundary evidence

- `Control Plane: .docs/long-running-operator-mode-contract.md:282-310` owns the
  workflow-authoritative state and guarded operator write boundary consumed by
  proof modules.
- `Control Plane: .docs/architecture.md:19-45` describes Temporal/workflow-owned
  run-control semantics and keeps generated proof and validation summaries
  separate from authority.
- `Control Plane: .docs/execution-substrate-integration.md:140-156` keeps supported
  proof summaries as CP-side evidence and preserves ES lifecycle, outcome,
  authority, and identity facts as evidence rather than write guards.
- `Control Plane: .docs/invariants.md:151-157` keeps presentation, channel, report, and
  artifact surfaces from becoming actionability truth or intervention truth.

## ES boundary evidence

- `Execution Substrate: .docs/mvp.md:44-68` freezes ES as admission, submit handoff,
  runtime-profile compatibility, lifecycle projection, retained opaque result
  bundle, and runtime handoff owner, while classifying IM readiness, profile,
  support-bundle, and provenance artifacts as evidence, projection, or
  diagnostics only.
- `Execution Substrate: .docs/system_overview/boundaries.md:432-448` keeps ES status,
  logs, result, cancel, outcome evidence, retained bundles, `authority_handoff`,
  profiles, support bundles, reports, traces, and proof artifacts from becoming
  CP workflow truth or broad authority.

## Proof repo convention

- `Governed Execution Proofs: .docs/proof-module-conventions.md:11-38`
  records isolated module layout and the static/example-first validation
  default.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:74-96`
  records repo-relative evidence-reference rules and sensitive/generated
  artifact exclusions.
- `Governed Execution Proofs: .docs/proof-module-conventions.md:111-119`
  says the convention doc does not create a shared proof framework, product
  schema, validation runner, generated artifact contract, or product
  architecture.

## Evidence quality notes

- Evidence above was inspected as docs, source, and tests only.
- No generated artifacts, `.out` payloads, live bundles, raw logs, raw reports,
  traces, retained bundles, support bundles, raw prompts, raw model outputs,
  credentials, or local process records were opened or copied.
- This evidence map is not itself command output. Codex-reported deterministic
  IM validation is recorded separately from the static example, and
  support-bundle claims remain unvalidated.
