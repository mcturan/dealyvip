# Cloudflare Pages Deployment Architecture

## Repository Links
- **GitHub Repository:** https://github.com/mcturan/dealyvip
- **Production Branch:** `main`

## Build Settings
- **Framework Preset:** Astro
- **Build Command:** `npm run build`
- **Build Output Directory:** `dist`
- **Node.js Version:** `20.x` or higher (Set `NODE_VERSION` environment variable if needed).

## Environment Variables
- `SITE_URL`: Should strictly match the production domain. Leave undefined for preview branches.

## Preview Deployments
- Cloudflare Pages natively intercepts PRs or pushes to non-main branches and deploys them to `*.pages.dev` domains.
- Since `SITE_URL` is omitted in previews, SEO metadata is safely disabled, preventing preview indexing.

## Rollback & Custom Domains
- **Rollback:** Performable instantly via Cloudflare Pages dashboard by selecting a previous build.
- **Custom Domains:** Can be mapped through Cloudflare Dashboard -> Pages -> Custom Domains once the domain is purchased and DNS is active on Cloudflare.
- **HTTPS:** Managed entirely and automatically by Cloudflare.
