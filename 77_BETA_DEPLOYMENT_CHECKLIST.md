# Beta Deployment Checklist

Use this checklist when actually deploying the DealyVIP beta to production.

## 1. Before Domain Purchase / Selection
- [ ] Finalize the exact production domain (e.g., `dealyvip.com`).
- [ ] Choose a static hosting provider (e.g., Cloudflare Pages, Netlify, Vercel).
- [ ] Confirm no backend/database is required by the host.

## 2. Production URL Configuration
- [ ] Set `SITE_URL` environment variable in the hosting provider's dashboard to the exact primary domain (e.g., `https://www.dealyvip.com`).
- [ ] Ensure the URL does not contain a trailing slash (Astro config handles it safely, but cleaner without).

## 3. Hosting Connection
- [ ] Connect the hosting provider to the `main` branch of this repository.
- [ ] Configure the build settings:
  - **Build Command:** `npm run build`
  - **Output Directory:** `dist`

## 4. HTTPS & Custom Domain
- [ ] Configure the custom domain in the hosting provider.
- [ ] Ensure automatic HTTPS / SSL provisioning is complete.
- [ ] Verify redirects (e.g., HTTP -> HTTPS, non-www -> www if desired).

## 5. Contact Configuration
- [ ] If ready to receive inquiries, set the contact details in `src/config/contact.ts`.
- [ ] To do this safely, you may edit the file and commit, or in the future move it to environment variables. Currently, it defaults to a closed state.

## 6. Sitemap & Robots.txt
- [ ] Once deployed, navigate to `https://[YOUR_DOMAIN]/sitemap-index.xml` and verify it resolves.
- [ ] Navigate to `https://[YOUR_DOMAIN]/robots.txt` and verify it outputs the correct sitemap URL.

## 7. Search Console & Webmaster Tools
- [ ] Add the property to Google Search Console.
- [ ] Submit the `sitemap-index.xml` URL.
- [ ] Do the same for Bing Webmaster Tools.

## 8. Final Smoke Test
- [ ] Test the 404 page: navigate to `https://[YOUR_DOMAIN]/this-should-404`.
- [ ] Verify the Mobile layout on a physical phone.
- [ ] Inspect Open Graph tags using a tool like [opengraph.dev] or by sharing a link on a test channel.
- [ ] Check internal links using the site navigation.

## 9. Rollback Basics
- [ ] If an issue occurs, rollback is performed via the hosting provider's dashboard (e.g., "Revert to this deployment" in Cloudflare Pages) or by reverting the commit in git.
