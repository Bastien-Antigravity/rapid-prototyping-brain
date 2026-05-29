# 🧪 Labs Testing Playbook

This document defines how to test prototype scripts inside Level 04.

---

## 🛡️ Sandbox Validation Rules

1.  **Isolated execution**: Run python or go scripts with isolated standard libraries only.
2.  **No production imports**: Never import production code paths to prevent circular dependency structures or build errors.
3.  **Local Mocking**: Mock out external system configurations (e.g. gRPC ports, database connections) inside local variables.
