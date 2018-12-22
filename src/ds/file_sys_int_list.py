import os
import sys
from tempfile import TemporaryFile

from src.algs.sorting import quick_sort_inplace


class FileSysIntList:

    def __init__(
        self,
        file=None,
        int_length=4,
        byte_order=sys.byteorder,
        signed=True
    ):
        self.file = file or TemporaryFile('rb+')
        self.int_length = int_length
        self.byte_order = byte_order
        self.signed = signed
        self._last_i = -1

    def __len__(self):
        self.file.seek(0, os.SEEK_END)
        return self.file.tell() // self.int_length

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError
        self.file.seek(self.int_length * item)
        bytes_ = self.file.read(self.int_length)
        return int.from_bytes(bytes_, self.byte_order,
                              signed=self.signed)

    def __setitem__(self, key, value):
        self.file.seek(self.int_length * key)
        bytes_ = value.to_bytes(self.int_length, self.byte_order,
                                signed=self.signed)
        self.file.write(bytes_)
        self._last_i = max(self._last_i, key)

    def __del__(self):
        self.file.close()

    def append(self, value):
        self._last_i += 1
        self[self._last_i] = value

    def pop(self):
        if not len(self):
            raise IndexError(f'pop from empty {type(self).__name__}')
        value = self[self._last_i]
        self.file.truncate(self._last_i * self.int_length)
        self._last_i -= 1
        return value

    sort = quick_sort_inplace
