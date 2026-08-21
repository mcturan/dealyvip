# Resource Verification Methodology (Revised)

## Core Principle
DealyVIP operates as a curated trust layer. We do not list broken links, fake APIs, or resources that cannot be independently validated.

**Crucial Distinction:**
Do not confuse "Resource Exists" with "Resource URL was automatically accessible" with "Resource was manually verified." The reporting must distinguish these accurately.

## Evidence Model

### 1. RESOURCE_IDENTITY
- **CONFIRMED**: The resource is definitively known and its existence is proven.
- **PARTIALLY_CONFIRMED**: Some evidence exists but is incomplete.
- **UNCONFIRMED**: Cannot prove the resource exists.

### 2. RESOURCE_OPERATOR
- **IDENTIFIED**: The managing authority or company is known.
- **PARTIALLY_IDENTIFIED**: Some links to an operator, but ambiguous.
- **UNCONFIRMED**: Operator unknown.

### 3. RESOURCE_PURPOSE
- **CONFIRMED**: The utility of the resource is understood.
- **PARTIALLY_CONFIRMED**: Claimed purpose is understood, but evidence of actual utility is thin.
- **UNCONFIRMED**: Purpose unclear.

### 4. URL_VALIDATION
- **RESOLVED**: HTTP 200/300 success.
- **REDIRECTED_TO_EXPECTED_DESTINATION**: Clean redirect.
- **AUTOMATED_ACCESS_BLOCKED**: HTTP 403 / 429 due to Cloudflare, bot protection, or WAF. (Does not mean the link is broken for a human).
- **AUTHENTICATION_REQUIRED**: HTTP 401.
- **TEMPORARILY_UNAVAILABLE**: HTTP 500/502/503.
- **UNVERIFIED**: Could not be tested.
- **BROKEN**: Domain NXDOMAIN or strict 404.

### 5. PUBLIC_ACCESS
- **PUBLIC**: Open to anyone.
- **PUBLIC_WITH_LIMITATIONS**: Geo-blocked, Captcha, or throttled.
- **REGISTRATION_REQUIRED**: Requires a free account.
- **LOGIN_REQUIRED**: Requires a citizen/corporate ID (e.g., e-Devlet).
- **UNKNOWN**: Cannot be determined.

### 6. PUBLICATION_STATUS
- **APPROVED_FOR_PUBLICATION**: Strong evidence supports publication.
- **PUBLISHED_WITH_ACCESS_LIMITATION**: Approved, but strictly noting access barriers.
- **NEEDS_FURTHER_VALIDATION**: Kept in repository, not published.
- **EXCLUDED**: Intentionally removed from UI (e.g., for compliance boundaries).

## Validation Checklist
Before any resource is committed to the repository, it must pass manual checks confirming identity, operator, and purpose. Automated tests handle URL validation, but `AUTOMATED_ACCESS_BLOCKED` requires manual confirmation before publication.

## Terminology Enforcement
- **"Official government resource":** Domains ending in `.gov`, `.gov.tr`, `.gov.ua`.
- **"Institution / Chamber":** e.g., TOBB, ISO.
- **"Third-party platform":** e.g., YouControl, Opendatabot.
