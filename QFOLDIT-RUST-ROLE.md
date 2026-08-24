# qFoldIT Rust Boundary

## Status

Canonical scientific capability boundary. `UEFN-QFOLDIT` / `qfoldit-core` owns mission, policy, provenance and orchestration semantics.

## Rule

This repository may own substantive protein-science capability, but it MUST NOT become a second qFoldIT runtime authority.

All qFoldIT integration MUST cross a versioned Rust contract carrying:

- mission identity;
- scientific object identity;
- capability identity/version;
- input/output hashes;
- engine/provider provenance;
- validation status.

Foreign implementation remains a bounded scientific execution provider. qFoldIT canonical state remains Rust-owned.

## Retirement condition

This repository may be absorbed only when its scientific capability has a verified replacement in the canonical Rust workspace without loss of provenance or scientific behavior.
