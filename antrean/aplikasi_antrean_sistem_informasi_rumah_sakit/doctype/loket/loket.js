// Copyright (c) 2023, Muhamad Jafar Sidik and contributors
// For license information, please see license.txt

frappe.ui.form.on('Loket', {
	refresh: function(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button('Panggil Antrean', () => {
				//frappe.new_doc("Transaksi Antrean", {"loket": frm.doc.nama_loket}, doc => {
					// doc.posting_date = frappe.datetime.get_today();
					// let row = frappe.model.add_child(doc, "accounts");
					// row.account = 'Bank - A';
					// row.account_currency = 'USD';
					// row.debit_in_account_currency = 100.0;
					// row.credit_in_account_currency = 0.0;
				//});
				
			},);
		}
	}
	
});
