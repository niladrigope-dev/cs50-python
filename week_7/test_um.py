from um import count


def test_basic():
    assert count("hello, um, world") == 1


def test_case():
    assert count("Um, thanks, UM") == 2


def test_multiple():
    assert count("Um, thanks, um...") == 2


def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0


def test_punctuation():
    assert count("um?") == 1
    assert count("um,") == 1


def test_empty():
    assert count("") == 0