app_name = "enhanced_crm"
app_title = "Enhanced CRM"
app_publisher = "Darshan Bharadwaj"
app_description = "Extends ERPNext CRM with financial verification and mapping"
app_email = "darshanbharadwaj04@gmail.com"
app_license = "mit"

# ---------------------------------------------------------
# CLIENT SCRIPTS
# ---------------------------------------------------------
doctype_js = {
    "Lead": "public/js/lead.js",
    "Customer": "public/js/customer.js",
    "Sales Order": "public/js/sales_order.js"
}

# ---------------------------------------------------------
# SERVER-SIDE EVENTS
# ---------------------------------------------------------
doc_events = {
    "Lead": {
        "validate": "enhanced_crm.validations.validate_lead_or_customer"
    },
    "Customer": {
        "validate": "enhanced_crm.validations.validate_lead_or_customer"
    },
    "Sales Order": {
        "onload": "enhanced_crm.api.load_customer_financials"
    }
}

# ---------------------------------------------------------
# INSTALL / MIGRATION HOOKS
# ---------------------------------------------------------
after_install = "enhanced_crm.setup.after_install"
after_migrate = "enhanced_crm.setup.after_migrate"

# ---------------------------------------------------------
# OVERRIDE LEAD → CUSTOMER MAPPING
# ---------------------------------------------------------
override_whitelisted_methods = {
    "erpnext.crm.doctype.lead.lead.make_customer":
        "enhanced_crm.api.custom_make_customer"
}

# ---------------------------------------------------------
# FIXTURES (Custom Fields)
# ---------------------------------------------------------
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["dt", "in", ["Lead", "Customer", "Sales Order"]]
        ]
    }
]
