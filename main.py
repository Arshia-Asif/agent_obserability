from agent.investigator import TelemetryAgent


def main() -> None:
    agent = TelemetryAgent()
    result = agent.investigate(
        incident="API latency increased after the latest deploy"
    )
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
