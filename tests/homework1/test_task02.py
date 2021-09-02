from homework1.task02 import check_fibonacci


def test_actual_sequence():
    """Testing that actual sequence returns True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


def test_negative_number():
    """Testing that sequence with negative number returns False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, -55, 89])


def test_not_sorted():
    """Testing that not sorted sequence returns False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 89, 55])


def test_last_changed():
    """Testing that incorrect last element returns False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 90])


def test_special_case():
    """Testing that sequence with one 1 in the beginning returns correct value"""
    assert check_fibonacci([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    assert not check_fibonacci([1, 2, 3, 5, 8, 13, 21, 34, 55, 90])


def test_single_correct():
    """Testing single number returns True"""
    assert check_fibonacci([34])


def test_single_incorrect():
    """Testing single number returns False"""
    assert not check_fibonacci([9])
