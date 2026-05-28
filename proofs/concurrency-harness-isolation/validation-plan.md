# Validation Plan

## Current evidence status

Current proof evidence:

- Codex-reported 0B no-network plan-only harness-isolation evidence: passed.
- Codex-reported 0C bounded live Remote Alpha `temporal-basic` evidence: passed.
- Confirmed class: CP to ES `temporal-basic` with explicit isolation leases.
- Other proof classes require a Proof 0 continuation before parallel live
  execution.
- Independent audit: not claimed.
- Public/demo readiness: not claimed.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

At initial static package creation, this authored module was added without
running live proofs, supported-local commands, Remote Alpha commands, Linux-host
commands, CP/ES/IM live validation commands, Temporal services, fake model
servers, Docker, Nomad, Vault, SPIRE, or product services.

The later bounded status is recorded in
`.docs/proof0-concurrency-2026-05-27.md`:

- 0B is Codex-reported passed as no-network, plan-only harness-isolation
  evidence;
- 0C is Codex-reported passed for two overlapping live Remote Alpha
  `temporal-basic` runs under the hardened generated-config/no-profile
  invocation;
- the initial config-plus-profile A/B invocation failed before workflow
  startup because profile reapplication could override isolation-critical
  Temporal fields after generated config materialized the lease;
- no raw generated artifacts, logs, traces, reports, profiles, run ids,
  provider ids, local paths, or sensitive payloads are imported into this
  module;
- the 0B/0C record is not independent inspection and does not establish general
  parallel proof coverage.

## Tier 0A: commit-only static package

Purpose: commit the authored Proof 0 module and any non-live harness-isolation
groundwork.

Pass interpretation:

- The proof module has the required authored files; its public-writing map is
  supplemental authored documentation.
- The static summary remains `validation_status: "not_run"`.
- Claims and non-claims are explicit.
- Authority boundaries stay separated.
- Generated artifacts remain evidence/projection/diagnostics only.

Fail interpretation:

- Static docs overclaim validation.
- Static docs import generated payloads.
- Static docs turn harness outputs into CP, ES, or IM authority.

## Tier 0B: Codex-reported local no-network harness-isolation validation

Purpose: record a deterministic no-network plan-only check that two planned
harness configurations do not share run id, output root, report root/index,
SQLite DB path, Temporal target/namespace/queues/DB path/UI port, fake-model
URL, attempt paths, or finalization paths.

Codex-reported status:

- two contact-free A/B plan summaries were reported;
- live actions were excluded;
- generated artifacts and generated runtime configs were classified as
  proof-local redaction-needed evidence/projection/diagnostics;
- no host contact or service startup is claimed.

Required controls before 0B:

- no live host contact;
- no supported-local execution unless the selected command is confirmed
  no-network and does not start services;
- no Temporal, fake model, Docker, Nomad, Vault, SPIRE, or product service
  startup;
- explicit endpoint/base-URL selections where `--isolation-id` leaves them as
  operator-owned inputs;
- generated plan or validation output treated as evidence-only.

## Tier 0C: Codex-reported live two-run Remote Alpha temporal-basic validation

Purpose: record the bounded CP to ES Remote Alpha `temporal-basic` class under
isolated harness configuration.

Codex-reported status:

- initial config+profile A/B invocation failed before workflow startup and is
  classified as a harness hazard;
- corrected/hardened A/B invocation passed with generated runtime config as
  live `--config` and no supported-local profile re-forwarding;
- both reported runs exited 0 and recorded distinct CP run ids, output roots,
  Temporal settings, fake-model/provider URLs, ES provider ids, retained refs,
  finalization refs, and materialization refs;
- 0C confirmed the CP to ES `temporal-basic` class only.

Required controls before 0C:

- explicit live-run authorization;
- unique Control Plane run roots and SQLite DB paths;
- unique report roots or non-shared report-index writes;
- unique Temporal target/namespace/queues, dev-server DB path, and UI port;
- unique fake-model URL/port or verified fake-model run-state isolation;
- no IM support-bundle ingestion in Proof 0 core;
- generated artifacts and validation outputs kept as evidence/projection only.

Other proof classes require a separate Proof 0 continuation before parallel live
execution.

## Claims not supported

This validation plan does not prove live Temporal behavior beyond the bounded
Codex-reported 0C path, supported-local behavior beyond that path, Remote Alpha
behavior beyond that path, Linux-host behavior, Docker, Nomad, Vault, SPIRE,
fake-model service behavior, ES runtime success, provider success, production
readiness, high availability, multi-tenancy, public/demo readiness,
independent audit, default shared-config safety, all interleavings, direct ES
proof parallelism, runtime identity/Vault proof parallelism, cancel/failure
proof parallelism, IM support-bundle proof parallelism, IM live-refresh
parallelism, or destructive/recovery proof parallelism.

## Generated artifacts

Later generated harness plans, validation summaries, reports, traces, logs,
profiles, retained bundles, and support bundles must remain out of this static
module unless separately authorized as redacted validation records. They remain
evidence/projection/diagnostics only.
