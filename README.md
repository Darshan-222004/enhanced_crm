📦 Enhanced CRM – Frappe/ERPNext Extension

Enhanced CRM is an installable Frappe app that extends ERPNext’s CRM functionality without modifying any core doctypes.
It introduces financial data capture, mock API verification, audit logging, and automatic propagation of financial identifiers across Lead → Customer → Sales Order.

🎯 Objectives (per assignment brief)
1. Additional Financial Fields

Adds BOID, PAN Number, Bank Account Number, and IFSC Code to both Lead and Customer doctypes, with regex validation triggered on every validate event.

2. External Verification Flow (Mock API)

A whitelisted backend function (enhanced_crm.api.verify_pan) that:

Reads mock endpoints and API keys from Financial Verification Settings (singleton doctype).

Simulates a remote PAN/IFSC verification request.

Logs each attempt in the Verification Log child table with status, timestamp, and JSON payload.

3. Verification Log (Audit Trail)

Shared child table (for both Lead and Customer) capturing:

Verification Type (PAN/IFSC)

Status (Success/Failed)

Timestamp

API Response JSON

4. Lead → Customer Mapping Override

During conversion (“Create → Customer”), all financial fields and the entire Verification Log table are carried forward using a custom mapping helper.

5. Sales Order Auto-Population

When a Customer is selected, Sales Orders automatically load read-only financial details:

Verified PAN Number

Verified Bank Account Number

This is implemented via a getter and lightweight client script.

6. Enhanced CRM Module / Workspace

A dedicated workspace groups all related items:

Lead

Customer

Opportunity

Verification Log

Financial Verification Settings

into one consolidated Enhanced CRM module.

📁 Project Structure
enhanced_crm/
├── README.md
├── requirements.txt
├── setup.py
├── fixtures/
│   └── custom_field.json
└── enhanced_crm/                   # Python package
    ├── api.py                      # Verification API, SO helpers
    ├── hooks.py                    # Events, fixtures, overrides
    ├── mapping.py                  # Lead → Customer propagation
    ├── setup.py                    # Custom field installers
    ├── validations.py              # Regex validation logic
    ├── config/
    │   └── desktop.py              # Module/workspace registration
    ├── public/
    │   └── js/
    │       ├── lead.js             # Verify PAN button
    │       ├── customer.js         # Verify PAN button
    │       └── sales_order.js      # Verified field auto-fill
    ├── doctype/
    │   ├── financial_verification_settings/
    │   │   ├── financial_verification_settings.json
    │   │   └── financial_verification_settings.py
    │   └── verification_log/
    │       ├── verification_log.json
    │       └── verification_log.py
    └── workspace/
        └── enhanced_crm/
            └── enhanced_crm.json    # Workspace definition

⚙️ Installation
Option 1 — Install from GitHub (recommended)
cd ~/frappe-bench
bench get-app enhanced_crm https://github.com/Darshan-222004/enhanced_crm.git
bench --site <your-site> install-app enhanced_crm
bench --site <your-site> migrate
bench restart

Option 2 — ZIP Download (easy method)

Open the GitHub repository

Click Download ZIP

Extract to:

frappe-bench/apps/enhanced_crm


Run:

bench --site <your-site> install-app enhanced_crm
bench migrate
bench restart

🧩 Configuration

Search for Financial Verification Settings in the Awesome Bar.
Admins can modify:

PAN API endpoint

PAN API key

IFSC API endpoint

IFSC API key

These values are used during mock verification calls.
