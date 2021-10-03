from homework3.task04 import is_armstrong


def test():
    assert is_armstrong(153) is True, 'Is Armstrong number'
    assert is_armstrong(9) is True, 'Is Armstrong number'
    assert is_armstrong(10) is False, 'Is not Armstrong number'
