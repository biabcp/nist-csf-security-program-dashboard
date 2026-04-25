# NIST-CSF-Security-Program-Tracker

An enterprise-grade portfolio project that shows how to run a cybersecurity program as a product, using the NIST Cybersecurity Framework (CSF) as the operating model and a lightweight ISO 27001 crosswalk for multi-framework reporting.

## Security Program as a Product
Traditional security programs often look like disconnected control checklists. This repository demonstrates a product-oriented model where controls, risks, metrics, and roadmap decisions are connected and measurable.

**Product characteristics in this project:**
- Clear backlog and roadmap tied to CSF outcomes.
- Quantified operational KPIs (MTTD, MTTR, coverage, risk trend).
- Executive reporting focused on risk-reduction and resilience outcomes.
- Continuous improvement loop from incidents and maturity assessments.

## Why NIST CSF Matters
NIST CSF provides a practical way to organize enterprise security capabilities into five business-friendly functions:
- **Identify** what matters and where risk lives.
- **Protect** assets and data through preventive controls.
- **Detect** threats quickly through telemetry and analytics.
- **Respond** effectively to contain impact.
- **Recover** critical services and institutionalize lessons learned.

This functional model helps leadership fund and track security as an ongoing capability—not a one-time compliance exercise.

## Repository Architecture

```text
NIST-CSF-Security-Program-Tracker/
├── README.md
├── data/
│   ├── control_catalog.csv
│   ├── control_catalog.json
│   ├── metrics.json
│   └── risk_register.csv
├── dashboard/
│   └── executive_dashboard.md
├── docs/
│   ├── iso27001_mapping.md
│   └── nist_csf_mapping.md
├── maturity/
│   └── maturity_model.md
└── roadmap/
    └── security_program_roadmap.md
```

## What’s Included

### 1) Control Catalog (`data/control_catalog.*`)
A realistic set of 32 controls across all CSF functions with:
- control ownership,
- implementation status,
- evidence references,
- and automation potential.

Available in both CSV (operations-friendly) and JSON (tooling/API-friendly).

### 2) Risk Register (`data/risk_register.csv`)
A CSF-linked risk register with practical scenarios (cloud misconfiguration, IAM weaknesses, logging gaps, patching debt, detection lag). Risk scoring is quantified with a simple Likelihood × Impact model.

### 3) Metrics (`data/metrics.json`)
Operational KPIs used by security and leadership:
- MTTD / MTTR,
- control coverage,
- automation percentage,
- open risk count,
- and multi-month risk reduction trend.

### 4) Product Roadmap (`roadmap/security_program_roadmap.md`)
CSF-aligned epics with initiatives written as user stories, including priorities and dependencies to reflect real delivery constraints.

### 5) Executive Dashboard (`dashboard/executive_dashboard.md`)
Leadership-ready summary with posture score, maturity by function, top risks, and operational metrics.

### 6) Maturity Model (`maturity/maturity_model.md`)
Defines a 0–5 maturity scale, current vs target state by CSF function, and practical gap analysis to guide investment planning.

### 7) Framework Mapping (`docs/`)
- `nist_csf_mapping.md`: explains control-to-CSF logic and operational use.
- `iso27001_mapping.md`: lightweight crosswalk for ISO 27001 alignment conversations.

## Example Use Cases
- **GRC Program Management:** Track control rollout, owners, and maturity gaps.
- **Audit Readiness:** Trace controls to evidence and governance cadence.
- **Security Leadership Reporting:** Provide CISO-level posture updates with defensible metrics.
- **Risk Committee Briefings:** Prioritize investments using quantified residual risk.
- **Customer Assurance:** Reuse control records for NIST and ISO conversations.

## Mock Dashboard / Screenshot Concepts
If this repo is extended into a web dashboard, typical views would include:
1. **CISO Overview Page:** posture score, open risks, MTTD/MTTR trend tiles.
2. **Control Operations Page:** implementation burn-up by CSF function.
3. **Risk Heatmap:** top residual risks by likelihood/impact quadrant.
4. **Maturity Progress View:** current vs target scores with quarterly trajectory.

## How to Extend This Project
- Add automated data ingestion from ticketing (Jira/ServiceNow) and SIEM APIs.
- Track KRIs/KPIs per business unit and critical service.
- Add control testing outcomes and evidence freshness scoring.
- Expand ISO mapping into full Statement of Applicability (SoA) alignment.
- Build a front-end dashboard (e.g., Streamlit, Power BI, React) against the JSON/CSV data sources.

## Portfolio Positioning
This project is designed to showcase senior-level cybersecurity architecture and GRC leadership capability: strategy-to-execution traceability, measurable outcomes, and executive communication quality aligned to industry-recognized frameworks.
