import json
import struct
import itertools
from os.path import join as path

class SaveFile:
    def __init__(self, fp):
        self.fp = fp

        with open(path(fp, 'save.dat'), 'rb') as inf:
            ts = inf.read(4)
            _key = itertools.cycle(ts)
            _data = inf.read()

        self.__data = json.loads(''.join(chr(i ^ next(_key)) for i in _data))
        self.__data['timestamp'], = struct.unpack('=L', ts)

        print(self.__data)

    def __repr__(self):
        return f'<SaveFile: fp={self.fp!r}>'

    def __bool__(self):
        return bool(self.fp)

    @property
    def data(self):
        return self.__data
