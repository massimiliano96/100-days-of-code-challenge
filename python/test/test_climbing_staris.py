from src.algo.climbing_stairs import climbing_stairs

def test1():
    n = 3
    assert climbing_stairs(n) == 3

def test2():
    n = 5
    assert climbing_stairs(n) == 8

