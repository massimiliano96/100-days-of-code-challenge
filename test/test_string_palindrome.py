from src.examples.string_palindrome import is_palindrom


def test1():
    random_string = "anna"
    assert is_palindrom(random_string)


def test2():
    random_string = ""
    assert is_palindrom(random_string)


def test3():
    random_string = "wefuhwifueh"
    assert not is_palindrom(random_string)
