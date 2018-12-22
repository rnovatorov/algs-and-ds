import os
from tempfile import TemporaryFile

from src.algs.sorting import quick_sort_inplace


class FileSysIntArr:

    DEFAULT_INT_LENGTH = 32
    DEFAULT_BYTE_ORDER = 'big'
    DEFAULT_SIGNED = True

    def __init__(self, file=None,
                 int_length=DEFAULT_INT_LENGTH,
                 byte_order=DEFAULT_BYTE_ORDER,
                 signed=DEFAULT_SIGNED):
        self.file = file or TemporaryFile('rb+')
        self.int_length = int_length
        self.byte_order = byte_order
        self.signed = signed

    def __len__(self):
        self.file.seek(0, os.SEEK_END)
        return self.file.tell() // self.int_length

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError
        self.file.seek(self.int_length * item)
        as_bytes = self.file.read(self.int_length)
        return int.from_bytes(as_bytes, self.byte_order,
                              signed=self.signed)

    def __setitem__(self, key, value):
        self.file.seek(self.int_length * key)
        as_bytes = value.to_bytes(self.int_length, self.byte_order,
                                  signed=self.signed)
        self.file.write(as_bytes)

    def __del__(self):
        self.file.close()

    def fill(self, iterable):
        for i, value in enumerate(iterable):
            self[i] = value

    sort = quick_sort_inplace
