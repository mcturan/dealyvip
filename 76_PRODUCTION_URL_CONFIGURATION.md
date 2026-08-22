# Production URL Configuration

## Core Requirement
The final production domain for DealyVIP is not yet selected. We must not hardcode an invented domain into the repository.

## Configuration Strategy
The Astro configuration (`astro.config.mjs`) reads the `SITE_URL` environment variable.

- **Local Development:** Defaults to `http://localhost:3000`.
- **Production Deployment:** The static hosting provider (e.g., Cloudflare Pages, Netlify) must be configured with an environment variable:
  `SITE_URL=https://www.actualdomain.com`

## Affected Behaviors
- **Sitemap:** The `@astrojs/sitemap` integration automatically prefixes generated routes with the configured `site`. If `SITE_URL` is omitted in production, it will improperly generate `localhost` URLs.
- **Canonical URLs:** `Astro.site` is used in layout headers to build absolute canonical links.
- **Open Graph URLs:** Social sharing protocols strictly require absolute URLs to resolve correctly.

This approach guarantees zero domain-hardcoding while preserving full SEO capability once the domain is known.
