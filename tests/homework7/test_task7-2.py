from homework7.task2 import backspace_compare


def test_positive():
    s = 'ab#c'
    t = 'ad#c'
    assert backspace_compare(s, t)


def test_double_and_first():
    s = 'a##c'
    t = '#a#c'
    assert backspace_compare(s, t)


def test_sharp_only():
    s = '###'
    t = '#'
    assert backspace_compare(s, t)


def test_negative():
    s = 'a#c'
    t = 'b'
    assert not backspace_compare(s, t)


def test_double_backspace():
    s = 'hellow##'
    t = 'hello#'
    assert backspace_compare(s, t)
