from a import *

def test_fibonacci():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(3) == 1
    assert fibonacci(3) == 2


def test_square():
    assert square(3) == 9
    assert square(3) == 9

def test_incr():
    assert incr(1) == 2