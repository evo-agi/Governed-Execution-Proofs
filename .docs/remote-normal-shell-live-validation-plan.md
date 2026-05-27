# Remote Normal-Shell Live Validation Plan

## Status

Status: plan only.

This document records a read-only Linux-box / Remote Alpha validation plan for a
future run. The remote normal-shell live proof remains not run. While creating
this plan, no Linux-host, Remote Alpha, supported-local, Docker, Nomad, Vault,
SPIRE, Temporal server, bringup, setup, proof, or validation commands were run.

Any future live run requires explicit operator authorization.

Historical/as-of note: this plan predates the bounded Phase A live ledger in
`.docs/live-validation-phase-a-2026-05-27.md`. Treat this file as the planning
baseline; current proof evidence status is carried by the later ledger and the
module validation-plan records, not by this plan-only status line.

## Scope

This plan covers the next validation phase for
`proofs/remote-normal-shell-live-proof-roadmap/`. It identifies later command
candidates, expected evidence, non-claims, mutation risk, audit gates, and stop
conditions. It does not authorize running those commands.

## Current proof portfolio state

- Static proof portfolio baseline:
  `9c23f9f0a4cab6e4e03aa27c32997373ac1878b6`.
- Deterministic validation ledger baseline:
  `53ec95be677b742729cdf55328dcaff85d45cf9c`.
- `.docs/deterministic-validation-2026-05-27.md:35-101` records
  Codex-reported deterministic validation for the stale-action, ES-envelope,
  and IM-support-packet modules only.
- `.docs/deterministic-validation-2026-05-27.md:103-108` records that the
  remote normal-shell live roadmap was not run.

## Branch/upstream provenance note

At plan creation, `trunk_dev` in this repo was clean. Local `HEAD`,
`origin/trunk_dev`, and the read-only `git ls-remote origin
refs/heads/trunk_dev` query all resolved to
`53ec95be677b742729cdf55328dcaff85d45cf9c`. The local upstream was
`origin/trunk_dev`, and the local left/right count for `@{u}...HEAD` was
behind `0`, ahead `0`.

The requested `git show-ref --heads --remotes | sort | sed -n '1,120p'`
command form was not supported by the local Git version. An equivalent local
refs listing was inspected with heads and remotes, showing `trunk_dev` and
`origin/trunk_dev` at the deterministic validation ledger commit.

No fetch or push was performed.

## Authority boundaries

- Execution Substrate owns admission, submission handoff, runtime-profile
  compatibility, Nomad/Docker-backed lifecycle projection, retained opaque
  result bundles, and runtime identity/workload-credential handoff boundaries.
- Control Plane owns workflow/run-control state, review/audit/policy gates,
  checkpoints, quarantine/restore, escalation, human intervention semantics,
  Temporal shell state, operator-facing control semantics, and finalization.
- Infrastructure Manager owns bootstrap, readiness, profile, provenance,
  diagnostics, and support evidence only.
- UI, report, channel, browser, CLI, dashboard, and notification surfaces are
  presentation, notification, or guarded action-adapter surfaces only.
- Generated artifacts, logs, reports, traces, support bundles, retained
  bundles, profiles, `.out`, local proof outputs, and validation outputs remain
  evidence/projection/diagnostics only.
- Remote Alpha is bounded/pre-live and is not production, HA, multi-tenant,
  provisioning, reconciler, or general deployment architecture.

Sources: `Execution Substrate: .docs/mvp.md:40-101`,
`Execution Substrate: .docs/system_overview/boundaries.md:82-109`,
`Control Plane: .docs/invariants.md:12-15`,
`Control Plane: .docs/long-running-operator-mode-contract.md:53-130`,
`Infrastructure Manager: .docs/architecture.md:5-26`,
`.docs/proof-module-conventions.md:40-60`.

## Modules covered

- `proofs/remote-normal-shell-live-proof-roadmap/`: covered as the future live
  Linux/Remote Alpha validation target.
