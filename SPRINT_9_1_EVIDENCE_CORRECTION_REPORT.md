# Sprint 9.1 Evidence Correction Report

## Initial Discrepancies Identified
- Validation scripts previously equated HTTP 403 (Cloudflare/Bot protection) with "broken link."
- Validation summaries sometimes stated "0 broken links" when 403 errors were actually encountered.
- MERSİS description claimed "Full access requires a Turkish e-Devlet... Non-citizens must utilize local coordination," which was slightly overstated; some minimal data may occasionally be accessible without e-Devlet depending on the query, although full lookup requires it.
- Resource counts mixed tools (7) with informational compliance nodes (2).

## Evidence Model Corrections
- Formally separated `RESOURCE_IDENTITY` from `URL_VALIDATION` and `PUBLIC_ACCESS`.
- A 403 error on URL validation no longer invalidates the resource identity but flags it as `AUTOMATED_ACCESS_BLOCKED`.

## 403 / Bot Protection Corrections
- We introduced `AUTOMATED_ACCESS_BLOCKED` and `COULD_NOT_AUTOMATICALLY_VERIFY` distinct from `BROKEN`.
- Tool limitations correctly reflect that automated scrapers or foreign IPs may be blocked, requiring manual access.

## Opendatabot
- **Final Classification:** `APPROVED_FOR_PUBLICATION`
- **Correction:** Access note updated to explicitly state: "Automated access is blocked by strict Cloudflare bot protection, requiring manual browser access."

## YouControl
- **Final Classification:** `APPROVED_FOR_PUBLICATION`
- **Correction:** Access note updated to state: "Strict bot protection is in place for automated access."

## MERSİS
- **Final wording / classification:** Reworded limitation to "Access to specific MERSİS functions depends on the required service. Many queries require a Turkish e-Devlet (e-Government) login, which may restrict access for non-citizens."
- This is a more precise limitation statement supported by evidence.

## Resource Count Reconciliation
- **Total Published Verification Resources:** 7
- **Compliance / Information Nodes:** 2 (Russia, Iran)
- **Excluded / Needs Validation:** 0

## External Link Validation (Based on strict evidence script)
- **Successfully reached:** 5
- **Redirected correctly:** 0
- **Automated access blocked:** 1 (YouControl, HTTP 403)
- **Authentication required:** 0
- **Could not automatically verify:** 1 (USR, Geo-blocked timeout)
- **Broken:** 0

## Public Claim Corrections
- Re-scanned repository. All terms like "verified", "safe", "guaranteed" are strictly framed in negative/boundary contexts ("does not guarantee").

## Final Status
PASS
