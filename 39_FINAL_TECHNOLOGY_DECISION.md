# Final Technology Decision

## Purpose
Establishes the definitive technical contract for the DealyVIP beta implementation. This removes all ambiguity regarding tooling, frameworks, and architecture.

## 1. Final Selected Technology
The beta website will be built exclusively using **Astro**.

## 2. Why Astro was Selected
- **Static-First & Zero-JS Default:** Produces minimal, semantic HTML by default, ensuring extremely fast page loads and excellent AI/search engine discoverability.
- **Content-Driven:** Native, first-class support for Markdown and MDX content collections.
- **Performance:** Component island architecture allows for interactive elements *only* where necessary, avoiding full-page client-side hydration.
- **Multilingual Support:** Native routing capabilities for structured internationalization.
- **Local Linux Development:** Standard Node.js tooling makes local development and previewing seamless.

## 3. Rejected Alternatives
- **Hugo / 11ty:** Rejected. While excellent for static sites, Astro provides a more robust, component-based developer experience and easier future transition if isolated interactive features are ever required.
- **React / Next.js / Nuxt (SPA):** Explicitly rejected. DealyVIP is an informational site; single-page application (SPA) architectures introduce unnecessary JavaScript weight, hydration delays, and complexity.
- **WordPress / Statamic (Traditional CMS):** Explicitly rejected. Introduces database overhead, security vulnerabilities, and PHP hosting requirements.

## 4. Planned Project Structure
The implementation must follow a clean Astro structure:
```
src/
  ├── components/   # Reusable UI elements (Header, Footer, CTA)
  ├── content/      # Markdown/MDX files (The actual content)
  ├── layouts/      # Base HTML structures (GuideLayout, CountryLayout)
  ├── pages/        # File-based routing logic
  └── styles/       # Native CSS
```

## 5. Content Organization
Content will be managed via Astro Content Collections.
The directory structure will support parallel language content without forcing strict 1:1 symmetry.
```
src/content/
  ├── guides/
  │   ├── en/
  │   │   ├── verify-company-turkiye.md
  │   │   └── supplier-prepayment-checklist.md
  │   ├── tr/
  │   │   └── turkiye-sirket-dogrulama.md
  │   ├── uk/
  │   └── ru/
```
Content items covering the same topic will use explicit frontmatter tags (e.g., `related_lang_id: verify-company-turkiye`) to associate them semantically, rather than relying on exact mirrored filenames.

## 6. Language Routing Strategy
- **Base Architecture:** Subdirectory routing (`/en/`, `/tr/`, `/uk/`, `/ru/`).
- **Controlled Multilingualism:** Pages may exist independently in one language. If a page exists in a language, serve that page. If a page does not exist in that language, do not silently redirect or automatically render another language version. Alternative language versions may be shown through explicit language links where they exist.

## 7. Component Philosophy
- Keep components structural and semantic.
- Build dedicated components for recurring structural needs (e.g., `<AvailabilityWarning />`, `<DirectAnswer />`).

## 8. CSS Philosophy
- Prefer **Native CSS** (CSS Modules or global CSS).
- Do not install heavy UI frameworks (e.g., Bootstrap, MUI) unless strictly justified. Tailwind CSS is permissible *only* if the implementer prefers utility classes, but native CSS is strongly preferred for maintainability and minimal footprint.

## 9. Local Development Workflow
- **Package Manager:** `npm`, `pnpm`, or `yarn`.
- **Development Command:** `npm run dev` (Starts local dev server).
- **Preview Command:** `npm run preview` (Locally previews the static build output).

## 10. Build Workflow
- **Build Command:** `npm run build` (Generates fully static HTML/CSS/assets into the `dist/` folder).

## 11. Deployment Compatibility
The `dist/` output must be 100% compatible with static edge hosting:
- Cloudflare Pages
- Netlify
- GitHub Pages

No server-side rendering (SSR) adapter should be used.

## 12. Explicitly Rejected Complexity
- **No Databases:** Content lives entirely in Git as Markdown.
- **No Authentication:** No user accounts or login systems.
- **No API Backend:** Data is built statically at compile time.
- **No React:** Do not install React unless an isolated component genuinely requires client-side state in the future (not applicable for beta).

## 13. Future Expansion Boundaries
If dynamic features (e.g., complex contact routing) are needed later, they will be handled via serverless functions or lightweight static form endpoints (e.g., Formspree), keeping the core site strictly static.

## Status
Confirmed.
