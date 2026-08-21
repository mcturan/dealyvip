# CTA and User Journey Map

## Primary Philosophy
Instead of pushing users immediately to a generic "Contact Us" form, the user journey is defined by **Contextual Qualification**.

## Journey Map
1. **Awareness:** User lands on `en/index.astro` or a direct guide via organic search.
2. **Education:** User reads a procedural guide (e.g., "Verify Turkish Company").
3. **Qualification:** At the bottom of the guide, the `ContactCTA` component evaluates the context:
   - If *Verification*, CTA = "Explore Coordination Options"
   - If *Assistance*, CTA = "Coordinate Local Assistance"
   - If *General*, CTA = "Understand Limitations"
4. **Preparation:** User lands on `/en/contact/` which outlines the required information (Business Context, Jurisdiction, Entity Details).
5. **Contact:** User clicks the mail or WhatsApp link (configured centrally), avoiding insecure web forms without backend infrastructure.

## CTA Normalization
- Removed "Contact DealyVIP" button defaults in favor of "Explore Coordination Options."
- Avoided all aggressive marketing pressure ("Contact us now!").
