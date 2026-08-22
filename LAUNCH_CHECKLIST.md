# V1.0 Launch Checklist

## Phase V1-A: Pre-Launch Infrastructure
- [x] Determine Nginx state (Ready, but waiting for systemd on real hardware)
- [x] Verify no development server exposed
- [x] Ensure production configuration operates on static root

## Phase V1-B: Domain & Network Activation
- [ ] Acquire domain
- [ ] Determine Public IP and check for CGNAT
- [ ] Configure DNS (A record -> Public IP)
- [ ] Configure Router Port Forwarding (80 -> 8081, 443 -> 443)
- [ ] Run `sudo /usr/local/bin/activate-dealyvip-domain` to activate Let's Encrypt and HTTPS

## Phase V1-C: Automated Launch Validation
- [x] Run `./validate_launch.sh` successfully

## Phase V1-D: Search & Discovery Activation
*To be completed after the domain is live:*
- [ ] Google Search Console: Create property and verify ownership
- [ ] Google Search Console: Submit `sitemap-index.xml` (Requires `SITE_URL` at build time)
- [ ] Bing Webmaster Tools: Create property and submit sitemap
- [ ] Check `robots.txt` is accessible
- [ ] Check canonical and hreflang URLs resolve correctly
- [ ] Verify structured data using Rich Results Test

## Phase V1-E: Post-Launch Observation
- [ ] Monitor Nginx logs (`/var/log/nginx/access.log`, `/var/log/nginx/error.log`)
- [ ] Monitor Let's Encrypt certificate renewals (`systemctl status certbot.timer`)
- [ ] Setup external uptime monitoring (e.g. UptimeRobot) pointing to the public domain
- [ ] Backup configuration (`/etc/nginx/sites-available/dealyvip`) and git repository regularly
