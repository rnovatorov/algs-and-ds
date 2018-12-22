
import pytest

from src.ds.file_sys_int_arr import FileSysIntArr


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
    fsa = FileSysIntArr()
    fsa.fill(array)
    fsa.sort()
    assert list(fsa) == sorted(array)
