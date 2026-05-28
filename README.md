# Governed Execution Proofs

This repository contains authored proof packages for governed execution claims.
It is a documentation, schema, and local-linting repo. It is not product
runtime code, not a generated proof-output store, and not a live validation
runner.

`.docs/` is the project source of truth. This README is a navigational summary;
when README wording and `.docs/` disagree, treat `.docs/` as authoritative and
fix the drift before widening any claim.

## What This Repo Protects

The proof portfolio keeps evidence claims bounded to the system surface that
owns them:

- Control Plane owns workflow/query state, guarded writes, review,
  intervention, escalation, materialization, and finalization.
- Execution Substrate owns admission, prepare, submit handoff, lifecycle
  projection, runtime outcome evidence, retained opaque result references, and
  runtime handoff boundaries.
- Infrastructure Manager owns readiness, profile, provenance, diagnostics,
  support-packet, redaction, and digest evidence.
- Generated outputs, reports, traces, logs, `.out` trees, retained bundles,
  support bundles, profiles, databases, and validation output remain
  evidence/projection/diagnostics only.

ES evidence does not become CP finalization. IM diagnostics do not become CP
run-control authority or ES runtime authority. Retained bundles and support
bundles do not become semantic finalization.

## Source Documents

Start here before changing claims, modules, or validation wording:

- `.docs/proof-module-conventions.md` - required module shape, status labels,
  authority labels, evidence-reference rules, and public-writing posture.
- `.docs/parallel-proof-execution-policy.md` - Proof 0 lease and parallel proof
  execution policy.
- `.docs/proof0-concurrency-2026-05-27.md` - Codex-reported Proof 0 concurrency
  ledger.
- `.docs/deterministic-validation-2026-05-27.md` - Codex-reported
  deterministic validation ledger.
- `.docs/live-validation-phase-a-2026-05-27.md` - bounded Codex-reported live
  Phase A ledger and post-run audit summary.
- `.docs/governed-lifecycle-proof-2026-05-28.md` - bounded two-pass governed
  lifecycle proof ledger.
- `.docs/remote-normal-shell-live-validation-plan.md` - future-facing remote
  normal-shell live validation plan.

## Repository Layout

```text
.docs/      Authored source-of-truth policy, convention, plan, and ledger docs
proofs/     Isolated authored proof modules
schemas/    JSON schemas for static summaries and validation records
tools/      Local proof-doc and redaction-risk checkers
tests/      Tests for schemas, checkers, and current proof modules
```

Each proof module under `proofs/` stands alone. The standard authored module
files are:

- `scenario.md`
- `claims.md`
- `evidence-map.md`
- `proof-summary.example.yaml`
- `validation-plan.md`

`public-writing-map.md` is allowed as supplemental documentation, but it is not
required.

## Current Proof Modules

| Module | Current evidence posture |
| --- | --- |
| `proofs/workflow-authority-rejects-stale-action-intent` | Codex-reported deterministic CP stale-action validation exists; live Temporal, provider-side cancel effect, ES runtime, and public/demo readiness are not claimed. |
| `proofs/es-envelope-is-not-cp-finalization` | Codex-reported deterministic ES boundary validation exists; ES envelope evidence remains separate from CP semantic finalization. |
| `proofs/im-support-packet-is-evidence-not-authority` | Codex-reported deterministic IM evidence-boundary validation exists; IM support-bundle claims remain unvalidated. |
| `proofs/remote-normal-shell-live-proof-roadmap` | Future-facing capstone roadmap with bounded Phase A evidence recorded separately; full roadmap completion, independent audit, and public/demo readiness are not claimed. |
| `proofs/concurrency-harness-isolation` | Static Proof 0 module with Codex-reported 0B/0C bounded evidence; only the confirmed CP-to-ES `temporal-basic` parallel class is covered. |
| `proofs/governed-execution-lifecycle` | First-class lifecycle module backed by Codex-reported two-pass serial `temporal-basic` evidence; broader cancel/failure/intervention, runtime identity/Vault, IM support-bundle, and public/demo readiness claims remain excluded. |

Static `proof-summary.example.yaml` files remain `validation_status: "not_run"`
by convention. They are examples, not run output. Deterministic, live, or
independently inspected outcomes belong in ledgers or validation records, not
in static example summaries.

## Local Checks

Run the local checks before committing proof-package or README changes:

```bash
python3 tools/check_proof_docs.py .
python3 tools/scan_redaction_risk.py .
python3 -m pytest
```

These checks validate authored document shape, schema expectations,
repo-relative references, static example status, claim hygiene, and
redaction-risk markers. They do not run product systems, contact hosts, inspect
raw generated artifacts, prove runtime truth, or promote local output into
authority.

## Working Rules

When changing this repo:

1. Read the relevant `.docs/` files first.
2. Keep proof modules isolated under `proofs/`.
3. Keep static example summaries static and labeled `not_run`.
4. Record validation results in ledgers or validation-plan updates with command
   provenance, supported claims, unsupported claims, artifact classes,
   independent-audit status, and redaction review.
5. Use repo-relative evidence references, preferably with narrow line anchors.
6. Keep raw generated artifacts and sensitive payloads out of the repo.
7. Preserve CP/ES/IM authority boundaries and label inference as inference.
8. Update `.docs/` whenever reality changes, then update module docs and this
   README to match.

Surface conflicts instead of working around them.

## Non-claims And Exclusions

Unless a future `.docs/` ledger explicitly records otherwise, this repo does
not claim independent audit, public/demo readiness, production readiness, HA,
multi-tenancy, general deployment architecture, remote provisioning,
reconciler behavior, browser/WebAuthn coverage, general Vault/SPIRE readiness,
runtime credential success, support-bundle authority, retained-bundle
finalization, all-mode CP validation, or all proof-class parallelism.

Do not commit or quote raw `.out` contents, logs, traces, reports, retained
payloads, support bundles, prompts, model outputs, workspaces, checkpoints,
quarantines, restores, databases, endpoint values, environment files, key or
certificate material, TLS/SPIFFE/Vault/WebAuthn/passkey material, API keys,
bearer material, tokens, secrets, credentials, or local process records.