- `proofs/es-envelope-is-not-cp-finalization/`: may receive supporting live ES
  lifecycle/result evidence if a future live run reaches status/result capture,
  but ES evidence still does not become CP finalization.
- `proofs/im-support-packet-is-evidence-not-authority/`: may receive supporting
  live support-bundle evidence if a future support bundle is generated and
  audited, but the bundle remains diagnostics/provenance only.

## Modules not requiring Linux validation

- `proofs/workflow-authority-rejects-stale-action-intent/` is already supported
  only by Codex-reported deterministic CP guard validation. Linux validation is
  not needed for that current claim.
- `proofs/es-envelope-is-not-cp-finalization/` does not need Linux validation to
  preserve the static/deterministic boundary claim that ES envelopes are not CP
  finalization.
- `proofs/im-support-packet-is-evidence-not-authority/` does not need Linux
  validation to preserve the static/deterministic claim that IM support packets
  are not authority.

## Linux/Remote Alpha prerequisites

- Expected profile lineage: a `control-plane.remote-supported-host-profile.v1`
  source profile, a derived `control-plane.supported-local-client-profile.v1`
  proof compatibility profile when needed, and
  `control-plane.remote-proof-profile-lineage.v1` provenance carrying source
  profile digest, derived profile digest, direct HTTPS/mTLS posture, runtime
  profile carry-through, and Mac-local Temporal fact.
- Expected CP local services: Mac-local Control Plane API/UI/worker context,
  Mac-local Temporal target, and any proof-only fake model/provider surface
  required by the selected validation mode.
- Expected ES/AGS/ARS/EGS endpoints: direct HTTPS/mTLS AGS and ES endpoints,
  with ES `GET /v1/executions:contract`, `POST /v1/executions:prepare`,
  `POST /v1/executions:submit`, status, logs, result, and cancel surfaces.
- Expected HTTPS/mTLS requirements: direct DNS/SAN posture, HTTPS URLs,
  `auth.mode = "mtls"`, readable Mac-side CA bundle/client certificate/client
  key paths, certificate metadata, endpoint host SAN alignment, and no bridge
  acceptance for Alpha.
- Expected runtime-profile compatibility: `control-plane-normal-shell/v1`
  enabled in the ES producer declaration with mandatory outcome-evidence
  carriers and non-authority classifications.
- Expected Nomad/Docker availability: remote Linux substrate has the ES-owned
  runtime prerequisites needed for submit-ready execution; this plan does not
  inspect or prove those prerequisites.
- Expected SPIRE/Vault/runtime identity prerequisites:
  `EXEC_WORKLOAD_IDENTITY_ENDPOINT` remains workload-visible discovery only;
  SPIRE owns JWT-SVID issuance; Vault owns token, secret, and lease issuance
  after workload-side login; ES does not broker credentials.
- Expected retained-result materialization path: ES returns an opaque retained
  result bundle from `GET /v1/executions/{run_id}/result`; CP materializes,
  reviews, and finalizes semantically.
- Expected CP review/finalization path: CP Temporal workflow/query state remains
  authoritative for terminal run-control and finalization, with ES facts only as
  evidence.
- Expected IM readiness/profile/support prerequisites: remote profile
  diagnostic, remote doctor, readiness report, live refresh when authorized, and
  support-bundle/redaction/digest packaging as diagnostics/provenance only.

Sources: `Control Plane: .docs/remote-supported-host-profile.md:21-54`,
`Control Plane: .docs/remote-supported-host-profile.md:95-151`,
`Control Plane: .docs/architecture.md:150-171`,
`Execution Substrate: .docs/execution_lifecycle/contracts.md:115-121`,
`Execution Substrate: .docs/system_overview/runtime_identity_handoff.md:27-127`,
`Infrastructure Manager: .docs/remote-supported-host-alpha.md:105-193`.

## Command inventory, not run

Every candidate below is future-facing and requires explicit operator
authorization before use.

