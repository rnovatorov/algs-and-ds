"""
Tests for sorting algorithms
"""

from src.sorting import insertion_sort, selection_sort, merge_sort, \
                        quick_sort, min_heap_sort, max_heap_sort, bubble_sort


def test_insertion_sort():
    sort_all_arrays(insertion_sort)


def test_selection_sort():
    sort_all_arrays(selection_sort)


def test_merge_sort():
    sort_all_arrays(merge_sort)


def test_quick_sort():
    sort_all_arrays(quick_sort)


def test_min_heap_sort():
    sort_all_arrays(min_heap_sort)

def test_max_heap_sort():
    sort_all_arrays(max_heap_sort)


def test_bubble_sort():
    sort_all_arrays(bubble_sort)


def sort_all_arrays(sorting_algorithm):
    for sorting_task in [
        sort_empty_array,
        sort_unsorted_array,
        sort_sorted_array,
        sort_array_of_same_elements
    ]:
        sorting_task(sorting_algorithm)


def sort_empty_array(sorting_algorithm):
    empty_array = []
    assert sorting_algorithm(empty_array) == empty_array


def sort_unsorted_array(sorting_algorithm):
    unsorted_array = [0, 4, -8, 15, -16, 23, -42, -42]
    assert sorting_algorithm(unsorted_array) == sorted(unsorted_array)


def sort_sorted_array(sorting_algorithm):
    sorted_array = [0, 4, 8, 15, 16, 23, 42, 42]
    assert sorting_algorithm(sorted_array) == sorted_array


def sort_array_of_same_elements(sorting_algorithm):
    array_of_same_elements = [42] * 8
    assert sorting_algorithm(array_of_same_elements) == array_of_same_elements
