# System Patterns (ADRs)

## ADR-YYYYMMDD-<short-name>
### Context
### Decision
### Alternatives
### Consequences
### Status (Proposed|Accepted|Superseded)
### Links (PRs, Issues, Docs)

## ADR-20250925-crawlee-python-adoption
### Context
We need to crawl the Splunk UI Kit site which contains dynamic, client-side rendered elements. The crawler must render JavaScript, manage a queue for deep link discovery, and persist results for reproducible runs.

### Decision
Adopt Crawlee (Python) with Playwright for browser automation. Use `FileSystemStorageClient` for local persistence (datasets, request queue, key-value store). Normalize extracted pages into Markdown with frontmatter.

### Alternatives
- Scrapy + Playwright: powerful but requires custom integration for rich browser automation
- Node Crawlee: mature, but we prefer Python for local tooling consistency
- Crawl4AI: optimized for AI-ready markdown, but we want lower-level control over crawl logic

### Consequences
- Async Python runtime required (Playwright-managed by Crawlee)
- Local storage directory will grow with runs; add cleanup/rotation later
- Clear separation of concerns: discovery (RequestQueue), rendering (Playwright), extraction (DOM parsing), formatting (Markdown)

### Status (Proposed|Accepted|Superseded)
Accepted

### Links (PRs, Issues, Docs)
- Docs cache: `.memory/docs-cache/crawlee-python@unknown__basic-usage.md`
