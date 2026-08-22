# Analytics Decision Log

## Guiding Principles
- **Privacy:** Avoid collecting personal identifying information (PII) without explicit, clear consent.
- **Performance:** Maintain the 0-JS footprint where possible; avoid render-blocking tracking scripts.

## Evaluation
1. **No Analytics:** Maximum privacy, zero performance cost. Con: Blind to user engagement and traffic sources.
2. **Cloudflare Web Analytics (Recommended):** Native to the hosting platform. Privacy-first, cookie-less, no consent banner required. Negligible performance footprint.
3. **Google Analytics:** High visibility but heavy payload, privacy implications, requires cookie banner.

## Decision
- **Status:** OPEN DECISION
- **Recommendation:** Utilize **Cloudflare Web Analytics** upon domain activation. It requires no code changes (injectable via Cloudflare dashboard proxy) and preserves the strict privacy/performance baseline.
