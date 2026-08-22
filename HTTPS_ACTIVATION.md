# HTTPS Activation Guide

HTTPS requires a registered domain and a verified public DNS record pointing to this machine.

## Prerequisites
1. Domain purchased.
2. Router port 80 forwarded to this machine's 8081 port.
3. DNS A record propagated.

## How to Activate
Do **NOT** run Certbot directly. The integrated domain activation script handles the safe transition to HTTPS:
`sudo /usr/local/bin/activate-dealyvip-domain`

This script will:
- Update Nginx `server_name`
- Run `certbot --nginx` to request Let's Encrypt certificates automatically via HTTP-01 challenge.
- Enable automatic HTTP -> HTTPS redirects in Nginx.

## Automatic Renewals
Certbot is installed with a systemd timer that will attempt to renew certificates 30 days before expiration automatically.
