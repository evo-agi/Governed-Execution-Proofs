# Evidence Map

## Authority boundaries

Primary static anchors:

- `Control Plane: .docs/invariants.md:18-60`
- `Control Plane: .docs/invariants.md:110-160`
- `Control Plane: .docs/execution-substrate-integration.md:19-42`
- `Control Plane: .docs/supported-local-operator-runbook.md:7-19`
- `Control Plane: .docs/supported-local-operator-runbook.md:64-102`
- `Execution Substrate: .docs/execution_lifecycle/contracts.md:92-140`
- `Execution Substrate: .docs/system_overview/boundaries.md:82-120`
- `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:699-760`
- `Governed Execution Proofs: .docs/proof-module-conventions.md:40-76`
- `Governed Execution Proofs: .docs/parallel-proof-execution-policy.md`
- `Governed Execution Proofs: .docs/proof0-concurrency-2026-05-27.md`

## Harness-isolation anchors

Control Plane manual-smoke and validation-driver anchors:

- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:35-61`
  supports generated validation-plan and summary redaction classification labels
  only.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:360-445`
  supports the static derivation of harness-owned run roots, SQLite DB path,
  Temporal queues, Temporal DB path, report paths, provider URL recording, and
  plan-only excluded live actions.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:449-487`
  supports only that plan-only CLI mode exits after writing the plan and before
  the validation ladder.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:560-578`
  supports only that runtime-config overrides are derived from the plan.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:722-749`
  supports only that the generated runtime config path is passed to live
  invocation when present and that profile-derived environment overrides are
  carried separately.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:786-830`
  supports only that the nested smoke command receives a profile argument only
  when the resolved live config path is the source config path, and that
  subprocess env placeholders can receive profile-derived environment values.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:1035-1077`
  supports only that validation summaries label the current run as not
  contact-free and keep the harness plan embedded as evidence/projection.
- `Control Plane: tests/manual_smoke/supported_local_validation_driver.py:1377-1395`
  supports only the deterministic profile-forwarding rule for generated runtime
  configs and the subprocess environment merge.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:40-47`
  supports generated runtime-config redaction classification labels only.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:232-254`
  supports only that generated-runtime-config plus profile ambiguity and
  profile Temporal override overlap are blocked before connectivity probes.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:307-320`
  supports only that profile and harness overrides trigger generation of a
  proof-local runtime config.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:645-699`
  supports only the fail-fast ambiguity fields: generated runtime config with
  profile, and profile Temporal values overlapping Temporal harness overrides.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:1185-1247`
  supports only the generated runtime-config output-root acknowledgement and raw
  YAML overlay behavior.
- `Control Plane: tests/manual_smoke/supported_local_client_profile.py:1275-1304`
  supports only the runtime-config raw override fields written to disk.
- `Control Plane: tests/test_supported_local_validation_driver.py:705-981`
  supports only no-network unit coverage for disjoint plan derivation,
  plan-only no-contact behavior, live-config propagation, profile non-reapply
  behavior, subprocess env propagation, fail-fast ambiguity guards, and
  generated runtime-config contents.

0B and 0C Codex-reported evidence interpretation:

- The Proof 0 2026-05-27 ledger is treated as Codex-reported bounded evidence
  only. It supports an audit conclusion that 0B plan-only A/B lease records
  were reported passed and that the corrected generated-config/no-profile 0C
  A/B shape was reported passed.
- The initial failed A/B shape is treated as evidence of CP harness
  config/profile ambiguity, not as a product runtime failure.
- No raw generated artifacts, profiles, logs, traces, run ids, provider ids,
  local absolute paths, or sensitive payloads are imported into this module.
- The report does not support independent inspection, general concurrency
  support, Remote Alpha behavior beyond the bounded report, or production
  readiness.

Existing deterministic source anchors for later review, not Proof 0 pass
evidence:

- `Control Plane: tests/test_monitoring_interventions.py:463-940` supports only
  later review of existing guarded intervention write-coordinate tests.
- `Control Plane: tests/test_temporal_shell.py:2067-2900` supports only later
  review of existing Temporal shell deterministic workflow-state tests.

ES static run-scoping anchors for later review:

- `Execution Substrate: es/admission/executionlocator.go:20-60`
- `Execution Substrate: es/admission/executionpackage.go:73-140`
- `Execution Substrate: es/admission/results.go:193-240`
- `Execution Substrate: es/admission/runtimeidentity.go:23-80`

## Evidence quality notes

The source anchors above support static planning and source-level inspection.
The Proof 0 ledger records bounded Codex-reported 0B and 0C status, not
independent inspection. The static example summary remains `not_run`.

Generated harness plans, summaries, reports, traces, profile copies, retained
bundles, support bundles, and validation outputs are evidence/projection or
diagnostics only. They must not become CP workflow authority, ES runtime
authority, or IM provisioning authority.

## Claims not supported

This evidence map does not support live Temporal behavior beyond the bounded
Codex-reported 0C path, supported-local behavior beyond that path, Remote Alpha
behavior beyond that path, Linux-host behavior, Docker, Nomad, Vault, SPIRE,
fake-model service behavior, production readiness, high availability,
multi-tenancy, public/demo readiness, independent audit, or unbounded parallel
proof coverage.