| Candidate command or family | Source | Phase | Linux host contact | Local mutation | Remote mutation | Generated evidence | Prerequisites | Claim supported | Claims not supported | Risk | Authorization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `GET /v1/executions:contract` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:115`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:279-287`; `Control Plane: .docs/execution-substrate-integration.md:7-18` | preflight/readiness; ES contract | Contacts remote ES over HTTPS/mTLS in Remote Alpha | No, unless caller writes summaries | No | Optional summaries/reports only | Direct HTTPS/mTLS, caller identity, ES reachable | Producer compatibility and required runtime profile | Health, submit readiness, run existence, credential truth, scheduler API | medium | required |
| `GET /health` | `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:181-189`; `Infrastructure Manager: .docs/remote-supported-host-alpha.md:142-146` | preflight/readiness | Contacts remote ES/AGS if pointed at Remote Alpha | No, unless summarized | No | Optional readiness summary | Direct HTTPS/mTLS endpoint | Service reachability only | Producer compatibility, submit readiness, live proof | medium | required |
| `POST /v1/artifacts:publish` | `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:191-207`; `Control Plane: .docs/execution-substrate-integration.md:7-24` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote AGS | Possible local summaries | Yes, publishes artifact record | Publish response digest summary | Contract gate passed, package built, AGS reachable | Artifact publication digest evidence | Execution, retained result, CP finalization | high | required |
| `POST /v1/executions:prepare` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:116`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:294-300`; `Control Plane: .docs/execution-substrate-integration.md:24` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES | Possible local summaries | No run object or scheduler handoff by contract | Prepare result summary | AGS publish result, runtime profile annotation, mTLS | Artifact-specific admission/preflight | Submit, execution, retained result, CP finalization | high | required |
| `POST /v1/executions:submit` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:117`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:300-301` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES and hands off to provider | Possible local summaries | Yes, starts/submits execution | Submit receipt, provider run id, authority handoff | Contract, publish, prepare, submit-ready environment | ES submission handoff | CP semantic success, production, credential success | high | required |
| `GET /v1/executions/{run_id}/status` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:118`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:204,209-238` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES | Possible local summaries | No | Status/lifecycle projection summary | Submitted run id | Nomad-backed lifecycle projection evidence | CP write coordination, finalization, scheduler id truth | medium | required |
| `GET /v1/executions/{run_id}/logs` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:119`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:205,218-241` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES | Possible local summaries; raw logs excluded | No | Log metadata or redacted snippets only | Submitted run id, logs available | Bounded stdout retrieval metadata | Complete stdout/stderr truth, CP finalization, credential truth | medium | required |
| `GET /v1/executions/{run_id}/result` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:120`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:206,521-538`; `Control Plane: .docs/architecture.md:160` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES | May write local materialization/summary under CP run output | May cause or fetch retained bundle state from ES | Retained-result ref, digest, materialization summary | Terminal run, retained result available | ES opaque retained result evidence | CP semantic finalization by itself, retained-bundle finalization | high | required |
| `POST /v1/executions/{run_id}:cancel` | `Execution Substrate: .docs/execution_lifecycle/contracts.md:121`; `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:207,227-238`; `Control Plane: README.md:124-148` | ES contract/prepare/submit/status/log/result/cancel | Contacts remote ES | Possible local summaries | Yes, bounded provider cancel request | Cancel receipt/outcome evidence | Running submitted run and CP guarded action path | Bounded cancel request evidence | Terminal stop proof, CP rejection/finalization by itself | high | required |
| `scripts/01_bringup.sh check`; `VERIFY_RUNTIME_CONFIG=1 scripts/10_health_check.sh` | `Execution Substrate: .docs/supported_local_cp_consumer_runbook.md:290-293`; `Execution Substrate: .docs/mvp.md:198` | preflight/readiness | Not a Remote Alpha host-contact command unless run on/against that host | May generate readiness output | May inspect local substrate services if run in environment | Readiness output, logs, possible `.out` | Supported-local environment | Submit-ready environment on supported-local | Live Remote Alpha proof, CP finalization, production | high | required |
| `scripts/72_supported_local_setup.sh setup`; `scripts/73_supported_local_proof.sh run` | `Execution Substrate: PLANS.md:55`; `Execution Substrate: .docs/mvp.md:199` | preflight/readiness | No Remote Alpha contact by itself | Yes, setup/proof workspaces and `.out` | May mutate supported-local guest/services | Proof outputs and managed proof material | Supported-local prerequisites | Supported-local proof path | Remote Alpha proof, production, general deployment | high | required |
| `scripts/remote_alpha_runtime_security_boundary_check.sh` | `Execution Substrate: PLANS.md:1411-1412`; `Infrastructure Manager: .docs/commands.md:299-305` | runtime identity/Vault evidence | Host-local or remote-helper context depending operator route | May write summary | No intended mutation for check-only mode | `runtime-security-boundary-check.json` | Remote Alpha helper context | Runtime/security boundary evidence only | Service health, submit readiness, governed proof | high | required |
| `scripts/remote_alpha_stage_es_config_tls_prep.sh --output-dir .out/remote-alpha-m75q` and corresponding `--apply` | `Infrastructure Manager: .docs/remote-supported-host-alpha.md:538`; `Infrastructure Manager: .docs/commands.md:363` | IM Remote Alpha readiness/support bundle | Yes when staged through SSH/operator route | Yes, output summaries | `--apply` mutates remote config/TLS posture | Check-only/apply summaries, staging records | Operator-approved Remote Alpha helper route | Config/TLS hardening evidence | Governed execution proof, production, CP finalization | high | required |
| `scripts/remote_alpha_check_es_writable_state_readiness.sh` | `Infrastructure Manager: .docs/commands.md:365-370`; `Infrastructure Manager: .docs/commands.md:293-298` | IM Remote Alpha readiness/support bundle | Depends on operator route | Yes, summary output | No intended mutation for readiness check | `es-writable-state-readiness.json` | Remote Alpha host/helper prerequisites | ES writable-state readiness evidence only | Runtime proof, de-root approval, production | high | required |
| `scripts/remote_alpha_migrate_es_service_user.sh --output-dir .out/remote-alpha-m75q` | `Infrastructure Manager: .docs/remote-supported-host-alpha.md:545`; `Infrastructure Manager: .docs/commands.md:272-274` | IM Remote Alpha readiness/support bundle | Yes when operator route uses host | Yes, summary output | Apply mode may mutate service user posture | Migration check/apply summaries | Explicit migration decision | Service-user posture evidence | Governed proof, production, CP authority | high | required |
| `scripts/remote_alpha_migrate_vault_service_user.sh` | `Infrastructure Manager: .docs/remote-supported-host-alpha.md:548`; `Infrastructure Manager: .docs/commands.md:275-276` | runtime identity/Vault evidence | Yes when operator route uses host | Yes, summary output | Apply mode may mutate Vault service user posture | Vault migration check/apply summaries | Explicit Vault service-user decision | Vault service-user posture evidence | Vault production readiness, credential success, proof | high | required |
| `scripts/remote_alpha_vault_workload_auth_check.sh` or operator `vault-workload-auth-check` route | `Execution Substrate: PLANS.md:401-414`; `Execution Substrate: PLANS.md:1403` | runtime identity/Vault evidence | Yes | May write summary | No intended mutation for check route | Workload-auth summary | Fresh SPIRE/Vault/runtime identity posture | Bounded workload-side auth evidence | ES token brokerage, production Vault readiness | high | required |
| `diagnose-remote-profile <profile>` | `Control Plane: .docs/remote-supported-host-profile.md:95-151` | profile/lineage | No | May write JSON/Markdown report | No | Remote profile diagnostic | Source profile file | Profile acceptance diagnostics | Live TLS handshake, ES health, proof | low | required |
| `python ../execution_substrate_temporal_normal_shell_smoke.py ... --preflight-only` | `Control Plane: .docs/supported-local-operator-runbook.md:139-142`; `Infrastructure Manager: .docs/architecture.md:90-95` | preflight/readiness | Contacts configured endpoints, including Remote Alpha if profile points there | Yes, summaries under `.out` | No intended remote mutation | Preflight summary | Profile/config, endpoints, mTLS material | Bounded reachability/config preflight | Publish, prepare, submit, workflow, retained result | medium | required |
| `python ../execution_substrate_temporal_normal_shell_smoke.py ... --contract-probe-only` | `Control Plane: .docs/supported-local-operator-runbook.md:139-142`; `Control Plane: .docs/invariants.md:43` | ES contract/prepare/submit/status/log/result/cancel | Contacts AGS/ES | Yes, summaries under `.out` | Yes, publishes artifact and prepares | Contract-probe summary | Preflight passed, producer contract | Producer, AGS publish, ES prepare evidence | Submit, execution, retained result, Temporal history | high | required |
| `python ../fake_model_server.py --port 18081` | `Control Plane: .docs/supported-local-operator-runbook.md:64-69` | CP Temporal normal-shell proof | No | Starts local service and may log | No | Local process output if captured | Fixture project and compatible proof config | Controlled local model/provider input | ES runtime proof, Remote Alpha readiness | medium | required |
| `temporal server start-dev --db-filename .out/temporal/dev-server.db` | `Control Plane: README.md:150-161`; `Control Plane: .docs/architecture.md:171` | CP Temporal normal-shell proof | No | Yes, Temporal DB under `.out` | No | Temporal DB/logs | Temporal dev tooling, CP config | Local Temporal availability | Remote ES proof, production Temporal | high | required |
| `run-temporal-shell-worker --config config.yaml` | `Control Plane: README.md:158-170`; `Control Plane: .docs/architecture.md:171` | CP Temporal normal-shell proof | Indirectly when workflow uses Remote Alpha profile | Yes, worker process and run outputs | Indirectly via proof activities | `.out` run summaries, manifests, reports | Temporal server, config, queues | CP worker availability | Proof success by itself, production | high | required |
| `python ../supported_local_validation_driver.py --mode temporal-basic --config <remote-proof-config> --project-root . --supported-local-profile <derived-profile>` | `Control Plane: .docs/supported-local-operator-runbook.md:78-119`; `Control Plane: README.md:198-201` | CP Temporal normal-shell proof | Yes when profile points at Remote Alpha | Yes, `.out/<run_id>` summaries and artifacts | Yes, publish/prepare/submit through ES | Validation summary, attempt manifests, retained refs | Profile lineage, CP services, ES/AGS readiness | One CP Temporal normal-shell proof mode | All proof modes, production, HA, multi-tenancy | high | required |
| `python ../supported_local_golden_path_capture.py ...` | `Control Plane: .docs/supported-local-operator-runbook.md:121-137` | post-run audit/support packaging | No new host contact if reading existing output | Yes, proof summaries under `.out` | No | Golden-path proof summary and snapshot | Prior validation summary | CP-owned interpretation over evidence | New live evidence, production certification | medium | required |
| `infra-manager remote-doctor [--input <json>] [--output <json>]` | `Infrastructure Manager: .docs/commands.md:93-115`; `Infrastructure Manager: .docs/remote-supported-host-alpha.md:83-103` | IM Remote Alpha readiness/support bundle | No | May write doctor report | No | Remote doctor JSON | Optional fixture/stage input | Doctor vocabulary/provenance | Live host liveness, proof, authority | low | required |
| `infra-manager remote-readiness-report --cp-diagnostic <json> --doctor <json>` | `Infrastructure Manager: .docs/commands.md:565-609` | IM Remote Alpha readiness/support bundle | No | May write readiness JSON/Markdown | No | Readiness report | CP diagnostic and IM doctor | Pre-live readiness posture | Workflow, ES submit, retained result | low | required |
| `infra-manager remote-alpha-live-refresh --profile-dir .out/remote-alpha-m75q --ssh-alias <alias> --cp-proof-run-dir <run-dir> --cp-post-service-user-smoke-run-dir <run-dir>` | `Infrastructure Manager: .docs/commands.md:117-145`; `Infrastructure Manager: .docs/remote-supported-host-alpha.md:105-193` | IM Remote Alpha readiness/support bundle | Yes, read-only SSH plus Mac-side HTTPS/mTLS probes | Yes, live evidence and reports under profile dir | No intended remote mutation | Live doctor input, doctor, readiness, copied evidence | Existing profile dir, SSH alias, optional CP proof refs | Live readiness/provenance evidence | ES prepare/submit, CP run-control authority, proof by itself | high | required |
| `infra-manager remote-alpha-live-support-bundle --profile-dir .out/remote-alpha-m75q --output-root .out/remote-alpha-m75q/support-bundles` | `Infrastructure Manager: .docs/commands.md:216-305`; `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:699-710` | post-run audit/support packaging | No | Yes, support bundle output | No | Bundle, manifest, redaction report, evidence index | Existing live-refresh/readiness artifacts | Digest/redaction support packaging | Runtime health proof, run-control authority | medium | required |
| `infra-manager remote-alpha-hardening-checkpoint --profile-dir .out/remote-alpha-m75q` | `Infrastructure Manager: .docs/commands.md:457-562` | post-run audit/support packaging | No | Yes, checkpoint JSON/Markdown if output used | No | Hardening checkpoint summary | Existing readiness/bundle artifacts | Digest-first hardening posture summary | Proof, host mutation, production | medium | required |
| `infra-manager remote-support-bundle ... --output-dir <dir>` | `Infrastructure Manager: .docs/commands.md:611-655`; `Infrastructure Manager: .docs/remote-supported-host-support-bundle.md:681-697` | post-run audit/support packaging | No | Yes, static support bundle | No | Bundle, redaction report, evidence index | Supplied JSON summaries | Static support packaging | Live collection, proof, host liveness | medium | required |
| `infra-manager up`; `infra-manager profile`; `infra-manager check`; `infra-manager down` | `Infrastructure Manager: .docs/commands.md:7-92`; `Infrastructure Manager: README.md:23-55` | preflight/readiness | No Remote Alpha contact by itself | Yes, supported-local instance state and `.out` | May affect supported-local guest/services | Profiles, checks, instance state | Supported-local prerequisites | Supported-local environment/profile/check only | Remote Alpha live proof, production | high | required |

