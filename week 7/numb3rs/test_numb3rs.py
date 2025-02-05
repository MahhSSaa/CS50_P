import pytest
from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("249.249.249.249") == True

def test_invalid_ips():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("199.911.288.882") == False

if __name__ == "__main__":
    pytest.main()
