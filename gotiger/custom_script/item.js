frappe.ui.form.on('Item', {
	refresh(frm) {
		// your code here
	},
	validate(frm){
	    if(frm.doc.assortment_status =="Deactivated"){
            frm.set_value('end_date',frappe.datetime.nowdate());
            frm.refresh_field('end_date');
        }
	},
	after_save(frm){
	    if(frm.doc.units_per_case){
            var tbl = frm.doc.uoms;
                    var i = tbl.length;
                    while (i--)
                    {
                        if(frm.doc.units_per_case === 0)
                        {
                            frm.get_field("uoms").grid.grid_rows[i].remove();
                        }
                    }
                    frm.refresh_field("uoms");
	    }        
        frm.doc.uoms.forEach(u =>{
            if(u.uom =="Case"){
                u.conversion_factor = frm.doc.units_per_case;
            }
        }); 
        
        
        }
});