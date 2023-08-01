# Copyright (c) 2023, Muhamad Jafar Sidik and contributors
# For license information, please see license.txt

import frappe, json,os, antrean
from frappe.model.document import Document
class ReferensiJadwalDokter(Document):
	DATA_FILE = 'data_file.json'
	
	@staticmethod
	def get_list(args):
		data = ReferensiJadwalDokter.get_current_data()
		return [frappe._dict(doc) for name, doc in data.items()]
	
	@staticmethod
	def get_count(args) -> int:
		"""Similar to reportview.get_count, return total count of documents on listview."""
		data = ReferensiJadwalDokter.get_current_data()
		return len(data)
	@staticmethod
	def get_stats(args):
		"""Similar to reportview.get_stats, return sidebar stats."""
		return {}
	
	@staticmethod
	def get_current_data() -> list[frappe._dict]:
		"""Similar to reportview.get_list"""
		if not os.path.exists(ReferensiJadwalDokter.DATA_FILE):
			return {}
		with open(ReferensiJadwalDokter.DATA_FILE) as f:
			return json.load(f)
		
	@staticmethod
	def update_data(data: dict[str, dict]) -> None:
		"""Flush updated data to disk"""
		with open(ReferensiJadwalDokter.DATA_FILE, "w+") as data_file:
			json.dump(data, data_file)
	    
	# ============ instance methods ============
	def db_insert(self, *args, **kwargs) -> None:
		"""Serialize the `Document` object and insert it in backend."""
		d = self.get_valid_dict(convert_dates_to_str=True)
		data = self.get_current_data()
		data[d.name] = d
		self.update_data(data)
		


	def load_from_db(self) -> None:
		"""Using self.name initialize current document from backend data.

		This is responsible for updatinng __dict__ of class with all the fields on doctype."""
		data = self.get_current_data()
		d = data.get(self.name)
		super(Document, self).__init__(d)
		

	def db_update(self, *args, **kwargs) -> None:
		"""Serialize the `Document` object and update existing document in backend."""
		self.db_insert(*args, **kwargs)
		

	def delete(self, *args, **kwargs) -> None:
		"""Delete the current document from backend"""
		data = self.get_current_data()
		data.pop(self.name, None)
		self.update_data(data)