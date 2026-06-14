# NIST CSF Security Program Dashboard

A local Streamlit dashboard for internal cybersecurity program reporting using the NIST Cybersecurity Framework (CSF). The dashboard combines security posture metrics, maturity tracking, control ownership, risk prioritization, and operational resilience trends into one executive-facing view.

The application is designed for security leadership, GRC, compliance, IT operations, and executive stakeholders who need a practical way to monitor program health and make risk-informed decisions.

## What the Dashboard Shows

The Streamlit app (`streamlit_app.py`) reads the existing repository data and presents it as a realistic security program reporting tool:

- **Executive Overview:** posture score, reporting period, implemented controls, control coverage, open risks, MTTD, MTTR, and the executive summary from `data/metrics.json`.
- **NIST CSF Maturity:** current vs. target maturity by CSF function with interpretation of the largest improvement gaps.
- **Control Coverage:** implementation status counts, function/status filters, search, and a control table with ownership, automation potential, maturity scores, and KPIs.
- **Risk Register:** top risks sorted by risk score, risk filters, heatmap-style likelihood/impact scatter plot, mitigation strategy, owner, target date, and status.
- **Trends:** monthly open risk trend and monthly control coverage trend from `data/metrics.json`.
- **Program Context:** explanation of how the dashboard supports governance, NIST CSF maturity tracking, control ownership, risk-based prioritization, evidence readiness, operational resilience, and executive reporting.

## Repository Architecture

```text
NIST-CSF-Security-Program-Tracker/
├── .streamlit/
│   └── config.toml
├── README.md
├── requirements.txt
├── streamlit_app.py
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

## Data Sources

The dashboard uses these existing repository files:

- `data/metrics.json` — reporting period, posture metrics, maturity by function, trend data, and executive summary.
- `data/control_catalog.csv` — control records, CSF function mapping, implementation status, owners, maturity scores, automation potential, and KPIs.
- `data/risk_register.csv` — risk descriptions, likelihood, impact, risk score, mitigation strategy, owner, target completion date, status, and residual risk.
- `dashboard/executive_dashboard.md` — optional supporting context displayed in an expandable section. The app continues to run if this optional file is unavailable.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/chrisfsolis/nist-csf-security-program-dashboard.git
cd nist-csf-security-program-dashboard
```

### 2. Create and activate a virtual environment

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run streamlit_app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`. Open that URL in a browser to view the dashboard.

## Demo Runbook

Use this runbook for a local walkthrough or internal program review.

1. **Start the app**
   ```bash
   streamlit run streamlit_app.py
   ```
2. **Open the Executive Overview** and confirm the homepage immediately shows the posture score, reporting period, implemented controls, control coverage, open risks, MTTD, MTTR, and executive summary.
3. **Review NIST CSF Maturity** to compare current and target scores by Identify, Protect, Detect, Respond, and Recover.
4. **Review Control Coverage** using the NIST CSF function and implementation status filters. Search for a control owner, KPI, or control ID to narrow the table.
5. **Review the Risk Register** by filtering status, owner, CSF function, and residual risk. Use the likelihood/impact scatter plot to identify high-priority risk concentrations.
6. **Review Trends** to connect risk reduction and control implementation progress to monthly leadership reporting.
7. **Close with Program Context** to explain how the dashboard supports governance, evidence readiness, operational resilience, and executive reporting.

## Common Use Cases

- **Security program governance:** Maintain a shared view of CSF-aligned capability maturity, control status, and risk exposure.
- **GRC and compliance operations:** Track control ownership, implementation status, KPIs, and evidence readiness.
- **Risk committee reporting:** Prioritize remediation based on risk score, residual risk, mitigation strategy, owner, and target completion.
- **IT and security operations:** Connect operational metrics such as MTTD, MTTR, telemetry coverage, vulnerability remediation, and recovery testing to program outcomes.
- **Executive reporting:** Provide a concise view of posture, maturity gaps, open risks, and trend direction without requiring stakeholders to inspect raw CSV or JSON files.

## Troubleshooting

### `streamlit` command not found

Install dependencies in the active environment:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python -m streamlit run streamlit_app.py
```

### Blank page or data loading error

Confirm the required files exist and are not empty:

```bash
python -m py_compile streamlit_app.py
python - <<'PY'
from pathlib import Path
for path in ['data/metrics.json', 'data/risk_register.csv', 'data/control_catalog.csv']:
    p = Path(path)
    print(path, 'exists=', p.exists(), 'size=', p.stat().st_size if p.exists() else 0)
PY
```

### CSV parsing error

Open the referenced CSV and check for unescaped commas, missing headers, or partially edited rows. The dashboard validates required columns and shows a clear error if a required source is missing, malformed, or empty.

### Port already in use

Run Streamlit on a different port:

```bash
streamlit run streamlit_app.py --server.port 8502
```

## Development Notes

- The app uses safe paths relative to the repository root; no absolute local paths are required.
- Data loading is cached with Streamlit caching for responsive filtering and charting.
- Dependencies are intentionally minimal: Streamlit, pandas, and Plotly.
- The app is compatible with local Windows, macOS, Linux environments and Streamlit Community Cloud.
