#22/07/2026

from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    # Valid conversions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1

    # Invalid conversions
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("2/-5")

    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
