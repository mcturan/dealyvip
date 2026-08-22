# Network and Domain Activation Guide

The server is currently ready for local and LAN traffic via port `8081`. 

## Manual Steps to Activate Public Internet Access:
1. **Assign Stable LAN IP:** Ensure this PC has a static LAN IP or DHCP reservation on your router.
2. **Forward Ports:** On your router, configure Port Forwarding:
   - External Port 80 -> Internal IP of this PC, Port 8081
   - External Port 443 -> Internal IP of this PC, Port 443
3. **CGNAT Check:** Confirm your ISP provides a real public IP (not Carrier-Grade NAT). If the WAN IP on the router matches your IP on `whatismyip.com`, you are clear.
4. **Point Domain (DNS):** Go to your domain registrar and create an A record pointing your domain (and optionally `www`) to your public IP.
5. **DNS Propagation:** Wait for DNS to propagate (can take a few minutes to hours).
6. **Activate Domain Setup:** Run the domain activation script:
   `sudo /usr/local/bin/activate-dealyvip-domain`
