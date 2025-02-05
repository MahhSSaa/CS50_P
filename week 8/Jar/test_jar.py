import pytest
from jar import Jar


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(2)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(100)
