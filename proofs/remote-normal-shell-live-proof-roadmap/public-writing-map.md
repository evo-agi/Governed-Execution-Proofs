# Public Writing Map

## Article title

The Remote Normal-Shell Proof We Have to Earn

## Precise thesis

The remote normal-shell capstone proof should be presented as a governed chain
of authority handoffs, not as a vague "remote run worked" claim. CP owns the
workflow and finalization. AGS and ES own publication, admission, submission,
runtime projection, retained opaque outputs, and bounded handoff evidence. IM
owns readiness and diagnostics only. Runtime identity and Vault credential
success must be validated before being claimed.

## What the future proof should demonstrate

- Control Plane starts and owns the Temporal shell workflow.
- The remote normal-shell path is explicit and opt-in.
- `control-plane-normal-shell/v1` is required.
- The ES producer declaration passes before real AGS publish, ES prepare, ES
  submit, or real attempt-manifest creation.
- AGS publish, ES prepare, and ES submit occur in order.
- Nomad and Docker execute the workload on the remote Linux host.
- Runtime identity and Vault handoff are validated as workload-side behavior,
  not ES token brokerage.
- ES retains an opaque result bundle.
- Control Plane fetches, materializes, reviews, checkpoints, and finalizes under
  CP-owned semantics.
- The machine-readable summary and human narrative separate authority,
  evidence, projection, diagnostics, and non-claims.

## What this roadmap does not demonstrate

- live Linux validation yet;
- production readiness;
- high availability;
- multi-tenancy;
- general deployment architecture;
- remote provisioning or a remote reconciler;
- remote Control Plane deployment;
- default remote normal-shell behavior;
- runtime identity credential success;
- Vault token, secret, lease, or Codex credential success;
- retained result semantic finalization before CP performs it;
- support-bundle authority.

## Safe public diagram

Use a left-to-right diagram with these labeled zones:

1. CP authority: Temporal shell workflow, packaging, review, checkpoint,
   intervention, and finalization.
2. AGS/ES authority: publish, producer contract gate, prepare, submit,
   lifecycle projection, outcome evidence, and retained opaque result.
3. Remote runtime authority: Nomad placement, Docker execution, SPIRE identity
   issuance, Vault token/secret/lease issuance after workload-side login.
4. IM diagnostics: remote profile, doctor stages, readiness report, support
   bundle metadata, and redaction.
5. Proof outputs: machine-readable summary and narrative, labeled
   non-authoritative.

Do not include real run ids, real provider ids, real hashes, local absolute
paths, remote filesystem paths, logs, retained bundle contents, support bundle
contents, screenshots of sensitive state, prompts, model outputs, or
credentials.

## Safe wording

- "This is the validation contract for the future remote normal-shell capstone
  proof."
- "The proof has not run yet."
- "Control Plane owns workflow state, review, checkpoint, intervention, and
  finalization."
- "ES owns admission, submit handoff, lifecycle projection, retained opaque
  bundles, and bounded runtime identity handoff boundaries."
- "IM readiness and support bundles are diagnostics/provenance, not authority."
- "Runtime identity and Vault credential success must be proven by same-run
  validation before publication can claim it."
- "Retained-result bytes are not semantic finalization until CP reviews and
  finalizes them."

## Wording to avoid

- "The remote Linux proof passed."
- "Remote Alpha is production-ready."
- "The support bundle proves the run."
- "IM readiness is run-control truth."
- "The producer contract proves submit readiness."
- "Prepare proves execution."
- "ES finalizes the Control Plane run."
- "Vault credentials were obtained" before same-run validation proves it.
- "ES brokers Vault or Codex credentials."
- "Remote normal shell is now the default."
- "This is the general deployment architecture."
- "The harness defines the architecture."

## Sensitive details to omit

Omit:

- raw generated artifact contents;
- `.out` contents;
- raw logs, traces, reports, prompts, model outputs, retained bundles, support
  bundles, and archives;
- databases and local process records;
- env files;
- keys, certificate bodies, tokens, secrets, API keys, bearer material, and
  credential payloads;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, and private-key material;
- raw Codex stdout, stderr, final, review, audit, or metadata payloads;
- workspaces, checkpoints, quarantines, and restores;
- real run ids, real provider ids, real hashes, real bundle references, local
  absolute paths, and remote filesystem paths.

## Evidence labels for publication

Use these labels consistently:

- **CP authority**: workflow state, task progression, review, checkpoints,
  interventions, and finalization.
- **AGS/ES authority**: publication facts, admission, prepare, submit handoff,
  lifecycle projection, retained opaque bundles, and bounded runtime identity
  handoff.
- **Runtime authority**: Nomad scheduler placement, Docker execution, SPIRE
  identity issuance, and Vault token/secret/lease issuance after workload-side
  login.
- **ES evidence/projection**: lifecycle projection, outcome evidence,
  `authority_handoff`, logs/result/cancel evidence, and retained-result refs.
- **IM provenance/diagnostics**: profiles, doctor output, readiness reports,
  support bundles, redaction, and source-profile lineage.
- **Static example**: this module's `proof-summary.example.yaml`.
- **Not run**: every validation stage until a later authorized validation pass
  records fresh same-run evidence.

## Theory vs evidence vs validation vs inference

- Theory: why a remote proof should be decomposed into authority handoffs rather
  than one broad "remote worked" assertion.
- Repo-grounded evidence: cited CP, ES, and IM documentation in
  `evidence-map.md`.
- Codex-reported validation: none for runtime behavior; only documentation
  inspection and static module creation.
- Inference: the capstone proof should be tiered so profile readiness, producer
  compatibility, publish/prepare/submit, runtime identity, retained result, and
  CP finalization can fail independently without widening claims.

