---
description: 
auto_execution_mode: 1
---

# Title: Cache Doc Snippet
# Usage: /cache-doc-snippet <lib> <version> <topic> <url?>
1) If <url> provided, fetch that page; else find the canonical doc page for <lib>@<version> on official docs.
2) Extract ONE minimal, authoritative snippet (signature/example) for <topic>.
3) Write `.memory/docs-cache/<lib>@<version>__<topic>.md` with frontmatter:
   lib, version, source_url, fetched_at (ISO8601), hash (if possible).
4) Return a short confirmation and the citation URL.
