app_name = "site_name_swap"
app_title = "Site Name Swap"
app_publisher = "munyaradzi chirove"
app_description = "This app changes the url and site name of a frappe site"
app_email = "chirovemunyaradzi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "site_name_swap",
# 		"logo": "/assets/site_name_swap/logo.png",
# 		"title": "Site Name Swap",
# 		"route": "/site_name_swap",
# 		"has_permission": "site_name_swap.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/site_name_swap/css/site_name_swap.css"
# app_include_js = "/assets/site_name_swap/js/site_name_swap.js"

# include js, css files in header of web template
# web_include_css = "/assets/site_name_swap/css/site_name_swap.css"
# web_include_js = "/assets/site_name_swap/js/site_name_swap.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "site_name_swap/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "site_name_swap/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "site_name_swap.utils.jinja_methods",
# 	"filters": "site_name_swap.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "site_name_swap.install.before_install"
# after_install = "site_name_swap.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "site_name_swap.uninstall.before_uninstall"
# after_uninstall = "site_name_swap.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "site_name_swap.utils.before_app_install"
# after_app_install = "site_name_swap.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "site_name_swap.utils.before_app_uninstall"
# after_app_uninstall = "site_name_swap.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "site_name_swap.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"site_name_swap.tasks.all"
# 	],
# 	"daily": [
# 		"site_name_swap.tasks.daily"
# 	],
# 	"hourly": [
# 		"site_name_swap.tasks.hourly"
# 	],
# 	"weekly": [
# 		"site_name_swap.tasks.weekly"
# 	],
# 	"monthly": [
# 		"site_name_swap.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "site_name_swap.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "site_name_swap.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "site_name_swap.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["site_name_swap.utils.before_request"]
# after_request = ["site_name_swap.utils.after_request"]

# Job Events
# ----------
# before_job = ["site_name_swap.utils.before_job"]
# after_job = ["site_name_swap.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"site_name_swap.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

