import pytest
from contact_list import ContactList
class ContactList:
    def setup_method(self):
        self.contact_names = ["Ala", "Bartek", "Czesiu", "Dominika", "Ewelina"]
        self.contact_class = ContactList(self.contact_names)

    def test_suggest_contact_name_exact_match(self):
        # czy zwraca dokładne dopasowanie
        contact_name = "Bartek"
        result = self.contact_class.suggest_contact_name(contact_name)
        assert result == contact_name

    def test_suggest_contact_name_partial_match(self):
        # czesciowe dopasowanie
        contact_name = "Eweline"
        result = self.contact_class.suggest_contact_name(contact_name)
        assert result == "Ewelina"

    def test_suggest_contact_name_no_match(self):
        # brak dopasowania
        contact_name = "Frodo"
        result = self.contact_class.suggest_contact_name(contact_name)
        assert result is None

    def test_suggest_contact_name_empty_list(self):
        # none dla pustej listy
        contact_class = ContactList([])
        contact_name = "Ala"
        result = contact_class.suggest_contact_name(contact_name)
        assert result is None

