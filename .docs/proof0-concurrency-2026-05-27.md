# Proof 0 Concurrency Ledger 2026-05-27

## Title

Proof 0 concurrency and harness-isolation audit ledger for 2026-05-27.

## Status

Status is Codex-reported, bounded, not independently audited, and not
public/demo readiness. The static example summary in the Proof 0 module remains
`validation_status: "not_run"` because it is not generated validation output.

This ledger records a safe-summary audit of generated Proof 0 classes. It does
not embed raw generated artifacts.

## Scope

The audit inspected safe generated summaries, plans, manifests, and metadata
classes for Proof 0 0B and 0C. Raw logs, raw traces, retained bundles,
payloads, raw prompts, raw model outputs, workspaces, databases, local process
records, credentials, key material, TLS, SPIFFE, Vault, WebAuthn, passkey,
bearer, token, secret, and API-key material were excluded.

Path references in this ledger are class references only, such as the Control
Plane Proof 0 generated output roots for harness-isolation plans and live
`temporal-basic` summaries. Raw artifacts are not committed here.

## Baseline

The baseline reported to this ledger was:

- Control Plane contained Proof 0 harness-isolation changes and the hardened
  generated-config/no-profile patch.
- Governed Execution Proofs contained Phase C/tooling and Proof 0 module
  changes.
- Execution Substrate and Infrastructure Manager were expected to remain
  untouched.

Authority boundaries remain unchanged. CP owns workflow/run-control, ES owns
admission/runtime/lifecycle/result authority within its boundary, and IM owns
readiness/provenance/diagnostics/support evidence.

## 0B Result Summary

0B was Codex-reported passed as no-network, plan-only harness-isolation
evidence. The safe plan summaries recorded two contact-free A/B lease plans and
excluded live actions.

The sanitized audit confirmed the plans recorded distinct run ids, output
roots, execution run roots, runtime-config roots, SQLite DB paths, Temporal
settings, fake-model/provider base URLs, report roots, attempt roots, and
finalization roots. The plans classified generated artifacts and generated
runtime configs as proof-local redaction-needed evidence/projection/diagnostics.

0B did not run live proof execution, supported-local execution, Remote Alpha
execution, Linux-host contact, Temporal startup, fake-model startup, Docker,
Nomad, Vault, SPIRE, or product services.

## 0C Result Summary

0C was Codex-reported passed for two overlapping live Remote Alpha
`temporal-basic` runs. The safe generated summaries and manifests confirmed the
bounded CP to ES `temporal-basic` class under the corrected generated-config
and no-profile live invocation shape.

The sanitized audit confirmed both live A/B summaries reported a passing final
classification, live proof execution, Temporal history exercise, and exit code
0. The audit also confirmed distinct CP run ids, output roots, execution run
roots, runtime-config roots, report roots, SQLite DB paths, Temporal settings,
fake-model/provider base URLs, ES provider ids, retained refs, finalization
refs, and materialization refs.

The overlap itself remains Codex-reported and not independently audited because
raw logs, traces, and local process records were intentionally excluded.

## Initial Failed Invocation

The initial A/B config+profile invocation was Codex-reported failed before
workflow startup. The safe summaries showed the live stage failed, workflow
startup was not reached, a runtime config was present, and the live command
still forwarded a supported-local profile.

This is recorded as a harness hazard: profile reapplication can override
isolation-critical Temporal fields after generated config has materialized the
lease. It is not a product architecture claim and not an ES or IM failure.

## Hardened Invocation

The hardened invocation passed by using the generated runtime config as the
live config source and omitting supported-local profile re-forwarding to the
nested live smoke. Profile-derived environment placeholders may still be
carried separately, but the profile is not reapplied over the generated config.

Control Plane documentation and tests now describe or cover the fail-fast
guards for direct generated-config/profile ambiguity and profile Temporal
override overlap. The 0C evidence confirms only the bounded corrected
`temporal-basic` class.

