from __future__ import unicode_literals
import frappe
from frappe.utils import cint, formatdate, flt, getdate
from frappe import _, throw
from erpnext.setup.utils import get_company_currency
import frappe.defaults
import ast
import logging
import string
import datetime
import re
import json
from frappe.utils import getdate, flt,validate_email_add,cint
from frappe.model.naming import make_autoname
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from erpnext.controllers.status_updater import StatusUpdater

class CustomError(Exception): 
  pass


@frappe.whitelist()
def call_me(kwargs):
  if isinstance(kwargs, basestring):
      doc = frappe.get_doc(json.loads(kwargs)) 
      frappe.msgprint(doc.doctype)
      #frappe.throw(_("xyz"))



@frappe.whitelist()
def validate_rate_with_reference_doc(kwargs): 
	  ref_details=[["Purchase Order", "purchase_order", "po_detail"],["Purchase Receipt", "purchase_receipt","pr_detail"]]
	  if isinstance(kwargs, basestring):
	      doc = frappe.get_doc(json.loads(kwargs)) 
	  for ref_dt, ref_dn_field, ref_link_field in ref_details:
				for d in doc.get("items"):
					if d.get(ref_link_field):
						ref_rate = frappe.db.get_value(ref_dt + " Item", d.get(ref_link_field), "rate")

						if (flt(d.rate - ref_rate)) > 0:
                                                        #frappe.throw(_("{0}").format(ref_rate))
							#frappe.throw(_("Row #{0}: Rate is more than {1}: {2} rate ({3} / {4}) ")
							#	.format(d.idx, ref_dt, d.get(ref_dn_field), d.rate, ref_rate))
                                                        doc_rt=d.rate
                                                        itemx=d.idx
                                                        chk=1
                                                        return (itemx,ref_dt, doc_rt,ref_rate,chk)                                              

  
                 

