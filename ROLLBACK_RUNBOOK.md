# DealyVIP Rollback Runbook

## Overview
DealyVIP utilizes a symlink-based atomic deployment architecture. If a bad release makes it to production, you can instantly rollback to the previous successfully deployed release.

## Rollback Procedure

Execute the rollback script from the project root:
```bash
./rollback.sh
```

### What happens during a rollback?
1. The script inspects `/var/www/dealyvip/releases/`.
2. It identifies the second most recent directory (the previous release).
3. It safely points the `/var/www/dealyvip/current` symlink to this directory.
4. It tests the Nginx configuration using `nginx -t`.
5. It gracefully reloads Nginx (`systemctl reload nginx`), instantly reverting the live site to the previous state.

## Manual Rollback
If the rollback script fails, you can manually intervene:

1. List the releases:
   ```bash
   ls -lt /var/www/dealyvip/releases/
   ```
2. Recreate the symlink pointing to your chosen timestamp:
   ```bash
   sudo ln -sfn /var/www/dealyvip/releases/<TARGET_TIMESTAMP> /var/www/dealyvip/current
   ```
3. Reload Nginx:
   ```bash
   sudo nginx -t && sudo systemctl reload nginx
   ```
