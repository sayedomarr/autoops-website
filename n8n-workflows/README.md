Instructions to import the workflow skeleton into n8n:
1. Open n8n UI (http://localhost:5678).
2. Go to Workflows -> Import -> Paste JSON from `autoops-workflow.json`.
3. Edit credentials: Slack webhook, HTTP request URL (backend), and ensure Webhook node path matches ingress.
4. For production, configure Approval step on Slack before Execute Remediation node runs.


