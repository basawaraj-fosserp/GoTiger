from . import __version__ as app_version

app_name = "gotiger"
app_title = "Gotiger"
app_publisher = "Raaj Tailor"
app_description = "Customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "raaj@akhilaminc.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gotiger/css/gotiger.css"
# app_include_js = "/assets/gotiger/js/gotiger.js"

# include js, css files in header of web template
# web_include_css = "/assets/gotiger/css/gotiger.css"
# web_include_js = "/assets/gotiger/js/gotiger.js"

doctype_js = {
	"Item":"custom_script/item.js"
	}

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gotiger/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gotiger.install.before_install"
# after_install = "gotiger.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gotiger.uninstall.before_uninstall"
# after_uninstall = "gotiger.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gotiger.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item":{
		"validate":"gotiger.gotiger.doctypes_triggers.item.item.validate"
	},
	"Item Price":{
		"validate":"gotiger.gotiger.doctypes_triggers.item_price.item_price.validate"
	}
}

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gotiger.tasks.all"
#	],
#	"daily": [
#		"gotiger.tasks.daily"
#	],
#	"hourly": [
#		"gotiger.tasks.hourly"
#	],
#	"weekly": [
#		"gotiger.tasks.weekly"
#	]
#	"monthly": [
#		"gotiger.tasks.monthly"
#	]
# }

fixtures = [
	{"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Item-temperature_zone","Item-shopify_running_number","Item-description_german","Item-launch_date","Item-column_break_30","Item-other_details","Item-case_dimension_length","Item-case_dimension_width","Item-case_dimension_height","Item-column_break_55","Item-unit_dimension_length","Item-unit_dimension_width","Item-unit_dimension_height","Item-case_volume_in_l","Item-unit_volume_in_l","Item-case_weight_in_g","Supplier-payment_type","Item-commercial_name_in_german","Item-main_category","Item Supplier-pallet_factor","Item-class_of_fruit_and_veg","Item-packaging_weight","Item-unit_weight","Item-case_weight","Item-pallet_weight","Item-intrastat_code","Item-gt_country_of_origin","Item-gt_cuisine","Item-product_claim","Item-assortment_status","Item-shopify_published_status","Item-shopify_status","Item-unit_size_volume","Item-unit_measure","Item Supplier-layer_factor","Item-warehouse_shelf_life","Item-store_shelf_life","Item-customer_shelf_life","Purchase Order-delivery_time","Item Group-temperature_zone","Item-units_per_case","Item-end_date","Item-gt_packaging","Item Barcode-packaging_bar_code","Item-description_german","Item-item_price"
            ]
        ]
    ]},
	{"dt": "Property Setter", "filters": [
        [
            "name", "in", ["Purchase Receipt Item-from_warehouse-hidden","Purchase Invoice Item-from_warehouse-hidden","Delivery Note Item-target_warehouse-hidden","Sales Invoice Item-target_warehouse-hidden","Purchase Invoice-scan_barcode-hidden","Sales Invoice-scan_barcode-hidden","Stock Entry-scan_barcode-hidden","POS Invoice-scan_barcode-hidden","Purchase Receipt-scan_barcode-hidden","Delivery Note-scan_barcode-hidden","Material Request-scan_barcode-hidden","Sales Order-scan_barcode-hidden","Purchase Order-scan_barcode-hidden","Item-barcodes-hidden","Stock Entry Detail-barcode-hidden","Clinical Procedure Item-barcode-hidden","Sales Invoice Item-barcode-hidden","Item Barcode-barcode-hidden","POS Invoice Item-barcode-hidden","Delivery Note Item-barcode-hidden","Job Card-barcode-hidden","Stock Reconciliation Item-barcode-hidden","Purchase Receipt Item-barcode-hidden","Item-item_code-hidden","Item-item_code-reqd","Item-naming_series-reqd","Item-naming_series-hidden","Item-weight_uom-hidden","Item-weight_per_unit-hidden","Item-has_serial_no-hidden","Item-retain_sample-hidden","Item-create_new_batch-hidden","Item-variants_section-hidden","Warehouse-account-hidden","Warehouse-default_in_transit_warehouse-hidden","Purchase Order-more_info-hidden","Purchase Order-subscription_section-hidden","Purchase Order-payment_schedule_section-read_only","Purchase Order-shipping_rule-hidden","Purchase Order Item-stock_qty-label","Purchase Order-sec_warehouse-hidden","Purchase Order-accounting_dimensions_section-hidden","Purchase Order-cost_center-default","Purchase Order-apply_tds-hidden","Purchase Order-get_items_from_open_material_requests-hidden","Purchase Order-schedule_date-label","Purchase Order-transaction_date-label","Item-lead_time_days-hidden","Item-safety_stock-hidden","Item-min_order_qty-hidden","Item Supplier-supplier_part_no-label","Item-has_expiry_date-default","Item-has_batch_no-default","Item-description-read_only","Item-opening_stock-hidden","Purchase Receipt-naming_series-options","Delivery Note-naming_series-options","Sales Order-naming_series-options","Purchase Order-naming_series-options","Sales Invoice-naming_series-options","Item-main-quick_entry","Item-description-label","Item-item_group-label","Item-hub_publishing_sb-hidden","Item-inspection_criteria-hidden","Item-manufacturing-hidden","Item-customer_details-hidden","Item-deferred_expense_section-hidden","Item-deferred_revenue-hidden","Item-sales_details-hidden","Item-delivered_by_supplier-hidden","Item-is_customer_provided_item-hidden","Item-valuation_method-hidden","Item-default_material_request_type-hidden","Item-end_of_life-hidden","Item-warranty_period-hidden","Item-is_item_from_hub-hidden","Item-over_billing_allowance-hidden","Item-over_delivery_receipt_allowance-hidden","Item-is_fixed_asset-hidden","Item-include_item_in_manufacturing-hidden","Item-valuation_rate-hidden","Item-item_name-label","Item-item_code-label","Supplier-is_internal_supplier-hidden","Supplier-is_transporter-hidden","Supplier-prevent_pos-hidden","Supplier-prevent_rfqs-hidden","Supplier-warn_pos-hidden","Supplier-warn_rfqs-hidden","Supplier-pan-hidden","Supplier-supplier_group-hidden","Supplier-supplier_group-default","Supplier-supplier_group-in_standard_filter","Supplier-supplier_group-in_list_view","Contact-designation-label","Item-naming_series-default","Item-naming_series-options","Item-allow_alternative_item-hidden","Item-brand-in_list_view","Item-opening_stock-in_list_view","Item-item_code-in_list_view","Item-item_group-in_list_view","Item-item_name-in_list_view","Purchase Receipt-provisional_expense_account-hidden","Packed Item-rate-read_only","Delivery Note-tax_id-print_hide","Delivery Note-tax_id-hidden","Sales Invoice-tax_id-print_hide","Sales Invoice-tax_id-hidden","Sales Order-tax_id-print_hide","Sales Order-tax_id-hidden","Customer-naming_series-hidden","Customer-naming_series-reqd"
            ]
        ]
    ]}
]

# Testing
# -------

# before_tests = "gotiger.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gotiger.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gotiger.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gotiger.auth.validate"
# ]

