# Claims

Validation status: static example only. The example remains `not_run`; bounded
Codex-reported 0B and 0C status is recorded in
`.docs/proof0-concurrency-2026-05-27.md`.

## Supported claims

This module may make these narrow claims:

- Proof 0 has an authored scenario for generic parallel-proof execution and
  harness-isolation policy.
- Proof 0 identifies the harness-owned resources that must be unique before
  parallel live proof execution.
- A proof isolation lease is the required parent-allocated boundary for live
  proof writers.
- Static/audit subagents may be used for read-only planning, inspection, docs,
  proof-package updates, and post-run audits.
- Live proof subagents may run in parallel only with explicit leases and a
  confirmed or deliberately tested proof class.
- Control Plane harness isolation belongs to proof-run configuration and
  generated evidence surfaces, not product runtime authority.
- ES run-scoped staging, retained-result, provider-id, and runtime-handoff
  facts remain ES-owned evidence or runtime boundaries.
- IM evidence/support roots remain diagnostics/provenance and stay outside
  Proof 0 core.
- Static proof documentation keeps generated artifacts and validation outputs
  evidence-only.
- Codex-reported 0B may be described only as no-network plan-only
  harness-isolation evidence.
- Codex-reported 0C may be described only as bounded live evidence for the CP
  to ES `temporal-basic` class under the hardened generated-config/no-profile
  invocation shape.
- The initial config+profile 0C failure may be described as a harness hazard:
  profile reapplication can override isolation-critical Temporal fields after
  generated config materializes the lease.

## Explicit non-claims

This module must not claim:

- independently inspected Proof 0 pass;
- live Temporal behavior beyond the bounded Codex-reported 0C path;
- supported-local behavior beyond the bounded Codex-reported 0C path;
- Remote Alpha behavior beyond the bounded Codex-reported 0C path;
- Linux-host behavior;
- Docker, Nomad, Vault, SPIRE, or fake-model service behavior;
- ES runtime success;
- provider success;
- general parallel proof coverage;
- default shared-config safety;
- all interleavings;
- direct ES proof parallelism;
- runtime identity/Vault proof parallelism;
- cancel, failure, destructive, recovery, restart, or support-bundle
  parallelism;
- IM live-refresh or support-bundle concurrency;
- CP semantic finalization from ES evidence;
- IM support-bundle authority;
- production readiness;
- high availability;
- multi-tenancy;
- public/demo readiness;
- independent audit;
- proof harness behavior as product architecture.

## Authority owners

Control Plane owns:

- workflow state and Temporal shell state;
- run-control updates;
- guarded operator semantics;
- review, checkpoint, escalation, and finalization;
- proof-harness summaries as evidence/projection only.

Execution Substrate owns:

- admission and submission handoff;
- provider/run identifiers below the ES boundary;
- lifecycle projection and outcome evidence;
- retained opaque result bundles;
- runtime handoff and identity-handoff evidence.

Infrastructure Manager owns:

- readiness/profile/provenance diagnostics;
- remote profile and support evidence;
- support-bundle packaging when separately authorized.

Support-bundle generation should snapshot completed evidence and should not run
concurrently with live proof writers unless separately proved.

## Sensitive/generated classes excluded

The proof must exclude raw generated and sensitive classes, including:

- raw `.out` contents;
- raw logs, traces, reports, profiles, and validation outputs;
- retained bundles and support bundles;
- archives and databases;
- environment files;
- key, certificate, token, secret, API key, bearer, TLS, SPIFFE, Vault,
  WebAuthn, passkey, JWT-SVID, and private-key material;
- raw prompts and raw model outputs;
- real run ids, provider ids, hashes, bundle refs, and local absolute paths.
