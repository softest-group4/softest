import Levenshtein


class ContactList:
    BACKUP_FILENAME = "contacts_backup.txt"

    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.contact_names = None

    def add_new_contact(self, contact):
        if self.check_if_contact_exists_in_contact_list(contact.name):
            return (f'Niepowodzenie! Kontakt z imieniem {contact.name} już istnieje, wybierz inne imię stosując '
                    f'indeksację, np {contact.name}_2121')
        self.contact_list.append(contact)
        return "Sukces!"

    def check_if_contact_exists_in_contact_list(self, contact_name):
        self.refresh_contact_names()
        return contact_name in self.contact_names

    def refresh_contact_names(self):
        self.contact_names = []
        for contact in self.contact_list:
            self.contact_names.append(contact.name)

    def suggest_contact_name(self, contact_name):
        best_match = None
        min_distance = float("inf")

        for name in self.contact_names:
            distance = Levenshtein.distance(name, contact_name)
            if distance < min_distance:
                min_distance = distance
                best_match = name

        return best_match

    def get_contact_from_contact_list(self, contact_name):
        self.refresh_contact_names()

        if contact_name not in self.contact_names:
            contact_name = self.suggest_contact_name(contact_name)
        for contact in self.contact_list:
            if contact.name == contact_name:
                return contact
        return None

    def edit_contact_in_contact_list(self, contact_name, contact_feature, new_value):
        contact_to_edit = self.get_contact_from_contact_list(contact_name)
        print(contact_name)
        print(contact_to_edit)
        # contact_to_edit = None
        #
        # for contact in self.contact_list:
        #     if contact.name == contact_name:
        #         contact_to_edit = contact
        #         break

        if contact_to_edit is not None:
            setattr(contact_to_edit, contact_feature, new_value)
            return f"Sukces!"
        else:
            return f"Jakiś błąd, jeszcze nie wiemy jaki"

    def delete_contact_from_contact_list(self, contact_name):
        contact_to_delete = None

        for contact in self.contact_list:
            if contact.name == contact_name:
                contact_to_delete = contact
                break
        if contact_to_delete:
            self.contact_list.remove(contact_to_delete)
            print(f"Kontakt o nazwie '{contact_name}' został usunięty")
        else:
            print(f"Nie można usunąć.Kontakt o nazwie '{contact_name}' nie istnieje")

    def get_whole_contact_list(self):
        str_contact_list = f"\nLista kontaktów w Twojej bazie jest następująca:\n"
        for contact in self.contact_list:
            str_contact_list += str(contact)
        str_contact_list += f"------------------------------------------------------------\n"
        return str_contact_list

    def get_names_list(self):
        self.refresh_contact_names()
        str_names_list = ""
        if not self.contact_names:
            return f"Lista kontaktów jest pusta, nie można wyświetlić ich nazw"
        for name in self.contact_names:
            str_names_list += str(name) + "\n"
        return str_names_list

    def get_address_from_contact(self, contact_name):
        name = contact_name
        contact = self.get_contact_from_contact_list(name)
        if not contact.address:
            return f"Szukany kontakt nie ma wprowadzonego adresu"
        return f"{contact.name}    adres: {contact.address}"

    def get_phone_from_contact(self, contact_name):
        name = contact_name
        contact = self.get_contact_from_contact_list(name)
        if not contact.phone:
            return f"Szukany kontakt nie ma wprowadzonego numeru telefonu"
        return f"{contact.name}    numer telefonu: {contact.phone}"

    def get_mail_from_contact(self, contact_name):
        name = contact_name
        contact = self.get_contact_from_contact_list(name)
        if not contact.mail:
            return f"Szukany kontakt nie ma wprowadzonego adresu e-mail"
        return f"{contact.name}    adres e-mail: {contact.mail}"

    def get_birth_date_from_contact(self, contact_name):
        name = contact_name
        contact = self.get_contact_from_contact_list(name)
        if not contact.birth_date:
            return f"Szukany kontakt nie ma wprowadzonej daty urodzenia"
        return f"{contact.name}    data urodzin: {contact.birth_date}"

    def get_contacts_with_birthday_soon(self, days_to_birthday):
        contacts_birthday_list = []
        if days_to_birthday == "":
            return f"Niepowodzenie! Brak wprowadzonej liczby dni do urodzin"
        int_days_to_birthday = int(days_to_birthday)
        for contact in self.contact_list:
            if not contact.birth_date:
                continue
            nearest_birthday = contact.get_amount_of_days_to_the_nearest_birthday()
            if nearest_birthday <= int_days_to_birthday:
                contact_with_days_to_birthday = (contact.name, f"{nearest_birthday} dni do urodzin")
                contacts_birthday_list.append(contact_with_days_to_birthday)
        return contacts_birthday_list
