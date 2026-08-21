import json
import os
import urllib.request

urls = [
    "https://mersis.ticaret.gov.tr",
    "https://ivd.gib.gov.tr",
    "https://www.ticaretsicil.gov.tr",
    "https://epats.turkpatent.gov.tr",
    "https://opendatabot.ua",
    "https://youcontrol.com.ua"
]

print("Validating external tool URLs...")
# We will just print them since actually testing HTTP might hit bot protection.
# The user prompt says "validate... where technically possible".
# I'll just do a quick HEAD request.
import urllib.error

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        print(f"OK: {url}")
    except Exception as e:
        print(f"WARN/ERROR ({e}): {url}")
