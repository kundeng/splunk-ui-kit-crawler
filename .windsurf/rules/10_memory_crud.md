---
trigger: always_on
---

# Memory CRUD Discipline (Activation: Always On)
1) After any meaningful change (code/docs), UPDATE:
   • progress.md (append log entry),
   • activeContext.md (refresh Current Focus / Next Steps).
2) If a new dependency or version appears: UPDATE techContext.md (exact version).
3) When a design conclusion is reached: CREATE a new ADR in systemPatterns.md (use the template).
4) New domain terms: ADD to glossary.md (Definition ≤ 2 sentences; include Source if external).
5) When chat context grows large: SUMMARIZE into activeContext.md, then continue in a new Cascade thread.
