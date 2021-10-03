import hashlib
import random
import struct
import time
from multiprocessing import Pool
from timeit import default_timer as timer


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocess_calculate(n):
    start = timer()
    values = range(0, n)
    with Pool(processes=60) as pool:
        res = pool.map(slow_calculate, values)
    end = timer()
    exec_time = end - start  # for tests
    return sum(res), exec_time
