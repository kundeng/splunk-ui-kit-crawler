# Technology Context
## Languages & Frameworks (with versions)
<!-- e.g., Python 3.11, Next.js 14.2.4, Tailwind 3.4 -->
- Python (>=3.10) managed via uv
- Crawlee (Python) — web crawling & browser automation
- Playwright (via Crawlee) — headless browser for dynamic content rendering

## Services/Endpoints
<!-- Internal/external services this project depends on -->
- Splunk UI Kit documentation site (public web)

## Data Stores
<!-- DBs, caches, queues; include schemas/links -->
- Local file system storage (Crawlee FileSystemStorageClient) for:
  - Datasets (extracted page records)
  - RequestQueue (crawl state)
  - KeyValueStore (run metadata, config)

## Build/Deploy Tooling
<!-- CI/CD, IaC (Terraform), containerization, runners -->
- Local runs via CLI (Python)
- Optional: GitHub Actions for scheduled crawls (future)

## Local Dev
<!-- How to run locally; env vars (without secrets) -->
- Use `uv` for Python project management and dependency installation
- Initialize project: `uv init` and `uv add crawlee[all]`
- Install Playwright browsers: `uv run playwright install`
- Run crawler: `uv run python src/main.py`

## Compatibility/Constraints
<!-- OS, browsers, perf/SLOs, compliance -->
- macOS development environment
- Respect robots.txt and site rate limits; add delays/retries as needed
