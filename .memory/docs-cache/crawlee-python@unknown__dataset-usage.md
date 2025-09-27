---
lib: crawlee-python
version: unknown
topic: dataset usage
source:
  - https://github.com/apify/crawlee-python/blob/master/docs/guides/storages.mdx#_snippet_5
  - https://github.com/apify/crawlee-python/blob/master/docs/examples/add_data_to_dataset.mdx#_snippet_1
cached_at: 2025-09-25T02:29:57-04:00
---

Dataset basics within a Playwright handler:

```python
from crawlee import Dataset

async def handle_page(context):
    # Extract content and push to default dataset
    data = {
        'url': context.request.url,
        'title': await context.page.title(),
        'html': await context.page.content(),
    }
    await Dataset.push_data(data)
```

Manual dataset for custom grouping:

```python
from crawlee import Dataset

async def save_component(component):
    async with await Dataset.open('splunk-ui-components') as ds:
        await ds.push_data(component)
```

Notes:
- Default dataset location: ./storage/datasets/default/
- Use named datasets to segment outputs (e.g., components, guides).
