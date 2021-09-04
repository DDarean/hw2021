"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import Counter
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """Returns quantity of the tuples (i, j, k, l) for which:
        a[i] + b[j] + c[k] + c[l] == 0"""

    right = Counter([x + y for x in a for y in b])
    left = Counter([x + y for x in c for y in d])
    counter = 0
    for key in right.keys():
        if left[key]:
            counter += right[key] * left[key]
    return counter
