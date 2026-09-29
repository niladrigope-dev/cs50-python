from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_str():
    jar = Jar(5)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
                                                  

def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    try:
        jar.deposit(1)
        assert False
    except ValueError:
        pass


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    try:
        jar.withdraw(1)
        assert False
    except ValueError:
        pass


def test_properties():
    jar = Jar(10)

    assert jar.capacity == 10
    assert jar.size == 0

    jar.deposit(4)
    assert jar.size == 4
    assert jar.capacity == 10
