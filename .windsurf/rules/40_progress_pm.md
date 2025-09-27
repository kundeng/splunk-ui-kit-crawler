---
trigger: always_on
---

# Progress & PM Signals (Activation: Always On)
1) For each task completion: append a progress.md entry (timestamped; newest first).
2) Include: Summary, Files Touched, Tests/CI result, PR/Commit link, TODO/NEXT.
3) If blockers arise: add to activeContext.md → Open Questions or Risks.
4) Weekly (Fri 16:00 local): run `/snapshot-state` to condense progress into activeContext.md.
