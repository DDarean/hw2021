from homework1.task05 import find_maximal_subarray_sum


def test_k3():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert (find_maximal_subarray_sum(nums, k)) == 16


def test_k2():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    assert (find_maximal_subarray_sum(nums, k)) == 13


def test_k1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 1
    assert (find_maximal_subarray_sum(nums, k)) == max(nums)


def test_k0():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 0
    assert (find_maximal_subarray_sum(nums, k)) == 0
