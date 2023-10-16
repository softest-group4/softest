class Mdb:
    def __init__(self, connection):
        self.connection = connection

    def init_connection(self):
        pass

    def select_db_content(self):
        contact_list = None
        notes = None
        return contact_list, notes

    def insert_contact_into_db(self, contact):
        pass

    def update_contact_in_db(self, contact):
        pass

    def delete_contact_from_db(self, contact):
        pass

    def insert_note_into_db(self, note):
        pass

    def update_note_in_db(self, note):
        pass

    def delete_note_from_db(self, note):
        pass

    def close_connection(self):
        pass
