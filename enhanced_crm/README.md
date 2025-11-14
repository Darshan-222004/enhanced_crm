# Enhanced CRM

Custom ERPNext app that keeps financial identifiers (BOID, PAN, bank account, IFSC) consistent and verified all the way from Lead → Customer → Sales Order.

---

## Features at a glance
- Extra fields on **Lead** and **Customer** (BOID, PAN, Bank Account Number, IFSC) with regex validation.
- **Verification Log** child table that records every PAN/IFSC check.
- “**Verify PAN**” buttons (Lead & Customer) calling `enhanced_crm.api.verify_pan` to simulate an API response and log the result.
- **Financial Verification Settings** singleton where admins can edit mock endpoints/API keys.
- Lead → Customer mapping override that copies the financial fields and the verification log.
- Sales Order getter + client script that auto-fill `Verified PAN Number` and `Verified Bank Account Number` when a customer is selected.

---

## Installation
```bash
cd ~/frappe-bench
bench get-app enhanced_crm /path-or-git-url
bench --site enhanced.localhost install-app enhanced_crm
bench --site enhanced.localhost migrate
bench restart
```

---

## How to test quickly
1. **Create a Lead**  
   Fill BOID, PAN, Bank Account Number, IFSC and click **Save**.
2. **Verify PAN**  
   Press the button; a JSON popup appears and a row is added to “Verification Log”.
3. **Convert to Customer**  
   Use **Create → Customer** from that Lead. Open the Customer to confirm the custom fields + log entries copied.
4. **Verify PAN on Customer**  
   Click the button on the Customer form to log another attempt.
5. **Create a Sales Order**  
   Add a Sales Order for that Customer. The read-only fields `Verified PAN Number` and `Verified Bank Account Number` fill in automatically.
6. **Change API settings**  
   Search “Financial Verification Settings”, change the PAN endpoint/key, save, and run Verify PAN again to see the new endpoint in the result.

That’s it—you now have a ready-to-demo Enhanced CRM app.
