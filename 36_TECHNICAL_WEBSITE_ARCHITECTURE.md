# Technical Website Architecture

## Purpose
Recommend an implementation architecture that prioritizes simplicity, maintainability, SEO, and performance, while explicitly rejecting unnecessary overengineering.

## Recommended Architecture: Static Site Generator (SSG)
A file-based SSG is the optimal choice for a highly informational, multilingual website without user accounts.

- **Technology:** Astro, Hugo, or Eleventy (11ty).
- **Why:** 
  - Produces clean, zero-JS (or minimal JS) static HTML.
  - Native support for Markdown content authoring.
  - Excellent for i18n (multilingual) directory structures (e.g., `/en/`, `/tr/`).
  - Easy to run locally on a Linux PC (`npm run dev` or `hugo server`).
- **Content Storage:** Git repository (Markdown files). No external database required.
- **Deployment Model:** Edge CDN (e.g., Cloudflare Pages, Netlify, Vercel, or standard Nginx/Apache on a VPS).
- **Contact Handling:** Serverless form handler (e.g., Formspree, Netlify Forms) or a lightweight worker script to send emails.
- **Analytics:** Privacy-first analytics (e.g., Plausible, Fathom) or standard server log analysis.

## Alternative 1: Lightweight Flat-File CMS
- **Technology:** Statamic or Grav.
- **Why:** Provides a visual admin interface for non-technical writers while keeping data in flat files (no database).

## Alternative 2: Traditional CMS
- **Technology:** WordPress.
- **Why:** Universal familiarity.
- **Tradeoffs:** Requires a MySQL database, PHP hosting, and rigorous security maintenance. Overkill for a strictly informational site, but acceptable if the team requires specific CMS plugins.

## Explicitly Rejected
- **React/Next.js/Nuxt as SPAs:** Unnecessary client-side complexity for static content.
- **Microservices:** No backend APIs needed.
- **Databases:** Content lives in Git.
- **Authentication:** No user accounts.

## Status
Confirmed.
