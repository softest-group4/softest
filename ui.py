from contact import Contact
from contact_list import ContactList
from note import Note
from notes import Notes
from mdb import Mdb


class Ui:
    def __init__(self):
        self.cmd_seq = None
        self.inp = None
        self.contacts = None
        self.notes = None
        self.mdb = None
        self.arg_n = None
        self.arg_a = None
        self.arg_p = None
        self.arg_m = None
        self.arg_b = None
        self.arg_t = None
        self.arg_c = None
        self.arg_n1 = None
        self.arg_t1 = None

    def load_from_db(self):
        self.mdb = Mdb()
        self.mdb.init_connection()
        contact_list, notes = self.mdb.select_db_content()
        self.contacts = ContactList(contact_list)
        self.notes = Notes(notes)

    def run(self):
        while True:
            self.inp = input(f"Gotowy > ")
            self.cmd_seq = self.inp.split(f" ")
            while f"" in self.cmd_seq:
                self.cmd_seq.remove(f"")
            if self.cmd_seq[0] == 'quit' or self.cmd_seq[0] == "exit":
                print(f"Do zobaczenia następnym razem :)")
                self.mdb.close_connection()
                break
            elif self.cmd_seq[0] == f"help":
                self.print_help()
            else:
                self.perform_selected_action_and_print_outcome()

    def perform_selected_action_and_print_outcome(self):
        if self.cmd_seq[0] == f"disp":
            print(self.perform_disp())
            print(self.contacts.get_whole_contact_list())
        elif self.cmd_seq[0] == f"add":
            print(self.perform_add())
            print(self.contacts.get_whole_contact_list())
        elif self.cmd_seq[0] == f"edit":
            print(self.perform_edit())
            print(self.contacts.get_whole_contact_list())
        elif self.cmd_seq[0] == f"del":
            print(self.perform_delete())
            print(self.contacts.get_whole_contact_list())
        else:
            print(f"Nie rozpoznano polecenia, wpisz 'help' aby wyświetlić pomoc... ")

    @staticmethod
    def print_help():
        print(f"Cześć, jestem Twoim osobistym asystentem")
        print(f"Wybierz jedną z dostępnych opcji:")
        print(f"disp -cn \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla imiona wszystkich Twoich kontaktów")
        print(f"disp -nt \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla tematy wszystkich Twoich notatek")
        print(f"disp contact -n <contact_name> \t\t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla wszystkie informacje o wybranym "
              f"kontakcie")
        print(f"disp contact -n <contact_name> -a \t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla adres wybranego kontaktu")
        print(f"disp contact -n <contact_name> -p \t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla numer telefonu wybranego kontaktu")
        print(f"disp contact -n <contact_name> -m \t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla adres mail wybranego kontaktu")
        print(f"disp contact -n <contact_name> -b \t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla datę urodzenia wybranego kontaktu")
        print(f"disp -b <days> \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla kontakty, które obchodzą urodziny w "
              f"ciągu najbliższych <days> dni")
        print(f"disp note -t <title_name> \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t wyświetla treść notatki o wybranym tytule")
        print(f"add contact -n <contact_name> [ -a <address> -p <phone> -m <mail> -b <birth_date> ] "
              f" dodaje informację o nowym kontakcie (składniki -a, -p, -m oraz -b są opcjonalne)")
        print(f"add note -t <title> -c <content> \t\t\t\t\t\t\t\t\t\t\t\t\t dodaje notatkę do Twoich notatek ")
        print(f"edit contact -n <contact_name> -n1 <new_contact_name> \t\t\t\t\t\t\t\t modyfikuje nazwę kontaktu")
        print(f"edit contact -n <contact_name> <property> <new_property_value> "
              f"\t\t\t\t\t\t modyfikuje wybraną właściwość wybranego kontaktu"
              f"\t możliwe wartości parametru <property> to -a, -p -m lub -b")
        print(f"edit note it <title> -t1 <new_title> \t\t\t\t\t\t\t\t\t\t\t\t zmienia tytuł wybranej notatki")
        print(f"edit note -t <title> -c <new_content> \t\t\t\t\t\t\t\t\t\t\t\t zmienia treść wybranej notatki")
        print(f"del contact -n <contact_name> \t\t\t\t\t\t\t\t\t\t\t\t\t\t usuwa kontakt z Twojej listy kontaktów")
        print(f"del note -t <title> \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t usuwa wybraną notatkę z Twojej listy notatek")
        print(f"quit or exit \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t kończy działanie asystenta")

    def perform_disp(self):
        if self.cmd_seq[-1] == "-a" or self.cmd_seq[-1] == "-p" or self.cmd_seq[-1] == "-m" or self.cmd_seq[-1] == "-b" or self.cmd_seq[-1] == "-t":
            self.cmd_seq.append("")
        self.get_arguments_values()
        if len(self.cmd_seq) == 1:
            return f"Niepowodzenie! Brak argumentów dla polecenia disp"
        if self.cmd_seq[1] == "-cn":
            result = ContactList.get_names_list(self.contacts)
            return f"Lista imion Twoich kontaktów jest następująca: {result}"
        elif self.cmd_seq[1] == "-nt":
            result = Notes.get_titles_list(self.notes)
            return f"Lista tytułów Twoich notatek jest następująca: {result}"
        elif self.cmd_seq[1] == "contact":
            self.get_arguments_values()
            if len(self.cmd_seq) == 4:
                result = str(ContactList.get_contact_from_contact_list(self.contacts, self.arg_n))
                return result
            if "-a" in self.cmd_seq:
                result = ContactList.get_address_from_contact(self.contacts, self.arg_n)
                return result
            elif "-p" in self.cmd_seq:
                result = ContactList.get_phone_from_contact(self.contacts, self.arg_n)
                return result
            elif "-m" in self.cmd_seq:
                result = ContactList.get_mail_from_contact(self.contacts, self.arg_n)
                return result
            elif "-b" in self.cmd_seq:
                result = ContactList.get_birth_date_from_contact(self.contacts, self.arg_n)
                return result
        elif self.cmd_seq[1] == "-b":
            result = ContactList.get_contacts_with_birthday_soon(self.contacts, self.arg_b)
            return result
        elif self.cmd_seq[1] == "note":
            if self.arg_t == "":
                return f"Niepowodzenie! Nie wprowadzono tytułu notatki"
            else:
                result = Notes.get_content_from_note(self.notes, self.arg_t)
                return result

    def perform_add(self):
        if len(self.cmd_seq) == 1:
            return f"Niepowodzenie! Brak argumentów dla polecenia add"
        if self.cmd_seq[1] == "contact":
            if "-n" not in self.cmd_seq:
                return f'Niepowodzenie! Nie odnaleziono wymaganego argumentu -n dla polecenia add contact'
            self.get_arguments_values()
            if Contact.validate_phone_number(self.arg_p) is False:
                return f"Niepowodzenie! Niepoprawny format numeru telefonu. Wprowadź numer, używając formatu +48xxxxxxxxx"
            if Contact.validate_email_address(self.arg_m) is False:
                return f"Niepowodzenie! Niepoprawny format adresu mail"
            if Contact.validate_date_of_birth(self.arg_b) is False:
                return f"Niepowodzenie! Niepoprawny format daty urodzenia. Wprowadź datę w formacie YYYY-mm-dd"
            new_contact = Contact(self.arg_n, self.arg_a, self.arg_p, self.arg_m, self.arg_b)
            result = self.contacts.add_new_contact(new_contact)
            if result == "Sukces!":
                self.mdb.insert_contact_into_db(new_contact)
            return result
        elif self.cmd_seq[1] == "note":
            if "-t" not in self.cmd_seq:
                return f'Niepowodzenie! Nie odnaleziono wymaganego argumentu -t dla polecenia add note'
            self.get_arguments_values()
            new_note = Note(self.arg_t, self.arg_c)
            result = self.notes.add_new_note(new_note)
            if result == "Sukces!":
                self.mdb.insert_contact_into_db(new_note)
        else:
            return f'Niepowodzenie! Nieobsługiwany argument funkcji add, wybierz argument "add contact " lub "add note "'

    def perform_edit(self):
        if len(self.cmd_seq) == 1:
            return f"Niepowodzenie! Brak argumentów dla polecenia edit."
        if self.cmd_seq[1] == "contact":
            if "-n" not in self.cmd_seq:
                return f"Niepowodzenie! Nie odnaleziono wymaganego argumentu -n dla polecenia edit contact."
            self.get_arguments_values()
            contact = self.contacts. get_contact_from_contact_list(self.arg_n)
            print(contact)
            contact_name = self.arg_n
            new_contact_name = self.arg_n1

            if self.arg_a:
                result = self.contacts.edit_contact_in_contact_list(self.arg_n, "address", self.arg_a)
            elif self.arg_p:
                result = self.contacts.edit_contact_in_contact_list(self.arg_n, "phone",  self.arg_p)
            elif self.arg_m:
                result = self.contacts.edit_contact_in_contact_list(self.arg_n, "email",  self.arg_m)
            elif self.arg_b:
                result = self.contacts.edit_contact_in_contact_list(self.arg_n, "birth_date", self.arg_b)
            else:
                result = self.contacts.edit_contact_in_contact_list(self.arg_n, "name", self.arg_n1)

            return result

        elif self.cmd_seq[1] == "note":
            title = self.arg_t
            new_title = self.arg_t1
            new_content = self.arg_c

            if self.arg_c:
                result = self.notes.edit_note_in_notes(self.arg_t, self.arg_c)
            else:
                result = self.notes.edit_note_in_notes(self.arg_t, self.arg_t1)

            return result

        else:
            return f"Niepowodzenie! Nieobsługiwany argument funkcji edit, wybierz argument 'edit contact' lub 'edit note'."


    def perform_delete(self):
        if len(self.cmd_seq) == 1:
            return f"Niepowodzenie! Brak argumentów dla polecenia delete."
        if self.cmd_seq[1] == "contact":
            if "-n" not in self.cmd_seq:
                return f"Niepowodzenie! Nie odnaleziono wymaganego argumentu -n dla polecenia delete contact."
            contact_name = self.arg_n
            if self.arg_a:
                result = self.contacts.delete_contact_from_contact_list(self.arg_a)
            elif self.arg_p:
                result = self.contacts.delete_contact_from_contact_list(self.arg_p)
            elif self.arg_m:
                result = self.contacts.delete_contact_from_contact_list(self.arg_m)
            elif self.arg_b:
                result = self.contacts.delete_contact_from_contact_list(self.arg_b)
            else:
                result = self.contacts.delete_contact_from_contact_list(self.arg_n)

            return result

        elif self.cmd_seq[1] == "note":
            title = self.arg_t

            if self.arg_c:
                result = self.notes.delete_note_from_notes(self.arg_t)
            else:
                result = self.notes.delete_note_from_notes(self.arg_t)

            return result

        else:
            return f"Niepowodzenie! Nieobsługiwany argument funkcji delete, wybierz argument 'delete contact' lub 'delete note'."

    def find_location_of_arg(self, arg):
        location = 0
        for var in self.cmd_seq:
            if var == arg:
                return location
            location += 1
        return -1

    def find_arg_value(self, arg):
        if arg in self.cmd_seq:
            arg_location = self.find_location_of_arg(arg)
            return self.cmd_seq[arg_location + 1]
        return f""

    def get_arguments_values(self):
        self.arg_n = self.find_arg_value(f"-n")
        self.arg_n1 = self.find_arg_value(f"-n1")
        self.arg_a = self.find_arg_value(f"-a")
        self.arg_p = self.find_arg_value(f"-p")
        self.arg_m = self.find_arg_value(f"-m")
        self.arg_b = self.find_arg_value(f"-b")
        self.arg_t = self.find_arg_value(f"-t")
        self.arg_t1 = self.find_arg_value(f"-t1")
        self.arg_c = self.find_arg_value(f"-c")
