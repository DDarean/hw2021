"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:

"""


def custom_range(data, *args):
    """
    :param data: iterable of unique values
    :param args:
        start - first element to iterate
        stop - last element to iterate
        step - iteration step
    :return: sequence of elements from start to stop
    """
    if len(args) == 1:
        if isinstance(args[0], int) and args[0] < 0:
            step = args[0]
            return data[::step]
        start, stop, step = 0, data.index(args[0]), 1
        return [x for x in data[start:stop:step]]
    elif len(args) == 2:
        if args[0] in data and args[1] in data:
            start, stop, step = data.index(args[0]), data.index(args[1]), 1
            return [x for x in data[start:stop:step]]
        else:
            return "Incorrect key"
    elif len(args) == 3:
        if args[0] in data and args[1] in data:
            start, stop, step = data.index(args[0]), data.index(args[1]), \
                                args[2]
            return [x for x in data[start:stop:step]]
        else:
            return "Incorrect key"
