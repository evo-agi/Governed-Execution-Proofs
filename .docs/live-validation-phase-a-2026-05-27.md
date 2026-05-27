# Live Validation Phase A Ledger: 2026-05-27

## Scope

This ledger records Codex-reported live Phase A evidence and the
Codex-reported post-run audit for one bounded Remote Alpha `temporal-basic`
normal-shell validation path. It is authored proof documentation only.

Raw generated artifacts are not committed here. This ledger is not independent
audit. This ledger is not public/demo readiness.

The ledger does not authorize new validation, rerun any product system, contact
any host, inspect raw retained/generated payloads, or promote generated evidence
into authority.

## Status

Status: Codex-reported live Phase A passed; Codex-reported post-run audit ready
for proof-doc update.

The static proof examples remain static examples. Generated artifacts, `.out`,
reports, traces, support bundles, retained bundles, profiles, logs, local proof
outputs, and validation outputs remain evidence/projection/diagnostics only.

No independent audit claim should be made. Public/demo readiness remains
unclaimed.

## Baseline commits

- Static proof portfolio baseline:
  `9c23f9f0a4cab6e4e03aa27c32997373ac1878b6`.
- Deterministic validation ledger baseline:
  `53ec95be677b742729cdf55328dcaff85d45cf9c`.
- Remote normal-shell live validation plan baseline:
  `54c66ef3d9e8ee0902a92354812e98a176145f31`.

## Phase A command/result summary

One bounded Remote Alpha `temporal-basic` run was Codex-reported completed
through the documented Control Plane stage-gated driver.

- Run id/timestamp:
  `supported-local-validation-temporal-basic-20260527T162148Z`.
- Main generated run directory:
  `Control Plane: tests/manual_smoke/project/.out/supported-local-validation-temporal-basic-20260527T162148Z/`.
- Contract-probe directory:
  `Control Plane: tests/manual_smoke/project/.out/supported-local-validation-temporal-basic-20260527T162148Z-contract-probe/`.
- Report HTML:
  `Control Plane: tests/manual_smoke/project/.out/reports/supported-local-validation-temporal-basic-20260527T162148Z.html`.
- Temporal DB path class:
  `Control Plane: tests/manual_smoke/project/.out/temporal/dev-server.db`.

Services started by Phase A were reported stopped. No IM support bundle was
generated.

## Phase B post-run audit summary

The Codex-reported post-run audit recorded:

- generated run and contract-probe directories were found;
- report HTML and report index were found by metadata;
- the Temporal DB path existed by metadata only, and DB contents were not
  opened;
- ports 18081, 7233, and 8233 were closed;
- CP summaries/manifests reported proof passed, Temporal workflow/history
  exercised, CP finalization/review/materialization evidence, and terminal
  success;
- ES evidence showed contract/probe/preflight, submit handoff,
  lifecycle/status/result evidence, and retained-result references;
- IM evidence was limited to profile/config/preflight provenance;
- no IM support bundle was generated;
- generated summaries/manifests/reports are redaction-needed;
- raw logs, traces, retained payloads, prompts, model outputs, workspaces, DB
  contents, credentials, and secret-adjacent material were not quoted;
- normalized planner/audit/review files have a classification tension and
  remain redaction-needed or unknown until publication policy explicitly allows
  them.

Phase B recommendation: ready for proof-doc update. IM support-bundle
generation remains deferred.

## Artifact inventory by class

| Class | Example reference | Classification | Repo treatment |
| --- | --- | --- | --- |
| CP generated run directory | `Control Plane: tests/manual_smoke/project/.out/supported-local-validation-temporal-basic-20260527T162148Z/` | Generated evidence/projection | Excluded from this repo |
| CP contract-probe directory | `Control Plane: tests/manual_smoke/project/.out/supported-local-validation-temporal-basic-20260527T162148Z-contract-probe/` | Generated contract/preflight evidence | Excluded from this repo |
| CP report HTML/index | `Control Plane: tests/manual_smoke/project/.out/reports/supported-local-validation-temporal-basic-20260527T162148Z.html` | Generated report, redaction-needed | Excluded from this repo |
| Temporal DB path class | `Control Plane: tests/manual_smoke/project/.out/temporal/dev-server.db` | Generated database artifact | Metadata only; contents not opened |
| ES contract/preflight/handoff/result references | Summarized Phase A/B evidence classes | ES evidence/projection | Not CP finalization authority |
| IM profile/config/preflight provenance | Summarized Phase A/B evidence classes | IM diagnostics/provenance | Not readiness/support authority |
| Support bundle | None generated | Deferred | No bundle claim |

## Claims supported

Codex-reported live Phase A evidence supports only these bounded claims:

- one bounded `temporal-basic` CP Temporal normal-shell path completed;
- stage-gated validation passed for that bounded run;
- ES contract/preflight/handoff/retained-result evidence supports the run;
- CP-owned review, finalization, and materialization completed for the run;
- generated outputs remain evidence/projection/diagnostics.

## Claims not supported

This ledger does not support:

- production readiness;
- HA;
- multi-tenancy;
- general deployment architecture;
- remote provisioning or reconciliation;
- default remote runtime;
- all CP proof modes;
- browser/WebAuthn coverage;
- provider-side cancel behavior;
- support-bundle authority;
- retained-bundle semantic finalization by ES;
- general Vault/SPIRE production readiness;
- independent audit;
- public/demo readiness.

## Security/redaction status

Raw generated artifacts are not committed here. Generated summaries, manifests,
reports, and normalized planner/audit/review files remain redaction-needed or
unknown until explicit publication policy allows them.

This ledger does not quote raw logs, traces, retained payloads, prompts, model
outputs, workspaces, checkpoint/quarantine/restore contents, DB contents,
credentials, TLS/SPIFFE/Vault/WebAuthn/passkey/API-key material, local process
records, or secret-adjacent material.

## Authority-boundary status

The proof repo remains authored documentation and local linting only. It is not
Control Plane run-control authority, Execution Substrate runtime authority, or
Infrastructure Manager readiness/support authority.

CP-owned review/finalization/materialization evidence remains CP authority for
the bounded run. ES contract, preflight, handoff, lifecycle/status/result, and
retained-result references remain ES evidence/projection. IM profile/config and
preflight provenance remain IM diagnostics/provenance.

Generated artifacts, reports, `.out`, traces, support bundles, retained
bundles, profiles, logs, local proof outputs, and validation outputs remain
evidence/projection/diagnostics only.

## Support-bundle status

IM support-bundle generation remains deferred. No support bundle was generated,
committed, inspected as raw content, or used as authority.

Support-bundle claims remain unvalidated until a separately authorized run
records its own scope, command provenance, redaction review, artifact
classification, and non-claims.

## Public-writing implications

Public writing may say, if it keeps the labels attached, that there is
Codex-reported live Phase A evidence for one bounded `temporal-basic` CP
Temporal normal-shell path and a Codex-reported post-run audit ready for
proof-doc update.

Public writing must not call this independent audit, public/demo readiness,
production readiness, HA, multi-tenancy, general deployment architecture,
default remote runtime, all-mode CP validation, provider-side cancel behavior,
support-bundle authority, ES semantic finalization, or general Vault/SPIRE
production readiness.

## Follow-up tasks

- Keep generated/raw artifacts out of this repo.
- Re-audit any publication text against supported claims and non-claims.
- Resolve the normalized planner/audit/review file classification tension
  before publication.
- Generate and audit an IM support bundle only under separate explicit
  authorization.
- Obtain independent audit separately before making any independent-audit
  claim.
