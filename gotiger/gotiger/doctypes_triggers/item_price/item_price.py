import frappe
from frappe import _
from frappe.utils import today, add_to_date

def validate(doc,method):
    # When is a new document, just ignore
    if doc.is_new():
        return
    
    # Fetch previous rate and validity start
    old_rate, old_valid_from = frappe.db.get_value(doc.doctype, doc.name, ['price_list_rate', 'valid_from'])
    
    if old_rate != doc.rate:
        _today = today()
        
        # Ensure validity on actual document
        doc.valid_from = _today
        doc.valid_upto = None
        
        # Insert an historical price
        frappe.new_doc('Item Price').update({
            'item_code': doc.item_code,
            'uom': doc.uom,
            'packing_unit': doc.packing_unit,
            'item_name': doc.item_name,
            'item_description': doc.item_description,
            'price_list': doc.price_list,
            'buying': doc.buying,
            'selling': doc.selling,
            'currency': doc.currency,
            'price_list_rate': old_rate,
            'valid_from': old_valid_from,
            'valid_upto': add_to_date(_today, days=-1)
        }).insert()
