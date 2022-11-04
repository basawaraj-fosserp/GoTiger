frappe.ui.form.on('Item', {
	refresh(frm) {
		// your code here
	},
    assortment_status:function(frm){
        if(frm.doc.assortment_status == "Listed"){
            frm.set_value('shopify_published_status','True')
            frm.set_value('shopify_status','Active')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(frm.doc.assortment_status == "New Listing"){
            frm.set_value('shopify_published_status','False')
            frm.set_value('shopify_status','Draft')
            frm.refresh_field('shopify_published_status','shopify_status')
            
        }
        if(frm.doc.assortment_status == "Deactivated"){
            frm.set_value('shopify_published_status','False')
            frm.set_value('shopify_status','Archived')
            frm.refresh_field('shopify_published_status','shopify_status')
            
        }
        if(frm.doc.assortment_status == "Stop-Status"){
            frm.set_value('shopify_published_status','False')
            frm.set_value('shopify_status','Draft')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(frm.doc.assortment_status == "Out"){
            frm.set_value('shopify_published_status','True')
            frm.set_value('shopify_status','Active')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(frm.doc.assortment_status == "Temporary Delisted"){
            frm.set_value('shopify_published_status','False')
            frm.set_value('shopify_status','Draft')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(frm.doc.assortment_status == "IN"){
            frm.set_value('shopify_published_status','False')
            frm.set_value('shopify_status','Draft')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
        if(frm.doc.assortment_status == "Temp Listing"){
            frm.set_value('shopify_published_status','True')
            frm.set_value('shopify_status','Active')
            frm.refresh_field('shopify_published_status','shopify_status')
        }
    },
    
	validate(frm){
	    if(frm.doc.assortment_status =="Deactivated"){
            frm.set_value('end_date',frappe.datetime.nowdate());
            frm.refresh_field('end_date');
        }
        if(frm.doc.units_per_case === 0){
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
        
        
        
        // else{
        //     frm.set_value('item_name',frm.doc.naming_series)
        //     frm.refresh_field('item_name')
        //     frm.set_value('commercial_name_in_german',frm.doc.naming_series)
        //     frm.refresh_field('commercial_name_in_german')
        // }
        
        if(frm.doc.case_dimension_length != 0 && frm.doc.case_dimension_width != 0 && frm.doc.case_dimension_height != 0){
            frm.set_value('case_volume_in_l',flt(frm.doc.case_dimension_length*frm.doc.case_dimension_width*frm.doc.case_dimension_height)/1000)
            frm.refresh_field('case_volume_in_l')
        }
        
        if (frm.doc.units_per_case != 0){
            frm.set_value('unit_volume_in_l',flt(frm.doc.case_volume_in_l/frm.doc.units_per_case))
            frm.refresh_field('unit_volume_in_l')
        }
        
        


	},
	after_save(frm){
        frm.doc.uoms.forEach(u =>{
            if(u.uom =="Case"){
                u.conversion_factor = frm.doc.units_per_case;
            }
        }); 
        
        
        },
    //  before_save(frm){
    //     if(frm.doc.brand && frm.doc.description && frm.doc.unit_size_volume && frm.doc.unit_measure && frm.doc.description_german){
    //         let description_value = convertToPlain(frm.doc.description)
    //         // console.log(description_value)
    //         frm.set_value('item_name',frm.doc.brand + " " + description_value  + " "+frm.doc.unit_size_volume + " "+ frm.doc.unit_measure)
    //         frm.refresh_field('item_name')
    //         frm.set_value('commercial_name_in_german',frm.doc.brand + " " +frm.doc.description_german + " "+ frm.doc.unit_size_volume + " "+ frm.doc.unit_measure)
    //         frm.refresh_field('commercial_name_in_german')
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