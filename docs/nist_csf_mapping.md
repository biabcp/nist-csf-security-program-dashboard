# NIST CSF Control Mapping Approach

## Purpose
This document explains how the security control catalog is mapped to NIST CSF so the program can be managed as a measurable product.

## Mapping Principles
1. **Primary function ownership:** Every control is assigned one primary CSF Function for accountability.
2. **Category/subcategory alignment:** Controls map to the most relevant CSF category code (e.g., PR.AC, DE.CM).
3. **Evidence-first design:** Each control includes an evidence artifact link to support audit and continuous assurance.
4. **Execution status transparency:** Controls are tracked as Not Started, In Progress, or Implemented to measure rollout progress.
5. **Automation lens:** Automation potential is captured to prioritize scalable implementation.

## Function Coverage Summary
- **Identify:** Asset, governance, business context, and supplier risk controls (ID.AM, ID.GV, ID.BE, ID.SC).
- **Protect:** Identity, access, data security, secure engineering, and awareness controls (PR.AC, PR.DS, PR.IP, PR.AT).
- **Detect:** Telemetry, analytics, and continuous monitoring controls (DE.AE, DE.CM, DE.DP).
- **Respond:** Incident planning, communications, mitigation, and lessons learned controls (RS.RP, RS.CO, RS.MI, RS.IM).
- **Recover:** Recovery planning, communications, and improvement controls (RC.RP, RC.CO, RC.IM).

## Example Traceability Flow
1. Control **PR-02 (Privileged Access Management)** maps to **PR.AC-4**.
2. Related risk in register: **R-002** (unauthorized admin activity).
3. KPI impact: improved access governance lowers incident likelihood and response complexity.
4. Executive reporting: maturity uplift in Protect function and reduced top-risk score.

## How to Use in Program Operations
- Use mapping during quarterly planning to identify underrepresented CSF categories.
- Link control status to risk treatment plans to demonstrate risk-informed investment.
- Use evidence links to support internal audit, external audit, and customer assurance responses.
