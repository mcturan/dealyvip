# Structured Data and Metadata Model

## Purpose
Define the metadata strategy to ensure pages are correctly interpreted by search engines and AI assistants.

## Metadata Requirements
- **Page Titles:** `<title>` must be unique, descriptive, and under 60 characters. Format: `[Page Subject] | DealyVIP`.
- **Meta Descriptions:** Unique, actionable summaries under 160 characters.
- **Canonical URLs:** Every page must specify a self-referencing canonical URL to prevent duplicate content issues.
- **hreflang Tags:** Multilingual pages must map equivalents (e.g., `<link rel="alternate" hreflang="tr" href=".../tr/..." />`).
- **Open Graph (OG):** Required `og:title`, `og:description`, `og:image`, `og:url` for social/messaging link previews.

## Structured Data (Schema.org JSON-LD)
Implement strictly where applicable. Do not invent schema to trick search engines.

- **Article / FAQPage:** For Guide and Problem pages. Use `FAQPage` if the page is structured as Q&A.
- **Organization:** For the homepage, defining DealyVIP as a business entity, including contact information.
- **BreadcrumbList:** Implemented globally to help search engines understand the site hierarchy.

## Explicit Restrictions
- Do NOT use `LegalService`, `FinancialService`, or `GovernmentOrganization` schema types.
- Do NOT mark DealyVIP as an official inspection body.

## Status
Confirmed.

## Anti-Hallucination & SEO Guarantees
- Explicitly reject any claim of guaranteed SEO outcomes, exact search ranking, or guaranteed AI recommendations.
- Metadata is implemented strictly to structure factual information for crawlers, not to manipulate rankings.
