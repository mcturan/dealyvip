# Homepage Implementation

## Sections Implemented (English Root)
1. **Header & Navigation:** Persistent top bar with logo, language-agnostic mobile toggle, and primary routing.
2. **Hero:** Focused, direct copy ("Cross-Border Business, Verified on the Ground"). Features clear CTAs for Assistance and Guides.
3. **Explore by Country:** Grid layout featuring Türkiye, Ukraine, Russia, and Iran with contextualized subtitles.
4. **Explore by Need:** Action-oriented grid (Verify, Supply, Visit, etc.). Links applied only where routes exist.
5. **Business Guides:** Dynamic card component featuring an example guide alongside structural placeholders for layout visualization.
6. **The DealyVIP Approach:** Core editorial trust section emphasizing transparency, limitations, and on-the-ground reality.
7. **Contact CTA:** Standardized section directing users to the contact funnel.
8. **Footer:** Comprehensive global links organized by category.

## Components Used
- `BaseLayout.astro`
- `CTASection.astro`
- `CountryCard.astro`
- `NeedCard.astro` (New)
- `GuideCard.astro`

## Copy & Content Status
- **Hero & Trust Sections:** Copy is finalized for beta. Adheres strictly to the tone guidelines (no fluff, no unsupported claims).
- **Placeholders:** Certain guides in the "Featured Guides" section are explicitly labeled in the HTML as structural placeholders.

## Responsive Behavior
- Heading typography automatically scales using `clamp()`.
- The multi-column grids (Countries, Needs, Guides) gracefully collapse to single columns on mobile devices due to CSS Grid `auto-fill`.
- Mobile navigation is fully functional.

## Known Limitations
- The homepage currently uses structural placeholders for some featured guides until Sprint 6 populates the CMS content.
- Hero section lacks a supporting abstract visual element; currently relies solely on typographic composition.
