from datetime import datetime
from contact import Contact
from contact_list import ContactList


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

    def load_from_db(self):
        # self.contacts = self.mdb.select_db_content()
        contact_1 = Contact("Andrzej", "Wrocław", "000000000", "andrzej.b.czajka@gmail.com", datetime(1970, 1, 1))
        contact_2 = Contact("Marta", "Wrocław", "000000000", "adres@gmail.com", datetime(1970, 1, 1))
        self.contacts = ContactList([contact_1, contact_2])

    def run(self):
        while True:
            self.inp = input(f"Gotowy > ")
            self.cmd_seq = self.inp.split(f" ")
            while f"" in self.cmd_seq:
                self.cmd_seq.remove(f"")
            if self.cmd_seq[0] == 'quit' or self.cmd_seq[0] == "exit":
                print(f"Do zobaczenia następnym razem :)")
                break
            elif self.cmd_seq[0] == f"help":
                self.print_help()
            else:
                self.perform_selected_action_and_print_outcome()

    def perform_selected_action_and_print_outcome(self):
        if self.cmd_seq[0] == f"disp":
            self.perform_disp()
        elif self.cmd_seq[0] == f"add":
            print(self.perform_add())
            print(self.contacts.get_whole_contact_list())
        elif self.cmd_seq[0] == f"edit":
            self.perform_edit()
        elif self.cmd_seq[0] == f"del":
            self.perform_delete()
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
        pass

    def perform_add(self):
        if len(self.cmd_seq) == 1:
            return f"Niepowodzenie! Brak argumentów dla polecenia add"
        if self.cmd_seq[1] == "contact":
            if "-n" not in self.cmd_seq:
                return f'Niepowodzenie! Nie odnaleziono wymaganego argumentu -n dla polecenia add contact'
            self.get_arguments_values()
            if Contact.validate_phone_number(self.arg_p) is False:
                return f"Niepowodzenie! Niepoprawny format numeru telefonu"
            if Contact.validate_email_address(self.arg_m) is False:
                return f"Niepowodzenie! Niepoprawny format adresu mail"
            if Contact.validate_date_of_birth(self.arg_b) is False:
                return f"Niepowodzenie! Niepoprawny format daty urodzenia. Wprowadź datę w formacie YYYY-mm-dd"
            new_contact = Contact(self.arg_n, self.arg_a, self.arg_p, self.arg_m, self.arg_b)
            result = self.contacts.add_new_contact(new_contact)
            if result == "Sukces!":
                pass
                # self.mdb.insert_contact_into_db(new_contact)
            return result
        elif self.cmd_seq[1] == "note":
            pass
        else:
            return f'Niepowodzenie! Nieobsługiwany argument funkcji add, wybierz argument "add contact " lub "add note "'

    def perform_edit(self):
        pass

    def perform_delete(self):
        pass

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
        self.arg_a = self.find_arg_value(f"-a")
        self.arg_p = self.find_arg_value(f"-p")
        self.arg_m = self.find_arg_value(f"-m")
        self.arg_b = self.find_arg_value(f"-b")
