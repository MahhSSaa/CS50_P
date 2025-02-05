import pytest
from fuel import convert, gauge

def test_convert_correct():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("0/100") == 0
    assert convert("1/1") == 100

def test_convert_incorrect():
    with pytest.raises(ValueError):
        convert("2/1")  # corrected invalid example

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(74) == "74%"
    assert gauge(98) == "98%"
    assert gauge(3) == "3%"
    assert gauge(100) == "F"
