# backend/app/main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .analyzer import analyze_log

app = FastAPI(title="AutoOps Demo Backend")

class AnalyzeRequest(BaseModel):
    log: str
    context: dict = {}

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/simulate-alert")
async def simulate_alert():
    """
    Returns a sample log, analysis, and a proposed action.
    This endpoint simulates what Prometheus -> n8n -> backend flow would look like.
    """
    sample_log = (
        "2025-10-08T12:34:56Z ERROR backend-service: panic: runtime: out of memory\n"
        "container killed with OOMKilled\n"
        "Stacktrace: ...\n"
    )
    analysis = analyze_log(sample_log)
    # Decide naive action for demo
    action = "restart_pod" if "oom" in analysis.lower() or "out of memory" in analysis.lower() else "open_ticket"
    # Respect SAFE MODE: real infra actions are NOT executed here
    return {"log": sample_log, "analysis": analysis, "action": action}

@app.post("/api/analyze")
async def analyze(req: AnalyzeRequest):
    if not req.log:
        raise HTTPException(status_code=400, detail="log is required")
    analysis = analyze_log(req.log, context=req.context)
    return {"log": req.log, "analysis": analysis}


