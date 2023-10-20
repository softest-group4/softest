import pymongo


class Mdb:
    def __init__(self, connection_string):
        self.connection_string = connection_string
# tu trzeba dostosowac do serwera, format: mongodb://username:password@host:port/database

        self.client = None  # pymongo.MongoClient(self.connection_string)
        self.db = None  # self.client.get_database("baza_danych_softest")

    def init_connection(self):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client.get_database()

    def select_db_content(self):
        contact_collection = self.db.get_collection("contacts")
        note_collection = self.db.get_collection("notes")
        contact_list = list(contact_collection.find({}))
        notes = list(note_collection.find({}))
        return contact_list, notes

# teraz pytanie - czy przenosimy wszytko live z aplikacji do bazy danych?
# jesli tak, to trzeba  metody zaktualizowac o polaczenie z mongo
# np. do usuwania kontaktu self.mdb.delete_contact_from_db(contact_to_delete) itp.
# a wydaje mi sie ze chyba powinnismy

    def insert_contact_into_db(self, contact):
        contact_collection = self.db.get_collection("contacts")
        contact_data = {
            "name": contact.name,
            "address": contact.address,
            "phone": contact.phone,
            "mail": contact.mail,
            "birth_date": contact.birth_date.strftime("%Y-%m-%d") if contact.birth_date else None
        }
        contact_collection.insert_one(contact_data)

    def update_contact_in_db(self, contact):
        contact_collection = self.db.get_collection("contacts")
        contact_data = {
            "name": contact.name,
            "address": contact.address,
            "phone": contact.phone,
            "mail": contact.mail,
            "birth_date": contact.birth_date.strftime("%Y-%m-%d") if contact.birth_date else None
        }
        contact_collection.update_one({"_id": contact.id}, {"$set": contact_data})

    def delete_contact_from_db(self, contact):
        contact_collection = self.db.get_collection("contacts")
        contact_collection.delete_one({"_id": contact.id})

    def insert_note_into_db(self, note):
        note_collection = self.db.get_collection("notes")
        note_data = {
            "title": note.title,
            "note": note.note,
            "creation_date": note.creation_date,
            "tag": note.tag
        }
        note_collection.insert_one(note_data)

    def update_note_in_db(self, note):
        note_collection = self.db.get_collection("notes")
        note_data = {
            "title": note.title,
            "content": note.note,
            "creation_date": note.creation_date,
            "tag": note.tag
        }
        note_collection.update_one({"_id": note.id}, {"$set": note_data})

    def delete_note_from_db(self, note):
        note_collection = self.db.get_collection("notes")
        note_collection.delete_one({"_id": note.id})

    def close_connection(self):
        if self.client:
            self.client.close()
