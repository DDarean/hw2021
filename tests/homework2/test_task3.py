from homework2.task3 import combinations


def test_comb():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_comb1():
    assert combinations([1, 2, 3], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 3],
        [3, 4]
    ]
