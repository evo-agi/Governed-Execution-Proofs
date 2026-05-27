# ES Envelope Is Not CP Finalization

## Scenario summary

This proof documents a bounded Execution Substrate execution envelope moving
through producer contract, prepare, submit, status/result, and retained-output
references without becoming Control Plane semantic review or finalization.

Execution Substrate labels each surface by what ES owns:

- producer contract is a compatibility declaration;
- prepare is preflight;
- submit is runtime handoff;
- lifecycle/status/result are runtime evidence or projection;
- retained bundles are opaque output artifacts;
- CP alone owns semantic review, checkpoint, intervention, and finalization.

This module is static proof-planning material. It is not live validation output,
not a generated proof artifact, and not product architecture.

## Operator story

A CP-owned governed task attempt points at an ES producer. Before work can move
through ES, the consumer reads the ES producer declaration, then performs
preflight, then submits the bounded execution envelope. ES may later serve
status, logs, cancel receipts, result headers, and retained result references.
Those surfaces help CP observe and materialize runtime evidence, but they do not
review the work, accept it, checkpoint it, or finalize the governed run.

## Envelope surfaces

### Producer contract

`GET /v1/executions:contract` is a read-only ES compatibility declaration. It
can say whether the current governed-execution producer contract and mandatory
outcome-evidence carriers are present. It is not service health, submit
readiness, artifact-specific admission proof, run authority, lifecycle truth,
credential truth, policy truth, scheduler API, or CP finalization.

Supporting anchors:

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:171-248`
- `Execution Substrate: es/admission/producercontract.go:23-50`
- `Control Plane: .docs/execution-substrate-integration.md:16-18`

### Prepare

`POST /v1/executions:prepare` is bounded preflight. It verifies the current ES
admission inputs for the requested artifact envelope and returns preflight
success only. It creates no `run_id`, scheduler handoff, proto-execution state,
durable ES execution record, workload-vault plan, signer detail, or workload
identity detail. It does not treat CP review, checkpoint, finalization,
task-attempt, or proof-harness metadata as shared admission facts.

Supporting anchors:

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:257-376`
- `Execution Substrate: es/admission/types.go:44-50`

### Submit

`POST /v1/executions:submit` is the bounded runtime handoff surface. A
successful receipt says ES revalidated admission, staged the current runtime
package, and handed a real execution to the scheduler through ES. The receipt is
not durable ES lifecycle ownership, not a sync execution result, not a retry or
reschedule policy, and not CP review, checkpoint, intervention, approval, or
finalization.

Supporting anchors:

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:386-475`
- `Execution Substrate: es/admission/types.go:52-62`

### Status and lifecycle projection

`GET /v1/executions/{run_id}/status` is a Nomad-backed lifecycle projection
served through ES. `lifecycle_projection.revision` is an opaque same-run
read-coordination token, not a scheduler id, global ES run revision, or write
precondition. `outcome_evidence` labels the observation ES just served; it does
not become CP workflow truth or finalization state.

Supporting anchors:

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:485-650`
- `Execution Substrate: es/admission/types.go:64-101`

### Result and retained output references

`GET /v1/executions/{run_id}/result` returns an ES-retained opaque terminal
output bundle when the bounded workload wrote files under the reserved result
directory. ES packages and serves the retained output envelope, but it does not
parse CP semantics, checkpoint decisions, review outcomes, or finalization
metadata from the files. CP may materialize, validate, review, and finalize
contents semantically above the ES boundary.

Supporting anchors:

- `Execution Substrate: .docs/execution_lifecycle/contracts.md:734-815`
- `Execution Substrate: es/admission/results_test.go:62-147`
- `Control Plane: .docs/architecture.md:160-161`
- `Control Plane: .docs/execution-substrate-integration.md:150-160`

## Authority boundary map

- ES authority: public admission, producer compatibility declaration, preflight,
  bounded submit handoff, Nomad-backed lifecycle projection, outcome-evidence
  labels, non-secret runtime handoff evidence, and opaque retained-output
  envelope ownership.
- CP authority: orchestration, Temporal workflow state, task progression,
  review, checkpoints, quarantine/restore, escalation, intervention semantics,
  semantic result materialization, and finalization.
- Evidence/projection only: ES `lifecycle_projection`, `outcome_evidence`,
  logs/result/cancel evidence, retained bundle references, `authority_handoff`,
  generated proof summaries, reports, traces, support bundles, retained bundles,
  and `.out` classes.

Supporting anchors:

- `Execution Substrate: .docs/mvp.md:44-60`
- `Execution Substrate: .docs/mvp.md:120-145`
- `Execution Substrate: .docs/system_overview/boundaries.md:415-559`
- `Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:80-94`
- `Control Plane: .docs/architecture.md:192-204`

## Explicit exclusions

This proof does not include or inspect:

- raw `.out` contents;
- raw logs, traces, or reports;
- retained bundle payloads or support bundle payloads;
- archives or generated artifact payloads;
- databases;
- environment files;
- key, certificate, token, API key, or bearer material;
- TLS, SPIFFE, Vault, WebAuthn, passkey, JWT-SVID, or private-key material;
- raw prompts or raw model outputs;
- raw Codex stdout, stderr, final, meta, review, or audit payloads;
- workspaces, checkpoints, quarantines, restores, or local process records;
- real run ids, provider ids, hashes, bundle references, or local absolute
  paths.

## Validation status

Current status: `not_run`.

No tests, scripts, servers, bringup commands, proof commands, validation
commands, supported-local commands, Docker, Nomad, Vault, SPIRE, Temporal, or
remote-alpha commands were run to create this module. The module is static
narrative and example material only.
