# 🗺️ Labs Architecture Overview

This document describes the structure and directory layout of the **Rapid Prototyping Labs**.

---

## 🏛️ Directory Layout

```
04-Rapid-Prototyping/
├── README.md               # Onboarding and agent handoff protocols
├── AI-Init.md              # Bootstrapping prompt for Prototyper sessions
├── AI-Project-DNA.md       # High-level vision and constraints
├── AI-Session-State.md     # Active checklists and state logs
├── archive.py              # Packaging python script for clean-ups
├── Template-Experiment.md  # Standard scaffolding for pitch files
├── experiments/            # Hidden archive folder for past spikes
│   ├── .aiignore           # Ignores files from active RAG context
│   ├── .geminiignore
│   └── .mcpignore
├── Role-Prompts/           # Colocated agent prompts
│   └── 03-Developer/
│       └── Squad/
│           └── Prompt-Prototyper.md
└── quick-overview/         # Ignored human onboarding documents
```

---

## 🛡️ Sandbox Boundary
The entire lab is isolated from the main fleet codebases. No active network bindings or database configurations are exposed directly, ensuring that experiments cannot affect live processes.
