import pytest
from src.algo.fibonacci import fibonacci

def test1():
    n = 5
    assert fibonacci(n) == 5

def test2():
    n = 0
    assert fibonacci(n) == 0

def test3():
    n = 10
    assert fibonacci(n) == 55