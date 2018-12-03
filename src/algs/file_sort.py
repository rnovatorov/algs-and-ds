import os
from tempfile import TemporaryFile
from .sorting import quick_sort_inplace


def file_sort(src_file, dst_file):
    array = FilesystemArray.from_numbers_file(
        src_file=src_file,
        int_len=4,
        signed=True
    )
    quick_sort_inplace(array)
    array.to_numbers_file(dst_file)


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
        as_bytes = self.file.read(self.int_len)
        return int.from_bytes(as_bytes, self.BYTE_ORDER,
                              signed=self.signed)

    def __setitem__(self, key, value):
        self.file.seek(self.int_len * key)
        as_bytes = value.to_bytes(self.int_len, self.BYTE_ORDER,
                                  signed=self.signed)
        self.file.write(as_bytes)

    def __del__(self):
        self.file.close()

    def to_numbers_file(self, dst):
        self.file.seek(0)
        for number in self:
            dst.write(f'{number}\n')

    @classmethod
    def from_numbers_file(
        cls,
        src_file,
        int_len,
        signed
    ):
        dst_file = TemporaryFile('rb+')
        for line in src_file:
            number = int(line.strip())
            as_bytes = number.to_bytes(int_len, cls.BYTE_ORDER,
                                       signed=signed)
            dst_file.write(as_bytes)
        return cls(dst_file, int_len, signed)
