from proboscis import test
from hamcrest import assert_that, is_, equal_to
from src.sorting import quick_sort, heap_sort


EMPTY_ARRAY = []
UNSORTED_ARRAY = [4, -8, 15, -16, 23, -42, -42]
SORTED_ARRAY = [4, 8, 15, 16, 23, 42, 42]


@test(groups=["sorting"])
class TestSorting(object):

    @test
    def quick_sort(self):
        self.sort_all_arrays(quick_sort)

    @test
    def heap_sort(self):
        self.sort_all_arrays(heap_sort)

    def sort_all_arrays(self, sorting_algorithm):
        for sorting_task in [
            self.sort_empty_array,
            self.sort_unsorted_array,
            self.sort_sorted_array
        ]:
            sorting_task(sorting_algorithm)

    def sort_empty_array(self, sorting_algorithm):
        assert_that(
            sorting_algorithm(EMPTY_ARRAY),
            is_(equal_to(EMPTY_ARRAY))
        )

    def sort_unsorted_array(self, sorting_algorithm):
        assert_that(
            sorting_algorithm(UNSORTED_ARRAY),
            is_(equal_to(sorted(UNSORTED_ARRAY)))
        )

    def sort_sorted_array(self, sorting_algorithm):
        assert_that(
            sorting_algorithm(SORTED_ARRAY),
            is_(equal_to(SORTED_ARRAY))
        )