## Artifact and evidence classification

| Artifact class | Owner/surface | Classification | Public-safe | Redaction/raw-content rule | Digest/metadata acceptable |
| --- | --- | --- | --- | --- | --- |
| Machine-readable proof summary | CP/proof repo | Evidence summary | Only after audit | Exclude raw payloads | Yes |
| Human-readable operator narrative | CP/proof repo | Evidence narrative | Only after audit | Exclude raw logs/results/secrets | Yes |
| Retained result refs or summaries | ES evidence consumed by CP | Opaque ES retained evidence | Summary only | Exclude raw bundle | Yes |
| ES lifecycle/status/result evidence | ES | Evidence/projection | Summary only | Exclude raw logs/result bundles | Yes |
| CP Temporal/workflow/finalization evidence | CP | CP run-control/finalization authority for the run | Summary only | Exclude raw prompts, model outputs, DBs, workspaces | Yes |
| IM readiness/profile/support/redaction/digest evidence | IM | Diagnostics/provenance | Summary only | Exclude raw credential-adjacent material | Yes |
| Logs/traces/reports | CP/ES generated outputs | Projection/evidence | No raw publication | Redacted snippets only | Yes |
| `.out` paths and local proof outputs | CP/ES/IM generated outputs | Evidence/projection/diagnostics | No raw publication | Path names should be minimized or pseudonymized | Yes |
| Support bundles | IM assembly | Diagnostics/provenance | Only after deny scan | Raw bundle contents excluded from proof docs | Manifest/digest only |
| Generated profiles | CP/IM profile/provenance | Configuration/provenance | Summary only | Do not copy auth material, key paths, or raw cert/key bodies | Yes |
| Credential-adjacent material | SPIRE/Vault/TLS/WebAuthn/passkey/API-key surfaces | Sensitive/excluded | No | Raw contents excluded | Presence/freshness/redaction status only |

