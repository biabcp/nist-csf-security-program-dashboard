# Executive Security Dashboard

**Reporting Date:** 2026-04-25  
**Audience:** CISO, CIO, Audit & Risk Committee

## Overall Security Posture Score
# **76 / 100**

Interpretation: Program fundamentals are established, with strong progress in protection and response. Primary drag factors are detection engineering backlog, IAM modernization completion, and third-party control assurance.

## Maturity Score by NIST CSF Function (0–5)
| CSF Function | Current Maturity | Target Maturity (12 months) | Trend |
|---|---:|---:|---|
| Identify | 3.4 | 4.2 | Improving |
| Protect | 3.6 | 4.3 | Improving |
| Detect | 2.9 | 4.0 | Needs Acceleration |
| Respond | 3.7 | 4.2 | Stable-Improving |
| Recover | 3.3 | 4.1 | Improving |

## Top 5 Risks (by residual score)
| Risk ID | Risk Statement | Score | Status | Executive Action |
|---|---|---:|---|---|
| R-001 | Cloud storage misconfiguration exposes confidential data | 20 | Open | Fund guardrails-as-code and auto-remediation |
| R-002 | Privileged access weaknesses allow unauthorized admin actions | 20 | Open | Accelerate PAM phase 2 |
| R-004 | Patch SLA breaches on legacy infrastructure | 16 | Open | Enforce risk acceptance with CIO sign-off |
| R-010 | Detection content lags emerging attacker techniques | 16 | Open | Add detection engineering sprint capacity |
| R-003 | Logging gaps reduce forensic readiness | 15 | Open | Prioritize telemetry onboarding for crown jewels |

## Control Coverage and Automation
- **Implemented controls:** 17 / 32 (**53.1%**)  
- **Controls in progress:** 14 / 32 (**43.8%**)  
- **Not started:** 1 / 32 (**3.1%**)  
- **Controls with high automation potential:** 14 / 32 (**43.8%**)

## Operational Metrics
- **MTTD:** 6.8 hours (target: < 8h) ✅
- **MTTR:** 18.4 hours (target: < 24h) ✅
- **Open enterprise cyber risks:** 8
- **Risk reduction trend:** Residual risk index improved from 61 (Nov 2025) to 48 (Apr 2026)

## Leadership Notes
1. Detection maturity is the primary program bottleneck and requires sustained engineering capacity.
2. IAM and PAM completion will materially reduce top residual risk exposure.
3. Recovery testing quality has improved; next focus is evidence quality for audit defensibility.
