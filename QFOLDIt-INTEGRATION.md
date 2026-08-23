# qFoldIT Integration Status

Protein-MCP is a **scientific domain adapter**, not the canonical qFoldIT runtime.

## Canonical architecture

```text
Protein-MCP
    ↓
Protein / sequence / structure adapter
    ↓
qFoldIT Scientific Object + Mission Contract
    ↓
Scientific Action Envelope
    ↓
UAG / runtime
    ↓
Validation + Evidence
```

The repository retains its upstream ProteinMCP lineage and license. qFoldIT should progressively move shared contracts into the Rust `qfoldit-core` crate hosted by `UEFN-QFOLDIT`, while this repository remains focused on protein-specific engines, workflows and integrations.

The existing ProteinMCP architecture already combines multiple protein-engineering MCPs and workflow skills; those remain reusable as domain capabilities rather than becoming a second qFoldIT orchestration core.

## Migration rule

- Do not duplicate mission/state/provenance contracts here.
- Use the canonical qFoldIT contract when integrating with qFoldIT.
- Keep scientific engine dependencies local to this adapter.
- Preserve upstream license and attribution for all third-party components.
