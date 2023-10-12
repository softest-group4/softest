from datetime import date

from contact import Contact
from contact_list import ContactList


def main():
    contact_1 = Contact("andrzej", "Wrocław", "000000000", "andrzej.b.czajka@gmail.com", date(1970, 1, 1))
    contact_2 = Contact("marta", "Wrocław", "000000000", "adres@gmail.com", date(1970, 1, 1))
    contact_3 = Contact("gabriela", "Wrocław", "000000000", "adres@wp.pl", date(1970, 1, 1))
    contacts = ContactList([contact_1, contact_2])
    contacts.add_new_contact(contact_3)
    print(contacts.get_contact_from_contact_list("marta"))
    print(contacts.get_contact_from_contact_list("marzena"))


if __name__ == "__main__":
    main()
