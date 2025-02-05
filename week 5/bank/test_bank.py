from bank import value

def test_hello_greetings():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0

def test_h_greetings():
    assert value("hi world") == 20
    assert value("HI WORLD") == 20

def test_other_greetings():
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100
