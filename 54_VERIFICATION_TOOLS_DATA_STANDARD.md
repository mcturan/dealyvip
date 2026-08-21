# Verification Tools Data Standard

All new verification tools added to DealyVIP must adhere to the Zod schema defined in `src/content/config.ts` and the following factual standards:

## Schema Definition
```json
{
  "countryId": "string (must match a country id)",
  "name": "string (The official name of the tool)",
  "shortDescription": "string (1-2 sentences)",
  "category": "string (e.g., company-registry, tax-fiscal, business-information)",
  "operator": "string (The government or corporate entity managing it)",
  "officialStatus": "ENUM: OFFICIAL | INSTITUTIONAL | THIRD-PARTY | INFORMATIONAL",
  "url": "string (Must be verified and use HTTPS if available)",
  "whatItCanVerify": ["string array"],
  "whatItCannotVerify": ["string array"],
  "accessLimitations": "string (Optional. E.g., 'Requires e-Devlet')",
  "lastVerified": "YYYY-MM-DD"
}
```

## Status Classification Rules
- **OFFICIAL:** Operated directly by a state or federal government body (e.g., Ministry of Trade, Revenue Administration).
- **INSTITUTIONAL:** Operated by an officially recognized chamber, union, or non-profit regulatory body (e.g., TOBB, local Chambers of Commerce).
- **THIRD-PARTY:** A private commercial entity that aggregates data (e.g., Opendatabot, YouControl). Must never be presented as official state actors.
- **INFORMATIONAL:** General guides, static lists, or non-authoritative references.

## Verification Constraints
- **whatItCanVerify:** Must be strictly limited to what the registry officially confirms (e.g., "Registration date", not "Business reliability").
- **whatItCannotVerify:** Must actively combat common user assumptions (e.g., "Cannot verify current financial health").
