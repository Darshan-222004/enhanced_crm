"""Setup helpers that provision all required custom fields and doctypes."""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def ensure_customizations():
    """Create/update the custom fields required by the app."""
    frappe.reload_doc("enhanced_crm", "doctype", "verification_log")
    frappe.reload_doc("enhanced_crm", "doctype", "financial_verification_settings")

    custom_fields = {
        "Lead": [
            {
                "fieldname": "boid",
                "label": "BOID",
                "fieldtype": "Data",
                "insert_after": "email_id",
            },
            {
                "fieldname": "pan_number",
                "label": "PAN Number",
                "fieldtype": "Data",
                "insert_after": "boid",
            },
            {
                "fieldname": "bank_account_number",
                "label": "Bank Account Number",
                "fieldtype": "Data",
                "insert_after": "pan_number",
            },
            {
                "fieldname": "ifsc_code",
                "label": "IFSC Code",
                "fieldtype": "Data",
                "insert_after": "bank_account_number",
            },
            {
                "fieldname": "verification_log",
                "label": "Verification Log",
                "fieldtype": "Table",
                "options": "Verification Log",
                "insert_after": "ifsc_code",
            },
            {
                "fieldname": "verify_pan",
                "label": "Verify PAN",
                "fieldtype": "Button",
                "insert_after": "verification_log",
            },
        ],
        "Customer": [
            {
                "fieldname": "boid",
                "label": "BOID",
                "fieldtype": "Data",
                "insert_after": "customer_name",
            },
            {
                "fieldname": "pan_number",
                "label": "PAN Number",
                "fieldtype": "Data",
                "insert_after": "boid",
            },
            {
                "fieldname": "bank_account_number",
                "label": "Bank Account Number",
                "fieldtype": "Data",
                "insert_after": "pan_number",
            },
            {
                "fieldname": "ifsc_code",
                "label": "IFSC Code",
                "fieldtype": "Data",
                "insert_after": "bank_account_number",
            },
            {
                "fieldname": "verification_log",
                "label": "Verification Log",
                "fieldtype": "Table",
                "options": "Verification Log",
                "insert_after": "ifsc_code",
            },
            {
                "fieldname": "verify_pan",
                "label": "Verify PAN",
                "fieldtype": "Button",
                "insert_after": "verification_log",
            },
        ],
        "Sales Order": [
            {
                "fieldname": "verified_pan_number",
                "label": "Verified PAN Number",
                "fieldtype": "Data",
                "read_only": 1,
                "insert_after": "customer",
            },
            {
                "fieldname": "verified_bank_account_number",
                "label": "Verified Bank Account Number",
                "fieldtype": "Data",
                "read_only": 1,
                "insert_after": "verified_pan_number",
            },
        ],
    }

    create_custom_fields(custom_fields, update=True)


def after_install():
    ensure_customizations()


def after_migrate():
    ensure_customizations()
