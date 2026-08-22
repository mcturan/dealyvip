import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
  let robotsTxt = `User-agent: *\nAllow: /\n`;
  if (site) {
    const sitemapURL = new URL('sitemap-index.xml', site);
    robotsTxt += `\nSitemap: ${sitemapURL.href}\n`;
  }
  return new Response(robotsTxt.trim(), {
    headers: {
      'Content-Type': 'text/plain',
    },
  });
};
