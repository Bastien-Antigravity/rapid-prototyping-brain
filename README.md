---
microservice: rapid-prototyping-brain
type: experiment
status: active
tags:
- '#service/rapid-prototyping-brain'
- '#state/active'
- '#type/experiment'
- '#zone/2-fluid'
---
# 🧪 Zone 2: Rapid Prototyping Labs (Implementation Lab)

Welcome to the **Implementation Lab**. This zone serves as the cognitive boundary for converting raw LLM brainstorm transcripts, third-party code samples, and human ideas into fleet-compliant code.

---

## 🏛️ Core Workflow Paradigm

The Prototyper Agent operates on a four-stage progressive validation pipeline:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ 1. LLM INGESTION │ ──> │ 2. CLONE & STUB  │ ──> │ 3. COMPARE/MERGE │ ──> │ 4. ALIGN & DECIDE│
└──────────────────┘     └──────────────────┘     └──────────────────┘     └──────────────────┘
```

### 📥 Step 1: LLM Chat Ingestion
*   **Action**: Load the raw, long chat conversation transcript with the LLM (saved as `CHAT-XXX-[Slug].md` in the root).
*   **Objective**: Perform extraction. Distill the conversation, isolate code blocks, compile specifications, and parse logical flows, discarding the conversational noise.

### 🧬 Step 2: Clone & Stub Extraction
*   **Action**: **Create a dedicated workspace folder at the root of `04-Rapid-Prototyping/`** for this new test (e.g. `04-Rapid-Prototyping/EXP-XXX-[Slug]/`). Reference or clone target production files (from active microservice repositories mapped in `06-Microservices/` or `05-Fleet-Operation/00-Repo-Control/inventory.json`) or default templates.
*   **Automation**: Use `lab_manager.py` within the `.venv` virtual environment to automate sandbox creation, repository cloning, and file stub extraction:
    ```bash
    python lab_manager.py create EXP-XXX-[Slug]
    python lab_manager.py clone EXP-XXX-[Slug] <repo_name_or_url>
    python lab_manager.py extract EXP-XXX-[Slug] <repo_name> <relative_path_to_file>
    ```
*   **Objective**: Analyze structural patterns in isolation. Extract the active schemas, interfaces, base classes, and import requirements to establish a clean, compatible baseline. **All active spike code must live inside this root-level sandbox folder so the AI can access and edit it.**

### 🔄 Step 3: Comparison & Merging
*   **Action**: Perform side-by-side comparison between:
    1.  The extracted production codebase / template files.
    2.  The draft logic parsed from the LLM chat transcript.
*   **Objective**: Merge the draft logic with the production stubs. Generate temporary runnable scripts (e.g. `spike_*.py` or `lab_*.go`) inside the dedicated root sandbox folder (`04-Rapid-Prototyping/EXP-XXX-[Slug]/`) to run isolated local tests.

### 🏁 Step 4: Ecosystem Review & Merge Decisions
*   **Action**: Audit the finalized sandbox scripts against the **Bastien-Antigravity Ecosystem Rules** (e.g. Virtual Environment Re-Execution, UTF-8 output encoding, nil-safe logging guards, and FFI Static Loading Laws) and propose the graduation path (`EXP-XXX-[Slug].md`).
*   **Objective**: Execute one of the following decisions:
    1.  **Accepted/Merged**: Propose the final diffs and merge them into the production microservice codebase.
    2.  **Refused**: Reject the proposal. The root sandbox folder and spike files are deleted, and the history file (`EXP-XXX-[Slug].md`) is marked as `status: deprecated` or moved to the `/experiments/` archive.
    3.  **Saved**: Retain the work for future implementation. The root sandbox folder is moved into `/experiments/` (where it is immediately ignored by `.aiignore` to prevent AI context pollution) and the proposal is marked as `status: draft`.
    4.  **Completely Removed**: Delete the root sandbox folder, spike files, raw chats, and proposal notes entirely, leaving zero traces.

---

## 🤖 Agent Handoff Protocols (Hire the Prototyper)

To execute a spike following this paradigm, invoke the squad using these hiring prompts:

### 🎭 Ingestion & Isolation Prompt
> *"Hire the Prototyper Agent. Read the long LLM chat transcript in `04-Rapid-Prototyping/CHAT-XXX-[Slug].md` and extract all raw code blocks. Then, **create a dedicated sandbox folder at the root of L04** (`04-Rapid-Prototyping/EXP-XXX-[Slug]/`) to mount the cloned production interface stubs."*

### 🔄 Merging & Validation Prompt
> *"Hire the Prototyper Agent. Compare the raw draft logic against the production stubs. Merge them into a runnable spike file **inside the root sandbox folder** and verify its execution behavior under isolated conditions."*

### 🏁 Graduation & Decisions Prompt
> *"Hire the Prototyper Agent. Review the completed spike against the Ecosystem Tech Stack guidelines and generate the merge proposal (`EXP-XXX-[Slug].md`). Present the four resolution choices: Merge, Refuse, Save, or Remove."*

---
*See Also: [[AI-Project-DNA]], [[AI-Session-State]], [[Template-Experiment]]*
