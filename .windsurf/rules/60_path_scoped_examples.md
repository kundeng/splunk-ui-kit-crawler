---
trigger: always_on
---

# Path-Scoped Behavior (Activation: Glob)
# Apply only when editing files under the matched paths.
## Glob: src/**/*
- After non-trivial edits under src/, propose updating progress.md and activeContext.md.

## Glob: tests/**/*
- Ensure tests reflect the latest ADRs and techContext versions; if diverging, open an issue in progress.md.

## Glob: docs/**/*
- When referencing external material, add/refresh an entry in docs-cache and link it from the edited doc.
