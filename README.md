# Splunk UI Kit Documentation Crawler

A Python crawler built with Crawlee that extracts documentation from the Splunk UI Kit website (splunkui.splunk.com) and converts it to well-formatted Markdown files.

## Features

- **SPA-Aware Crawling**: Uses Playwright to render JavaScript-heavy single-page applications
- **Intelligent Content Extraction**: Extracts headings, content, code blocks, and metadata
- **Markdown Export**: Generates clean Markdown files with YAML frontmatter
- **Respectful Crawling**: Implements delays and rate limiting to be respectful to the target site
- **Structured Output**: Organizes extracted documentation by package, section, and component

## Project Structure

```
├── src/
│   ├── main.py              # Main crawler entry point
│   ├── routes.py            # Route handlers for different page types
│   ├── markdown_exporter.py # Markdown generation and export
│   └── __init__.py
├── docs/                    # Generated Markdown documentation (output)
├── .memory/                 # Project memory and documentation cache
├── pyproject.toml          # uv project configuration
└── README.md
```

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for Python dependency management.

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Install Playwright browsers**:
   ```bash
   uv run playwright install
   ```

## Usage

Run the crawler:

```bash
uv run python src/main.py
```

The crawler will:
1. Start from the Splunk UI Kit packages index
2. Discover and crawl documentation pages
3. Extract content and code examples
4. Generate Markdown files in the `docs/` directory

## Configuration

Key settings in `src/main.py`:

- `max_requests_per_crawl`: Limit total requests (set to 50 for testing)
- `headless`: Run browser in headless mode (True for production)
- `browser_type`: Browser engine to use ('chromium' recommended)

## Output

Generated Markdown files include:

- **Frontmatter**: YAML metadata with title, URL, type, package info, tags
- **Content**: Extracted and formatted page content
- **Code Examples**: Syntax-highlighted code blocks

Example output structure:
```markdown
---
title: Button Component
url: https://splunkui.splunk.com/Packages/react-ui/Button
type: component
package: react-ui
component: Button
tags: [react-ui, component]
crawled_at: 2025-09-25T02:46:39-04:00
---

## Button Component

[Extracted content...]

## Code Examples

### Example 1

```javascript
import { Button } from '@splunk/react-ui';
```
```

## Development

The project follows the memory-driven development pattern with documentation in `.memory/`:

- `projectBrief.md`: Project objectives and scope
- `techContext.md`: Technology stack and setup
- `systemPatterns.md`: Architecture decisions (ADRs)
- `activeContext.md`: Current focus and next steps
- `progress.md`: Development progress log
- `docs-cache/`: Cached external documentation snippets

## Architecture

Built using:
- **Crawlee (Python)**: Web crawling framework with Playwright integration
- **Playwright**: Headless browser for SPA content rendering
- **uv**: Modern Python package management
- **YAML + Markdown**: Structured documentation output

See `.memory/systemPatterns.md` for detailed architecture decisions.
