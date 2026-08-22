import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const siteUrl = process.env.SITE_URL;
const integrations = [];

// Only include sitemap if a production URL is configured.
// This prevents localhost from being baked into production metadata.
if (siteUrl) {
  integrations.push(sitemap());
}

export default defineConfig({
  site: siteUrl, // Will be undefined in local dev unless set
  outDir: './dist',
  server: { port: 3000 },
  integrations
});
