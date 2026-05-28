# Public Writing Map

## Article/demo title idea

The Governed Execution Lifecycle: From CP Intent to Runtime Evidence

## Thesis

The proof story is not that a remote run magically worked. The proof story is
that a bounded governed lifecycle can keep authority separated: CP owns the
Temporal workflow and finalization, ES owns admission and runtime evidence, the
runtime boundary executes after submit, and IM remains diagnostics/provenance.

## Public-safe narrative

Describe the lifecycle as a narrow, auditable chain:

1. CP starts with explicit `temporal-basic` intent.
2. CP uses Temporal workflow state and producer compatibility checks before
   runtime handoff.
3. ES performs prepare/admission and submit handoff.
4. Nomad/Linux runtime execution happens after submit.
5. ES projects lifecycle/result metadata and retained-result refs as evidence.
6. CP materializes, reviews, and finalizes under CP-owned semantics.

Keep the public narrative attached to the two Codex-reported happy-path
rehearsals recorded in `.docs/governed-lifecycle-proof-2026-05-28.md` and to
the safe filming posture in `.docs/governed-lifecycle-filming-script.md`.

## What can be claimed after the proof

- Two bounded serial governed lifecycle rehearsals completed.
- CP Temporal workflow/history evidence exists by safe metadata.
- ES prepare/submit/lifecycle/result metadata exists.
- Retained-result materialization and CP finalization metadata exist.
- The happy-path-twice checklist is complete for filming preparation.

## Must not claim

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
- raw retained-bundle, prompt, model-output, workspace, database, credential, or
  secret-adjacent content claims.

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
- real provider ids, real hashes, real bundle references, local absolute paths,
  remote filesystem paths, endpoint values, and local process records.

## Exact evidence distinctions

- **Theory**: authority-separated execution should be easier to audit than a
  single broad "execution worked" story.
- **Repo-grounded design**: authored CP/ES/IM boundary docs and
  `.docs/proof-module-conventions.md` define who owns workflow, runtime,
  diagnostics, evidence, and finalization.
- **Codex-reported validation**: the lifecycle ledger records two bounded
  serial `temporal-basic` happy-path rehearsals and their safe metadata status.
- **Live proof**: a separately authorized run that produces fresh runtime
  evidence under stated controls. This module does not authorize or rerun one.
- **Inference**: the public story may infer that the recorded rehearsals support
  filming preparation for the governed lifecycle, but it must not infer
  production readiness, public/demo readiness, independent audit, or unrun
  behaviors.

## Safe wording

- "This is a Codex-reported, bounded, serial governed lifecycle proof."
- "Two `temporal-basic` happy-path rehearsals are recorded in the lifecycle
  ledger."
- "CP owns workflow state, materialization, review, and finalization."
- "ES owns admission, submit handoff, lifecycle/result evidence, and
  retained-result refs."
- "IM support-bundle and runtime identity/Vault behavior are separate future
  proof topics."
- "Public/demo readiness is not claimed until a final demo-readiness audit."

## Wording to avoid

- "The system is production ready."
- "The proof is independently audited."
- "The support bundle proves the run."
- "ES finalizes the CP run."
- "Runtime identity and Vault credentials succeeded."
- "The lifecycle ledger alone proves public/demo readiness."
