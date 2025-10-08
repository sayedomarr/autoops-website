# backend/app/analyzer.py
import os
import logging
import openai
from typing import Optional

logging.basicConfig(level=logging.INFO)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # change per availability

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

def _rule_based_analyze(log: str) -> str:
    l = log.lower()
    if "out of memory" in l or "oom" in l or "oomkilled" in l:
        return "Detected OOMKilled / OutOfMemory. Probable causes: memory limit too low or memory leak. Suggested fix: increase memory limit, inspect allocations, restart pod."
    if "connection refused" in l or "connection error" in l:
        return "Detected Connection Refused: possible DB down, service not reachable, or network/DNS issue. Suggested fix: check DB status and network policies."
    if "panic" in l or "traceback" in l:
        return "Application panic / unhandled exception. Suggested fix: check recent deployments, app logs, unit tests."
    return "Unknown error pattern. Recommend collect full logs & metrics for deeper analysis."

def analyze_log(log: str, context: Optional[dict] = None) -> str:
    """
    Try OpenAI-based analysis first (if key present), otherwise fallback to rules.
    Returns a short human-readable diagnosis + suggested actions.
    """
    if OPENAI_API_KEY:
        try:
            prompt = (
                "You are an AI assistant specialized in DevOps incident analysis.\n"
                "Given the following log snippet, provide:\n"
                "1) short diagnosis (one line)\n"
                "2) root cause hypotheses (2-3 bullet points)\n"
                "3) suggested remediation steps (ordered, include safe-mode notes)\n\n"
                f"Log:\n```\n{log}\n```\n"
            )
            # Use ChatCompletion if available
            resp = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[{"role":"system","content":"You are a helpful DevOps analyst."},
                          {"role":"user","content": prompt}],
                max_tokens=400,
                temperature=0.0,
            )
            text = resp["choices"][0]["message"]["content"].strip()
            return text
        except Exception as e:
            logging.exception("OpenAI call failed, falling back to rule-based analyzer")
            return _rule_based_analyze(log)
    else:
        return _rule_based_analyze(log)


