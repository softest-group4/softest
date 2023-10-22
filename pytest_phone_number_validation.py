from contact import Contact


def test_empty_phone_number():
    assert Contact.validate_phone_number("")


def test_valid_phone_number():
    assert Contact.validate_phone_number("+48123456789")


def test_invalid_phone_number_missing_country_code():
    assert not Contact.validate_phone_number("123456789")


def test_invalid_phone_number_incorrect_digit_count():
    assert not Contact.validate_phone_number("+4812345678")


def test_invalid_phone_number_extra_digit():
    assert not Contact.validate_phone_number("+481234567890")