## Sensitive and excluded artifact plan

Do not copy or quote raw `.out`, logs, traces, reports, retained bundles,
support bundles, archives, databases, environment files, key material,
certificate bodies, TLS material, SPIFFE material, Vault material, WebAuthn
material, passkeys, API keys, bearer material, tokens, secrets, raw prompts,
raw model outputs, workspaces, checkpoints, quarantines, restores, or local
process records. Mention those classes only as exclusions, non-claims, or
redaction requirements.

## Audit gates

- Before live run: inspect docs, scripts, configs, and source-level command
  references for drift; verify clean branches, explicit authorization, profile
  lineage, direct HTTPS/mTLS posture, runtime profile, Mac-local Temporal, no
  shared filesystem, and non-authority labels.
- Immediately after live run: inspect only redacted summaries, manifests,
  digests, and stage summaries; verify producer gate, publish, prepare, submit,
  status/result, retained-result fetch, and CP finalization are separated.
- After support-bundle generation: inspect bundle manifest, local-only evidence
  index, redaction report, deny-scan outcome, digest inventory, and overclaim
  labels.
- Before public/demo writing: classify every statement as theory, static docs,
  Codex-reported deterministic validation, live validation output,
  independently inspected evidence, or inference.
- Before any push or publication: verify no generated/sensitive artifacts are
  tracked, docs match evidence, non-claims remain explicit, and the worktree is
  clean except intentional docs.

