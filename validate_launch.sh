#!/bin/bash
set -e

echo "Running Launch Validation..."

echo "[1/4] Building static site..."
npm run build

echo "[2/4] Validating internal links and assets..."
python3 -c '
import os, glob
from html.parser import HTMLParser

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.srcs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href": self.links.append(value)
        elif tag == "img":
            for name, value in attrs:
                if name == "src": self.srcs.append(value)

files = glob.glob("dist/**/*.html", recursive=True)
broken_links = []
broken_images = []

for f in files:
    with open(f, "r") as html_file:
        content = html_file.read()
    
    if "localhost" in content or "127.0.0.1" in content:
        print(f"WARNING: localhost leakage detected in {f}")

    parser = Extractor()
    parser.feed(content)
    
    for link in parser.links:
        if link.startswith("/") and not link.startswith("//"):
            path = "dist" + link
            if not os.path.exists(path) and not os.path.exists(path + "index.html") and not os.path.exists(path.rstrip("/") + "/index.html"):
                if path.endswith(".html") and not os.path.exists(path):
                    broken_links.append((f, link))
                elif not path.endswith(".html") and not os.path.exists(path + "/index.html"):
                    broken_links.append((f, link))
                    
    for src in parser.srcs:
        if src.startswith("/") and not src.startswith("//"):
            path = "dist" + src
            if not os.path.exists(path):
                broken_images.append((f, src))

if broken_links:
    for f, link in set(broken_links):
        print(f"FAIL: Broken link in {f} -> {link}")
    exit(1)
else:
    print("SUCCESS: No broken internal links.")

if broken_images:
    for f, src in set(broken_images):
        print(f"FAIL: Broken image in {f} -> {src}")
    exit(1)
else:
    print("SUCCESS: No broken internal images.")
'

echo "[3/4] Validating security configurations..."
if [ -f "dist/.env" ]; then
    echo "FAIL: .env exposed in dist/"
    exit 1
fi
echo "SUCCESS: No .env in dist/"

echo "[4/4] Validation complete!"
