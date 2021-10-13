"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""
from contextlib import contextmanager


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass


class SuppressorClass:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exception_type, value, traceback):
        if self.exception is exception_type:
            return True
