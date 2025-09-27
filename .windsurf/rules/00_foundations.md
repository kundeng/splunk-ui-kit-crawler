---
trigger: always_on
---

# Foundations (Activation: Always On)
1) Project scope = this workspace. Never import or reference memories from other repos.
2) On session start: READ all `.memory/*.md` in this order:
   projectBrief → techContext → systemPatterns → activeContext → progress → glossary.
3) When retrieving context for answers: prefer `.memory` files first, then Windsurf Memories panel entries.
4) If a section is missing: create it with the standard header from the file schemas.
5) Do not overwrite headers; append under the correct section; preserve newest-on-top ordering where specified.
