# Content Relationship Map

This document outlines how guides and tools are semantically linked within the Astro Content Collections.

## Structural Relationships
- **Guides ↔ Guides (`relatedGuides`):** Used to form lateral reading paths (e.g., linking "How to Verify Documents" with "Red Flags").
- **Guides ↔ Tools (`relatedTools`):** Used to attach actionable verified country resources directly below procedural guides.
- **Tools ↔ Countries (`countryId`):** Automatically maps a tool to its respective static country index (`/en/tools/[country].astro`).

## Current Content Clusters
**Verification Cluster:**
- Verify Turkish Company (Tools: MERSİS, Sicil, İVD)
- Verify Ukrainian Company (Tools: USR, Opendatabot, YouControl)
- Verify Overseas Supplier Existence (Guides: Red Flags, Public Records)
- Verify Business Documents (Guides: Red Flags, Public Records)
- Supplier & Factory Verification in Türkiye (Tools: MERSİS)

**Practical Assistance Cluster:**
- Prepare Business Visit (Guides: Coordinate Visit, Interpreter)
- Coordinate Factory Visit (Guides: Prepare Visit)
- Working With Interpreter (Guides: Prepare Visit)
- Prepare Before Contacting Supplier (Guides: Verify Existence)
