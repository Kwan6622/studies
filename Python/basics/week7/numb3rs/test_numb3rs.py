from numb3rs import validate


def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_invalid_numbers():
    assert validate("256.1.1.1") == False
    assert validate("275.3.6.28") == False
    assert validate("-1.2.3.4") == False


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1..3.4") == False


def test_non_numeric():
    assert validate("cat.dog.1.2") == False
    assert validate("1.2.three.4") == False