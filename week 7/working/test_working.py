import pytest
from working import convert

def test_valid_times_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:45 PM") == "12:30 to 13:45"
    assert convert("1:00 AM to 11:59 PM") == "01:00 to 23:59"

def test_valid_times_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("hello world")

if __name__ == "__main__":
    pytest.main()
