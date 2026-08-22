# Self-Hosted Deployment Guide

This project is configured to run on a dedicated Linux host (Pardus) via Nginx.

## Architecture
- **Git Repository:** `/home/turan/Projects/dealyvip`
- **Web Root:** `/var/www/dealyvip/current`
- **Web Server:** Nginx (listening on 8081 (HTTP) and 443 (HTTPS) internally)
- **Deployment Script:** `/usr/local/bin/deploy-dealyvip`

## How to Deploy Updates
When changes are pushed to `main` on GitHub, run the following command on this machine to securely pull, build, and deploy the new version:

```bash
sudo systemctl start dealyvip-deploy
```
*(This triggers the systemd oneshot service, which runs `/usr/local/bin/deploy-dealyvip` in the background and logs to journalctl).*

To deploy manually and see real-time output:
```bash
/usr/local/bin/deploy-dealyvip
```

## Security
The deployment process ensures the Git tree is kept outside the public web root. Nginx strictly serves built static files and enforces security headers.
