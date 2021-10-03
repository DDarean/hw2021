from homework3.task01 import cache


def test(n=2):
    @cache(n)
    def summa(a, b):
        return a + b

    def test_cycle():
        result = []
        for i in range((n+1) * 2):
            result.append(summa(2, 3))
        return result

    print(test_cycle())
    assert test_cycle() == [(5, 1), (5, 0), (5, 0),
                            (5, 1), (5, 0), (5, 0)]
