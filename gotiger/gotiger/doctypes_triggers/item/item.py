import frappe
from frappe import _
from frappe.utils import today
import html2text

def validate(doc,method):
    set_item_name(doc)
    set_status_on_change(doc)
    set_dates(doc)
    uom_value = 'Case'
    uoms_list = [d.uom for d in doc.uoms]
    if doc.units_per_case and uom_value not in uoms_list:
        doc.append('uoms', {
            'uom': uom_value,
            'conversion_factor':doc.units_per_case
        })

    # if doc.case_dimension_length != 0 and doc.case_dimension_width != 0 and doc.case_dimension_height != 0:
    #     doc.case_volume_in_l = (doc.case_dimension_length*doc.case_dimension_width*doc.case_dimension_height)/1000
    # if doc.units_per_case != 0:
    #     doc.unit_volume_in_l = doc.case_volume_in_l/doc.units_per_case

    for barcode in doc.barcodes:
        if len(barcode.barcode) >= 12:
            barcode.barcode_type = "UPC-A"
        if len(barcode.barcode) >= 13:
            # frappe.msgprint(str(barcode.barcode))
            barcode.barcode_type = "EAN"    

def set_item_name(doc):
    doc.item_name = html2text.html2text(doc.brand + " " +doc.description + " "+ str(doc.unit_size_volume) + " "+ doc.unit_measure)
    doc.commercial_name_in_german = html2text.html2text(doc.brand + " " +doc.description_german + " "+ str(doc.unit_size_volume) + " "+ doc.unit_measure)

def set_status_on_change(doc):
    if doc.assortment_status == "Listed":
        doc.shopify_status = "Active"
        doc.shopify_published_status = "True"
    elif doc.assortment_status == "New Listing":
        doc.shopify_status = "Draft"
        doc.shopify_published_status = "False"
    elif doc.assortment_status == "Sourcing":
        doc.shopify_status = "Draft"
        doc.shopify_published_status = "False"
    elif doc.assortment_status == "Temp Listing":
        doc.shopify_status = "Active"
        doc.shopify_published_status = "True"
        set_is_purchase(doc)
    elif doc.assortment_status == "Out":
        doc.shopify_status = "Active"
        doc.shopify_published_status = "True"
        set_is_purchase(doc)
    elif doc.assortment_status == "Temp Delisting":
        doc.shopify_status = "Draft"
        doc.shopify_published_status = "False"
        set_is_purchase(doc)
    elif doc.assortment_status == "Deactivated":
        doc.shopify_status = "Archived"
        doc.shopify_published_status = "False"
        set_is_purchase(doc)

def set_is_purchase(doc):
    doc.is_purchase_item = 0

def set_dates(doc):
    old_assort = frappe.db.get_value("Item", doc.name, "assortment_status")

    if doc.assortment_status != old_assort:
        if doc.assortment_status == "Listed":
            doc.listed_date = today()
        elif doc.assortment_status == "Deactivated":
            doc.deactivated_date = today()
