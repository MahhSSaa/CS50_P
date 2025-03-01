from plates import is_valid


# “All vanity plates must start with at least two letters.”
def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("60") == False
    assert is_valid("D7") == False
    assert is_valid("6") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_length():
    assert is_valid("HASS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False


# “Numbers cannot be used in the middle of a plate; they must come at the end.
#  For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_num():
    assert is_valid("FFF888") == True
    assert is_valid("AAA22A") == False
    assert is_valid("ZZZ033") == False


# “No periods, spaces, or punctuation marks are allowed.”
def test_punct():
    assert is_valid("CS50!") == False
