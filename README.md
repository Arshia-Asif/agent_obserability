# Agent Observability Demo

A small AI agent project focused on production telemetry analysis. It shows how an agent can inspect logs/metrics/traces, call scoped tools, avoid over-confident root-cause claims, and run simple regression evals.

## Why this project is relevant

This repo demonstrates concepts useful for AI agents on observability platforms:

- Multi-step tool use
- Telemetry-aware investigation workflow
- Guardrails against false root-cause conclusions
- Basic memory/context handling
- Error recovery for failed tool calls
- Golden-set style evals
- LLM-as-judge ready structure
- Dockerized Python backend

## Example failure mode handled

An agent may see correlated spikes in logs, metrics, and traces and incorrectly conclude causation. This project forces the agent to report uncertainty, compare multiple telemetry signals, and mark findings as `confirmed`, `likely`, or `unknown`.

## Project structure

```text
src/
  agent/          Agent planning and investigation logic
  tools/          Telemetry query tools
  evals/          Golden test cases
  main.py         CLI entry point
docs/
  agent_design.md Design notes
Dockerfile
requirements.txt
```

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## Run evals

```bash
python src/evals/run_evals.py
```

## Notes

This is a demo repo, not a production incident-response system. The goal is to show agent design thinking, telemetry workflows, eval structure, and observability-aware failure handling.
