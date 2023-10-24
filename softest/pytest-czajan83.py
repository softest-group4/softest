import pytest

from ui3 import Ui


@pytest.fixture
def ui():
    ui = Ui()
    return ui


def test_if_arguments_from_user_input_are_properly_decoded_case_1(ui):
    ui.inp = "add contact -n Andrzej"
    assert ui.find_arg_value(f" -n ") == f"Andrzej"
    assert ui.find_arg_value(f" -n1 ") == f""
    assert ui.find_arg_value(f" -a ") == f""
    assert ui.find_arg_value(f" -p ") == f""
    assert ui.find_arg_value(f" -m ") == f""
    assert ui.find_arg_value(f" -b ") == f""
    assert ui.find_arg_value(f" -t ") == f""
    assert ui.find_arg_value(f" -t1 ") == f""
    assert ui.find_arg_value(f" -c ") == f""


def test_if_arguments_from_user_input_are_properly_decoded_case_2(ui):
    ui.inp = "add contact -n Andrzej -a ul. Kiszonki 1, 00-999 Warszawa"
    assert ui.find_arg_value(f" -n ") == f"Andrzej"
    assert ui.find_arg_value(f" -n1 ") == f""
    assert ui.find_arg_value(f" -a ") == f"ul. Kiszonki 1, 00-999 Warszawa"
    assert ui.find_arg_value(f" -p ") == f""
    assert ui.find_arg_value(f" -m ") == f""
    assert ui.find_arg_value(f" -b ") == f""
    assert ui.find_arg_value(f" -t ") == f""
    assert ui.find_arg_value(f" -t1 ") == f""
    assert ui.find_arg_value(f" -c ") == f""


def test_if_arguments_from_user_input_are_properly_decoded_case_3(ui):
    ui.inp = "add contact -n Andrzej -a ul. Kiszonki 1, 00-999 Warszawa -m adres@adres.pl"
    assert ui.find_arg_value(f" -n ") == f"Andrzej"
    assert ui.find_arg_value(f" -n1 ") == f""
    assert ui.find_arg_value(f" -a ") == f"ul. Kiszonki 1, 00-999 Warszawa"
    assert ui.find_arg_value(f" -p ") == f""
    assert ui.find_arg_value(f" -m ") == f"adres@adres.pl"
    assert ui.find_arg_value(f" -b ") == f""
    assert ui.find_arg_value(f" -t ") == f""
    assert ui.find_arg_value(f" -t1 ") == f""
    assert ui.find_arg_value(f" -c ") == f""


def test_if_arguments_from_user_input_are_properly_decoded_case_4(ui):
    ui.inp = "disp -nt"
    assert ui.find_arg_value(f" -n ") == f""
    assert ui.find_arg_value(f" -n1 ") == f""
    assert ui.find_arg_value(f" -a ") == f""
    assert ui.find_arg_value(f" -p ") == f""
    assert ui.find_arg_value(f" -m ") == f""
    assert ui.find_arg_value(f" -b ") == f""
    assert ui.find_arg_value(f" -t ") == f""
    assert ui.find_arg_value(f" -t1 ") == f""
    assert ui.find_arg_value(f" -c ") == f""


def test_if_arguments_from_user_input_are_properly_decoded_case_5(ui):
    ui.inp = "disp -t title"
    assert ui.find_arg_value(f" -n ") == f""
    assert ui.find_arg_value(f" -n1 ") == f""
    assert ui.find_arg_value(f" -a ") == f""
    assert ui.find_arg_value(f" -p ") == f""
    assert ui.find_arg_value(f" -m ") == f""
    assert ui.find_arg_value(f" -b ") == f""
    assert ui.find_arg_value(f" -t ") == f"title"
    assert ui.find_arg_value(f" -t1 ") == f""
    assert ui.find_arg_value(f" -c ") == f""

