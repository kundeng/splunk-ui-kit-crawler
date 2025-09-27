---
lib: crawlee-python
version: unknown
topic: enqueue links
source:
  - https://github.com/apify/crawlee-python/blob/master/docs/introduction/03_adding_more_urls.mdx#_snippet_1
  - https://github.com/apify/crawlee-python/blob/master/docs/examples/crawl_website_with_relative_links.mdx#_snippet_1
cached_at: 2025-09-25T02:29:57-04:00
---

Enqueue links within a Playwright page handler:

```python
from crawlee.playwright_crawler import PlaywrightCrawler
from crawlee.enqueue_links import enqueue_links

async def handle_page(context):
    # Limit to same-domain and only docs paths for Splunk UI Kit
    await enqueue_links({
        'crawler': context.crawler,
        'request_queue': context.request_queue,
        'strategy': 'same-domain',
        'include': [r'^/components/.*', r'^/patterns/.*', r'^/guides/.*'],
        'selector': 'a[href]'
    })
```

Notes:
- Use `strategy: 'same-domain'` to avoid crawling the whole web.
- Use `include`/`exclude` regexes to constrain crawl scope to docs paths.
