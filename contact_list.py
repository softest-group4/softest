class ContactList:
    BACKUP_FILENAME = "contacts_backup.txt"

    def __init__(self, contact_list):
        self.contact_list = contact_list
        pass

    def add_new_contact(self, contact):
        pass

    def check_if_contact_exists_in_contact_list(self, contact_name):
        pass

    def get_contact_from_contact_list(self, contact_name):
        pass

    def edit_contact_in_contact_list(self, contact_name, contact_feature, new_value):
        pass

    def delete_contact_from_contact_list(self, contact_name):
        pass

    def load_contact_list_from_hard_disc(self):
        pass

    def save_contact_list_to_hard_disc(self):
        pass
