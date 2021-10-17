from homework2.task3 import combinations


def test_combinations_positive_case1_same_size():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_combinations_positive_case2_different_size():
    assert combinations([1, 2, 3], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 3],
        [3, 4]
    ]
