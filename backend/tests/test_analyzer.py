# Simple pytest tests for analyzer fallback
from app.analyzer import _rule_based_analyze

def test_oom_detected():
    log = "Container OOMKilled due to out of memory"
    res = _rule_based_analyze(log)
    assert "OOM" in res or "out of memory" in res.lower()

def test_connection_refused():
    log = "Error: connection refused at 10.0.0.5:5432"
    res = _rule_based_analyze(log)
    assert "connection" in res.lower()


