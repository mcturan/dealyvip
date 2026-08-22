# Product Quality Backlog

| ID | Severity | Area | Description | Evidence | Recommended Action | Status |
|---|---|---|---|---|---|---|
| BKL-001 | IMPROVEMENT | Mobile UI | Mobile menu animation is abrupt | `SiteHeader.astro` uses simple CSS display toggle | Add CSS transition for mobile menu sliding | DEFERRED |
| BKL-002 | IMPROVEMENT | Performance | Asset optimization for future images | Currently no large images, but as country flags/assets are added they should be optimized | Configure Astro image integration | DEFERRED |
| BKL-003 | IMPROVEMENT | I18n | Hardcoded English string in Mobile menu toggle label | `SiteHeader.astro` line 12 `aria-label="Toggle Navigation"` is not translated | Add `lang` based dictionary lookup for aria labels | DEFERRED |
