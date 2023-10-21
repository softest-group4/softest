from contact import Contact


def test_the_pattern_of_polish_phone_number():
    test_cases = [
        ("", True),
        ("+48123456789", True),
        ("1234567890", False),
        ("+4812345678", False),
        ("+481234567890", False)
    ]

    for phone, expected_result in test_cases:
        result = Contact.validate_phone_number(phone)
        assert result == expected_result, f"Failed for input: {phone}"
