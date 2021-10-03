from homework3.task02 import multiprocess_calculate


def test():
    n = 500
    assert multiprocess_calculate(n)[1] < 60


if __name__ == '__main__':
    test()
