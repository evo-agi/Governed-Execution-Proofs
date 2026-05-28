# Claims

Current evidence status: Codex-reported two-pass governed lifecycle evidence is
recorded in `.docs/governed-lifecycle-proof-2026-05-28.md`. The static example
remains `validation_status: "not_run"` because it is a template, not proof
evidence status. Independent audit and public/demo readiness are not claimed.

## Supported claims

This module may make these bounded claims:

- Two bounded serial governed lifecycle rehearsals completed.
- CP Temporal workflow/history evidence exists by safe metadata.
- ES prepare/submit/lifecycle/result metadata exists.
- Retained-result materialization and CP finalization metadata exist.

The supported claims are Codex-reported and scoped to the recorded
`temporal-basic` happy-path rehearsals. They do not expand the remote
normal-shell roadmap into a completed full-roadmap proof.

## Explicit non-claims

This module must not claim:

- production readiness;
- HA;
- multi-tenancy;
- general remote deployment;
- cancel/failure/intervention behavior;
- runtime identity/Vault credential success as a dedicated proof;
- IM support-bundle proof;
- independent audit;
- public/demo readiness by itself;
- support-bundle authority;
- retained bundle semantic finalization by ES;
- remote provisioning or remote reconciler behavior;
- general runtime identity architecture;
- raw retained-bundle, prompt, model-output, workspace, database, credential, or
  secret-adjacent content claims.

## Authority, evidence, and projection labels

- CP-owned facts include Temporal workflow state, workflow/history metadata,
  review, retained-result materialization, and finalization.
- ES-owned facts include producer compatibility, prepare/admission,
  submit handoff, lifecycle projection, result metadata, and retained-result
  references.
- Nomad/Linux runtime facts remain runtime execution evidence after submit.
- IM profile, readiness, provenance, and support-bundle surfaces remain
  diagnostics/provenance only unless a separate proof validates them.
- Generated artifacts and validation outputs remain evidence/projection/
  diagnostics only.

## Sensitive/generated classes excluded

This module excludes:

- raw generated artifact contents;
- `.out` contents;
- raw logs, traces, reports, retained bundles, support bundles, and archives;
- databases and local process records;
- env files;
- keys, certificates, tokens, secrets, API keys, bearer material, and credential
  payloads;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, and private-key material;
- raw prompts and raw model outputs;
- workspaces, checkpoints, quarantines, and restores;
- real provider ids, real hashes, real bundle references, local absolute paths,
  and remote filesystem paths.

## Claim-review checklist

Before using this module for audit or public writing, verify:

- The static example remains `validation_status: "not_run"`.
- CP/Temporal review and finalization stay CP-owned.
- ES lifecycle/result facts stay evidence/projection and do not become CP
  finalization.
- IM diagnostics stay outside CP run-control and ES runtime authority.
- Runtime identity/Vault, support bundle, and cancel/failure/intervention remain
  excluded unless separate future proofs are explicitly authorized and recorded.
- Raw generated artifacts are not copied into the proof repo.
