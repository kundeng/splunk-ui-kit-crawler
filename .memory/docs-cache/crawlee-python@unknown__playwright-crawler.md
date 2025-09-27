---
lib: crawlee-python
version: unknown
topic: playwright crawler
source:
  - https://github.com/apify/crawlee-python/blob/master/docs/examples/playwright_crawler.mdx#_snippet_0
  - https://github.com/apify/crawlee-python/blob/master/docs/guides/playwright_crawler_adaptive.mdx#_snippet_1
cached_at: 2025-09-25T02:29:57-04:00
---

Minimal PlaywrightCrawler usage (Python):

```python
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler

async def handle_page(context):
    page = context.page
    # Wait for main content to render (adjust selector for Splunk UI Kit)
    await page.wait_for_selector('main')
    title = await page.title()
    # Push data to dataset via context helper
    await context.push_data({
        'url': context.request.url,
        'title': title,
    })

async def main():
    crawler = PlaywrightCrawler(request_handler=handle_page)
    await crawler.run([
        'https://example.com'
    ])

if __name__ == '__main__':
    asyncio.run(main())
```

Notes:
- Use `await page.wait_for_selector(...)` for dynamic elements.
- Prefer narrow timeouts and retries for flaky components.
