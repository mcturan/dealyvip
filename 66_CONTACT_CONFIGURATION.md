# Contact Configuration Architecture

## Location
`/src/config/contact.ts`

## Design Decision
To remain true to the static, backend-free Astro architecture, we avoid implementing a mock contact form. Implementing a real form would require a serverless function, database, or third-party endpoint (e.g., Formspree), which violates the "no hidden APIs/backend" principle of this sprint.

Instead, contact channels are driven purely by configuration.

## Required Values
- `publicContactEnabled` (boolean): Master toggle. If false, the site displays a polite "channels closed" message.
- `email` (string): Direct `mailto:` link generator.
- `whatsapp` (string): Direct `wa.me/` link generator.

## Security & Privacy
- **DO NOT** commit real personal email addresses or phone numbers to the public repository unless they are explicitly authorized as public-facing business endpoints.
- No fake placeholders (`href="#"` or `example@example.com`) are permitted. If an endpoint is empty in the config, the component simply unmounts it from the DOM.
