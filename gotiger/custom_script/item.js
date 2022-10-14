frappe.ui.form.on('Item', {
	refresh(frm) {
		// your code here
	},
	validate(cur_frm){
	    if(cur_frm.doc.assortment_status =="Deactivated"){
            cur_frm.set_value('end_date',frappe.datetime.nowdate());
            cur_frm.refresh_field('end_date');
        }
        if(cur_frm.doc.units_per_case === 0){
            var tbl = cur_frm.doc.uoms;
                    var i = tbl.length;
                    while (i--)
                    {
                        if(cur_frm.doc.units_per_case === 0)
                        {
                            cur_frm.get_field("uoms").grid.grid_rows[i].remove();
                        }
                    }
                    cur_frm.refresh_field("uoms");
	    } 
        cur_frm.set_value('case_volume_in_l',flt(cur_frm.doc.case_dimension_length*cur_frm.doc.case_dimension_width*cur_frm.doc.case_dimension_height)/1000)  
        cur_frm.refresh_field('case_volume_in_l') 
        if(cur_frm.doc.units_per_case != 0){
            cur_frm.set_value('unit_volume_in_l',flt(cur_frm.doc.case_volume_in_l/cur_frm.doc.units_per_case))  
            cur_frm.refresh_field('unit_volume_in_l')
        }
        
	},
	after_save(cur_frm){
        cur_frm.doc.uoms.forEach(u =>{
            if(u.uom =="Case"){
                u.conversion_factor = frm.doc.units_per_case;
            }
            cur_frm.refresh_field("uoms");
        }); 
        
        
        }
});