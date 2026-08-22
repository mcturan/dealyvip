# Server Recovery & Rollback

## Rollback Procedure
If a new deployment is fundamentally broken, the automated deployment script preserves the immediate previous working version.
To roll back:
```bash
sudo rm -rf /var/www/dealyvip/current
sudo cp -a /var/www/dealyvip/previous /var/www/dealyvip/current
sudo chown -R www-data:www-data /var/www/dealyvip/current
sudo systemctl restart nginx
```

## Bare-Metal Recovery
In case of complete server loss, you need:
1. This GitHub repository.
2. Node.js, Nginx, and Certbot.
3. Your Nginx configuration file: `/etc/nginx/sites-available/dealyvip`.
No databases or secrets are required to restore the static site.
