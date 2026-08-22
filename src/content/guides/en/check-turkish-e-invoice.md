---
title: "How to Check a Turkish e-Invoice or e-Archive Invoice"
description: "Understand the difference between e-Fatura and e-Arşiv Fatura in Türkiye and how to verify their technical authenticity."
language: "en"
country: "turkiye"
topic: "Verification"
relatedTools: ["turkiye-ivd"]
relatedGuides: ["due-diligence-turkish-company"]
status: "draft"
lastUpdated: 2026-08-22
---

Türkiye operates a highly digitalized taxation system managed by the Revenue Administration (Gelir İdaresi Başkanlığı - GİB). As an international buyer, the invoices you receive from Turkish suppliers will almost always be generated electronically.

This guide explains the difference between the two main types of electronic invoices and how their authenticity can be verified.

## e-Invoice (e-Fatura) vs. e-Archive Invoice (e-Arşiv Fatura)

It is vital to understand which type of invoice you are holding:

1. **e-Invoice (e-Fatura):** This system is strictly for transactions **between two Turkish companies** that are both registered in the e-Fatura system. As a foreign buyer, you will generally *not* receive a standard e-Fatura, because your company is not registered in the Turkish tax system.
2. **e-Archive Invoice (e-Arşiv Fatura):** This is the invoice type issued to non-registered entities, including **international buyers (exports)** and individual consumers. It is electronically generated, digitally signed by the issuer or an integrator, and submitted to the GİB, but it is delivered to you in a human-readable format (usually a PDF).

## How to Verify a Turkish e-Archive Invoice

If you receive a PDF e-Archive Invoice from a Turkish supplier and want to confirm it is not a forged document, you can verify it using the official GİB portal.

### The Verification Workflow

1. Locate the official GİB document verification portal. (Historically accessed via `ebelge.gib.gov.tr` or the Interactive Tax Office portal).
2. You will need three critical pieces of information from the invoice PDF:
   - **The Vendor's VKN:** The 10-digit Tax Identification Number of the Turkish supplier.
   - **The Invoice Number (Fatura Numarası):** A 16-character alphanumeric string (e.g., `ABC2023000000123`).
   - **The ETTN / UUID:** A long Universally Unique Identifier string printed on the invoice (e.g., `123e4567-e89b-12d3-a456-426614174000`).
3. Enter these details into the portal along with the security captcha.

### What the Result Means

- **If the system confirms the invoice:** It means an invoice with that exact ID was successfully issued by the vendor and recorded in the state tax system.
- **If the system cannot find the invoice:** It may mean the document is forged, but it could also mean the vendor's integration system has not yet batched and transmitted the invoice to the government (which sometimes takes a few days). 

## Crucial Limitation: Technical Authenticity vs. Legal Validity

**Do not confuse technical verification with legal or commercial safety.**

If the GİB system confirms your e-Archive invoice, it *only* proves that the invoice exists in the tax database. 

It **does not guarantee**:
- That the goods have actually been shipped.
- That the company intends to fulfill the contract.
- That the bank account listed on the PDF belongs to the company (the government does not verify the banking details typed onto the invoice template).

Always combine invoice verification with comprehensive due diligence on the company's identity and banking information.

## How DealyVIP Can Help

Navigating foreign registries, translating legal documents, and confirming physical addresses remotely is difficult and error-prone. DealyVIP provides independent verification and local assistance to secure your cross-border transactions. 

Instead of guessing whether public records are accurate, **tell us what you need**. We can:
- Verify the company's registration and tax status using local resources.
- Review and cross-check the foundational documents provided by your supplier.
- Coordinate a physical site visit to confirm manufacturing capacity.

[Contact DealyVIP to request verification assistance](/en/contact/)
