
import pytest

from src.ds.file_sys_int_list import FileSysIntList


@pytest.fixture(name='fsl')
def fixture_fsl():
    return FileSysIntList()


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
def test_sorting(fsl, array):
    for value in array:
        fsl.append(value)
    fsl.sort()
    assert list(fsl) == sorted(array)


def test_mutating(fsl):
    assert len(fsl) == 0

    with pytest.raises(IndexError):
        fsl.pop()

    fsl.append(42)
    assert len(fsl) == 1
    assert fsl[0] == 42

    fsl.append(43)
    assert len(fsl) == 2
    assert fsl[1] == 43

    assert fsl.pop() == 43
    assert len(fsl) == 1

    assert fsl.pop() == 42
    assert len(fsl) == 0

    with pytest.raises(IndexError):
        fsl.pop()


def test_indexing(fsl):
    with pytest.raises(TypeError):
        fsl[:]

    with pytest.raises(IndexError):
        fsl.pop()

    with pytest.raises(IndexError):
        fsl[0]

    with pytest.raises(IndexError):
        fsl[0] = 42

    with pytest.raises(IndexError):
        fsl[-1]

    fsl.append(42)
    assert fsl[-1] == 42

    fsl[-1] = 43
    assert fsl[0] == fsl[-1] == 43
