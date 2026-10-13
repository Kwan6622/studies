# 22/07/2026

from bank import value

def main():
    test_greeting_hello()
    test_greeting_h()
    test_greeting_other()

def test_greeting_hello():
    assert value("Hello!") == 0
    assert value("Hello, Mr.Quang!") == 0

def test_greeting_h():
    assert value("Hi! How can I help you?") == 20
    assert value("Hey!") == 20

def test_greeting_other():
    assert value("What's up!") == 100
