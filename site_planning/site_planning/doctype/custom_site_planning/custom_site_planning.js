// Copyright (c) 2022, indictrans and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom Site Planning', {
	refresh : function(frm,cdt,cdn){
		if (frm.doc.docstatus == 1){	
			// add custom button 		
			frm.add_custom_button(__('Create Delivery Note'), function() {
				if (frm.doc.site_planning){				
					$.each(frm.doc.site_planning, function(idx, item){
					// add the frappe.call
					frappe.call({
						method : "site_planning.site_planning.doctype.custom_site_planning.custom_site_planning.delivery_note", 						 	
						args : {
							'site_name' : item
						}
					})			
				})
			}
			}, __('Action'));		
		}
	}
});

frappe.ui.form.on('Custom Site Planning Item', {
	site_name: function(frm,cdt,cdn){
		var row = locals[cdt][cdn]
		if(row.site_name){
			frappe.call({
				method : "site_planning.site_planning.doctype.custom_site_planning.custom_site_planning.get_site_details",
				args : {
					date : frm.doc.date,
					site_name : row.site_name
				},
				callback : function(r){
					if (r.message) {
						$.each(r.message, function(idx, item){
							console.log("item.type",item.type)
							if (item.type == "Dal") {
								frappe.model.set_value(row.doctype, row.name, 'dal', item.no_of_tiffin)
							}
							if (item.type == "Gud / Achar") {
								frappe.model.set_value(row.doctype, row.name, 'gud__achar', item.no_of_tiffin)
							}
							if (item.type == "Dal Khichadi") {
								frappe.model.set_value(row.doctype, row.name, 'dal_khichadi', item.no_of_tiffin)
							}
							if (item.type == "Roti") {
								frappe.model.set_value(row.doctype, row.name, 'roti', item.no_of_tiffin)
							}
							if (item.type == "Rice") {
								frappe.model.set_value(row.doctype, row.name, 'rice', item.no_of_tiffin)
							}
							if (item.type == "Salad") {
								frappe.model.set_value(row.doctype, row.name, 'salad', item.no_of_tiffin)
							}
							if (item.type == "Subji") {
								frappe.model.set_value(row.doctype, row.name, 'subji', item.no_of_tiffin)
							}
						});						
					}
				} //callback end 
			})
		}
		
	},  
})




