# Copyright (c) 2024, shivansh akshay abhinav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WageLog(Document):
	def before_save(self):
	  self.total_wage=self.hour_worked*self.wage_rate

