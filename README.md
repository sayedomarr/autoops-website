# AutoOps — Self-Healing Infrastructure (demo repo)

Short: AI-driven automation that analyzes logs and remediates infra incidents automatically (demo).

## Contents
- `docs/` : static explanatory site (index.html) with Lottie animation (no live backend)
- `backend/` : FastAPI demo app with analyzer module (OpenAI integration fallback)
- `n8n-workflows/` : exported n8n workflow skeleton (Webhook → Analyzer → Action)
- `docker-compose.yml` : run `backend` + `n8n` locally
- `.github/workflows/deploy-pages.yml` : CI to publish `docs/` to GitHub Pages

## Quick start (dev)
1. Copy `.env.example` to `.env` and set `OPENAI_API_KEY` (optional).
2. Build & run:
   ```bash
   docker-compose up --build
   ```

3. Open:

   * Frontend (static): `docs/index.html` (or use GitHub Pages)
   * Backend API: [http://localhost:8000/api/health](http://localhost:8000/api/health)
4. This site explains the concept only; no live calls are required. If you want to run the backend demo, use Docker Compose and test endpoints via curl.

## Live repository

This repo is hosted on GitHub: [`sayedomarr/autoops-website`](https://github.com/sayedomarr/autoops-website)

If you enable GitHub Pages (Actions → gh-pages workflow), the `docs/` site will be served automatically.

## Project structure

```text
autoops-website/
├─ .github/workflows/
│  └─ deploy-pages.yml              # Publish docs/ to GitHub Pages
├─ backend/
│  ├─ app/
│  │  ├─ __init__.py
│  │  ├─ analyzer.py                # OpenAI + rule-based analyzer
│  │  └─ main.py                    # FastAPI endpoints
│  ├─ tests/
│  │  └─ test_analyzer.py
│  ├─ Dockerfile
│  └─ requirements.txt
├─ docs/
│  ├─ assets/
│  │  ├─ README.md                  # Lottie instructions
│  │  └─ screenshots/               # Place your screenshots here
│  ├─ css/
│  │  └─ styles.css                 # Modern styles + dark mode
│  ├─ .nojekyll                     # Ensure assets served as-is
│  └─ index.html                    # Explanatory landing page (no backend)
├─ n8n-workflows/
│  ├─ README.md
│  └─ autoops-workflow.json         # n8n skeleton (Webhook → Analyze → Act)
├─ docker-compose.yml               # Backend + n8n for local demo
├─ env.example                      # Sample environment
├─ .env                             # Local env (do not commit secrets)
├─ LICENSE                          # MIT
└─ README.md
```

## Screenshots

Add your screenshots in `docs/assets/screenshots/` and reference them here:

![Landing](docs/assets/screenshots/landing.png)
![Health Endpoint](docs/assets/screenshots/health.png)
![Concept Workflow](docs/assets/screenshots/workflow.png)

## Safety & Production notes

* The demo runs in **SAFE MODE** by default (`AUTOOPS_SAFE_MODE=true`), which prevents destructive infra actions.
* Replace analyzer fallback with a managed LLM + vector DB for production.
* Secure `OPENAI_API_KEY`, Slack webhook, Jira tokens via GitHub Secrets for CI.

## Structure & files

(see repo root)

## Screenshots

Place screenshots under `docs/assets/screenshots/` and reference them here, for example:

![Landing](docs/assets/screenshots/landing.png)
![Health Endpoint](docs/assets/screenshots/health.png)
![Simulate Alert](docs/assets/screenshots/simulate-alert.png)

## License

MIT


