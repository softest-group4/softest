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

    def validate_phone_number(self):
        pass

    def validate_email_address(self):
        pass

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
