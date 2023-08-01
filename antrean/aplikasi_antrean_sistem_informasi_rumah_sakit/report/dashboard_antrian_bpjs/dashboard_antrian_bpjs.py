# Copyright (c) 2023, Muhamad Jafar Sidik and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count
from pypika.terms import Case
from frappe.utils import today, response
from pybpjs import bpjs

def execute(filters=None):
	columns = [
		{"fieldname": "kdppk","label": "kdppk",	"fieldtype": "Data"},
		{"fieldname": "waktu_task1","label": "waktu_task1",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task4","label": "avg_waktu_task4",	"fieldtype": "Data"},
		{"fieldname": "jumlah_antrean","label": "jumlah_antrean",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task3","label": "avg_waktu_task3",	"fieldtype": "Data"},
		{"fieldname": "namapoli","label": "namapoli",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task6","label": "avg_waktu_task6",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task5","label": "avg_waktu_task5",	"fieldtype": "Data"},
		{"fieldname": "nmppk","label": "nmppk",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task2","label": "avg_waktu_task2",	"fieldtype": "Data"},
		{"fieldname": "avg_waktu_task1","label": "avg_waktu_task1",	"fieldtype": "Data"},
		{"fieldname": "kodepoli","label": "kodepoli",	"fieldtype": "Data"},
		{"fieldname": "waktu_task5","label": "waktu_task5",	"fieldtype": "Data"},
		{"fieldname": "waktu_task4","label": "waktu_task4",	"fieldtype": "Data"},
		{"fieldname": "waktu_task3","label": "waktu_task3",	"fieldtype": "Data"},
		{"fieldname": "insertdate","label": "insertdate","fieldtype": "Data"},
		{"fieldname": "tanggal","label": "tanggal",	"fieldtype": "Data"},
		{"fieldname": "waktu_task2","label": "waktu_task2",	"fieldtype": "Data"},
		{"fieldname": "waktu_task6","label": "waktu_task6",	"fieldtype": "Data"}
	]
	#args = frappe._dict(kwargs)
	doc = frappe.get_doc('Setting Integrasi BPJS')
	if (doc.mode_bpjs == "Production"):
		baseurl = doc.base_url_antrean
		consumerid = doc.cons_id_antrean
		secretkey = doc.secret_key_antrean
		userkey = doc.user_key_antrean
	else:
		baseurl = doc.base_url_antrean_dev
		consumerid = doc.cons_id_antrean_dev
		secretkey = doc.secret_key_antrean_dev
		userkey = doc.user_key_antrean_dev

	credential = {
		"host": baseurl,
		"consid": consumerid,
		"secret": secretkey,
		"user_key": userkey,
		"is_encrypt": 1
	}
	
	endpoint = 'dashboard/waktutunggu/tanggal/'+today()+'/waktu/'

	method = 'get'
	payload = ''
	loads = bpjs.bridging(credential, endpoint, method, payload)
	
#data =[loads['response']]
	data = [{
            "kdppk": "1311R002",
            "waktu_task1": 0,
            "avg_waktu_task4": 0,
            "jumlah_antrean": 1,
            "avg_waktu_task3": 0,
            "namapoli": "BEDAH",
            "avg_waktu_task6": 0,
            "avg_waktu_task5": 0,
            "nmppk": "RSU AISYIYAH",
            "avg_waktu_task2": 0,
            "avg_waktu_task1": 0,
            "kodepoli": "BED",
            "waktu_task5": 0,
            "waktu_task4": 0,
            "waktu_task3": 0,
            "insertdate": 1627873951000,
            "tanggal": "2021-04-16",
            "waktu_task2": 0,
            "waktu_task6": 0
        }]
  	#{'nobpjs': 'Application of Funds (Assets)'},{'nobpjs': 'Current Assets - GTPL'}]
	return columns, data
