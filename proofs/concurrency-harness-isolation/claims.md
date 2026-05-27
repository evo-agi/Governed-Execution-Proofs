# Claims

Validation status: static example only. Proof 0 has not been run.

## Supported claims

This module may make these narrow static claims:

- Proof 0 has an authored scenario for concurrency and harness-isolation
  groundwork.
- Proof 0 identifies the harness-owned resources that must be unique before a
  later two-run validation.
- Control Plane harness isolation belongs to proof-run configuration and
  generated evidence surfaces, not product runtime authority.
- ES run-scoped staging, retained-result, provider-id, and runtime-handoff
  facts remain ES-owned evidence or runtime boundaries.
- IM evidence/support roots remain diagnostics/provenance and stay outside
  Proof 0 core.
- Static proof documentation keeps generated artifacts and validation outputs
  evidence-only.
- The later reported 0C result may be described only as Codex-reported bounded
  live evidence under the corrected generated-config/no-profile invocation
  shape, not as independent inspection or general concurrency support.

## Explicit non-claims

This module must not claim:

- independently inspected Proof 0 pass;
- live Temporal behavior;
- supported-local behavior;
- Remote Alpha behavior beyond the bounded Codex-reported 0C path;
- Linux-host behavior;
- Docker, Nomad, Vault, SPIRE, or fake-model service behavior;
- ES runtime success;
- provider success;
- general concurrency support;
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
