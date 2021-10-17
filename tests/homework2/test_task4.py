from homework2.task4 import cache


def test_cache():
    def func(a, b):
        return (a ** b) ** 2
    cache_func = cache(func)
    var1 = cache_func(3, 5)
    var2 = cache_func(3, 5)
    assert var1 is not var2


def test_cached():
    def func(a, b):
        return (a ** b) ** 2
    cache_func = cache(func)
    cache_func(3, 5)
    var2 = cache_func(3, 5)
    var3 = cache_func(3, 5)
    assert var2 is var3
