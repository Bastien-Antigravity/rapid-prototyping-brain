---
microservice: obsidian-brain
type: experiment
status: fluid
tags:
- \'#service/obsidian-brain\'
- '#state/fluid'
- null
- '#type/experiment'
---

# Experiment: [Name]

---
type: experiment
status: active | validated | abandoned | graduated
date: YYYY-MM-DD
target_repo: [repository name or "standalone"]
graduated_to: null
---

## 🎯 Hypothesis
What are you trying to prove? One sentence.

## 🧪 Prototype
- **Mode**: Fresh / Seed (Start from source)
- **Language**: Go / Python / Rust / Other
- **Source Context**: `[local path | github url | none]`
- **Ingestion Strategy**: `[full_ingest | module_only | interface_only]`
- **Location**: `<target-repo>/experiments/` or standalone script
- **Time Budget**: 2h / 4h / 1 day

## 📋 Steps
1. Build the minimum viable prototype.
2. Test locally.
3. Record results below.

## 📊 Results
_Fill after testing._

- **Outcome**: Success / Failure / Partial
- **Key Learning**: What did we discover?
- **Performance**: Any benchmarks or metrics?

## 🎓 Graduation Protocol
If `status: validated`, the **DocMaintainer** must:
1. Create a BDD spec in `02-Business-BDD/02-Behavior-Specs/<repo>/` based on the results.
2. Create a sandbox feature in `sandbox-testing/features/FEAT-XXX-<name>.yaml`.
3. Update this file: `status: graduated`, `graduated_to: FEAT-XXX`.
4. Switch the work to **Mode 1 (Spec-First)** for production hardening.
