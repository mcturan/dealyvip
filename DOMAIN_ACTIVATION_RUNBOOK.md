# Domain Activation & HTTPS Runbook

## Overview
Currently, DealyVIP is configured to listen on port 8081 without a specific domain (`server_name _;`). When the production domain is purchased, follow these steps to securely transition to HTTPS.

## 1. Configure DNS
Create an `A` record pointing the future domain (e.g., `dealyvip.com`) to this server's public IP address.
Create a `CNAME` or `A` record for `www.dealyvip.com` pointing to the same IP.

Wait for DNS propagation.

## 2. Update Astro configuration
Update `src/config/site.ts` (if it exists) or Astro's `SITE_URL` environment variables so sitemaps and canonical links generate correctly.
Run a deployment to push these changes:
```bash
./deploy.sh
```

## 3. Reconfigure Nginx
Edit the Nginx configuration file:
```bash
sudo nano /etc/nginx/sites-available/dealyvip
```

Change the `listen` directive to port `80` (ensure CasaOS or other services no longer conflict, or use a reverse proxy to route traffic).
Change the `server_name` directive:
```nginx
server_name dealyvip.com www.dealyvip.com;
```

Verify and reload:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

## 4. Install Certbot and Issue Certificate
Run Certbot to automatically fetch a Let's Encrypt SSL certificate and configure the Nginx HTTPS redirect:

```bash
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot --nginx -d dealyvip.com -d www.dealyvip.com
```

Certbot will automatically edit the Nginx configuration to add the SSL certificates and the HTTP-to-HTTPS redirects.

## 5. Verify Validation
Open `https://dealyvip.com` in a browser and verify the lock icon.
