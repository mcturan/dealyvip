# Design System

## Design Principles
- **Modern & Minimal:** A focus on spaciousness and clarity without unnecessary decoration or gradients.
- **Editorial Character:** Typography and layouts inspired by high-quality publications to communicate trust and authority.
- **Performance-First:** Heavy reliance on systemic fonts, CSS variables, and native capabilities instead of bloated external libraries.

## Color Tokens
- **Primary / Neutral:** `slate-900` (#0f172a) for text and primary elements.
- **Accent:** `blue-600` (#2563eb) reserved strictly for interactive elements like links and buttons to establish clear visual hierarchy.
- **Backgrounds:** Pure white (#ffffff) for primary content; `slate-50` (#f8fafc) for alternate sections to create depth without borders.
- **Borders:** `slate-200` (#e2e8f0) for subtle component outlining.

## Typography
- **Font Stack:** Leverages systemic sans-serif (`-apple-system`, `BlinkMacSystemFont`, etc.) ensuring zero network requests for fonts while maintaining native platform crispness.
- **Display Headings:** Heavy weight (800) with tight letter-spacing (-0.03em) to convey confidence.
- **Body Text:** Standard weight (400), 16px base size, with a comfortable 1.6 line-height for long-form reading.

## Spacing & Layout System
- **Maximum Width:** `1100px` for global containers to prevent line lengths from becoming unreadable on ultra-wide monitors.
- **Content Width:** `800px` specifically for optimal reading width on text-heavy sections.
- **Spacing Scale:** Built on a standardized rem scale (xs: 0.5rem, sm: 1rem, md: 2rem, lg: 4rem, xl: 8rem) utilized as CSS variables.

## Component Rules
- **Buttons:** Use consistent padding, slight border-radius (`4px`), and distinct hover states. `btn-accent` uses the blue color, while `btn-outline` offers a secondary hierarchy.
- **Cards:** Utilize subtle borders (`slate-200`) and reveal a soft shadow (`shadow-md`) on hover to indicate interactivity.
- **Links:** Native browser underlines replaced with a customized, offset `text-decoration` that elegantly animates on hover.

## Responsive Principles
- **Fluid Typography:** `clamp()` used for headings to dynamically scale between mobile and desktop without rigid breakpoints.
- **Grid Stacking:** CSS Grid utilizing `repeat(auto-fill, minmax(...))` handles card layouts gracefully across all device widths without media query bloat.

## Accessibility Principles
- **Focus States:** Explicit `:focus-visible` styles with a 3px outline in the accent color.
- **Contrast:** Slate-900 on white exceeds WCAG AAA standards for body text.

## Visual Anti-Patterns (Banned)
- Country flags.
- Cliché handshake or globe imagery.
- Vague marketing slogans.
- Fake trust badges or certificates.
