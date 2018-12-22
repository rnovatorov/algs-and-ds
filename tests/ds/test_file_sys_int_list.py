
import pytest

from src.ds.file_sys_int_list import FileSysIntList


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
    fsl = FileSysIntList()
    for value in array:
        fsl.append(value)
    fsl.sort()
    assert list(fsl) == sorted(array)


def test_append_and_pop():
    fsl = FileSysIntList()
    assert len(fsl) == 0

    with pytest.raises(IndexError):
        fsl.pop()

    fsl.append(0)
    assert len(fsl) == 1
    assert fsl[0] == 0

    fsl.append(1)
    assert len(fsl) == 2
    assert fsl[1] == 1

    assert fsl.pop() == 1
    assert len(fsl) == 1

    assert fsl.pop() == 0
    assert len(fsl) == 0

    with pytest.raises(IndexError):
        fsl.pop()
