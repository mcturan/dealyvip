# Production Environment Configuration

## SITE_URL
- **Purpose:** Defines the absolute URL for the production site. It is critical for generating correct canonical URLs, hreflang tags, Open Graph properties, and sitemap generation.
- **Where Configured:** Cloudflare Pages Environment Variables (for Production deployments).
- **Local Development Behavior:** Without `SITE_URL`, no canonicals or sitemaps are generated to prevent `localhost` leaks.
- **Preview Behavior:** Cloudflare Pages assigns a `.pages.dev` URL. If `SITE_URL` is mapped to this dynamically by CF (or left empty), it prevents the preview from impersonating production.
- **Production Behavior:** Must be set to the official verified domain (e.g., `https://example.com`) to enable full SEO functionality.
