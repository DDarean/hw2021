from homework2.task4 import cache


def test_cache():
    def func(a, b):
        return (a ** b) ** 2
    cache_func = cache(func)
    var1 = cache_func(3, 5)
    var2 = cache_func(3, 5)
    var3 = cache_func(7, 2)
    var4 = cache_func(7, 2)
    assert var1[0] == var2[0] and var1[1] == 0 and var2[1] == 1
    assert var3[0] == var4[0] and var3[1] == 0 and var4[1] == 1
