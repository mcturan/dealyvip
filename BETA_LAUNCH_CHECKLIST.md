# Beta Launch Checklist

## Repository
- [x] Codebase audited and cleaned
- [x] Environment files documented

## Build
- [x] Local static output verified
- [x] No `TODO`/`localhost`/fake domain leaks

## Hosting
- [ ] Cloudflare Pages project created
- [ ] Build command & output directory configured

## Domain & DNS
- [ ] Production domain finalized
- [ ] Custom domain linked in Cloudflare
- [ ] DNS verified
- [ ] HTTPS certificates active

## Environment
- [ ] `SITE_URL` set in Cloudflare Production Environment Variables

## SEO & Accessibility
- [ ] Sitemap generating correctly
- [ ] `robots.txt` allowing crawl
- [ ] Canonical URLs pointing to absolute production domain
- [ ] `hreflang` mapped correctly
- [ ] Structured data accurate
- [ ] Accessibility validated locally
- [ ] Mobile responsive layout verified

## Performance & Security
- [x] `_headers` deployed (CSP, HSTS)
- [ ] Cloudflare edge caching verified

## Contact & User Expectations
- [x] Honest expectation setting for contact workflows (Waitlists/paused state)

## Post-Launch
- [ ] Search Engine activation
- [ ] Analytics verification
- [ ] Rollback protocol acknowledged
