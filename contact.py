import re

class Contact:
    def __init__(self, name, address, phone, mail, birth_date):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birth_date = birth_date

    def validate_phone_number(self, phone):
        pattern = r"\+48\d{9}"
        if not re.match(pattern, phone):
            print("You entered wrong format of phone number")
            raise ValueError
        self.phone = phone

    def validate_email_address(self, mail):
        pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        if not re.match(pattern, mail):
            print("You entered wrong format of email address")
            raise ValueError
        self.mail = mail

    def edit_contact_address(self, new_address):
        self.address = new_address

    def edit_contact_name(self, new_name):
        self.name = new_name

    def edit_contact_phone(self, new_phone):
        if self.validate_phone_number(new_phone):
            self.phone = new_phone
        else:
            print("Invalid phone number. Correct the phone format")

    def edit_contact_email(self, new_email):
        if self.validate_email_address(new_email):
            self.email = new_email
        else:
            print("Invalid email address. Correct the email format")


    def edit_contact_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def get_amount_of_days_to_the_nearest_birthday(self):
        pass
