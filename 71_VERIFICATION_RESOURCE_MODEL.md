# Verification Resource Model

## Architecture Decision
The verification resource architecture uses static JSON files inside `src/content/tools/`. We have extended the existing schema to better represent realistic access conditions. DealyVIP does NOT scrape or query these resources automatically. It operates strictly as a directory and orientation platform.

## Supported Schema
- **countryId:** Maps the tool to a specific target country.
- **name:** Name of the resource.
- **shortDescription:** A brief summary.
- **category:** e.g., `company-registry`, `tax-invoice`, `intellectual-property`.
- **operator:** The authority operating the resource (e.g., "Ministry of Trade").
- **officialStatus:** `OFFICIAL`, `INSTITUTIONAL`, `THIRD-PARTY`, or `INFORMATIONAL`.
- **accessType:** Explicitly defines access realities:
  - `PUBLIC`: Open to anyone.
  - `PUBLIC_WITH_LIMITATIONS`: Geo-blocked or CAPTCHA restricted.
  - `REGISTRATION_REQUIRED`: Open but requires a local account.
  - `LOGIN_REQUIRED`: Strictly limited to citizens or local entities (e.g., e-Devlet).
  - `INFORMATION_ONLY`: No database search, just static info.
  - `EXTERNAL_PROFESSIONAL_REQUIRED`: Cannot be accessed without local legal/accounting representation.
- **languages:** Languages the UI is available in.
- **url:** Official URL.
- **whatItCanVerify:** Array of verifiable data points.
- **whatItCannotVerify:** Strict list of limitations (e.g., cannot verify QA).
- **requiredInformation:** What the user needs before using the tool (e.g., Tax Number, MERSİS No).
- **accessLimitations:** Human-readable access context.
- **lastVerified:** ISO date.
