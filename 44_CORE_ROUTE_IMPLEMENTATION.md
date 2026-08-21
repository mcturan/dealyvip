# Core Route Implementation

## Routes Implemented
- `/en/about/`: Detailed focus on operational limitations and clear statements about our coordination-first approach.
- `/en/countries/`: A structured hub linking only to available content without inventing fake country landing pages yet.
- `/en/guides/`: A categorized structure outlining the types of guides being produced.
- `/en/assistance/`: Describes scenarios for local support (meetings, factory visits) while strictly disclaiming any guarantee of availability.
- `/en/privacy/`: Explicitly defines the beta privacy baseline (no accounts, no payments, no forms).

## Navigation Corrections
- `SiteHeader.astro` and `SiteFooter.astro` were refactored to conditionally render links.
- Non-existent guide and country links were purged from the UI or stripped of their `href` attributes to serve purely as structural placeholders.
- The `lang` prop unused warning in `MetaHead.astro` was resolved by shifting language declaration entirely to `BaseLayout.astro`.

## Language Navigation Behavior
- Non-English routes (`/tr/`, `/uk/`, `/ru/`) now render headers and footers completely free of broken links. The English root exclusively carries the full beta navigation.

## Validation Method
- Ran `npm run build` to ensure type safety.
- Deployed a custom bash script (`test_links.sh`) parsing `href` strings across all HTML files in the output `dist/` directory, confirming every internal link points to an existing output route.

## Known Limitations
- The contact page remains informational without backend integration.
- Translated variants of the new core pages are not implemented.
