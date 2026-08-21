# Page and URL Specification

## Purpose
Define a clean, stable, semantic, and language-aware URL model. Avoid random IDs and query strings for content routing.

## Language URL Structure
**Recommendation:** Subdirectory-based language routing (`/en/`, `/tr/`, `/uk/`, `/ru/`).
- **Why:** Allows clean geographic targeting in search engines, supports independent caching per language, and integrates easily with static site generators.
- **Base rule:** English serves as the default root (`/` defaults to `/en/` or English sits at `/en/` explicitly).

## Example URLs (English Base)

**Homepage:**
- `https://dealyvip.com/` (or `.../en/`)

**Country Pages:**
- `https://dealyvip.com/en/turkiye/`
- `https://dealyvip.com/en/ukraine/`

**Guide Pages:**
- Verification: `https://dealyvip.com/en/guides/verification/verify-company-turkiye/`
- Supplier Search: `https://dealyvip.com/en/guides/sourcing/find-suppliers-turkiye/`
- Basics: `https://dealyvip.com/en/guides/basics/overseas-prepayment-checklist/`

**Local Assistance Pages:**
- `https://dealyvip.com/en/assistance/turkiye-local-business-assistance/`
- `https://dealyvip.com/en/assistance/business-interpreter-coordination/`

**Contact Page:**
- `https://dealyvip.com/en/contact/`

## Localization URL Example
If a page is authored in Turkish for local suppliers:
- `https://dealyvip.com/tr/rehber/tedarik/guvenilir-tedarikci-bulmak/` (Semantic, localized URL slug).

## Rules
- **No Query Strings:** Avoid `?lang=en` or `?id=123`.
- **Hyphens:** Use hyphens (`-`) to separate words. No underscores.
- **Lowercase:** All URLs must be strictly lowercase.
- **Trailing Slashes:** Standardize on trailing slashes `/` for directories to prevent redirect chains.

## Status
Confirmed.
