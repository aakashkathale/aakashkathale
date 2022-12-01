# Copyright (c) 2022, indictrans and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.utils import nowdate, nowtime
from frappe.model.document import Document

class CustomSitePlanning(Document):
	pass

@frappe.whitelist()
def get_site_details(site_name, date):
	
	#fetch date and site_name from custom site details and custom tiffin details 
	if date and site_name:
		data = frappe.db.sql("""select * from `tabCustom Site Details` sd join `tabCustom Tiffin Details` td on td.parent = sd.name where sd.date = '{0}' and sd.name = '{1}' """.format(date, site_name), as_dict = 1, debug = 1)
		return data		

@frappe.whitelist()
def delivery_note(site_name):

	result = json.loads(site_name)
	customer_name = frappe.db.get_value("Custom Site Details", result['site_name'], "customer")
	site_data = frappe.get_doc("Custom Site Details", result['site_name'])
	qty = result['labour_count']
	a = frappe.new_doc("Delivery Note")
	
	#fetch nowdate
	a.date = nowdate()

	#fetch nowtime
	a.posting_time = nowtime()

	#fetch the customer_name
	a.customer = customer_name

	#fetch the site_name
	a.site_name = result['site_name']

	#fetch the Item code, code, uom 
	a.append(
		"items",
		{
			"item_code" : "FG-CK-0001",
			"qty" :	qty,
			"UOM" : "stock_uom"
		},
	)

	#fetch the type and tiffin_details
	for row in site_data.tiffin_details:
		a.append('tiffin_details',{'type':row.type,'no_of_tiffin':row.no_of_tiffin})

	a.save()

	frappe.msgprint('Delivery Note Created')
	
	