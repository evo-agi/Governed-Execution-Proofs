# Validation Plan

## Current evidence status

Current evidence status: Codex-reported two-pass lifecycle condition recorded.

The evidence is recorded in `.docs/governed-lifecycle-proof-2026-05-28.md` and
is reflected in the broader remote normal-shell roadmap validation plan. The
recorded lifecycle evidence is bounded to two serial `temporal-basic`
happy-path rehearsals and supports the governed execution lifecycle proof
status. It is not independent audit and is not public/demo readiness by itself.

## Static example summary status

`proof-summary.example.yaml` is a static template only. It remains
`validation_status: "not_run"` by convention and is not the proof evidence
status.

## Future validation gates

Future validation is not authorized by this module. Any future proof work needs
an explicit operator decision and a new evidence record.

Future gates may include:

- final demo-readiness audit;
- optional future support-bundle proof;
- optional future runtime identity/Vault proof;
- optional future cancel/failure/intervention proof.

## Do not run from this module

This module does not authorize:

- new live proof runs;
- CP, ES, or IM validation outside proof-repo checks;
- supported-local bringup;
- Remote Alpha commands;
- Temporal, Docker, Nomad, Vault, or SPIRE commands;
- support-bundle generation;
- runtime identity/Vault credential validation;
- cancel/failure/intervention validation.

## Allowed proof-repo checks

Allowed local proof-repo checks are limited to authored-doc linting, schema
tests, redaction scanning, and diff whitespace checks. Those checks do not
contact product systems, run live proof commands, or promote generated artifacts
into authority.

## Pass/fail interpretation

A proof-repo checker pass means the authored module follows local proof
conventions. It does not mean production readiness, independent audit,
public/demo readiness, live runtime truth, support-bundle authority, or retained
bundle semantic finalization by ES.

Future validation records must continue to separate:

- authored static examples;
- Codex-reported validation status;
- live proof output when explicitly authorized;
- independent inspection when separately performed;
- inference.
