# Implementation Foundation

## Purpose
Documents the successful initialization of the DealyVIP Astro beta website structure, explicitly tracking dependencies, routing, and component architecture.

## Project Structure
- Astro successfully scaffolded within the root directory `/home/turan/Projects/dealyvip`.
- Legacy `.md` documentation files were strictly preserved.
- `src/components/`: Stores highly reusable UI blocks.
- `src/layouts/`: Contains `BaseLayout.astro` providing global structure, CSS, and metadata.
- `src/pages/`: Contains the language roots (`/en/`, `/tr/`, `/uk/`, `/ru/`) and static pages.
- `src/content/`: Initialized the `guides` Content Collection schema and folder structure.

## Dependencies
- `astro@^4.14.0`: The core static site generator.
- `@astrojs/check`: Type-checking utility for `.astro` files.
- `typescript`: For native type support.
- *No heavy CSS frameworks (like Tailwind) or SPA frameworks (like React) were installed, preserving a zero-JS footprint.*

## Local Commands
- `npm run dev`: Starts the local Astro development server.
- `npm run build`: Generates the production static HTML/CSS in `dist/`.
- `npm run preview`: Locally serves the static output for final verification.

## Implemented Routes
- `/`: Automatically redirects to `/en/`.
- `/en/`: Structural English homepage featuring Hero, Guide cards, Country cards, and CTA.
- `/tr/`, `/uk/`, `/ru/`: Structural localized homepages.
- `/en/contact/`: Structural placeholder for the contact page emphasizing required user inputs.

## Implemented Components
- `MetaHead.astro`: Handles title, description, and canonical routing.
- `SiteHeader.astro`: Contains logo and desktop navigation.
- `SiteFooter.astro`: Contains multi-column standard links.
- `LanguageSwitcher.astro`: Mocked UI for switching site languages based on actual availability.
- `Breadcrumbs.astro`: Reusable trail navigation.
- `CTASection.astro`: Standardized prompt guiding users to contact.
- `CountryCard.astro` / `GuideCard.astro`: Reusable content displays.

## Content Collection Model
- Defined via `src/content/config.ts`.
- Structured with Zod schema (`language`, `country`, `topic`, `priority`, `related_lang_id`) to ensure content consistency.
- One structural placeholder guide created at `src/content/guides/en/pre-payment-checklist.md`.

## Known Limitations
- The language switcher is currently a mocked list. It must eventually check active route availability dynamically to avoid generating 404s.
- The `SiteHeader` desktop navigation requires refinement on mobile viewports.
- The Contact page contains no functional submission backend yet (no form endpoints configured).

## Next Implementation Steps
- Style the mobile navigation (hamburger menu).
- Create dynamic routing for the `guides/` content collection (`src/pages/[lang]/guides/[...slug].astro`).
- Refine the global CSS variables and typography based on the final visual brand.
- Implement a serverless form endpoint for the Contact page.

## Status
Confirmed.
