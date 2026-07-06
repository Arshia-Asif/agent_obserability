def query_metrics(service: str) -> str:
    return f"{service}: p95 latency increased from 220ms to 950ms after deploy window. Error rate stayed mostly flat."


def query_logs(service: str) -> str:
    return f"{service}: repeated timeout warnings from payment dependency, but no widespread application errors."


def query_traces(service: str) -> str:
    return f"{service}: slow traces show time spent waiting on downstream payment service."
