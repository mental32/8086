import json
import struct
import struct
import pathlib
import platform
import itertools
from os.path import join as path
from time import time as _time

_save_file_dir = None
_system_type = platform.system().lower()

if _system_type == 'linux':
    _save_file_dir = pathlib.Path.home().absolute() / '._8086'

if not _save_file_dir.exists():
    os.mkdir(f'{_save_file_dir}')

_save_file_dir = f'{_save_file_dir}'


class SaveFile:
    def __init__(self, fp):
        self.fp = fp

        with open(path(fp, 'save.dat'), 'rb') as inf:
            ts = inf.read(4)
            self.__data = json.loads(self.xe(inf.read(), ts).decode())

        self.__data['timestamp'], = struct.unpack('=L', ts)

        print(self.__data)

    def __repr__(self):
        return f'<SaveFile: fp={self.fp!r}>'

    def __bool__(self):
        return bool(self.fp)

    @classmethod
    def new_save(cls, username):
        fp = os.path.join(_save_file_dir, username)
        ts = struct.pack('<L', int(_time()))

        os.mkdir(save_path)

        with open(path(fp, 'save.dat'), 'wb') as inf:
            inf.write(ts)
            inf.write(cls.xe('{"levels": []}'.encode('ascii'), ts))

        return cls(fp)

    @property
    def data(self):
        return self.__data

    @staticmethod
    def xe(p, k):
        k = itertools.cycle(k)
        return b''.join(struct.pack('<B', c ^ next(k)) for c in p)

