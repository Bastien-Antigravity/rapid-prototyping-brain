--- 
microservice: 04-Rapid-Prototyping
type: overview
status: active
tags:
- '#service/04-Rapid-Prototyping'
- '#type/overview'
- '#state/active'
- '#ai/ignore'
---
# 🎭 Labs Features & Spikes Behavior

This document outlines the standard behavioral expectations and lifecycles for spikes and experiments.

---

## 🚀 The 4-Stage Prototyping Pipeline

Every experiment follows this strict, progressive execution lifecycle:

1.  **LLM Chat Ingestion & Asset Parsing**
    *   Ingests the raw, long conversation transcript (`CHAT-XXX-[Slug].md`).
    *   Parses, filters, and extracts code blocks, specifications, and logic assets.

2.  **Isolated Sandbox Creation & Stub Extraction**
    *   **Creates a dedicated workspace directory at the root of `04-Rapid-Prototyping/`** (e.g. `EXP-XXX-[Slug]/`). Do NOT create it inside `/experiments/` during active testing to prevent the AI from being blocked by ignore rules.
    *   Uses the local Python virtual environment `.venv` and the `lab_manager.py` script to automate isolation tasks.
    *   References target production codebase files or templates from the fleet.
    *   Extracts structural templates, imports, variables, and API contracts inside the root sandbox directory.

3.  **Comparison & Merging**
    *   Compares the draft logic against production stubs side-by-side.
    *   Merges logic into a sandbox spike (e.g. `spike_*.py` or `lab_*.go`) inside the dedicated root sandbox directory and verifies execution.

4.  **Ecosystem Review & Merge Resolution Outcomes**
    *   Checks the prototype against the Ecosystem rules (virtual environment re-execution, UTF-8 output encoding, nil-safe logging, and FFI loading laws).
    *   Generates a formal Merge Proposal (`EXP-XXX-[Slug].md`) presenting four resolution outcomes:
        1.  **Accepted/Merged**: Diff files are integrated directly into production.
        2.  **Refused**: Rejected. The root sandbox folder and spike files are deleted, and the history log is marked as deprecated.
        3.  **Saved**: Parked. The root sandbox folder is moved into `experiments/` where it is ignored, and the proposal is marked as a draft.
        4.  **Completely Removed**: Deleted. The root sandbox directory, raw chats, and proposal notes are deleted entirely.
