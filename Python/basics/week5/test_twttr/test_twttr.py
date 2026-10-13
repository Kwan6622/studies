# 22/07/2026

from twttr import shorten

def test_shorten():
    assert shorten("Quang") == "Qng"
    assert shorten("I love my mom") == " lv my mm"
    assert shorten("Twitter has now became X") == "Twttr hs nw bcm X"

def test_shorten_number():
    assert shorten("1234") == "1234"
    assert shorten("LoveisLife123") == "LvsLf123"

def test_shorten_punctuation():
    assert shorten("?><!") == "?><!"
    assert shorten("$#@!") == "$#@!"

