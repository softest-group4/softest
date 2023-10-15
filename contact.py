from datetime import datetime

class Contact:
    def __init__(self, name, address, phone, mail, birth_date):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birth_date = birth_date


    def validate_phone_number(self):
        pass

    def validate_email_address(self):
        pass

    def edit_contact_address(self, new_address):
        pass

    def edit_contact_name(self, new_name):
        pass

    def edit_contact_phone(self, new_phone):
        pass

    def edit_contact_email(self, new_email):
        pass

    def edit_contact_birth_date(self, new_birth_date):
        pass

    def get_amount_of_days_to_the_nearest_birthday(contact_list, days):
        current_date = datetime.now()
        upcoming_birthday = []

        for contact in contact_list:
            birthday = datetime.strptime(contact["birth_date"], "%Y -%m -%d")
            days_until_birthday = birthday.replace(year=current_date.year)
            time_until_birthday = days_until_birthday - current_date

            if 0 <= time_until_birthday <= days:
                upcoming_birthday.append(contact)

        return upcoming_birthday




















