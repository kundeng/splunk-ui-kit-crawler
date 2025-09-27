---
trigger: always_on
---

# External Documentation Cache (Activation: Model Decision)
1) Before browsing or querying external docs: CHECK `.memory/docs-cache/` for an existing file.
2) If not present OR older than 30 days OR the version differs:
   a) Fetch the authoritative doc page (official site or repo README).
   b) Extract ONLY the minimal snippet/signature/example needed.
   c) SAVE to `.memory/docs-cache/<lib>@<version>__<topic>.md` with frontmatter.
3) When answering API/usage questions: CITE the cached snippet rather than re-fetching.
4) If confidence < 0.8 or the snippet conflicts with current code: REFRESH cache, then answer.