## Disjointness Summary

The sanitized 0B and 0C audit confirmed disjointness for the fields that Proof
0 tracks:

- CP run ids and run-id prefixes;
- proof output roots and execution run roots;
- runtime-config roots and generated config paths;
- report roots and report index roots;
- SQLite DB paths;
- Temporal target, UI port, namespace, workflow task queue, workspace task
  queue, and DB path;
- fake-model/provider base URL;
- ES provider ids;
- retained refs;
- finalization and materialization refs.

This disjointness is bounded to the inspected summaries/manifests and does not
prove all interleavings.

## Artifact Classification

Generated artifacts are proof-local redaction-needed
evidence/projection/diagnostics. Raw artifacts are not committed here.

Generated configs, summaries, plans, reports, traces, logs, retained refs,
profile copies, proof outputs, and validation outputs are not CP workflow
authority, ES runtime authority, IM readiness/provenance authority, semantic
finalization, or public evidence without separate redaction review.

No support bundle was found in the Proof 0 generated output class, and no IM
support bundle is part of this ledger.

## Claims Supported

This ledger supports these bounded Codex-reported claims:

- 0B produced two no-network plan-only harness-isolation lease records;
- 0C produced two live Remote Alpha `temporal-basic` A/B results under the
  hardened generated-config/no-profile invocation;
- the inspected 0C A/B results exited 0 and recorded distinct lease-critical
  fields;
- the initial config+profile failure was a harness hazard before workflow
  startup;
- generated artifacts are proof-local redaction-needed
  evidence/projection/diagnostics;
- raw generated artifacts remain excluded from authored proof docs.

## Claims Not Supported

This ledger does not prove production HA, multi-tenancy, scale, default
shared-config safety, or all interleavings. It also does not prove public/demo
readiness, independent audit, general Remote Alpha behavior, Linux-host
behavior, direct ES proof behavior, runtime identity/Vault proof behavior,
cancel/failure/destructive/recovery proof behavior, IM live-refresh behavior,
or concurrent support-bundle generation.

Proof 0 parallelism is not product architecture.

## Confirmed Proof Class

Confirmed proof class: CP to ES live Remote Alpha `temporal-basic` under a
parent-allocated isolation lease, generated runtime config as live `--config`,
and no supported-local profile re-forwarding to the nested live smoke.

The class is bounded to the inspected 0C summaries/manifests and the hardened
invocation shape.

## Unconfirmed Proof Classes

Unconfirmed classes include:

- direct ES proofs;
- runtime identity and Vault proofs;
- cancel, failure, hold, resume, reject, destructive, recovery, restart, and
  failover proofs;
- IM support-bundle proofs;
- IM live-refresh proofs;
- compare, experiment, wrapper, and child-run parallelism beyond the confirmed
  `temporal-basic` shape;
- any proof using shared profile/config defaults without explicit lease
  disjointness.

## Security/Redaction Status

Security/redaction status is bounded. The audit used safe generated summaries,
plans, manifests, and metadata only. Raw artifacts are not committed here, and
no sensitive payloads are quoted in this ledger.

Any future external-facing material needs a separate redaction review and must
preserve the evidence/projection/diagnostics label.

## Follow-Up Gates

Request Proof 0 continuation before parallelizing any unconfirmed proof class
or before running support-bundle generation concurrently with live proof
writers.

Future continuations should record explicit leases, expected artifact classes,
raw-excluded roots, redaction requirements, supported claims, non-claims, and
the authority owner for each boundary.

## Relationship To Governed Lifecycle Proof

Proof 0 can inform a governed lifecycle proof by defining when parallel proof
writers are allowed and what each writer must lease. It does not itself prove
the governed lifecycle proof, public/demo readiness, production operation, or
product HA/multi-tenancy/scale.

If lifecycle proof work needs any proof class beyond the confirmed CP to ES
`temporal-basic` shape, request a Proof 0 continuation before running parallel
live proof writers.
