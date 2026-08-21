# Mobile and Responsive Requirements

## Purpose
Ensure the informational website is highly readable and usable on mobile devices, respecting a mobile-first philosophy.

## Requirements

- **Mobile Navigation:** Must use a clean hamburger menu. The primary CTA (Contact) should remain easily accessible without opening the menu (e.g., sticky bottom bar).
- **Typography:** Base font size of at least 16px for readability. High contrast between text and background.
- **Line Length:** Content blocks should be constrained to 60-80 characters per line on desktop, and adapt to full width with padding on mobile.
- **Touch Targets:** Buttons and links must be at least 44x44 CSS pixels to prevent accidental taps.
- **Images:** Must be responsive (`max-width: 100%`) and utilize modern formats (WebP) with `loading="lazy"` to preserve bandwidth.
- **Tables:** Complex data tables must be horizontally scrollable on mobile devices to prevent layout breakage.
- **Long-Form Guides:** Implement sticky table of contents or "Back to top" buttons for lengthy guide pages to aid mobile scrolling.
- **CTA Visibility:** Call-to-action buttons should span the full width of the mobile screen.
- **Performance:** Pages should render meaningful content within 1.5 seconds on a 3G/4G connection. Avoid heavy client-side JavaScript frameworks.

## Status
Confirmed.
