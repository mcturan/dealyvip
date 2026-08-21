import json
import os
import urllib.request
import urllib.error

tools_dir = "src/content/tools/"
files = [f for f in os.listdir(tools_dir) if f.endswith(".json")]

for filename in files:
    with open(os.path.join(tools_dir, filename), 'r') as f:
        data = json.load(f)
    
    url = data.get("url")
    if not url or url.startswith("/"):
        continue

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        urllib.request.urlopen(req, timeout=5)
    except urllib.error.HTTPError as e:
        print(f"{filename}: HTTP {e.code}")
    except Exception as e:
        print(f"{filename}: BROKEN ({e})")
