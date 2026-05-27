# Proof Module Conventions

## Purpose

This document gives minimal guidance for authored proof modules in this repo. It
helps keep static proof planning, validation claims, evidence labels, and public
writing labels consistent without creating a shared proof framework.

## Scope

Proof modules are isolated folders under `proofs/`. Each module stands on its
own scenario, claims, evidence, example summary, validation plan, and public
writing posture. Module content may cite adjacent authored docs, source, and
tests, but it must not import generated payloads into the repo.

## Proof module layout

A module may contain:

- `scenario.md`
- `claims.md`
- `evidence-map.md`
- `proof-summary.example.yaml`
- `validation-plan.md`
- `public-writing-map.md`

Those files are authored documentation. They are not product runtime code,
schemas, scripts, tests, or generated proof output.

## Static/example-first default

Static examples are not validation output. A static example summary describes
the intended claim shape and expected evidence classes only.

`validation_status: "not_run"` means no validation command has been run for
that proof. Keep that label until a later authorized validation pass records its
own scope, command provenance, generated artifacts, redaction review, and
non-claims outside the static example.

## Authority and evidence labels

Use explicit labels for authority and non-authority surfaces:

- Control Plane workflow/query state, guarded writes, review, checkpoints,
  intervention, escalation, and finalization are CP authority.
- Execution Substrate admission, prepare, submit handoff, lifecycle projection,
  outcome evidence, retained opaque bundles, and runtime handoff are ES-owned
  runtime or evidence surfaces.
- Infrastructure Manager profile, doctor, readiness, provenance, support
  packet, redaction, and digest outputs are IM diagnostics/provenance/evidence
  surfaces.
- Generated proof outputs, `.out`, reports, traces, support bundles, profiles,
  logs, retained bundles, and validation output are evidence, projection, or
  diagnostics only.
- UI, report, channel, browser, CLI, dashboard, notification, and similar
  surfaces are presentation or guarded action-adapter surfaces only.

ES facts do not override CP workflow state. IM facts do not become CP
run-control authority or ES runtime authority. Retained bundles and support
bundles do not become semantic finalization.

## Validation status labels

Use validation labels plainly:

- `not_run`: no validation command was run for this proof.
- `planned`: future validation is described but not executed.
- `blocked`: validation could not proceed under the stated controls.
- `passed`: only for a later authorized validation record that names the scope,
  commands, evidence, and non-claims.

Static modules should default to `not_run`.

## Evidence reference rules

Use repo-relative references only, such as:

- `Control Plane: path/to/file.py:line-line`
- `Execution Substrate: path/to/file.md:line-line`
- `Infrastructure Manager: path/to/file.md:line-line`

Prefer narrow line anchors. If a broader anchor is unavoidable, state exactly
which claim it supports and avoid reading neighboring material as part of the
proof. Re-audit anchors after adjacent repos change.

## Sensitive/generated artifact exclusions

Proof modules must not copy or quote sensitive or generated payloads, including
raw `.out` contents, logs, traces, reports, retained bundles, support bundles,
archives, databases, environment files, key material, certificate bodies, TLS,
SPIFFE, Vault, WebAuthn, passkey, API key, bearer material, tokens, secrets,
raw prompts, raw model outputs, workspaces, checkpoints, quarantines, restores,
or local process records.

Mention those classes only as exclusions, non-claims, or redaction
requirements.

## Public-writing labels

Public writing must separate:

- theory;
- repo-grounded evidence;
- Codex-reported static inspection or validation status;
- inference.

Article, demo, and diagram claims must stay bounded to the module's validated or
static status. Public wording must not turn proof outputs, reports, UI, support
packets, retained bundles, or generated summaries into authority.

## Non-goals

This document does not create a shared proof framework, product schema,
validation runner, generated artifact contract, or product architecture.

Remote Alpha is bounded and pre-live. It is not production, HA, multi-tenant,
remote provisioning, a remote reconciler, or a general deployment architecture.

Proof modules do not define product architecture.