## Recommended live validation sequence

| Step | Candidate commands | Stop condition | Expected artifacts | Claim supported | Explicit non-claim | Audit note |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Pre-live branch/status/config check | `git status --short --branch`; `git rev-parse HEAD`; config/profile inspection | Dirty repo, wrong branch, unexpected HEAD, missing authorization | None or local operator notes | Clean baseline only | No runtime readiness | Record branch/upstream provenance without fetch unless separately authorized |
| 2. Remote profile/readiness verification | `diagnose-remote-profile <profile>`; `infra-manager remote-doctor`; `infra-manager remote-readiness-report`; later `infra-manager remote-alpha-live-refresh ...` | Profile blocked, not direct HTTPS/mTLS, bridge-only, stale/missing Vault/SPIRE evidence, unreadable auth material | Profile diagnostic, doctor, readiness report, lineage summary | Pre-live compatibility/readiness evidence | No governed execution, no ES submit, no CP finalization | Inspect summaries only; do not copy raw credential material |
| 3. ES contract/preflight | `GET /health`; `GET /v1/executions:contract`; CP `--preflight-only`; CP `--contract-probe-only` | Contract missing/malformed/unauthorized, runtime profile disabled, publish/prepare blocker | Health summary, producer declaration summary, preflight/contract-probe summary | ES compatibility and prepare gate | No execution, no retained result, no Temporal proof | Keep `/health`, contract, publish, and prepare claims separate |
| 4. CP Temporal normal-shell proof invocation | `python ../fake_model_server.py --port 18081`; `temporal server start-dev --db-filename .out/temporal/dev-server.db`; `run-temporal-shell-worker --config config.yaml`; `python ../supported_local_validation_driver.py --mode temporal-basic ...` | Worker/Temporal unavailable, stage blocker, missing provider run id, missing terminal CP outcome | CP validation summary, attempt manifests, Temporal summary, provider refs | One bounded CP Temporal normal-shell proof mode | Not all modes, not production, not default remote runtime | Do not inspect raw prompts/model outputs/workspaces |
| 5. ES status/result/retained-output evidence capture | `GET /v1/executions/{run_id}/status`; `GET /v1/executions/{run_id}/logs`; `GET /v1/executions/{run_id}/result` through CP adapter path | Missing outcome evidence, no retained result when success requires one, malformed result headers | ES lifecycle summary, log metadata, retained-result ref/digest | ES lifecycle/result evidence | ES evidence is not CP finalization | Prefer digest/metadata; exclude raw bundles/logs |
| 6. CP review/finalization evidence capture | CP validation summary and optional golden-path capture | Finalization inferred from ES output, missing `ExecutionFlowSnapshot v1`, missing CP review outcome | CP finalization summary, proof summary, snapshot summary | CP-owned review/finalization evidence | Retained bundle alone is not finalization | Verify CP owns terminal semantics |
| 7. IM support/redaction/digest packaging | `infra-manager remote-alpha-live-refresh ...`; `infra-manager remote-alpha-live-support-bundle ...`; optional `infra-manager remote-alpha-hardening-checkpoint ...` | Secret hit, deny-scan failure, stale evidence, digest mismatch, overclaim | Doctor/readiness refresh, support bundle, redaction report, digest index | IM diagnostics/provenance/support evidence | Support bundle authority, production readiness | Inspect manifest/redaction/digests before using |
| 8. Post-run audit | Review summaries, manifests, redaction reports, non-claim mapping | Any raw sensitive payload needed for a public claim, authority drift, unclassified artifact | Audit notes and claim map | Evidence quality and claim hygiene | Independent audit unless separately performed | Separate live output from inference |
| 9. Proof-doc update | Update proof docs after audit | Evidence not audited, claims would widen, generated data would need import | Authored documentation only | Recorded validation provenance | Raw generated output in repo | Keep repo-relative references and non-claims |

