import pymongo
from contact import Contact
from note import Note
from datetime import datetime


class Mdb:
    def __init__(self):
        self.client = None
        self.db = None
        self.contact_list_collection = None
        self.notes_collection = None

    def init_connection(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.get_database("softest")

    def select_db_content(self):
        self.contact_list_collection = self.db.get_collection("contact_list")
        self.notes_collection = self.db.get_collection("notes")
        contact_list_dict = list(self.contact_list_collection.find({}))
        notes_dict = list(self.notes_collection.find({}))
        contact_list = []
        notes = []
        for contact_dict in contact_list_dict:
            contact_list.append(
                Contact(contact_dict[f"name"], contact_dict["address"], contact_dict[f"phone"], contact_dict[f"mail"],
                        contact_dict["birth_date"]))
        for note_dict in notes_dict:
            notes.append(
                Note(note_dict[f"title"], note_dict[f"note"], note_dict[f"creation_date"], note_dict[f"tag"]))
        return contact_list, notes

    def insert_contact_into_db(self, contact):
        contact_data = {
            "name": contact.name,
            "address": contact.address,
            "phone": contact.phone,
            "mail": contact.mail,
            "birth_date": datetime.strptime(contact.birth_date, "%Y-%m-%d") if contact.birth_date else ""
        }
        self.contact_list_collection.insert_one(contact_data)

    def update_contact_in_db(self, contact_name, contact):
        contact_data = {
            "name": contact.name,
            "address": contact.address,
            "phone": contact.phone,
            "mail": contact.mail,
            "birth_date": contact.birth_date.strftime("%Y-%m-%d") if contact.birth_date else None
        }
        self.contact_list_collection.update_one(filter={"name": contact_name}, update={"$set": contact_data})

    def delete_contact_from_db(self, contact_name):
        self.contact_list_collection.delete_one(filter={"name": contact_name})

    def insert_note_into_db(self, note):
        note_data = {
            "title": note.title,
            "note": note.note,
            "creation_date": note.creation_date,
            "tag": note.tag
        }
        self.notes_collection.insert_one(note_data)

    def update_note_in_db(self, title, note):
        note_data = {
            "title": note.title,
            "note": note.note,
            "creation_date": note.creation_date,
            "tag": note.tag
        }
        self.notes_collection.update_one(filter={"title": title}, update={"$set": note_data})

    def delete_note_from_db(self, title):
        self.notes_collection.delete_one(filter={"title": title})

    def close_connection(self):
        if self.client:
            self.client.close()
