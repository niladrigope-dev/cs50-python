from project import count_words, count_characters, most_common_word


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("hello world python") == 3


def test_count_characters():
    assert count_characters("hello") == 5
    assert count_characters("hello world") == 11


def test_most_common_word():
    assert most_common_word("hello world hello") == "hello"
    assert most_common_word("python code python test python") == "python"