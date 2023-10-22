from datetime import datetime
import re


class Contact:
    def __init__(self, name, address, phone, mail, birth_date):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birth_date = birth_date

    def __str__(self):
        str_contact = f"{self.name}     "
        if len(self.address) > 0:
            str_contact += f"adres: {self.address}   "
        if len(self.phone) > 0:
            str_contact += f"telefon: {self.phone}   "
        if len(self.mail) > 0:
            str_contact += f"adres mail: {self.mail}   "
        if len(str(self.birth_date)) > 0:
            str_contact += f"data urodzenia: {self.birth_date}   "
        str_contact += "\n"
        return str_contact

    @staticmethod
    def validate_phone_number(phone):
        if len(phone) == 0:
            return True
        else:
            pattern = r"^\+48\d{9}$"
            if not re.match(pattern, phone):
                return False
            return True

    @staticmethod
    def validate_email_address(mail):
        if len(mail) == 0:
            return True
        else:
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.match(pattern, mail):
                return False
            return True

    @staticmethod
    def validate_date_of_birth(date_of_birth):
        if len(date_of_birth) == 0:
            return True
        else:
            try:
                datetime.strptime(date_of_birth, "%Y-%m-%d")
            except ValueError:
                return False
            return True

    def edit_contact_address(self, new_address):
        self.address = new_address

    def edit_contact_name(self, new_name):
        self.name = new_name

    def edit_contact_phone(self, new_phone):
        if self.validate_phone_number(new_phone):
            self.phone = new_phone
        else:
            print(f"Nieprawidłowy numer telefonu! Popraw format numeru telefonu.")

    def edit_contact_email(self, new_email):
        if self.validate_email_address(new_email):
            self.mail = new_email
        else:
            print(f"Nieprawidłowy adres email! Popraw format adresu email.")

    def edit_contact_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def get_amount_of_days_to_the_nearest_birthday(self):

        current_date = datetime.now()
        next_birthday = datetime(current_date.year, self.birth_date.month, self.birth_date.day)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)

        days_until_birthday = (next_birthday - current_date).days
        return days_until_birthday
