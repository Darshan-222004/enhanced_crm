# 📦 Enhanced CRM – Frappe/ERPNext Extension

Enhanced CRM is a powerful Frappe app that extends ERPNext's CRM functionality without touching any core doctypes. It brings financial data capture, mock API verification, comprehensive audit logging, and seamless data propagation from Lead → Customer → Sales Order.

## 🎯 What This Does (Assignment Objectives)

### 1. **Additional Financial Fields**
Adds essential financial identifiers to Lead and Customer:
- **BOID** (Beneficiary Owner Identification)
- **PAN Number** (Permanent Account Number)
- **Bank Account Number**
- **IFSC Code**

All fields include smart regex validation that triggers automatically on every save.

### 2. **External Verification Flow (Mock API)**
A backend verification system (`enhanced_crm.api.verify_pan`) that:
- Reads mock API endpoints and keys from **Financial Verification Settings**
- Simulates real-world PAN/IFSC verification requests
- Logs every attempt with status, timestamp, and full API response
- Provides instant feedback through a "Verify PAN" button

### 3. **Verification Log (Complete Audit Trail)**
A shared child table for both Lead and Customer that captures:
- **Verification Type** (PAN/IFSC)
- **Status** (Success/Failed)
- **Timestamp** (when verification occurred)
- **API Response JSON** (full payload for debugging)

### 4. **Lead → Customer Mapping Override**
When you convert a Lead to a Customer, everything carries over:
- All financial fields transfer automatically
- Complete Verification Log history is preserved
- No manual data re-entry needed
- Uses custom mapping helpers for seamless propagation

### 5. **Sales Order Auto-Population**
When creating a Sales Order:
- Select a Customer
- Verified financial details auto-populate (read-only):
  - Verified PAN Number
  - Verified Bank Account Number
- Implemented via smart getters and lightweight client scripts

### 6. **Enhanced CRM Module / Workspace**
A dedicated workspace that consolidates everything:
- Lead
- Customer
- Opportunity
- Verification Log
- Financial Verification Settings

All in one place for streamlined workflow.

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Installation

### Option 1 — Install from GitHub (Recommended)

```bash
cd ~/frappe-bench
bench get-app enhanced_crm https://github.com/Darshan-222004/enhanced_crm.git
bench --site <your-site> install-app enhanced_crm
bench --site <your-site> migrate
bench restart
```

### Option 2 — ZIP Download (Easy Method)

1. Open the GitHub repository
2. Click **Download ZIP**
3. Extract to: `frappe-bench/apps/enhanced_crm`
4. Run:

```bash
bench --site <your-site> install-app enhanced_crm
bench migrate
bench restart
```

---

## 🧩 Configuration

After installation, search for **Financial Verification Settings** in the Awesome Bar.

### Admin Settings Include:
- **PAN API Endpoint** - URL for PAN verification
- **PAN API Key** - Authentication key
- **IFSC API Endpoint** - URL for IFSC verification
- **IFSC API Key** - Authentication key

These values are used during all mock verification calls.

---

## 🚀 How to Use

### For Leads:
1. Create or open a Lead
2. Fill in financial details (BOID, PAN, Bank Account, IFSC)
3. Click **Verify PAN** button
4. Check **Verification Log** child table for results
5. Convert to Customer - all data carries over automatically

### For Customers:
1. Open any Customer
2. View inherited financial data from Lead
3. Click **Verify PAN** again if needed
4. Full verification history visible in Verification Log

### For Sales Orders:
1. Create a new Sales Order
2. Select a Customer
3. Verified PAN and Bank Account auto-populate (read-only)
4. Complete your sales order as usual

---

## 🔧 Technical Features

### Smart Validation
- **Regex patterns** for all financial fields
- **Real-time validation** on every save
- **User-friendly error messages**

### Mock API Integration
- Simulates real verification APIs
- Configurable endpoints and keys
- JSON response logging
- Status tracking (Success/Failed)

### Data Integrity
- **Automatic propagation** across doctypes
- **Complete audit trail** in Verification Log
- **Read-only verified fields** in Sales Orders
- **No core modifications** - all custom

### Developer Friendly
- Clean, modular code structure
- Well-documented functions
- Easy to extend and customize
- Follows Frappe best practices

---

## 📊 Workflow Overview

```
Lead (with financial data)
    ↓
[Verify PAN Button] → Mock API Call → Verification Log Entry
    ↓
Convert to Customer
    ↓
Customer (all data + verification history carried over)
    ↓
[Verify PAN Button] → Additional verification if needed
    ↓
Sales Order Creation
    ↓
Auto-populated verified financial fields (read-only)
```

---

## 🛠️ Troubleshooting

### App not showing after installation?
```bash
bench --site <your-site> migrate
bench --site <your-site> clear-cache
bench restart
```

### Verification button not appearing?
```bash
bench --site <your-site> clear-cache
bench build --app enhanced_crm
bench restart
```

### Permission issues?
```bash
bench --site <your-site> set-admin-password <new-password>
bench --site <your-site> add-system-manager Administrator
```

### Need to reinstall?
```bash
bench --site <your-site> uninstall-app enhanced_crm
bench --site <your-site> install-app enhanced_crm
bench migrate
bench restart
```

---

## 📝 Requirements

- **Frappe Framework**: v15.x or higher
- **ERPNext**: v15.x or higher
- **Python**: 3.10+
- **Node.js**: 18+

---

## 🤝 Contributing

Found a bug or have a feature request? Open an issue on GitHub!

Want to contribute? Pull requests are welcome!

---

## 📄 License

MIT License - feel free to use this in your projects!

---

## 👨‍💻 Author

**Darshan**  
GitHub: [@Darshan-222004](https://github.com/Darshan-222004)

---

## 🌟 Features at a Glance

✅ Financial field validation with regex  
✅ Mock API verification system  
✅ Complete audit trail in Verification Log  
✅ Seamless Lead → Customer data propagation  
✅ Auto-populated Sales Orders  
✅ Dedicated CRM workspace  
✅ Zero core modifications  
✅ Easy installation and configuration  
✅ Developer-friendly architecture  

---
