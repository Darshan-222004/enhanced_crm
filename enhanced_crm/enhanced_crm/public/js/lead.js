// Client script used on Lead to wire up the "Verify PAN" action.
frappe.ui.form.on("Lead", {
    refresh(frm) {
        frm.add_custom_button("Verify PAN", function () {
            frappe.call({
                method: "enhanced_crm.api.verify_pan",
                args: {
                    docname: frm.doc.name,
                    doctype: "Lead"
                },
                callback(r) {
                    frappe.msgprint("Result:<br>" + JSON.stringify(r.message, null, 2));
                    frm.reload_doc();
                }
            });
        });
    }
});
