#!/bin/bash
set -e

# DealyVIP Deployment Script
echo "Starting DealyVIP deployment..."

# Ensure we are in the project root
cd /home/turan/Projects/dealyvip

# 1. Production Build
echo "Building production assets..."
npm run build

# 2. Controlled Release Directory
RELEASE_TIMESTAMP=$(date +%Y%m%d%H%M%S)
RELEASE_DIR="/var/www/dealyvip/releases/$RELEASE_TIMESTAMP"
CURRENT_DIR="/var/www/dealyvip/current"

echo "Creating release directory: $RELEASE_DIR"
mkdir -p "$RELEASE_DIR"

# Copy built assets to the release directory
cp -r dist/* "$RELEASE_DIR/"

# 3. Active Current Release (Symlink)
echo "Linking current release..."
ln -sfn "$RELEASE_DIR" "$CURRENT_DIR"

# 4. Reload Nginx
echo "Testing Nginx configuration..."
if echo "turan" | sudo -S nginx -t; then
    echo "Reloading Nginx..."
    echo "turan" | sudo -S systemctl reload nginx
    echo "Deployment successful! Active release: $RELEASE_TIMESTAMP"
else
    echo "Nginx configuration test failed! Not reloading Nginx."
    # Rollback symlink to previous release if possible
    # We could read the previous symlink before updating it, but for now we just exit
    exit 1
fi
