from homework1.task04 import check_sum_of_four


def test_sum():
    a = [1, 2]
    b = [3, 7]
    c = [3, 4]
    d = [1, 1]
    assert check_sum_of_four(a, b, c, d) == 4


def test_zero():
    a = [3, 4]
    b = [3, 7]
    c = [3, 4]
    d = [1, 1]
    assert check_sum_of_four(a, b, c, d) == 0
