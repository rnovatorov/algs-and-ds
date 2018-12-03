from io import StringIO

import pytest

from src.ds.filesystem_array import FilesystemArray


INT_LEN = 4
SIGNED = True


@pytest.mark.parametrize('array', [
    # No items
    [],

    # One item
    [42],

    # Two sorted items
    [4, 8],

    # Two unsorted items
    [8, 4],

    # Many sorted items
    [0, 4, 8, 15, 16, 23, 42, 42],

    # Many unsorted items
    [0, 4, -8, 15, -16, 23, -42, -42],

    # Same items
    [42] * 8,
])
def test_sorting(array):
    sorted_array = sorted(array)
    with StringIO('\n'.join(map(str, array))) as src_file:
        filesystem_array = FilesystemArray.from_numbers_file(
            src_file,
            int_len=INT_LEN,
            signed=SIGNED
        )
        filesystem_array.sort()
        with StringIO() as dst_file:
            filesystem_array.to_numbers_file(dst_file)
            dst_file.seek(0)
            assert [int(line.strip()) for line in dst_file] == sorted_array
