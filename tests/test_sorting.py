from hamcrest import assert_that, is_, equal_to
from src.sorting import insertion_sort, selection_sort, merge_sort, \
                        quick_sort, heap_sort, bubble_sort


class TestSorting(object):
    """
    Tests for sorting algorithms
    """
    def test_insertion_sort(self):
        self.sort_all_arrays(insertion_sort)

    def test_selection_sort(self):
        self.sort_all_arrays(selection_sort)

    def test_merge_sort(self):
        self.sort_all_arrays(merge_sort)

    def test_quick_sort(self):
        self.sort_all_arrays(quick_sort)

    def test_heap_sort(self):
        self.sort_all_arrays(heap_sort)

    def test_bubble_sort(self):
        self.sort_all_arrays(bubble_sort)

    def sort_all_arrays(self, sorting_algorithm):
        for sorting_task in [
            self.sort_empty_array,
            self.sort_unsorted_array,
            self.sort_sorted_array,
            self.sort_array_of_same_elements
        ]:
            sorting_task(sorting_algorithm)

    def sort_empty_array(self, sorting_algorithm):
        empty_array = []
        assert_that(
            sorting_algorithm(empty_array),
            is_(equal_to(empty_array))
        )

    def sort_unsorted_array(self, sorting_algorithm):
        unsorted_array = [4, -8, 15, -16, 23, -42, -42]
        assert_that(
            sorting_algorithm(unsorted_array),
            is_(equal_to(sorted(unsorted_array)))
        )

    def sort_sorted_array(self, sorting_algorithm):
        sorted_array = [4, 8, 15, 16, 23, 42, 42]
        assert_that(
            sorting_algorithm(sorted_array),
            is_(equal_to(sorted_array))
        )

    def sort_array_of_same_elements(self, sorting_algorithm):
        array_of_same_elements = [42] * 8
        assert_that(
            sorting_algorithm(array_of_same_elements),
            is_(equal_to(array_of_same_elements))
        )
