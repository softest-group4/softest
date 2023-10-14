class ContactList:
    BACKUP_FILENAME = "contacts_backup.txt"

    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.contact_names = None

    def add_new_contact(self, contact):
        pass

    def check_if_contact_exists_in_contact_list(self, contact_name):
        self.refresh_contact_names()
        return contact_name in self.contact_names

    def refresh_contact_names(self):
        self.contact_names = []
        for contact in self.contact_list:
            self.contact_names.append(contact.name)

    def get_contact_from_contact_list(self, contact_name):
        for contact in self.contact_list:
            if contact.name == contact_name:
                print(f"Znaleziono kontakt: '{contact_name}'. Numer telefonu: {contact.phone}")
                return contact

        print(f"Kontakt o nazwie '{contact_name}' nie istnieje.")
        return None

    def edit_contact_in_contact_list(self, contact_name, contact_feature, new_value):
        pass

    def delete_contact_from_contact_list(self, contact_name):
        pass

    def load_contact_list_from_hard_disc(self):
        pass

    def save_contact_list_to_hard_disc(self):
        pass

    def get_whole_contact_list(self):
        str_contact_list = f"\nLista kontaktów w Twojej bazie jest następująca:\n"
        str_contact_list += f"******************************************************\n"
        for contact in self.contact_list:
            str_contact_list += str(contact)
            str_contact_list += f"******************************************************\n"
        return str_contact_list
