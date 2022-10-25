from unicodedata import name
import frappe

@frappe.whitelist()
def append_items(supplier,name):
    
    # doc = json.loads(doc)
    item_doc = frappe.get_doc('Item Purchase Plan', {'supplier':supplier })
    # frappe.msgprint(str(item_doc))
    # frappe.msgprint(str(item_doc.item))
    
    purchase_doc = frappe.get_doc('Purchase Order',{'name':name})
    # frappe.msgprint(str(purchase_doc.supplier))

    qty_value = frappe.db.sql("""
        select
        po.supplier,
        poi.item_code,
        poi.qty, 
        poi.received_qty,
        (poi.qty - poi.received_qty) as remain_qty
        from
        `tabPurchase Order` po,
        `tabPurchase Order Item` poi
        LEFT JOIN `tabPurchase Invoice Item` pii ON pii.po_detail = poi.name
        where
        poi.parent = po.name
        and po.docstatus = 1 and po.supplier = %s and poi.item_code = %s """,
        (purchase_doc.supplier,item_doc.item),as_dict = 1)	   
    # frappe.msgprint(str(qty_value[0]['remain_qty']))    
    
    if purchase_doc.supplier == item_doc.supplier:
       for item in purchase_doc.items: 
        if item.item_code == item_doc.item:
            uom_value = frappe.get_doc('Item',{'item_code':item_doc.item})
            # frappe.msgprint(str(uom_value.uoms))
            for u in uom_value.uoms:
                # frappe.msgprint(u.uom)
                if u.uom == "Case":
                    item.uom = u.uom
                    item.conversion_factor = uom_value.units_per_case
                    item_purchase_calculation = (((item_doc.sales_velocity*item_doc.lead_time_in_days)+(item_doc.sales_velocity*item_doc.coverage_days)) - (qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))))/uom_value.units_per_case
                    frappe.msgprint(str(item_purchase_calculation))
                    if item_purchase_calculation > 0:
                    # item.qty = qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))
                        item.qty = round((((item_doc.sales_velocity*item_doc.lead_time_in_days)+(item_doc.sales_velocity*item_doc.coverage_days)) - (qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))))/uom_value.units_per_case)
                        item.rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                        item.price_list_rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                        item.base_price_list_rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                        # item.amount = qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))*frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                        item.amount = round((((item_doc.sales_velocity*item_doc.lead_time_in_days)+(item_doc.sales_velocity*item_doc.coverage_days)) - (qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))))/uom_value.units_per_case*frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate'))
                    else:
                        frappe.throw("Qty value Can Not Be Negative")    
                else:
                    # item.qty = qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))
                    item.qty = ((item_doc.sales_velocity*item_doc.lead_time_in_days)+(item_doc.sales_velocity*item_doc.coverage_days)) - (qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days)))
                    item.rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                    item.price_list_rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                    item.base_price_list_rate = frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                    # item.amount = qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))*frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
                    #item.amount = ((item_doc.sales_velocity*item_doc.lead_time_in_days)+(item_doc.sales_velocity*item_doc.coverage_days)) - (qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days)))*frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')

            # purchase_doc.append("items",{
            #     'item_code':item_doc.item,
            #     'item_name':item_doc.item_name,
            #     'qty':qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days)),
            #     'price_list_rate':frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate'),
            #     'base_price_list_rate':frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate'),
            #     'rate': frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate'),
            #     'amount':qty_value[0]['remain_qty'] + frappe.db.get_value('Bin',{'warehouse':item_doc.warehouse,'item_code':item_doc.item},'actual_qty')-((item_doc.sales_velocity*item_doc.lead_time_in_days)-(item_doc.sales_velocity*item_doc.coverage_days))*frappe.db.get_value('Item Price',{'price_list':purchase_doc.buying_price_list,'item_code':item_doc.item},'price_list_rate')
            # })
  
    purchase_doc.save()  
           
   
