from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("Hello") == 0


def test_h_greeting():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20





def test_other_greetings():
    assert value("good morning") == 100
    assert value("What's up?") == 100




def test_case_insensitivity():
    assert value("HeLLo") == 0
    assert value("HEY") == 20
    assert value("GOOD MORNING") == 100