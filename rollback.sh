#!/bin/bash
set -e

# DealyVIP Rollback Script
echo "Starting DealyVIP rollback..."

RELEASES_DIR="/var/www/dealyvip/releases"
CURRENT_DIR="/var/www/dealyvip/current"

# Find the second most recent directory
PREVIOUS_RELEASE=$(ls -1td $RELEASES_DIR/* | sed -n '2p')

if [ -z "$PREVIOUS_RELEASE" ]; then
    echo "No previous release found to rollback to."
    exit 1
fi

echo "Rolling back to: $PREVIOUS_RELEASE"
ln -sfn "$PREVIOUS_RELEASE" "$CURRENT_DIR"

echo "Testing Nginx configuration..."
if echo "turan" | sudo -S nginx -t; then
    echo "Reloading Nginx..."
    echo "turan" | sudo -S systemctl reload nginx
    echo "Rollback successful!"
else
    echo "Nginx configuration test failed! Please check Nginx config."
    exit 1
fi
