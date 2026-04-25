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
| Identify | 3.4 | 4.2 | 0.8 |
| Protect | 3.6 | 4.3 | 0.7 |
| Detect | 2.9 | 4.0 | 1.1 |
| Respond | 3.7 | 4.2 | 0.5 |
| Recover | 3.3 | 4.1 | 0.8 |

## Gap Analysis
### Identify
Current governance and asset visibility are defined, but third-party and service dependency mapping remain incomplete. Closing this gap requires integrating supplier risk and CMDB service models into one operating view.

### Protect
Core preventive controls are broadly deployed, but privileged access, segmentation, and secure SDLC are still in rollout. The key gap is moving from implementation activity to measured control effectiveness.

### Detect
Detection is below target due to incomplete telemetry coverage and limited behavioral analytics. Program needs dedicated detection engineering sprints, stronger use case lifecycle management, and health-based data quality SLOs.

### Respond
Response readiness is comparatively mature with strong plan ownership and case handling. Remaining gap is consistency across regional communications and legal notification decisioning.

### Recover
Recovery capability is established, but testing depth and corrective-action closure cadence are inconsistent. Increasing scenario complexity and evidence quality will close audit and resilience gaps.

## Scoring Method (Practical)
- **Weighting:** 40% control implementation status, 30% KPI attainment, 20% evidence quality, 10% governance cadence.
- **Review cadence:** Monthly operational scoring, quarterly executive calibration.
- **Data sources:** Control catalog, risk register, incident postmortems, SOC and engineering telemetry.
