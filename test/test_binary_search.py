from src.examples.binary_search import binary_search


def test1():
    elements = [1, 3, 5, 6]
    target = 5

    assert binary_search(elements, target) == 2


def test2():
    elements = [1, 3, 5, 6]
    target = 2

    assert binary_search(elements, target) == 1


def test3():
    elements = [1, 3, 5, 6]
    target = 0

    assert binary_search(elements, target) == 0
