import string

from homework2.task5 import custom_range


def test_string_with_one_arg():
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c',
                                                         'd', 'e', 'f']


def test_string_with_two_arg():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i',
                                                              'j', 'k', 'l',
                                                              'm', 'n', 'o']


def test_string_with_three_arg():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n',
                                                                  'l', 'j',
                                                                  'h']


def test_int():
    assert custom_range([0, 1, 2, 3, 4, 5], -1) == [5, 4, 3, 2, 1, 0]


def test_incorrect_key():
    assert custom_range([0, 1, 2, 3, 4, 5], 0, 7, 2) == 'Incorrect key'


def test_different_types():
    assert custom_range([0, 1, 2, 'g', 4, 5], -1) == [5, 4, 'g', 2, 1, 0]
