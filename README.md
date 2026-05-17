---
microservice: rapid-prototyping-brain
type: experiment
status: fluid
tags:
- '#service/rapid-prototyping-brain'
- '#state/fluid'
- '#type/experiment'
- '#zone/fluid'
---

# 🧪 Zone 2: Rapid Prototyping Labs (Implementation Lab)

Welcome to the **Implementation Lab**. This zone is the primary entry point for converting raw **LLM Chat**, unstructured code spikes, and human ideas into organized, rule-compliant code.

The Labs serve as the "Execution Bridge" between the **[[02-Business-BDD/README|🎭 Business BDD]]** (which defines *what* to build) and the production fleet. Every experiment here aims to fulfill a specific **Behavior Specification** using the ecosystem's engineering standards.

## 🚀 Labs Workflow
1.  **The Archive (Pre-flight)**: Before starting a new experiment, move any existing **`CHAT-XXX-[Slug].md`** and **`EXP-XXX-[Slug].md`** files from the root into the **`experiments/`** folder. This archives the history and uses ignore files (`.aiignore`, `.mcpignore`, `.geminiignore`) to instantly hide them from active AI context, preventing distraction.
2.  **The Spark**: A new raw idea, prompt, or LLM chat transcript containing draft code is saved as a **`CHAT-XXX-[Name].md`** file in the **root** of this repository (No structure or linting required).
3.  **The Test**: The developer or AI runs quick, isolated tests on the raw code to verify the core concept works.
4.  **The Handoff**: The **Orchestrator** and **Developer** agents are "hired" to ingest the raw chat file, apply the **[[03-Tech-Stack/README|🏗️ Tech Stack Coding Rules]]**, and output clean, production-grade files in the target repository.
5.  **The Pitch**: The completed experiment is recorded as an **`EXP-XXX-[Name].md`** file in the **root** using the **[[Template-Experiment|🧪 Experiment Template]]** to preserve the transition and BDD links.

## 🤖 The Agent Handoff Protocol (From Chaos to Code)
To convert a raw scratchpad draft into fleet-compliant code, the user invokes the downstream agents using the following protocol:

### Step 1: Hire the Orchestrator
The **Orchestrator** reads the raw chat file, maps it to a target behavior in `02-Business-BDD/README`, and generates the execution path.
> **Hiring Prompt**:
> *"Hire the Orchestrator. Read the raw draft in `04-Rapid-Prototyping/CHAT-XXX-[Name].md`. Map this to the target behavior in `02-Business-BDD/README` and spawn the execution task for the Developer."*

### Step 2: Hire the Developer Specialist
The **Developer** (e.g., Go, Rust, or Python Specialist) takes the task, reads the chat file, and writes the production code in the target microservice repository—strictly adhering to Tier 3 coding rules (e.g., Go Concurrency, Memory management).
> **Hiring Prompt**:
> *"Hire the [Language] Specialist. Read the Orchestrator task and the raw draft in `04-Rapid-Prototyping/CHAT-XXX-[Name].md`. Implement this in the target repository following the Tech Stack Coding Rules."*

## 📂 Flat Structure
- **`README.md`**: The mission statement and agent protocols.
- **`AI-Init.md`**: The agent "hiring" instructions.
- **`Template-Experiment.md`**: The standard pitch template.
- **`CHAT-XXX-[Slug].md`**: The *current active* chat and brainstorm file.
- **`EXP-XXX-[Slug].md`**: The *current active* experiment record.
- **`experiments/`**: Archive directory for old experiments/chats. Contains `.aiignore`, `.mcpignore`, and `.geminiignore` to block AI context scanning.

## 🚦 Current Active Lab
- **None**. Waiting for the first spark.

---
> [!TIP]
> Use this zone to "See it working" before you "Make it perfect." By keeping only the active files at the root and archiving old ones to `experiments/`, we protect the AI from context overflow while preserving historical records.
