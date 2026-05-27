# Deterministic Validation Ledger: 2026-05-27

## Scope

This ledger records Codex-reported deterministic validation for the committed
static proof portfolio. It is a documentation ledger only. Raw command output is
not committed in this ledger, and this ledger is not live proof output.

The Codex-reported deterministic validation described here is bounded to
summarized deterministic command outcomes. No supported-local, Remote Alpha,
Linux-host, Docker, Nomad, Vault, SPIRE, or Temporal server commands were run.

## Portfolio baseline

- Governed Execution Proofs commit:
  `9c23f9f0a4cab6e4e03aa27c32997373ac1878b6`
- Commit message: `Add static Governed Execution proof portfolio`

## Validation status vocabulary

- Static example: authored proof-planning material, including
  `proof-summary.example.yaml`, that may remain `validation_status: "not_run"`.
- Codex-reported deterministic validation: command provenance and summarized
  deterministic outcomes reported by Codex, without committing raw command
  output.
- Independently inspected validation output: separately reviewed validation
  output with its own provenance and redaction record. This ledger does not
  claim that status.
- Live proof output: server-backed or host-backed proof output from an
  authorized live validation run. This ledger does not claim that status.
- Inference: a bounded conclusion drawn from static docs, source anchors, or
  reported deterministic outcomes. Inference must be labeled and must not be
  promoted into authority.

## CP deterministic validation

Codex-reported deterministic validation for
`proofs/workflow-authority-rejects-stale-action-intent` used these reported
commands:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_mismatched_actionability_fingerprint_rejects_before_mutation_and_valid_action_remains
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_actionability_fingerprint_rejects_request_copied_from_stale_snapshot
PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests/test_monitoring_interventions.py::test_guarded_current_attempt_cancel_uses_snapshot_fingerprint_and_durable_context
```

Reported summarized results:

- `1 passed in 1.09s`
- `1 passed in 0.35s`
- `1 passed in 0.34s`

The Codex-reported deterministic validation supports only deterministic CP
guard behavior for stale and current actionability fingerprints. It does not
claim live Temporal, supported-local, ES runtime, browser/WebAuthn, Remote
Alpha, Linux-host, Docker, Nomad, Vault, or SPIRE behavior.

## ES deterministic validation

Codex-reported deterministic validation for
`proofs/es-envelope-is-not-cp-finalization` used these reported commands:

```bash
go test -run TestPrimaryMilestoneRealignmentPreservesESOwnership -count=1 .
go test ./...
```

Reported summarized results:

- targeted test: `ok execution-substrate 0.242s`
- full `go test ./...` reported as passing across packages

The Codex-reported deterministic validation supports only deterministic ES
ownership and envelope/evidence boundaries. It does not claim live runtime
proof, Nomad/Docker/Vault/SPIRE/Temporal live behavior, Remote Alpha/Linux-host
behavior, CP semantic finalization, or live retained-result availability.

## IM deterministic validation

Codex-reported deterministic validation for
`proofs/im-support-packet-is-evidence-not-authority` included an initial bare
pytest collection issue:

- `ModuleNotFoundError: No module named 'infra_manager'`

The validator then reran with `PYTHONPATH=src` and no installs. This provenance
is recorded so the import-path issue is not hidden. The first collection issue
is not described as a proof failure, and the later Codex-reported deterministic
validation is not packaging or install validation.

Reported summarized passing batches:

- `6 passed`
- `32 passed`
- `72 passed`

The Codex-reported deterministic validation supports only deterministic IM
diagnostics/provenance/evidence boundaries and failure-closed handling for
malformed, stale, secret-like, or overclaiming evidence. It does not claim live
host contact, Remote Alpha live proof, Linux-host, Docker, Nomad, Vault, SPIRE,
Temporal, production readiness, CP authority, or ES runtime behavior.

## Remote roadmap status

Codex-reported deterministic validation did not run
`proofs/remote-normal-shell-live-proof-roadmap`. The remote normal-shell live
proof remains future-facing and not run. No Linux-host validation was performed,
and no supported-local or Remote Alpha commands were run.

## Claims supported

The Codex-reported deterministic validation supports:

- stale or mismatched CP actionability fingerprints reject before mutation;
- stale CP snapshot requests fail closed;
- valid guarded CP cancel uses a snapshot fingerprint and durable CP context;
- CP workflow/query state remains guarded-action authority;
- ES owns admission and runtime boundaries;
- ES prepare, submit, status, result, cancel, and log surfaces stay bounded
  envelope or evidence surfaces;
- ES lifecycle projection remains evidence/projection;
- retained results remain opaque ES artifacts;
- `authority_handoff` is non-secret handoff evidence, not credential or CP
  authority;
- IM outputs remain diagnostics/provenance/evidence only;
- Remote Alpha readiness and support artifacts preserve non-authority labels;
- support bundles do not become CP or ES authority;
- malformed, stale, secret-like, or overclaiming IM evidence fails closed;
- IM no-contact support-bundle boundary behavior is covered.

## Claims not supported

The Codex-reported deterministic validation does not support:

- live Temporal behavior;
- supported-local behavior;
- live ES runtime behavior;
- browser or WebAuthn behavior;
- Remote Alpha behavior;
- Linux-host behavior;
- Docker, Nomad, Vault, or SPIRE live behavior;
- CP semantic finalization from ES evidence;
- live retained-result availability;
- live host contact;
- production readiness;
- CP authority from IM evidence;
- ES runtime behavior from IM evidence.

This does not prove production readiness, HA, multi-tenancy, provider-side
cancel effect, live ES runtime, credential success, support-bundle authority,
retained-bundle finalization, or general deployment architecture.

## Generated/ignored artifact note

Generated artifacts, caches, `.out`, reports, logs, support bundles, retained
bundles, profiles, and validation output remain evidence/projection/diagnostics
only. They are not authority, not finalization, and not proof of production
readiness.

## Sensitive artifact exclusions

This ledger excludes raw logs, traces, reports, retained bundles, support
bundles, prompt or model outputs, workspaces, database files, environment files,
key material, certificates, tokens, secrets, API keys, bearer material, TLS,
SPIFFE, Vault, WebAuthn, passkey material, local process records, and raw
validation output.

## Public-writing implications

Public writing may refer to this as Codex-reported deterministic validation for
the committed static proof portfolio baseline. Public writing must not describe
this ledger as independently inspected validation output, live proof output,
production readiness, Remote Alpha success, Linux-host proof, credential
success, support-bundle authority, retained-bundle finalization, or general
deployment architecture.

## Follow-up validation ladder

Future validation should stay tiered:

- keep static examples labeled separately from Codex-reported deterministic
  validation;
- if raw validation output is independently inspected later, record separate
  provenance, redaction review, and non-claims;
- run supported-local or live proof commands only with explicit authorization;
- keep Remote Alpha, Linux-host, Docker, Nomad, Vault, SPIRE, and Temporal
  server validation as future-facing until separately run and recorded;
- never convert generated artifacts, retained bundles, support bundles, reports,
  logs, or validation output into CP, ES, or IM authority.
