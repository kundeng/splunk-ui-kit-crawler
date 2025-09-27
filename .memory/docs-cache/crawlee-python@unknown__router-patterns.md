---
lib: crawlee-python
version: unknown
topic: router patterns
source:
  - https://github.com/apify/crawlee-python/blob/master/docs/guides/request_router.mdx#_snippet_0
  - https://github.com/apify/crawlee-python/blob/master/docs/introduction/08_refactoring.mdx#_snippet_1
cached_at: 2025-09-25T02:29:57-04:00
---

Route handlers to separate concerns (components, patterns, guides):

```python
# src/routes.py
from crawlee.router import Router

router = Router()

@router.add('components')
async def handle_component(context):
    page = context.page
    await page.wait_for_selector('main')
    title = await page.title()
    await context.push_data({'type': 'component', 'url': context.request.url, 'title': title})

@router.add('patterns')
async def handle_pattern(context):
    page = context.page
    await page.wait_for_selector('main')
    h1 = await page.locator('h1').text_content()
    await context.push_data({'type': 'pattern', 'url': context.request.url, 'title': h1})

@router.add('guides')
async def handle_guide(context):
    page = context.page
    await page.wait_for_selector('article, main')
    h1 = await page.locator('h1').text_content()
    await context.push_data({'type': 'guide', 'url': context.request.url, 'title': h1})
```

Minimal main using the router:

```python
# src/main.py
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler
from src.routes import router

async def main():
    crawler = PlaywrightCrawler(router=router)
    await crawler.run(['https://example.com/splunk-ui-docs'])

if __name__ == '__main__':
    asyncio.run(main())
```

Notes:
- Use labels or URL matching in `router.add(...)` to map to specific handlers.
- Handlers can enqueue more links and push data to datasets.
