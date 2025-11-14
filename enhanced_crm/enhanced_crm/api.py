"""Server endpoints and helpers for the Enhanced CRM app.

This module wires together the public APIs used by the client scripts,
overrides ERPNext's lead→customer conversion, and exposes utilities that
populate Sales Orders with the verified financial data.
"""

import json

import frappe
from frappe.utils import now_datetime

from .mapping import copy_financial_fields_and_logs
from erpnext.crm.doctype.lead.lead import make_customer as erpnext_make_customer


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------
def _get_verification_settings():
    return frappe.get_cached_doc("Financial Verification Settings")


def _log_verification(doc, verification_type, status, response):
    """Append a Verification Log row and persist the document."""
    doc.append(
        "verification_log",
        {
            "verification_type": verification_type,
            "status": status,
            "timestamp": now_datetime(),
            "api_response": json.dumps(response),
        },
    )
    doc.save(ignore_permissions=True)


# ---------------------------------------------------------------------------
# Customer financial getters (used by JS + server hook)
# ---------------------------------------------------------------------------
@frappe.whitelist()
def get_customer_financials(customer):
    doc = frappe.get_doc("Customer", customer)
    return {
        "boid": doc.boid or "",
        "pan_number": doc.pan_number or "",
        "bank_account_number": doc.bank_account_number or "",
        "ifsc_code": doc.ifsc_code or "",
    }


def load_customer_financials(doc, method=None):
    """Server hook – populate verified fields when Sales Order loads."""
    if not doc.customer:
        return

    details = get_customer_financials(doc.customer)
    doc.verified_pan_number = details.get("pan_number")
    doc.verified_bank_account_number = details.get("bank_account_number")


# ---------------------------------------------------------------------------
# Lead → Customer mapping override
# ---------------------------------------------------------------------------
def custom_make_customer(source_name, target_doc=None, skip_validate=False):
    customer_doc = erpnext_make_customer(source_name, target_doc, skip_validate)
    copy_financial_fields_and_logs(source_name, customer_doc)
    return customer_doc


# ---------------------------------------------------------------------------
# PAN verification flow
# ---------------------------------------------------------------------------
@frappe.whitelist()
def verify_pan(docname, doctype):
    """
    Universal PAN verification for Lead & Customer.
    Reads mock API settings, simulates a response, logs it.
    """

    if doctype not in {"Lead", "Customer"}:
        frappe.throw("PAN verification is only available for Lead or Customer.")

    doc = frappe.get_doc(doctype, docname)
    if not doc.pan_number:
        frappe.throw("Please set a PAN Number before verifying.")

    settings = _get_verification_settings()
    endpoint = settings.pan_api_endpoint or "https://mock-pan.example/api"
    api_key = settings.pan_api_key or "demo-pan-key"

    # Simulate the response – consider PANs ending with digits 0-4 as failures.
    is_valid = bool(doc.pan_number) and doc.pan_number[-1] not in {"0", "1", "2", "3", "4"}

    display_name = doc.get("customer_name") or doc.get("company_name") or doc.get("lead_name")

    response_data = {
        "status": "valid" if is_valid else "invalid",
        "full_name": display_name or "Unknown",
        "pan": doc.pan_number,
        "endpoint_called": endpoint,
        "api_key_used": bool(settings.pan_api_key),
    }

    status = "Success" if is_valid else "Failed"
    _log_verification(doc, "PAN", status, response_data)

    return response_data
