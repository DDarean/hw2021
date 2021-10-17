from keyword import iskeyword
from os import path


class KVStorageClass:
    def __init__(self, file_name):
        super().__setattr__('data', dict())
        with open(path.join(path.dirname(__file__), file_name)) as f:
            for line in f:
                key, value = line.strip().split('=')
                if iskeyword(key):
                    raise ValueError('Keyword cannot be assigned as attribute')
                if key.isdigit():
                    raise ValueError('String expected as key')
                try:
                    self.data[key] = int(value)
                except ValueError:
                    self.data[key] = value

    def __getattr__(self, item):
        try:
            return self.data[item]
        except KeyError:
            raise KeyError('Unknown key')

    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError:
            raise KeyError('Unknown key')

    def __setattr__(self, key, value):
        self.data[key] = value
