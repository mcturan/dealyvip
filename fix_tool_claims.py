import json

def update_json(filename, updates):
    with open(f"src/content/tools/{filename}", 'r') as f:
        data = json.load(f)
    data.update(updates)
    with open(f"src/content/tools/{filename}", 'w') as f:
        json.dump(data, f, indent=2)

update_json("turkiye-mersis.json", {
    "accessType": "PUBLIC_WITH_LIMITATIONS",
    "accessLimitations": "Access to specific MERSİS functions depends on the required service. Many queries require a Turkish e-Devlet (e-Government) login, which may restrict access for non-citizens.",
})

update_json("ukraine-opendatabot.json", {
    "accessLimitations": "Aggregates public data. Extremely useful when official USR is geo-blocked. Note: Automated access is blocked by strict Cloudflare bot protection, requiring manual browser access."
})

update_json("ukraine-youcontrol.json", {
    "accessLimitations": "Deep analytics require a paid subscription. Basic profiling requires free registration. Strict bot protection is in place for automated access."
})
