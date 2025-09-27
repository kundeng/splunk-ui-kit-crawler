# Project Brief
## Objective
<!-- What are we building and why (business value)? -->
Build a reliable crawler using Crawlee (Python) to extract component and pattern documentation from the Splunk UI Kit website into well-formatted Markdown files. This enables offline search, versioned docs, and downstream processing (e.g., embedding for RAG), overcoming client-side rendering and dynamic UI challenges.

## Scope
<!-- In-scope and out-of-scope boundaries -->
In-scope
- Discover and crawl all public docs pages of Splunk UI Kit (components, patterns, guides).
- Handle client-side rendered content and interactive elements (tabs, accordions, code examples) via headful/headless browser automation.
- Normalize output into clean Markdown (frontmatter + headings + code blocks), preserving code examples and prop tables.
- Persist crawl state and outputs locally (datasets, KV store, request queue) for repeatable runs.

Out-of-scope
- Authentication-gated content or private areas.
- Non-doc assets (videos, large binaries) beyond minimal references.
- Full site mirroring; focus is docs-to-Markdown extraction.

## Stakeholders
<!-- Names, roles, decision makers -->
- Requester: You (project owner)
- Implementation: Cascade (agentic AI), collaborating in your IDE
- Decision maker: You

## Repositories
<!-- Monorepo layout or linked repos -->
- Primary workspace: `crawlee-splunkui/`
- Output directory: `docs/` (generated Markdown), configurable via env

## Milestones
<!-- Target dates & success criteria -->
- M1: Baseline crawl (site map discovery + static content extraction) — Success: all top-level docs pages saved as Markdown
- M2: Dynamic elements handling (tabs/accordions/code blocks rendered) — Success: parity with on-page content
- M3: Structure & quality pass (frontmatter, links, anchors, code syntax) — Success: lintable, link-check passes
- M4: Automation (CLI entrypoint + documented runbook) — Success: one-command reproducible run

## Non-Goals
<!-- Explicit exclusions to reduce scope creep -->
- Building a docs site; only generating Markdown content
- Content editorial rewrites; only faithful extraction with light normalization
- API rate-limit circumvention via paid proxies (can be added later as an ADR if needed)
