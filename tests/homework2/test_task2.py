from homework2.task2 import major_and_minor_elem


def test_major_and_minor_elem_case1():
    assert major_and_minor_elem([3, 2, 3]) == ([3], [2])


def test_major_and_minor_elem_case2():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == ([2], [1])


def test_major_and_minor_elem_several_major():
    assert major_and_minor_elem([2, 1, 1, 2, 2, 3, 3, 3]) == ([2, 3], [1])
