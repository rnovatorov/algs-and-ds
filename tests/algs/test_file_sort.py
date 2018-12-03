from io import StringIO

import pytest

from src.algs.file_sort import file_sort


def create_task(array):

    def task(algorithm):
        sorted_array = sorted(array)
        with StringIO('\n'.join(map(str, array))) as src_file:
            with StringIO() as dst_file:
                algorithm(src_file, dst_file)
                dst_file.seek(0)
                assert [int(line.strip()) for line in dst_file] == sorted_array

    return task


@pytest.mark.parametrize("task", map(create_task, [
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
]))
@pytest.mark.parametrize("algorithm", [
    file_sort
])
def test_sorting(task, algorithm):
    task(algorithm)
