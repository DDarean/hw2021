import tempfile

import pytest

from homework8.task1 import KVStorageClass


def test_iterable_name():
    with tempfile.NamedTemporaryFile(mode='w+t', dir='.', delete=False) as fp:
        fp.write('name=kek \n')
        fp.seek(0)
        storage = KVStorageClass(fp.name)
        assert storage['name'] == 'kek'


def test_iterable_attr():
    with tempfile.NamedTemporaryFile(mode='w+t', dir='.', delete=False) as fp:
        fp.write('last_name=top \n')
        fp.seek(0)
        storage = KVStorageClass(fp.name)
        assert storage.last_name == 'top'


def test_if_int():
    with tempfile.NamedTemporaryFile(mode='w+t', dir='.', delete=False) as fp:
        fp.write('power=9001')
        fp.seek(0)
        storage = KVStorageClass(fp.name)
        assert isinstance(storage.power, int)


def test_value_error():
    with tempfile.NamedTemporaryFile(mode='w+t', dir='.', delete=False) as fp:
        fp.write('1=ValueError')
        fp.seek(0)
        with pytest.raises(ValueError):
            KVStorageClass(fp.name)
