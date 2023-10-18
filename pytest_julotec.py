from datetime import datetime
from contact import Contact


def test_if_person_with_birthday_at_1st_of_january_indicated_during_nearest_90_days():
    contact = Contact("magda", "", "", "", datetime(1970, 1, 1))
    assert 60 < contact.get_amount_of_days_to_the_nearest_birthday() < 90
