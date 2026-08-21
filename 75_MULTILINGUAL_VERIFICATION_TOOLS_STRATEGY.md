# Multilingual Verification Tools Strategy

## Current State
- Tool data is stored centrally in JSON (`src/content/tools/*.json`).
- Titles, descriptions, and verification limits are currently in English.
- The UX components are language-aware but the data payload is monolingual (English fallback).

## Readiness
The UI does not assume English-only text. The `VerificationLimitations.astro` component supports a `context` and can be expanded for `lang="tr"|"uk"`. The tools schema now supports an explicit `languages` array (`["en", "tr"]`) indicating if the destination resource supports multiple languages.

## Future Translation Strategy
When tools are localized:
1. **Option A (Data Model Expansion):**
   Extend the schema to support nested objects:
   `name: { en: string, tr: string, uk: string }`
2. **Option B (File Separation):**
   Migrate `tools` from data collections to markdown content collections (`src/content/tools/en/*.md`, `tr/*.md`). The frontmatter would contain the rigid schema (URL, accessType, etc.), while the body contains the description and limitations.

**Decision:** Option B is preferable if long-form explanations of access limits are required per language. For now, we defer bulk translation of tools to avoid unnecessary maintenance overhead. Guides natively explain the tool in the target language (TR/UK), providing immediate value without needing to localize the entire tool database UI.
