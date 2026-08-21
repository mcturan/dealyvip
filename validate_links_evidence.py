import json
import os
import urllib.request
import urllib.error

tools_dir = "src/content/tools/"
files = [f for f in os.listdir(tools_dir) if f.endswith(".json")]

results = {
    "SUCCESSFULLY_REACHED": [],
    "AUTOMATED_ACCESS_BLOCKED": [],
    "AUTHENTICATION_REQUIRED": [],
    "BROKEN": []
}

for filename in files:
    with open(os.path.join(tools_dir, filename), 'r') as f:
        data = json.load(f)
    
    url = data.get("url")
    if not url or url.startswith("/"):
        continue

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        response = urllib.request.urlopen(req, timeout=5)
        results["SUCCESSFULLY_REACHED"].append(url)
    except urllib.error.HTTPError as e:
        if e.code in [403, 429]:
            results["AUTOMATED_ACCESS_BLOCKED"].append(url)
        elif e.code in [401]:
            results["AUTHENTICATION_REQUIRED"].append(url)
        else:
            results["BROKEN"].append(url)
    except Exception as e:
        results["BROKEN"].append(url)

print("External link validation:")
print(f"Successfully reached: {len(results['SUCCESSFULLY_REACHED'])}")
print(f"Automated access blocked: {len(results['AUTOMATED_ACCESS_BLOCKED'])}")
print(f"Authentication required: {len(results['AUTHENTICATION_REQUIRED'])}")
print(f"Could not automatically verify / Broken: {len(results['BROKEN'])}")
