# qFoldIT QSIS Integration Policy — Protein-MCP

**Snapshot:** 2026-11-11  
**Status:** Aggregate toolkit with legacy qFoldIT adapter; nested providers require individual qualification

## 1. Correct integration boundary

The inspected README inventories 38 MCP servers: 24 local and 14 community servers, plus workflow skills. The qFoldIT wrapper manifest remains adapter 0.2.0 under `qfoldit.scientific-adapter/1.0`; its current declared outputs include Action Envelope 1.0 and validation.completed 1.1.

Protein-MCP is therefore an **aggregate provider/tool catalog**, not one scientific operation and not a universal scientific validator.

Do not create one blanket `qfoldit.qsis.capability-manifest/0.1` for the full toolkit. Each actual scientific operation must have an independent capability identity and schema binding.

## 2. Required per-operation registry

For every nested MCP server or exposed operation, record:

- exact source repository, owner, immutable commit/release and implementation version;
- tool/function name and its input/output schemas;
- model/checkpoint revision and weight digest where applicable;
- input/output artifact format, media type, units and digest behavior;
- deployment mode, resource profile, network/data egress and data residency;
- source/model/data/container licences and any usage restrictions;
- capability authority role and specific scientific limitations;
- validator profile, if a downstream claim requires independent validation.

A composite skill such as binder design or GenMol → DiffDock → Boltz-2 is an orchestration package over multiple separately declared provider capabilities. The skill package cannot collapse those capabilities into one provider authority.

## 3. Scientific authority rules

- Sequence/structure prediction is a compute result, not experimental validation.
- Protein design proposes candidates; it does not prove expression, binding or efficacy.
- Docking scores and affinity predictions are not measured binding constants.
- Molecular dynamics completion is not proof of biological activity.
- Structure/pose diagnostics are limited to the exact profile and artifacts evaluated.
- No nested MCP or workflow skill may issue qFoldIT Evidence 1.2.

All consequential calls route through a mission-authorized qFoldIT adapter with Action Envelope 1.1 and QSIS Job Request/Result lineage. Independent validators and the Evidence 1.2 trust-plane publisher remain separate.

## 4. Migration sequence

1. Keep the legacy adapter manifest unchanged for historical compatibility.
2. Inventory the 38 nested MCPs and resolve ambiguous tool/model ownership.
3. Prioritize concrete qFoldIT mission operations, not the entire catalog at once.
4. Create one QSIS manifest and input/output schemas per selected operation.
5. Add offline tests, provider smoke, agent evaluation and claim-specific validator handoff.
6. Record each maturity level in the UAG-SOS migration register.

## 5. Canonical references

- [Scientific Agent Skill Package Standard](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/MCP/SCIENTIFIC-AGENT-SKILL-PACKAGE-STANDARD-v0.1.md)
- [Scientific MCP Provider Adapter Conformance Standard](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/MCP/SCIENTIFIC-MCP-PROVIDER-ADAPTER-CONFORMANCE-v0.1.md)
- [Legacy Action/Evidence Migration Plan](https://github.com/qfoldit/UAG-SOS/blob/main/STANDARDS/MCP/LEGACY-ACTION-EVIDENCE-MIGRATION-PLAN-2026-11-11.md)
- [Provider Adapter Migration Register](https://github.com/qfoldit/UAG-SOS/blob/main/SCHEMAS/QSIS/provider-adapter-migration-register.json)
