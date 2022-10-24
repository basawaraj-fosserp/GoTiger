frappe.ui.form.on('Purchase Order', {
	refresh(frm) {
    		frm.add_custom_button('Calculate and Import Required Items', () => {
                if(!frm.doc.set_warehouse){
                    frappe.throw("Please Set Value In Target Warehouse")
                }
                if(!frm.doc.supplier){
                    frappe.throw("Please Set Value In Supplier")
                }
                
                frappe.call({
                    method:'gotiger.gotiger.doctypes_triggers.purchase_order.purchase_order.append_items',
                    args: {
                        'supplier':frm.doc.supplier,
                         'name':frm.doc.name
                    },
                    callback:function(r){
                            console.log(r);
                            frm.reload_doc();
                    }
                })
            }, 'Tools');
            
	}
})