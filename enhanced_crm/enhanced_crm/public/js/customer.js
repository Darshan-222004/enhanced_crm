// Client script used on Customer to reuse the "Verify PAN" flow.
frappe.ui.form.on("Customer", {
    refresh(frm) {
        frm.add_custom_button("Verify PAN", function () {
            frappe.call({
                method: "enhanced_crm.api.verify_pan",
                args: {
                    docname: frm.doc.name,
                    doctype: "Customer"
                },
                callback(r) {
                    frappe.msgprint("Result:<br>" + JSON.stringify(r.message, null, 2));
                    frm.reload_doc();
                }
            });
        });
    }
});