## Stop conditions for live validation

Stop and report if:

- any repo is dirty before the live run;
- authorization is missing or ambiguous;
- profile lineage is missing or digest-incompatible;
- the profile is bridge-only, shared-filesystem-based, or not direct
  HTTPS/mTLS Alpha acceptance;
- ES producer contract is missing, malformed, disabled, unauthorized, or lacks
  `control-plane-normal-shell/v1`;
- publish, prepare, submit, status, logs, result, or cancel facts are being
  treated as CP write coordination or finalization authority;
- IM readiness, profile, support, or doctor output is being treated as CP
  run-control or ES runtime authority;
- runtime identity evidence implies ES token brokerage;
- Vault/SPIRE/runtime identity evidence is stale, sealed, missing, failed, or
  unverifiable;
- generated artifacts contain raw sensitive payloads;
- validation cannot distinguish preflight, prepare, submit, execution,
  retained-result fetch, and CP finalization.

## Public-writing implications

A future successful live run may support a bounded statement that one
authorized Remote Alpha profile/run exercised the CP Temporal normal-shell path
against remote ES/AGS over direct HTTPS/mTLS, produced ES lifecycle/result
evidence, materialized a retained result through CP, and recorded CP-owned
review/finalization evidence plus IM diagnostic/support evidence.

Public writing must distinguish theory, static proof docs, Codex-reported
deterministic validation, live validation output, independently inspected
evidence, and inference.

## Explicit non-claims

This plan does not prove production readiness, HA, multi-tenancy,
provider-side success, credential success, token brokerage, retained-bundle
finalization, support-bundle authority, or general deployment architecture.

The future live proof, even if authorized and completed, must not be described
as production, HA, multi-tenant, provisioning, reconciler, general deployment
architecture, independent audit, browser/WebAuthn validation, all CP proof
modes, full Nomad/Docker/Vault/SPIRE validation, or default remote runtime
unless those separate claims are explicitly run, audited, and recorded.

## Push/release considerations

Do not push as part of this planning step. At plan creation, local tracking
metadata and the read-only remote branch query indicated `trunk_dev` and
`origin/trunk_dev` at the deterministic validation ledger commit with no local
ahead/behind. The new docs should be audited before any later stage, commit,
push, release, public demo, or article claim.

## Follow-up after live validation

After an authorized live run, update proof documentation only after post-run
audit. The update should record command provenance, exact scope, generated
artifact classes, redaction review, digest/metadata references, claims
supported, claims not supported, and any blocked or failed stage. It must not
copy raw generated payloads into this repo.
