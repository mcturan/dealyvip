# Verification Tools Architecture

## 1. Core Concept
The DealyVIP Verification Tools system is designed to provide highly scalable, data-driven directories of official registries and verification resources per country. It avoids the overhead of a database, CMS, or backend API by utilizing Astro's native Content Collections.

## 2. Astro Content Collections
The architecture leverages two linked collections in `src/content/`:
- **`countries`**: A collection of country metadata (e.g., `id`, `name`, `description`).
- **`tools`**: A collection of specific verification resources (e.g., MERSİS, Opendatabot) mapped via `countryId` to the `countries` collection.

## 3. Data-Driven Routing
We use dynamic routing via `src/pages/en/tools/[country].astro`.
When Astro builds, `getStaticPaths()` reads the `countries` collection and generates a static HTML page for each verified country. The page then queries the `tools` collection, filtering by `countryId`, grouping them by category, and rendering the tool cards.

## 4. UI/UX Decisions
- **No Detail Pages:** Given the concise nature of the verification tool metadata (purpose, operator, limitations, URL), rendering them directly as comprehensive cards on the country tools index is most efficient. Creating a separate page per tool would result in "thin content."
- **Visual Status Badges:** The architecture introduces clear color-coded badges to instantly distinguish between `OFFICIAL`, `INSTITUTIONAL`, `THIRD-PARTY`, and `INFORMATIONAL` resources.
- **Strict Verification Boundaries:** The tool card explicitly renders what the tool "Can Verify" vs "Cannot Verify" as defined in the data model.

## 5. Rejected Alternatives
- **Database/CMS:** Rejected as it violates the static, low-maintenance principles of the beta phase.
- **Hard-coded Components:** Rejected as adding Germany, Belgium, or the UK later would require modifying page templates, violating the scalability requirement.
- **Search Boxes:** Rejected to prevent "dashboard/portal" scope creep. Categorized lists are sufficient for the current volume of tools.

## 6. Localization Readiness
Because the structure is fully driven by JSON data and dynamic routes (`/en/tools/[country].astro`), localization will involve creating localized schemas (`/tr/tools/`, etc.) that query language-specific JSON records, avoiding hard-coded English in the core component logic.
