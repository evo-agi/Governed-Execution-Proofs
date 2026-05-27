# Validation Plan

## Current status

Static example status: `not_run`.

This module was added without running live proofs, supported-local commands,
Remote Alpha commands, Linux-host commands, CP/ES/IM live validation commands,
Temporal services, fake model servers, Docker, Nomad, Vault, SPIRE, or product
services.

Later operator-supplied context reports that a bounded 0C live two-run Remote
Alpha `temporal-basic` proof was attempted and then completed under a corrected
invocation shape. This plan records that only as Codex-reported evidence
interpretation:

- the initial config-plus-profile A/B invocation failed before workflow startup
  because the nested live smoke reapplied the profile Temporal target over the
  generated isolated config;
- the corrected A/B invocation used the generated Remote Alpha runtime config
  as `--config`, omitted the profile argument, and was reported passed;
- no raw generated artifacts, logs, traces, reports, profiles, run ids,
  provider ids, local paths, or sensitive payloads are imported into this
  module;
- the report is not independent inspection and does not establish general
  concurrency support.

## Tier 0A: commit-only static package

Purpose: commit the authored Proof 0 module and any non-live harness-isolation
groundwork.

Pass interpretation:

- The proof module has the required six authored files.
- The static summary remains `validation_status: "not_run"`.
- Claims and non-claims are explicit.
- Authority boundaries stay separated.
- Generated artifacts remain evidence/projection/diagnostics only.

Fail interpretation:

- Static docs overclaim validation.
- Static docs import generated payloads.
- Static docs turn harness outputs into CP, ES, or IM authority.

## Tier 0B: future local no-network harness-isolation validation

Purpose: later, with explicit authorization, run a deterministic no-network
check that two planned harness configurations do not share run id, output root,
report root/index, SQLite DB path, Temporal target/namespace/queues/DB path/UI
port, fake-model URL, attempt paths, or finalization paths.

Required controls before 0B:

- no live host contact;
- no supported-local execution unless the selected command is confirmed
  no-network and does not start services;
- no Temporal, fake model, Docker, Nomad, Vault, SPIRE, or product service
  startup;
- explicit endpoint/base-URL selections where `--isolation-id` leaves them as
  operator-owned inputs;
- generated plan or validation output treated as evidence-only.

## Tier 0C: future live two-run Remote Alpha temporal-basic validation

Purpose: later, with explicit authorization, run two live Remote Alpha
`temporal-basic` validations using isolated harness configuration.

Required controls before 0C:

- explicit live-run authorization;
- unique Control Plane run roots and SQLite DB paths;
- unique report roots or non-shared report-index writes;
- unique Temporal target/namespace/queues, dev-server DB path, and UI port;
- unique fake-model URL/port or verified fake-model run-state isolation;
- no IM support-bundle ingestion in Proof 0 core;
- generated artifacts and validation outputs kept as evidence/projection only.

## Claims not supported

This validation plan does not prove 0B or 0C. It does not prove live Temporal,
supported-local, Remote Alpha, Linux-host, Docker, Nomad, Vault, SPIRE,
fake-model service behavior, ES runtime success, provider success, production
readiness, high availability, multi-tenancy, public/demo readiness, or
independent audit.

## Generated artifacts

Later generated harness plans, validation summaries, reports, traces, logs,
profiles, retained bundles, and support bundles must remain out of this static
module unless separately authorized as redacted validation records. They remain
evidence/projection/diagnostics only.
