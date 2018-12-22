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

    def __repr__(self):
        return f'{type(self).__name__}()'

    def __len__(self):
        self.file.seek(0, os.SEEK_END)
        return self.file.tell() // self.int_length

    def __getitem__(self, key):
        key = self._validate_key(key)
        self.file.seek(key * self.int_length)

        bytes_ = self.file.read(self.int_length)
        return int.from_bytes(bytes_, self.byte_order,
                              signed=self.signed)

    def __setitem__(self, key, value):
        key = self._validate_key(key)
        self.file.seek(key * self.int_length)

        bytes_ = value.to_bytes(self.int_length, self.byte_order,
                                signed=self.signed)
        self.file.write(bytes_)

    def __del__(self):
        self.file.close()

    def append(self, value):
        self.file.truncate((len(self) + 1) * self.int_length)
        self[len(self) - 1] = value

    def pop(self):
        if not len(self):
            raise IndexError(f'pop from empty {type(self).__name__!r}')

        value = self[len(self) - 1]
        self.file.truncate((len(self) - 1) * self.int_length)
        return value

    sort = quick_sort_inplace

    def _validate_key(self, key):
        if isinstance(key, slice):
            raise TypeError(f'{type(self).__name__!r} '
                            f'does not support slices')

        if key < 0:
            key += len(self)

        if not 0 <= key < len(self):
            raise IndexError(f'{type(self).__name__!r} '
                             f'assignment index out of range')

        return key
