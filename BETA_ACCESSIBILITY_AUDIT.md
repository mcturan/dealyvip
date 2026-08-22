# Beta Accessibility Audit

## Findings
- Previously, duplicate `nav` elements in `SiteFooter.astro` raised an ARIA `landmark-unique` warning.
- Fix: Assigned explicit `aria-label="Footer Navigation"` and `aria-label="Footer Legal Navigation"` to differentiate from the primary and breadcrumb navigation landmarks.
- Result: Accessibility warnings neutralized for standard landmarks.

## Semantic HTML
- All headings maintain logical order (H1 -> H2 -> H3).
- No unnecessary ARIA attributes have been injected.
