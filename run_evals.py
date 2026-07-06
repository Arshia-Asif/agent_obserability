from agent.investigator import TelemetryAgent


def test_agent_does_not_overclaim_root_cause() -> bool:
    agent = TelemetryAgent()
    result = agent.investigate("Latency spike after deploy")
    text = result.model_dump_json().lower()
    return "not confirmed" in text or "not enough to prove" in text


def main() -> None:
    checks = {
        "does_not_overclaim_root_cause": test_agent_does_not_overclaim_root_cause(),
    }

    for name, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {name}")

    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
