---
microservice: rapid-prototyping-brain
type: template
status: active
tags:
- '#type/template'
- '#service/rapid-prototyping-brain'
- '#zone/fluid'
---
# 🧪 Experiment: [Project Name]

## 📝 Abstract
*A one-sentence summary of what this experiment aims to prove or build.*

## 🎯 Objectives
- [ ] Primary Goal: 
- [ ] Secondary Goal: 

## 🔗 Business Alignment
- **Target Behavior**: `BEH-XXX - Behavior Name` (Refer to 02-Business-BDD/02-Behavior-Specs/)
- **Status**: [New Behavior / Extending Existing / Research Only]

## 🌐 Networking Mode
*Select one:*
- [ ] **Isolated**: No external dependencies. Local file system only.
- [ ] **Web-Only**: External HTTP/URL access required.
- [ ] **Fleet-Connected**: Requires connection to `teleremote-network` (NATS, Timescale, Config).

## 🛠️ Tech Stack & Toolbox
- **Language**: [Go / Python / Rust / JS]
- **Toolbox Usage**: [Yes / No]
- **Specialists Required**: [List specialist roles needed]

## 🔑 Secret Management
- [ ] **Public**: No secrets required.
- [ ] **Sovereign**: Uses `BASTIEN_PRIVATE_KEY` for in-memory decryption.
- [ ] **Mocked**: Uses hardcoded test credentials (ONLY for isolated mode).

## 🚀 Execution Strategy
*How will the prototype be built and tested?*
1. 
2. 

## 🚦 Success Criteria (Graduation Requirements)
- [ ] Functionality: [Describe expected behavior]
- [ ] Performance: [Describe performance targets]
- [ ] **Fleet Readiness**: [ ] Dockerized? [ ] Internal DNS? [ ] Healthy?

---
*Created on: [YYYY-MM-DD]*
