# Language SEO & Hreflang Implementation

- **Rule:** `hreflang` tags are ONLY injected if an explicit, controlled alternative is mapped.
- **Mechanism:** The `BaseLayout` receives an `alternatives` array prop. This is passed to `MetaHead`, which generates `<link rel="alternate" hreflang="x" href="y" />`.
- **Integrity:** We do not loop through all languages. If a Turkish page has no English equivalent yet, it does not fake an English hreflang.
- **Canonical URLs:** The base URL (https://dealyvip.com) is hardcoded for the hreflang domain prefix.
