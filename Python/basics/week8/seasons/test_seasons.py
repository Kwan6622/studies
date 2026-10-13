from seasons import verify_date, convert
import inflect
import pytest
from datetime import date

def test_valid_date():
    assert verify_date("1999-01-01") == (1999, 1, 1)

def test_invalid_date():
    with pytest.raises(SystemExit):
        verify_date("1999-13-01")



