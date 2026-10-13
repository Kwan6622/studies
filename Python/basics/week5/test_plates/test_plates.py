#22/07/2026

from plates import is_valid

def main():
    test_is_valid_length()
    test_is_valid_first_letter()
    test_is_valid_first_number()
    test_is_valid_punctuation()
    test_is_valid_number_location()

def test_is_valid_length():
    assert is_valid("C") == "Invalid"
    assert is_valid("CS50CS50") == "Invalid"
    assert is_valid("CS50") == "Valid"

def test_is_valid_first_letter():
    assert is_valid("CS") == "Valid"
    assert is_valid("50CS") == "Invalid"
    assert is_valid("50") == "Invalid"
    assert is_valid("COMSCI") == "Valid"

def test_is_valid_first_number():
    assert is_valid("CS05") == "Invalid"
    assert is_valid("IM007") == "Invalid"
    assert is_valid("CS50") == "Valid"

def test_is_valid_punctuation():
    assert is_valid("CC 5") == "Invalid"
    assert is_valid("CS5%") == "Invalid"

def test_is_valid_number_location():
    assert is_valid("CS50") == "Valid"
    assert is_valid("CS50CS") == "Invalid"
