frappe.ui.form.on('Item', {
	refresh(frm) {
		// your code here
	},
    assortment_status:function(cur_frm){
        if(cur_frm.doc.assortment_status == "Listed"){
            cur_frm.set_value('shopify_published_status','True')
            cur_frm.set_value('shopify_status','Active')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(cur_frm.doc.assortment_status == "New Listing"){
            cur_frm.set_value('shopify_published_status','False')
            cur_frm.set_value('shopify_status','Draft')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
            
        }
        if(cur_frm.doc.assortment_status == "Deactivated"){
            cur_frm.set_value('shopify_published_status','False')
            cur_frm.set_value('shopify_status','Archived')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
            
        }
        if(cur_frm.doc.assortment_status == "Stop-Status"){
            cur_frm.set_value('shopify_published_status','False')
            cur_frm.set_value('shopify_status','Draft')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(cur_frm.doc.assortment_status == "Out"){
            cur_frm.set_value('shopify_published_status','True')
            cur_frm.set_value('shopify_status','Active')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(cur_frm.doc.assortment_status == "Temporary Delisted"){
            cur_frm.set_value('shopify_published_status','False')
            cur_frm.set_value('shopify_status','Draft')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(cur_frm.doc.assortment_status == "IN"){
            cur_frm.set_value('shopify_published_status','False')
            cur_frm.set_value('shopify_status','Draft')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(cur_frm.doc.assortment_status == "Temp Listing"){
            cur_frm.set_value('shopify_published_status','True')
            cur_frm.set_value('shopify_status','Active')
            cur_frm.refresh_field('shopify_published_status','shopify_status')
        }
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
        
        
        
        // else{
        //     cur_frm.set_value('item_name',cur_frm.doc.naming_series)
        //     cur_frm.refresh_field('item_name')
        //     cur_frm.set_value('commercial_name_in_german',cur_frm.doc.naming_series)
        //     cur_frm.refresh_field('commercial_name_in_german')
        // }
        
        if(cur_frm.doc.case_dimension_length != 0 && cur_frm.doc.case_dimension_width != 0 && cur_frm.doc.case_dimension_height != 0){
            cur_frm.set_value('case_volume_in_l',flt(cur_frm.doc.case_dimension_length*cur_frm.doc.case_dimension_width*cur_frm.doc.case_dimension_height)/1000)
            cur_frm.refresh_field('case_volume_in_l')
        }
        if (cur_frm.doc.unit_volume_in_l != 0){
            cur_frm.set_value('unit_volume_in_l',flt(cur_frm.doc.case_volume_in_l/cur_frm.doc.units_per_case))
            cur_frm.refresh_field('unit_volume_in_l')
        }
        
        


	},
	after_save(cur_frm){
        cur_frm.doc.uoms.forEach(u =>{
            if(u.uom =="Case"){
                u.conversion_factor = cur_frm.doc.units_per_case;
            }
        }); 
        
        
        },
    //  before_save(cur_frm){
    //     if(cur_frm.doc.brand && cur_frm.doc.description && cur_frm.doc.unit_size_volume && cur_frm.doc.unit_measure && cur_frm.doc.description_german){
    //         let description_value = convertToPlain(cur_frm.doc.description)
    //         // console.log(description_value)
    //         cur_frm.set_value('item_name',cur_frm.doc.brand + " " + description_value  + " "+cur_frm.doc.unit_size_volume + " "+ cur_frm.doc.unit_measure)
    //         cur_frm.refresh_field('item_name')
    //         cur_frm.set_value('commercial_name_in_german',cur_frm.doc.brand + " " +cur_frm.doc.description_german + " "+ cur_frm.doc.unit_size_volume + " "+ cur_frm.doc.unit_measure)
    //         cur_frm.refresh_field('commercial_name_in_german')
    //         }
    //  }   
});


function convertToPlain(html){

    // Create a new div element
    var tempDivElement = document.createElement("div");

    // Set the HTML content with the given value
    tempDivElement.innerHTML = html;

    // Retrieve the text property of the element 
    return tempDivElement.textContent || tempDivElement.innerText || "";
}

// var htmlString= "<div><h1>Bears Beets Battlestar Galactica </h1>\n<p>Quote by Dwight Schrute</p></div>";

// console.log(convertToPlain(htmlString));