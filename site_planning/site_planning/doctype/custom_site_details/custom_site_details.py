# Copyright (c) 2022, indictrans and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate
from frappe.model.document import Document

class CustomSiteDetails(Document):
	pass
# 	def before_save(self):
# 		print("----",self)
# 		Custom_Site_Details(self)

def Custom_Site_Details(doc):
	print("=====",doc)
	a = frappe.new_doc("Custom Site Planning")
	a.transaction_date = nowdate()
	a.date = nowdate()
	a.append("site_planning", {

	"site_name"	:doc.site_name,
	"labour_count" :doc.labour_count,
	# "gud__achar" : doc.tiffin_details.gud__achar,
	# "roti" : doc.tiffin_details.roti,
	# "dal" : doc.tiffin_details.dal,
	# "rice" : doc.tiffin_details.rice,
	# "salad" : doc.tiffin_details.salad,
	# "driver_name" : doc.driver_name,
	# "vehicle_no" : doc.vehicle_no 
	})
	a.save()


	

