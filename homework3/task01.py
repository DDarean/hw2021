def cache(n):
    cache_storage = {}
    counter = n

    def decorator(func):

        def calculate(*args):
            nonlocal counter
            if args in cache_storage:
                if counter != 0:
                    counter -= 1
                    calculated_flag = 0  # for tests
                    return cache_storage[args], calculated_flag
                else:
                    cache_storage[args] = func(*args)
                    counter = n
                    calculated_flag = 1  # for tests
                    return func(*args), calculated_flag
            elif args not in cache_storage:
                cache_storage[args] = func(*args)
                calculated_flag = 1  # for tests
                return func(*args), calculated_flag
        return calculate
    return decorator
