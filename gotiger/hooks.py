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
                "Item-temperature_zone","Item-shopify_running_number","Item-description_german","Item-launch_date","Item-column_break_30","Item-other_details","Item-case_dimension_length","Item-case_dimension_width","Item-case_dimension_height","Item-column_break_55","Item-unit_dimension_length","Item-unit_dimension_width","Item-unit_dimension_height","Item-case_volume_in_l","Item-unit_volume_in_l","Item-case_weight_in_g","Supplier-payment_type","Item-commercial_name_in_german","Item-main_category","Item Supplier-pallet_factor","Item-class_of_fruit_and_veg","Item-packaging_weight","Item-unit_weight","Item-case_weight","Item-pallet_weight","Item-intrastat_code","Item-gt_country_of_origin","Item-gt_cuisine","Item-product_claim","Item-assortment_status","Item-shopify_published_status","Item-shopify_status","Item-unit_size_volume","Item-unit_measure","Item Supplier-layer_factor","Item-warehouse_shelf_life","Item-store_shelf_life","Item-customer_shelf_life","Purchase Order-delivery_time","Item Group-temperature_zone","Item-units_per_case","Item-end_date","Item-gt_packaging","Item Barcode-packaging_bar_code"
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

