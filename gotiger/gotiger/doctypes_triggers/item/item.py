import frappe
from frappe import _

def validate(doc,method):
    uom_value = 'Case'
    uoms_list = [d.uom for d in doc.uoms]
    if doc.units_per_case and uom_value not in uoms_list:
        doc.append('uoms', {
            'uom': uom_value,
            'conversion_factor':doc.units_per_case
        })

    doc.case_volume_in_l = (doc.case_dimension_length*doc.case_dimension_width*doc.case_dimension_height)/1000
    if doc.units_per_case != 0:
        doc.unit_volume_in_l = doc.case_volume_in_l/doc.units_per_case

    for barcode in doc.barcodes:
        if len(barcode.barcode) >= 12:
            barcode.barcode_type = "UPC-A"
        if len(barcode.barcode) >= 13:
            # frappe.msgprint(str(barcode.barcode))
            barcode.barcode_type = "EAN"