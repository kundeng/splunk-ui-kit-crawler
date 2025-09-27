---
lib: crawlee-python
version: unknown
topic: basic usage
source:
  - https://crawlee.dev/python/docs/quick-start
  - https://crawlee.dev/python/docs/examples/playwright-crawler
  - https://crawlee.dev/python/docs/introduction/adding-more-urls
  - https://crawlee.dev/python/docs/guides/storages
 cached_at: 2025-09-25T02:32:33-04:00
---

Minimal basics for Crawlee (Python) from crawlee.dev:

```bash
python -m pip install 'crawlee[all]'
playwright install
```

```python
# Minimal Playwright crawler with default handler and dataset writes
import asyncio
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext

async def main() -> None:
    crawler = PlaywrightCrawler(max_requests_per_crawl=10, headless=True, browser_type='chromium')

    @crawler.router.default_handler
    async def handle(context: PlaywrightCrawlingContext) -> None:
        await context.page.wait_for_selector('main')
        title = await context.page.title()
        await context.push_data({'url': context.request.url, 'title': title})
        # Discover more links in-scope
        await context.enqueue_links(strategy='same-domain')

    await crawler.run(['https://example.com'])

if __name__ == '__main__':
    asyncio.run(main())
```

```python
# Dataset basics (open, push)
from crawlee.storages import Dataset

async def save_record(record: dict) -> None:
    ds = await Dataset.open(name='splunk-ui')
    await ds.push_data(record)
```

Notes:
- Most Crawlee Python APIs are async; use `asyncio.run(...)` in scripts.
- Use `context.enqueue_links(...)` with strategy/filters to constrain scope (e.g., same-domain).
- Default dataset is persisted under `./storage/datasets/default/`; named datasets can segment outputs.
