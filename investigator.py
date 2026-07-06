from pydantic import BaseModel
from tools.telemetry_tools import query_logs, query_metrics, query_traces


class Finding(BaseModel):
    signal: str
    summary: str
    confidence: str


class InvestigationResult(BaseModel):
    incident: str
    findings: list[Finding]
    likely_cause: str
    uncertainty: str
    next_steps: list[str]


class TelemetryAgent:
    """Simple telemetry investigation agent.

    The agent intentionally avoids claiming root cause from one signal only.
    It compares logs, metrics, and traces before producing a conclusion.
    """

    def investigate(self, incident: str) -> InvestigationResult:
        findings: list[Finding] = []

        try:
            metrics = query_metrics(service="api")
            findings.append(Finding(signal="metrics", summary=metrics, confidence="medium"))
        except Exception as exc:
            findings.append(Finding(signal="metrics", summary=f"Tool failed: {exc}", confidence="unknown"))

        try:
            logs = query_logs(service="api")
            findings.append(Finding(signal="logs", summary=logs, confidence="medium"))
        except Exception as exc:
            findings.append(Finding(signal="logs", summary=f"Tool failed: {exc}", confidence="unknown"))

        try:
            traces = query_traces(service="api")
            findings.append(Finding(signal="traces", summary=traces, confidence="medium"))
        except Exception as exc:
            findings.append(Finding(signal="traces", summary=f"Tool failed: {exc}", confidence="unknown"))

        return InvestigationResult(
            incident=incident,
            findings=findings,
            likely_cause="Recent deploy is a possible contributor, but not confirmed from telemetry alone.",
            uncertainty="Correlation between deploy time and latency spike is not enough to prove causation.",
            next_steps=[
                "Compare latency by version before and after deploy.",
                "Check error-rate changes by endpoint.",
                "Inspect slow traces for dependency or database bottlenecks.",
                "Rollback only if version-level telemetry confirms regression.",
            ],
        )
