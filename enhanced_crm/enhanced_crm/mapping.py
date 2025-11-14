"""Helper utilities that move financial data between documents."""

import frappe

# Fields to copy from Lead to Customer
CUSTOM_FIELDS = ["boid", "pan_number", "bank_account_number", "ifsc_code"]

def copy_financial_fields_and_logs(lead_name: str, customer_doc):
    """
    Called during Lead → Customer conversion.
    Copies:
        - BOID
        - PAN
        - Bank Account Number
        - IFSC Code
        - All Verification Log rows
    """

    lead = frappe.get_doc("Lead", lead_name)

    # ---------------------------------------------------------
    # 1. Copy simple value fields
    # ---------------------------------------------------------
    for field in CUSTOM_FIELDS:
        if hasattr(lead, field):
            setattr(customer_doc, field, getattr(lead, field))

    # ---------------------------------------------------------
    # 2. Copy Verification Log (child table)
    # ---------------------------------------------------------
    customer_doc.set("verification_log", [])

    if hasattr(lead, "verification_log") and lead.verification_log:
        for row in lead.verification_log:
            customer_doc.append("verification_log", {
                "timestamp": row.timestamp,
                "verification_type": row.verification_type,
                "status": row.status,
                "api_response": row.api_response
            })

    return customer_doc
