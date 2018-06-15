"""
Tests for sorting algorithms
"""

import pytest
from src.algs.sorting import insertion_sort, selection_sort, merge_sort,\
    quick_sort, min_heap_sort, max_heap_sort, bubble_sort


@pytest.fixture()
def arrays_to_be_sorted():
    return [
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
        [42] * 8
    ]


def test_insertion_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert insertion_sort(array) == sorted(array)


def test_selection_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert selection_sort(array) == sorted(array)


def test_merge_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert merge_sort(array) == sorted(array)


def test_quick_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert quick_sort(array) == sorted(array)


def test_min_heap_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert min_heap_sort(array) == sorted(array)


def test_max_heap_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert max_heap_sort(array) == sorted(array)


def test_bubble_sort(arrays_to_be_sorted):
    for array in arrays_to_be_sorted:
        assert bubble_sort(array) == sorted(array)
