---
microservice: rapid-prototyping-brain
type: governance
status: active
tags:
- '#service/rapid-prototyping-brain'
- '#type/governance'
- '#state/active'
- '#zone/2-fluid'
---
# 🧬 AI Project DNA: Rapid Prototyping Labs

This document defines the constraints, naming conventions, and technology restrictions specific to the **Rapid Prototyping Labs (L04)**.

---

## 🎯 1. High-Level Vision

The primary mission of the Labs is to serve as the **Execution Bridge** between raw brainstormed chats and the production fleet. It provides an isolated sandbox to ingest conversations, clone and analyze production files inside dedicated workspace folders, compare and merge logic, and propose ecosystem-aligned merge plans that can be accepted, refused, saved, or completely removed.

---

## 🛡️ 2. Core Constraints

1.  **Ingestion & Extraction Limit**: LLM transcripts (`CHAT-*.md`) must be processed to isolate raw code blocks and specifications, filtering out conversational noise before code generation starts.
2.  **Dedicated Workspace Sandbox & Automation**: **For every new test or experiment, a dedicated directory must be created at the root of `04-Rapid-Prototyping/`** (e.g. `04-Rapid-Prototyping/EXP-XXX-[Slug]/`). Use the local `.venv` virtual environment and `lab_manager.py` script to automate sandbox creation, cloning target fleet repositories, and stub extraction. All spike code and cloned production stubs must reside inside this folder to allow AI access during development.
3.  **Archive Isolation**: The `experiments/` folder contains `.aiignore`, `.geminiignore`, and `.mcpignore` files set to `*`. Active sandboxes live at the root of L04 and are moved to `experiments/` **only when archived/saved** to keep them hidden from active RAG scanning once resolved.
4.  **Local Mocking**: Sandbox spikes must mock out external resources (e.g. active databases, network sockets) to remain runnable inside L04 in isolation.
5.  **Ecosystem Alignment & Resolution**: Every completed experiment must end with an **Ecosystem Merge Proposal** presenting four clear outcomes:
    *   **Accepted/Merged**: Merge the diffs directly into production.
    *   **Refused**: Delete the root sandbox folder and spike files, marking the history log as deprecated.
    *   **Saved**: Move the root sandbox folder into `experiments/` (where it is immediately ignored by the AI context) and mark the proposal as a draft.
    *   **Completely Removed**: Delete the sandbox directory, raw chats, and proposal logs entirely.

---

## 🏷️ 3. Naming Conventions

*   **Active Chats**: `CHAT-XXX-[Slug].md` (raw LLM chat logs to ingest).
*   **Pitch Proposals**: `EXP-XXX-[Slug].md` (finalized Ecosystem Merge Proposals).
*   **Active Sandbox Directories**: `04-Rapid-Prototyping/EXP-XXX-[Slug]/` (created in the root).
*   **Archived Sandbox Directories**: `04-Rapid-Prototyping/experiments/EXP-XXX-[Slug]/` (moved to experiments/ upon completion).
*   **Sandbox Spikes**: Prefix temporary scripts with `spike_` or `lab_` inside the dedicated sandbox directory.
