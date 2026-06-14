"""Streamlit dashboard for NIST CSF security program reporting."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd
import plotly.express as px
import streamlit as st

APP_TITLE = "NIST CSF Security Program Dashboard"
APP_SUBTITLE = (
    "Executive view of cybersecurity program maturity, risk, control coverage, "
    "and operational resilience"
)
REPO_ROOT = Path(__file__).resolve().parent
DATA_DIR = REPO_ROOT / "data"
METRICS_PATH = DATA_DIR / "metrics.json"
RISK_PATH = DATA_DIR / "risk_register.csv"
CONTROL_PATH = DATA_DIR / "control_catalog.csv"
EXECUTIVE_MD_PATH = REPO_ROOT / "dashboard" / "executive_dashboard.md"

REQUIRED_CONTROL_COLUMNS = [
    "control_id",
    "control_name",
    "nist_csf_function",
    "implementation_status",
    "control_owner",
    "automation_potential",
    "maturity_score_current",
    "maturity_score_target",
    "kpi",
]
REQUIRED_RISK_COLUMNS = [
    "risk_id",
    "risk_description",
    "related_csf_function",
    "likelihood_1_to_5",
    "impact_1_to_5",
    "risk_score",
    "mitigation_strategy",
    "status",
    "owner",
    "target_completion",
    "residual_risk",
]


st.set_page_config(page_title=APP_TITLE, page_icon="🛡️", layout="wide")


class DataLoadError(Exception):
    """Raised when a required dashboard data source cannot be loaded."""


def _missing_columns(frame: pd.DataFrame, required_columns: list[str]) -> list[str]:
    return [column for column in required_columns if column not in frame.columns]


@st.cache_data(show_spinner=False)
def load_metrics() -> dict[str, Any]:
    if not METRICS_PATH.exists():
        raise DataLoadError(f"Missing required file: {METRICS_PATH.relative_to(REPO_ROOT)}")
    try:
        metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DataLoadError(f"Malformed JSON in {METRICS_PATH.relative_to(REPO_ROOT)}: {exc}") from exc
    if not isinstance(metrics, dict) or not metrics:
        raise DataLoadError("metrics.json is empty or does not contain a JSON object.")
    return metrics


@st.cache_data(show_spinner=False)
def load_csv(path: Path, required_columns: list[str]) -> pd.DataFrame:
    if not path.exists():
        raise DataLoadError(f"Missing required file: {path.relative_to(REPO_ROOT)}")
    try:
        frame = pd.read_csv(path)
    except pd.errors.EmptyDataError as exc:
        raise DataLoadError(f"{path.relative_to(REPO_ROOT)} is empty.") from exc
    except pd.errors.ParserError as exc:
        raise DataLoadError(f"Malformed CSV in {path.relative_to(REPO_ROOT)}: {exc}") from exc
    if frame.empty:
        raise DataLoadError(f"{path.relative_to(REPO_ROOT)} has headers but no records.")
    missing = _missing_columns(frame, required_columns)
    if missing:
        raise DataLoadError(f"{path.relative_to(REPO_ROOT)} is missing columns: {', '.join(missing)}")
    return frame


@st.cache_data(show_spinner=False)
def load_optional_markdown() -> str:
    if not EXECUTIVE_MD_PATH.exists():
        return ""
    return EXECUTIVE_MD_PATH.read_text(encoding="utf-8")


def as_number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def filter_multiselect(label: str, values: pd.Series, key: str) -> list[str]:
    options = sorted(values.dropna().astype(str).unique().tolist())
    return st.multiselect(label, options=options, default=options, key=key)


def searchable_table(frame: pd.DataFrame, search_columns: list[str], key: str) -> pd.DataFrame:
    search = st.text_input("Search table", placeholder="Type to filter visible records", key=key)
    if not search:
        return frame
    mask = pd.Series(False, index=frame.index)
    for column in search_columns:
        mask = mask | frame[column].astype(str).str.contains(search, case=False, na=False)
    return frame[mask]


def executive_overview(metrics: dict[str, Any], controls: pd.DataFrame, risks: pd.DataFrame) -> None:
    st.header("Executive Overview")
    st.caption("Leadership-ready snapshot of program posture, control adoption, operational response, and active risk.")

    implemented_controls = int(metrics.get("implemented_controls", (controls["implementation_status"] == "Implemented").sum()))
    open_risks = int(metrics.get("open_risks", risks[risks["status"].isin(["Open", "Mitigating"])].shape[0]))

    cols = st.columns(6)
    cols[0].metric("Posture Score", "76 / 100")
    cols[1].metric("Reporting Period", str(metrics.get("reporting_period", "Not provided")))
    cols[2].metric("Implemented Controls", f"{implemented_controls}")
    cols[3].metric("Control Coverage", f"{as_number(metrics.get('control_coverage_percent')):.1f}%")
    cols[4].metric("Open Risks", f"{open_risks}")
    cols[5].metric("MTTD / MTTR", f"{as_number(metrics.get('mttd_hours')):.1f}h / {as_number(metrics.get('mttr_hours')):.1f}h")

    st.info(metrics.get("executive_summary", "Executive summary is not available in metrics.json."))


def maturity_section(metrics: dict[str, Any]) -> None:
    st.header("NIST CSF Maturity")
    maturity = metrics.get("maturity_by_function", {})
    if not maturity:
        st.warning("Maturity by function is unavailable in metrics.json.")
        return

    maturity_frame = pd.DataFrame(
        [
            {"Function": function, "Current": values.get("average_current"), "Target": values.get("average_target")}
            for function, values in maturity.items()
        ]
    )
    chart_frame = maturity_frame.melt(id_vars="Function", value_vars=["Current", "Target"], var_name="Maturity", value_name="Score")
    st.plotly_chart(
        px.bar(chart_frame, x="Function", y="Score", color="Maturity", barmode="group", range_y=[0, 5], text_auto=".2f"),
        use_container_width=True,
    )
    maturity_frame["Gap"] = maturity_frame["Target"] - maturity_frame["Current"]
    biggest_gap = maturity_frame.sort_values("Gap", ascending=False).iloc[0]
    st.write(
        f"The largest maturity gap is in **{biggest_gap['Function']}** "
        f"({biggest_gap['Gap']:.2f} points). Closing these gaps reduces execution risk, improves resilience, "
        "and gives leadership a clearer basis for funding and sequencing security initiatives."
    )


def control_coverage_section(controls: pd.DataFrame) -> None:
    st.header("Control Coverage")
    status_counts = controls["implementation_status"].value_counts().rename_axis("Status").reset_index(name="Count")
    st.plotly_chart(px.bar(status_counts, x="Status", y="Count", color="Status", text_auto=True), use_container_width=True)

    left, right = st.columns(2)
    with left:
        functions = filter_multiselect("Filter by NIST CSF function", controls["nist_csf_function"], "control_functions")
    with right:
        statuses = filter_multiselect("Filter by implementation status", controls["implementation_status"], "control_statuses")

    filtered = controls[controls["nist_csf_function"].astype(str).isin(functions) & controls["implementation_status"].astype(str).isin(statuses)]
    filtered = searchable_table(filtered, ["control_id", "control_name", "control_owner", "kpi"], "control_search")
    st.dataframe(filtered[REQUIRED_CONTROL_COLUMNS], use_container_width=True, hide_index=True)


def risk_register_section(risks: pd.DataFrame) -> None:
    st.header("Risk Register")
    risks = risks.copy()
    for column in ["likelihood_1_to_5", "impact_1_to_5", "risk_score"]:
        risks[column] = pd.to_numeric(risks[column], errors="coerce")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        statuses = filter_multiselect("Status", risks["status"], "risk_status")
    with col2:
        owners = filter_multiselect("Owner", risks["owner"], "risk_owner")
    with col3:
        functions = filter_multiselect("CSF Function", risks["related_csf_function"], "risk_function")
    with col4:
        residuals = filter_multiselect("Residual Risk", risks["residual_risk"], "risk_residual")

    filtered = risks[
        risks["status"].astype(str).isin(statuses)
        & risks["owner"].astype(str).isin(owners)
        & risks["related_csf_function"].astype(str).isin(functions)
        & risks["residual_risk"].astype(str).isin(residuals)
    ].sort_values("risk_score", ascending=False)

    st.subheader("Top Risks by Score")
    st.plotly_chart(
        px.scatter(
            filtered,
            x="likelihood_1_to_5",
            y="impact_1_to_5",
            size="risk_score",
            color="residual_risk",
            hover_name="risk_id",
            hover_data=["risk_description", "owner", "status"],
            range_x=[0.5, 5.5],
            range_y=[0.5, 5.5],
            labels={"likelihood_1_to_5": "Likelihood", "impact_1_to_5": "Impact"},
        ),
        use_container_width=True,
    )
    visible = searchable_table(filtered, ["risk_id", "risk_description", "mitigation_strategy", "owner"], "risk_search")
    st.dataframe(
        visible[["risk_id", "risk_description", "risk_score", "mitigation_strategy", "owner", "target_completion", "status"]],
        use_container_width=True,
        hide_index=True,
    )


def trends_section(metrics: dict[str, Any]) -> None:
    st.header("Trends")
    left, right = st.columns(2)
    with left:
        risk_trend = pd.DataFrame(metrics.get("monthly_risk_reduction_trend", []))
        if risk_trend.empty:
            st.warning("Monthly risk trend is unavailable.")
        else:
            st.plotly_chart(px.line(risk_trend, x="month", y="open_risks", markers=True, title="Monthly Open Risk Trend"), use_container_width=True)
    with right:
        coverage_trend = pd.DataFrame(metrics.get("monthly_control_coverage_trend", []))
        if coverage_trend.empty:
            st.warning("Monthly control coverage trend is unavailable.")
        else:
            st.plotly_chart(px.line(coverage_trend, x="month", y="implemented_percent", markers=True, title="Monthly Control Coverage Trend"), use_container_width=True)
    st.write(
        "These trends connect security operations and risk management with executive reporting by showing whether "
        "control implementation is increasing while open risk is being reduced over time."
    )


def program_context_section(markdown_context: str) -> None:
    st.header("Program Context")
    st.write(
        "This dashboard supports internal security program governance by aligning NIST CSF maturity, control "
        "ownership, and risk-based prioritization in one reporting view. It helps teams maintain evidence readiness, "
        "monitor operational resilience, and brief executives using consistent program metrics."
    )
    with st.expander("Optional executive dashboard notes", expanded=False):
        if markdown_context:
            st.markdown(markdown_context)
        else:
            st.caption("Optional dashboard/executive_dashboard.md file was not found; the live dashboard remains available.")


def main() -> None:
    st.title(APP_TITLE)
    st.subheader(APP_SUBTITLE)

    try:
        metrics = load_metrics()
        controls = load_csv(CONTROL_PATH, REQUIRED_CONTROL_COLUMNS)
        risks = load_csv(RISK_PATH, REQUIRED_RISK_COLUMNS)
        markdown_context = load_optional_markdown()
    except DataLoadError as exc:
        st.error(str(exc))
        st.stop()

    executive_overview(metrics, controls, risks)
    st.divider()
    maturity_section(metrics)
    st.divider()
    control_coverage_section(controls)
    st.divider()
    risk_register_section(risks)
    st.divider()
    trends_section(metrics)
    st.divider()
    program_context_section(markdown_context)


if __name__ == "__main__":
    main()
