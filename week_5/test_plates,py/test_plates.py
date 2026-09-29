from plates import is_valid

def test_length():
    assert is_valid("CS456456") == False
    assert is_valid("CS") == True
    assert is_valid("CS4567") == True
    assert is_valid("C") == False

def test_starting_letters():
    assert is_valid("c1235") == False
    assert is_valid("1c235") == False


def test_numbers():
    assert is_valid("cs05") == False
    assert is_valid("cs50A") == False

def test_characters():
    assert is_valid("cs_-1 ") == False