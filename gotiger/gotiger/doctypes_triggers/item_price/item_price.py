import frappe
from frappe import _
from frappe.utils import today

def validate(doc,method):
    itemprice = frappe.db.get_value('Item', {'name': doc.item_code}, 'item_code')
    item_doc = frappe.get_doc('Item', itemprice)
    price_item = [c.period_rate for c in item_doc.item_price]
    if doc.price_list_rate not in price_item:
        item_doc.append('item_price',{
            'from_date' :doc.valid_from,
            'to_date': frappe.utils.today(),
            'period_rate':doc.price_list_rate
        })
    item_doc.save()