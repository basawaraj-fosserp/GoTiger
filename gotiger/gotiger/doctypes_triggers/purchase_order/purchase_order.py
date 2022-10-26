
import frappe

@frappe.whitelist()
def append_items(supplier, name):
    # Get the actual PO
    doc = frappe.get_doc('Purchase Order', name)

    # Get the Plans filtered by supplier and warehouse
    plans = frappe.get_list('Item Purchase Plan', filters={
        'supplier': supplier,
        'warehouse': doc.set_warehouse
    }, fields='*')

    # Iterate trought the plans
    for plan in plans:
        # Fetch the purchase_uom and stock_uom
        purchase_uom, stock_uom = frappe.db.get_value('Item', {
            'item_code': plan.item
        }, ['purchase_uom', 'stock_uom'])

        if not purchase_uom:
            # assume purchase_uom is stock_uom
            purchase_uom = stock_uom
        
        # Fetch the conversion factor from the purchase_uom
        conversion = frappe.db.get_value('UOM Conversion Detail', {
            'parent': plan.item, 
            'uom': purchase_uom
        }, 'conversion_factor') or 1.0
        
        try:
            actual_qty, ordered_qty = frappe.db.get_value('Bin', {
                'warehouse': plan.warehouse,
                'item_code': plan.item
            }, ['actual_qty', 'ordered_qty'])
        except TypeError as e:
            # This happen, when the item have no registry in stock yet
            # no stock transaction, no transfer, no receive, nothing
            # probably this is a fresh item
            actual_qty, ordered_qty = 0, 0

        # We compute how many in the next days
        qty = (plan.sales_velocity + plan.coverage_days) * plan.lead_time_in_days
        
        # we reduce the actual stock and the
        #  items on transit (ordered but not received yet)
        qty -= (actual_qty + ordered_qty)

        # We divide everything by the conversion factor
        qty /= conversion

        if qty < 0:
            # We have enought stock, so nothing to do here
            continue

        # Verify if PO already have the item
        if (d := doc.get('items', {'item_code': plan.item})):
            d = d[0]
        else:
            # Othewise create a new line
            d = doc.append('items', {'item_code': plan.item})
        
        # Set the item values to initiate the transaction
        d.update({
            'qty': qty,
            'warehouse': plan.warehouse,
            'uom': purchase_uom,
            'stock_uom': stock_uom,
            'conversion_factor': conversion
        })

    # Force ERPNext to fetch all missing information on PO and Items
    doc.run_method('set_missing_values')
    
    # Force ERPNext to recalculate taxes and totals
    doc.run_method('calculate_taxes_and_totals')
    
    # TODO: This should be aways avoided
    # -- append_items should respond to a "GET"
    # the doc should be returned to screen and synced
    # save only should happen, when the data is trustable
    doc.save()
