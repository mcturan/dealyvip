# Country Onboarding Guide

To add a new country (e.g., Germany) to the DealyVIP Verification Tools system in the future, follow these steps. Do not modify Astro components directly.

## Step 1: Create Country Metadata
Create `src/content/countries/germany.json`:
```json
{
  "id": "germany",
  "name": "Germany",
  "description": "Official and third-party tools for verifying companies in Germany."
}
```

## Step 2: Research & Verify Authoritative Resources
Identify official state registries (e.g., Unternehmensregister, Handelsregister). Verify their official URLs, access limitations, and what data they actually provide.

## Step 3: Add Tool Records
For each verified tool, create a file in `src/content/tools/`, such as `germany-unternehmensregister.json`:
```json
{
  "countryId": "germany",
  "name": "Unternehmensregister",
  "shortDescription": "The German federal company register.",
  "category": "company-registry",
  "operator": "Bundesanzeiger Verlag",
  "officialStatus": "OFFICIAL",
  "url": "https://www.unternehmensregister.de",
  ... (fill out remaining fields according to the Data Standard)
}
```

## Step 4: Build and Validate
Run `npm run build`. The dynamic routing logic in `src/pages/en/tools/[country].astro` will automatically detect the new `germany.json` file, create the `/en/tools/germany/` route, and populate the page with the associated tool cards.

## Step 5: Update the Navigation (Optional)
If necessary, link to the new country route from other guide pages. The top-level `/en/tools/` index page will automatically include Germany in the grid.
