---
trigger: always_on
---

# Hallucination & Safety (Activation: Always On)
1) Never invent APIs or parameters. If uncertain, consult docs-cache; if missing, run `/cache-doc-snippet`.
2) Prefer official docs over blogs; prefer cached snippets over raw browsing.
3) If suggested code contradicts ADRs: flag contradiction, reference ADR ID, and propose a compliant alternative.
4) Keep answers within versions listed in techContext.md; if a mismatch is detected, update techContext.md first.
5) When token pressure is high: summarize to activeContext.md and continue.
