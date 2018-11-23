import os
from tempfile import TemporaryFile


def file_sort(src_filename, dst_filename):
    array = FilesystemArray.from_numbers_file(
        src_filename=src_filename,
        int_len=4,
        signed=False
    )
    quick_sort_in_place(array, 0, len(array))
    array.to_numbers_file(dst_filename)


def quick_sort_in_place(array, start, stop):
    raise NotImplementedError


class FilesystemArray:

    BYTE_ORDER = 'big'

    def __init__(self, file, int_len, signed):
        self.file = file
        self.int_len = int_len
        self.signed = signed

    def __len__(self):
        self.file.seek(0, os.SEEK_END)
        return self.file.tell() // self.int_len

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError
        self.file.seek(self.int_len * item)
        return self.file.read(self.int_len)

    def __setitem__(self, key, value):
        assert len(value) == self.int_len
        self.file.seek(self.int_len * key)
        self.file.write(value)

    def __del__(self):
        self.file.close()

    def to_numbers_file(self, dst_filename):
        self.file.seek(0)
        with open(dst_filename, 'w') as dst:
            for as_bytes in self:
                number = int.from_bytes(as_bytes, self.BYTE_ORDER, signed=self.signed)
                dst.write(f'{number}\n')

    @classmethod
    def from_numbers_file(
            cls,
            src_filename,
            int_len,
            signed
    ):
        with open(src_filename, 'r') as src_file:
            dst_file = TemporaryFile('rb+')
            for line in src_file:
                number = int(line.strip())
                as_bytes = number.to_bytes(int_len, cls.BYTE_ORDER, signed=signed)
                dst_file.write(as_bytes)
        return cls(dst_file, int_len, signed)
