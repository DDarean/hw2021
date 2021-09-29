from os import path

from homework1.task03 import find_maximum_and_minimum


def test_one():
    filename = path.join(path.dirname(__file__), 'test_task03.txt')
    assert find_maximum_and_minimum(filename) == (-5, 7)
