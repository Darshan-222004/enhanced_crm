// Whenever a customer is chosen, pull the verified financial details.
frappe.ui.form.on("Sales Order", {
    customer: function(frm) {
        if (!frm.doc.customer) return;

        frappe.call({
            method: "enhanced_crm.api.get_customer_financials",
            args: {
                customer: frm.doc.customer
            },
            callback: function(r) {
                if (!r.message) return;

                frm.set_value("verified_pan_number", r.message.pan_number);
                frm.set_value("verified_bank_account_number", r.message.bank_account_number);
                frm.refresh_fields();
            }
        });
    }
});
