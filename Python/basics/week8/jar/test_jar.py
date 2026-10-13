import pytest
from jar import Jar


def test_init():
    # Default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Invalid capacities
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(3.5)

    with pytest.raises(ValueError):
        Jar("10")


def test_str():
    jar = Jar(3)
    assert str(jar) == ""

    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(5)

    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)