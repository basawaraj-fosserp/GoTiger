import frappe
from frappe import _
from frappe.utils import today
import html2text

def validate(doc,method):
    set_item_name(doc)
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
