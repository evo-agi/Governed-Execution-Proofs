# Parallel Proof Execution Policy

## Purpose

Proof 0 defines a generic policy for parallel proof execution and harness
isolation. It is a proof-execution isolation policy and evidence package, not
product architecture.

The policy keeps proof-run coordination separate from authority boundaries:
Control Plane remains workflow and run-control authority, Execution Substrate
remains admission, runtime, lifecycle, and result authority inside its
boundary, and Infrastructure Manager remains readiness, provenance,
diagnostics, and support-evidence owner. Generated artifacts remain
evidence/projection/diagnostics only.

## Scope

This policy applies to future proof-track planning, subagent use, proof-package
updates, and authorized live proof execution. It does not grant general
parallelism for every proof class.

Remote Alpha remains bounded and pre-live. Proof parallelism is not product HA,
multi-tenancy, scale, or production readiness. It is also not a remote
provisioning, reconciler, production deployment, or public/demo readiness
claim.

## Proof Isolation Lease

A proof isolation lease is the parent coordinator's explicit allocation of
resources to one live proof writer or one deliberately paired proof run. It is
evidence/projection for the proof harness only. It does not become CP, ES, or
IM authority.

The lease must be allocated before live execution starts, must name exclusive
resources, and must identify raw-excluded roots and non-claims. If two leases
would share an isolation-critical field, the live proof must stop or be
reclassified as a deliberate Proof 0 continuation.

## Confirmed Parallel Proof Class

Proof 0 0C confirmed only the Control Plane to Execution Substrate
`temporal-basic` class under the hardened generated-config/no-profile
invocation:

- two Codex-reported overlapping live Remote Alpha `temporal-basic` runs;
- generated runtime config passed as the live `--config`;
- no supported-local profile re-forwarded to the nested live smoke;
- distinct CP run ids, output roots, Temporal settings, fake-model/provider
  URLs, ES provider ids, retained refs, finalization refs, and materialization
  refs;
- generated summaries and manifests treated as proof-local redaction-needed
  evidence/projection/diagnostics.

This confirmed class does not cover other live proof shapes, shared-config
defaults, all interleavings, or product concurrency.

## Unconfirmed Proof Classes

These proof classes are not automatically covered by Proof 0:

- direct ES proofs;
- runtime identity and Vault proofs;
- cancel, failure, hold, resume, reject, and other intervention proofs;
- IM support-bundle proofs;
- IM live-refresh proofs;
- destructive, recovery, restart, or failover proofs;
- compare, experiment, wrapper, or child-run proof classes beyond the specific
  confirmed `temporal-basic` shape;
- any proof that shares Temporal services, provider endpoints, output roots,
  databases, profiles, support-bundle roots, or retained-result roots without a
  fresh lease review.

## Live-Proof Subagent Policy

Live proof subagents may run in parallel only when the parent allocates explicit
isolation leases and the proof class has either been confirmed by Proof 0 or is
being deliberately tested as a Proof 0 continuation.

For an already confirmed class, the parent may assign one lease per live proof
writer and require each subagent to stay inside its lease. For an unconfirmed
class, the parent must label the run as a new Proof 0 continuation before any
parallel live execution begins. Any lease collision, unallocated shared
resource, profile/config ambiguity, redaction gap, or authority-boundary drift
is a stop condition.

## Static/Audit Subagent Policy

Subagents may be used freely for read-only planning, source inspection, docs,
proof-package updates, and post-run audits. Static and audit subagents may work
in parallel because they do not write live proof artifacts, contact hosts, start
services, or compete for runtime resources.

Static/audit subagents must still preserve authority boundaries, avoid
importing generated payloads into authored docs, and keep generated artifacts
classified as evidence/projection/diagnostics only.

## Resource Lease Fields

Each proof isolation lease should record these fields:

- `proof_id`;
- `proof_class`;
- `run_id_prefix`;
- `project_root`;
- `output_root`;
- `execution_run_root`;
- `runtime_config_root`;
- `report_root` or derived report rule;
- `sqlite_db`;
- Temporal target;
- Temporal UI port;
- Temporal namespace;
- workflow task queue;
- workspace task queue;
- Temporal DB path;
- fake model/provider base URL;
- remote profile path or profile lineage ref;
- evidence root;
- support bundle output root, if applicable;
- raw-excluded roots;
- redaction-required flag;
- exclusive resources;
- expected artifact classes;
- non-claims.

## Artifact And Redaction Rules

Generated configs, generated plans, summaries, reports, traces, logs, retained
bundles, support bundles, profiles, proof outputs, and validation outputs are
evidence/projection/diagnostics only. They are redaction-required unless a
separate review narrows their publication class.

Authored proof docs may reference generated artifact classes and proof-local
path classes, but they must not copy or quote raw generated artifacts, raw logs,
raw traces, retained bundles or payloads, raw prompts, raw model outputs,
workspace contents, databases, local process records, credentials, key
material, TLS, SPIFFE, Vault, WebAuthn, passkey, bearer, token, secret, or API
key material.

Raw artifacts are excluded from this repo. Validation output does not become
runtime authority.

## Support-Bundle Rules

Support-bundle generation should not run concurrently with live proof writers
unless that concurrency class is separately proved. A support bundle should
snapshot completed evidence after live writers have stopped.

IM owns support-bundle packaging and support evidence. A support bundle is
diagnostics/provenance evidence only; it does not become CP run-control
authority, ES runtime authority, semantic finalization, or independent audit.

## Failure Classification

Classify failures by the earliest truthful boundary:

- `lease_collision`: two proof writers share an isolation-critical resource;
- `unsupported_parallel_class`: parallelism was attempted outside a confirmed
  or deliberately tested class;
- `profile_config_ambiguity`: generated runtime config and profile use are
  ambiguous or conflicting;
- `external_prerequisite_blocked`: a required external service or endpoint is
  unavailable before the proof's runtime claim begins;
- `proof_assertion_failed`: the live proof ran but its evidence contract did
  not pass;
- `artifact_redaction_blocked`: generated or raw artifacts cannot be safely
  summarized without redaction;
- `support_bundle_overlap`: support-bundle generation overlaps live proof
  writers without a proved lease class;
- `authority_boundary_drift`: generated artifacts, ES evidence, or IM
  diagnostics are being treated as CP/ES/IM authority outside their boundary.

## Claims Supported By Proof 0

Proof 0 supports these bounded claims:

- a proof isolation lease is required for parallel live proof execution;
- static and audit subagents may operate in parallel when they stay read-only
  or within authored proof-package edits;
- 0B was Codex-reported as no-network, plan-only harness-isolation evidence;
- 0C was Codex-reported for the CP to ES `temporal-basic` class under the
  hardened generated-config/no-profile invocation;
- the initial config+profile failure is a harness hazard and not product
  architecture;
- generated artifacts remain proof-local redaction-needed
  evidence/projection/diagnostics;
- raw artifacts are excluded from authored proof docs.

## Claims Not Supported By Proof 0

Proof 0 does not support these claims:

- product HA, multi-tenancy, scale, production readiness, or public/demo
  readiness;
- general parallel execution for all proof classes;
- default shared-config safety;
- all possible interleavings;
- direct ES proof parallelism;
- runtime identity or Vault proof parallelism;
- cancel, failure, destructive, recovery, restart, or support-bundle
  parallelism;
- IM live-refresh or support-bundle concurrency;
- independent audit;
- CP semantic finalization from ES evidence;
- IM diagnostics as CP run-control or ES runtime authority.

## When To Request Proof 0 Continuation

Request a Proof 0 continuation when a future proof needs a new class of
parallelism, a new shared service shape, support-bundle overlap with live
writers, runtime identity/Vault overlap, cancel/failure/destructive/recovery
parallelism, IM live refresh, shared profile/config defaults, or any resource
lease field that cannot be made exclusive.

The continuation should state the new proof class, allocate explicit leases,
identify expected artifacts and raw exclusions, run only under explicit live
authorization when live execution is needed, and record supported claims and
non-claims separately.
