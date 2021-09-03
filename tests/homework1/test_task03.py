import os
from homework1.task03 import find_maximum_and_minimum


def test_one():
    filename = 'test_task03.txt'
    file_path = os.path.join(os.getcwd(), filename)
    assert find_maximum_and_minimum(file_path), (-5, 7)


print(test_one())
