import json
import os

tools = [
    {
        "filename": "turkiye-mersis.json",
        "data": {
            "countryId": "turkiye",
            "name": "MERSİS (Central Registration System)",
            "shortDescription": "The primary official commercial registry system of Türkiye.",
            "category": "company-registry",
            "operator": "Turkish Ministry of Trade",
            "officialStatus": "OFFICIAL",
            "accessType": "LOGIN_REQUIRED",
            "languages": ["tr"],
            "url": "https://mersis.ticaret.gov.tr",
            "whatItCanVerify": ["Legal corporate existence", "Company registration number", "Current active/inactive status"],
            "whatItCannotVerify": ["Financial health or debt status", "Manufacturing capacity", "Physical presence of a factory"],
            "requiredInformation": ["Tax Number (VKN)", "MERSİS Number", "Company Name"],
            "accessLimitations": "Full access requires a Turkish e-Devlet (e-Government) login. Non-citizens must utilize local coordination.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "turkiye-ivd.json",
        "data": {
            "countryId": "turkiye",
            "name": "İnteraktif Vergi Dairesi (İVD)",
            "shortDescription": "Official portal to verify Turkish Tax Numbers (VKN).",
            "category": "tax-invoice",
            "operator": "Turkish Revenue Administration",
            "officialStatus": "OFFICIAL",
            "accessType": "PUBLIC",
            "languages": ["tr"],
            "url": "https://ivd.gib.gov.tr",
            "whatItCanVerify": ["Tax number validity", "Registered company name", "Tax office alignment"],
            "whatItCannotVerify": ["Tax debt amount", "Bank account ownership", "Commercial reliability"],
            "requiredInformation": ["Tax Number (VKN)", "Province", "Tax Office"],
            "accessLimitations": "Accessible without login for basic VKN validation. Captcha required.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "turkiye-ticaret-sicil.json",
        "data": {
            "countryId": "turkiye",
            "name": "Ticaret Sicil Gazetesi",
            "shortDescription": "Official Trade Registry Gazette for corporate structure and history.",
            "category": "company-registry",
            "operator": "Union of Chambers and Commodity Exchanges of Türkiye (TOBB)",
            "officialStatus": "OFFICIAL",
            "accessType": "REGISTRATION_REQUIRED",
            "languages": ["tr"],
            "url": "https://www.ticaretsicil.gov.tr",
            "whatItCanVerify": ["Board of directors changes", "Capital structure updates", "Registered corporate address changes"],
            "whatItCannotVerify": ["Real-time operational status", "Current production capacity"],
            "requiredInformation": ["Company Name", "MERSİS Number or Trade Registry Number"],
            "accessLimitations": "Requires creating a free account. Interface is strictly in Turkish.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "turkiye-turkpatent.json",
        "data": {
            "countryId": "turkiye",
            "name": "TURKPATENT",
            "shortDescription": "Official database for trademarks, patents, and designs.",
            "category": "intellectual-property",
            "operator": "Turkish Patent and Trademark Office",
            "officialStatus": "OFFICIAL",
            "accessType": "PUBLIC",
            "languages": ["tr", "en"],
            "url": "https://epats.turkpatent.gov.tr",
            "whatItCanVerify": ["Trademark ownership", "Patent registration status", "Design protection"],
            "whatItCannotVerify": ["Company existence", "Export authorization"],
            "requiredInformation": ["Brand Name", "Applicant Name", "Application Number"],
            "accessLimitations": "Publicly searchable. Advanced features require login.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "ukraine-usr.json",
        "data": {
            "countryId": "ukraine",
            "name": "Unified State Register (USR)",
            "shortDescription": "The official state register of legal entities in Ukraine.",
            "category": "company-registry",
            "operator": "Ministry of Justice of Ukraine",
            "officialStatus": "OFFICIAL",
            "accessType": "PUBLIC_WITH_LIMITATIONS",
            "languages": ["uk"],
            "url": "https://usr.minjust.gov.ua",
            "whatItCanVerify": ["Legal existence", "EDRPOU Code", "Authorized directors", "Bankruptcy status"],
            "whatItCannotVerify": ["Physical infrastructure damage", "Current operational capacity", "Debt"],
            "requiredInformation": ["EDRPOU Code (8 digits)"],
            "accessLimitations": "Geo-blocked from many international IP addresses due to martial law. Often requires local access or VPN.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "ukraine-opendatabot.json",
        "data": {
            "countryId": "ukraine",
            "name": "Opendatabot",
            "shortDescription": "Third-party open data aggregator for Ukrainian corporate data.",
            "category": "company-registry",
            "operator": "Opendatabot",
            "officialStatus": "THIRD-PARTY",
            "accessType": "PUBLIC",
            "languages": ["uk", "en"],
            "url": "https://opendatabot.ua",
            "whatItCanVerify": ["Basic corporate data", "Tax status", "Court register mentions"],
            "whatItCannotVerify": ["Real-time classified war-time data", "Guaranteed corporate reliability"],
            "requiredInformation": ["EDRPOU Code", "Company Name"],
            "accessLimitations": "Aggregates public data. Extremely useful when official USR is geo-blocked.",
            "lastVerified": "2024-05-20"
        }
    },
    {
        "filename": "ukraine-youcontrol.json",
        "data": {
            "countryId": "ukraine",
            "name": "YouControl",
            "shortDescription": "Advanced compliance and risk analysis platform for Ukrainian companies.",
            "category": "company-registry",
            "operator": "YouControl",
            "officialStatus": "THIRD-PARTY",
            "accessType": "REGISTRATION_REQUIRED",
            "languages": ["uk", "en"],
            "url": "https://youcontrol.com.ua",
            "whatItCanVerify": ["Corporate structure", "Sanctions screening", "Financial analytics (historical)"],
            "whatItCannotVerify": ["Physical factory validation"],
            "requiredInformation": ["EDRPOU Code"],
            "accessLimitations": "Deep analytics require a paid subscription. Basic profiling requires free registration.",
            "lastVerified": "2024-05-20"
        }
    }
]

for t in tools:
    with open(f"src/content/tools/{t['filename']}", 'w') as f:
        json.dump(t["data"], f, indent=2)

