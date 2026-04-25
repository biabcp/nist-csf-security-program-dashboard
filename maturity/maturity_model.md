# NIST CSF Maturity Model (0–5)

## Maturity Scale Definition
- **0 — Nonexistent:** Control capability absent, ad hoc activity only.
- **1 — Initial:** Basic activities occur inconsistently and are person-dependent.
- **2 — Developing:** Repeatable practices exist in parts of the organization.
- **3 — Defined:** Enterprise standard exists with documented processes and ownership.
- **4 — Managed:** Performance is measured, governed, and improved via KPIs.
- **5 — Optimized:** Control effectiveness is continuously improved with automation and threat-informed adaptation.

## Current vs Target by CSF Function
| CSF Function | Current State | Target State (12 months) | Gap |
|---|---:|---:|---:|
| Identify | 3.17 | 4.36 | 1.19 |
| Protect | 3.19 | 4.55 | 1.36 |
| Detect | 2.74 | 4.38 | 1.64 |
| Respond | 2.83 | 4.34 | 1.51 |
| Recover | 2.79 | 4.37 | 1.58 |

## Gap Analysis
### Identify
Current governance and asset visibility are defined, but third-party and service dependency mapping remain incomplete. Closing this gap requires integrating supplier risk and CMDB service models into one operating view.

### Protect
Core preventive controls are broadly deployed, but privileged access, segmentation, and secure SDLC are still in rollout. The key gap is moving from implementation activity to measured control effectiveness.

### Detect
Detection is below target due to incomplete telemetry coverage and limited behavioral analytics. Program needs dedicated detection engineering sprints, stronger use case lifecycle management, and health-based data quality SLOs.

### Respond
Response capabilities are established but inconsistent for playbook depth, forensic readiness, and corrective-action closure. Remaining gap is raising execution consistency across regions and escalation workflows.

### Recover
Recovery capability is established, but testing depth and corrective-action closure cadence are inconsistent. Increasing scenario complexity and evidence quality will close audit and resilience gaps.

## Scoring Method (Data Alignment)
- **Roll-up basis:** Current and target maturity values are direct arithmetic averages from control-level maturity scores in the control catalog and are synchronized with `data/metrics.json`.
- **Review cadence:** Monthly operational scoring, quarterly executive calibration.
- **Data sources:** Control catalog, risk register, incident postmortems, and SOC/engineering telemetry.
