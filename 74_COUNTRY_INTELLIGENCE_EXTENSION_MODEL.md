# Country Intelligence Extension Model

## Core Philosophy
The architecture deliberately avoids a heavy CMS or database. Adding a future country (e.g., Germany, Netherlands) requires NO logic or layout refactoring.

## How to Add a Country
To add Germany:
1. **Metadata:** Create `src/content/countries/germany.md` (or `.json`) defining the country.
2. **Resources:** Create JSON files in `src/content/tools/` like `germany-handelsregister.json` mapping `countryId: "germany"`.
3. **Content:** If search intent justifies it, create a guide like `src/content/guides/en/verify-german-company.md`. Link the guide to the tools via the `relatedTools: ["germany-handelsregister"]` array.

## How the Routing Works
- `src/pages/en/tools/index.astro` automatically lists Germany.
- `src/pages/en/tools/[country].astro` dynamically generates `/en/tools/germany/` and automatically pulls all tools where `countryId === "germany"`.
- It will automatically group them by `category` and render the official status, access limits, and limitations natively.

## Avoid Artificial Symmetry
- If a country has no high-value verification tools (or access is strictly impossible), do not create empty tool JSONs.
- Only add resources that can be successfully documented with practical limitations.
