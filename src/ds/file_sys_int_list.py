import os
import sys
from tempfile import TemporaryFile

from src.algs.sorting import quick_sort_inplace


class FileSysIntList:

    def __init__(
        self,
        file=None,
        int_len=4,
        byteorder=sys.byteorder,
        signed=True
    ):
        self._file = file or TemporaryFile('rb+')
        self.int_len = int_len
        self.byteorder = byteorder
        self.signed = signed

    def __repr__(self):
        return f'{type(self).__name__}()'

    def __len__(self):
        self._file.seek(0, os.SEEK_END)
        return self._file.tell() // self.int_len

    def __getitem__(self, key):
        key = self._validate_key(key)
        self._file.seek(key * self.int_len)

        bytes_ = self._file.read(self.int_len)
        return int.from_bytes(bytes_, self.byteorder,
                              signed=self.signed)

    def __setitem__(self, key, value):
        key = self._validate_key(key)
        self._file.seek(key * self.int_len)

        bytes_ = value.to_bytes(self.int_len, self.byteorder,
                                signed=self.signed)
        self._file.write(bytes_)

    def __del__(self):
        self._file.close()

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def append(self, value):
        self._file.truncate((len(self) + 1) * self.int_len)
        self[len(self) - 1] = value

    def pop(self):
        if not len(self):
            raise IndexError(f'pop from empty {type(self).__name__}')

        value = self[len(self) - 1]
        self._file.truncate((len(self) - 1) * self.int_len)
        return value

    sort = quick_sort_inplace

    def _validate_key(self, key):
        if isinstance(key, slice):
            raise TypeError(f'{type(self).__name__} '
                            f'does not support slices')

        if key < 0:
            key += len(self)

        if not 0 <= key < len(self):
            raise IndexError(f'{type(self).__name__} '
                             f'assignment index out of range')

        return key
