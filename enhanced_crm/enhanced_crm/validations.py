"""Validation hooks for Lead and Customer financial fields."""

import re

import frappe

# PAN Format: ABCDE1234F
PAN_REGEX = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

# IFSC Format: ABCD0XXXXXX
IFSC_REGEX = r"^[A-Z]{4}0[A-Z0-9]{6}$"

def validate_lead_or_customer(doc, method=None):

    # --------------------------
    # BOID → Must be 16 digits
    # --------------------------
    if doc.boid and not re.fullmatch(r"\d{16}", doc.boid):
        frappe.throw("BOID must be exactly 16 digits.")

    # --------------------------
    # PAN Format Validation
    # --------------------------
    if doc.pan_number and not re.fullmatch(PAN_REGEX, doc.pan_number):
        frappe.throw("Invalid PAN format. Expected format: ABCDE1234F")

    # --------------------------
    # IFSC Format Validation
    # --------------------------
    if doc.ifsc_code and not re.fullmatch(IFSC_REGEX, doc.ifsc_code):
        frappe.throw("Invalid IFSC Code format (e.g., HDFC0XXXXXX).")

    # --------------------------
    # Bank Account Number
    # --------------------------
    if doc.bank_account_number:
        if not doc.bank_account_number.isdigit():
            frappe.throw("Bank Account Number must contain digits only.")

        if len(doc.bank_account_number) < 9:
            frappe.throw("Bank Account Number must be at least 9 digits.")
