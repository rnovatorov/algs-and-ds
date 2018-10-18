import pytest
from src.algs.sorting import insertion_sort, selection_sort, merge_sort,\
    quick_sort, min_heap_sort, max_heap_sort, bubble_sort


def create_task(array):

    def task(algorithm):
        assert sorted(array) == algorithm(array)

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
    insertion_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    min_heap_sort,
    max_heap_sort,
    bubble_sort,
])
def test_sorting(task, algorithm):
    task(algorithm)
