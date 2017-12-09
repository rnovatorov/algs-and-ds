from proboscis import test
from hamcrest import assert_that, is_, equal_to
from src.sorting import quick_sort


EMPTY_ARRAY = []
UNSORTED_ARRAY = [4, -8, 15, -16, 23, -42, -42]
SORTED_ARRAY = [4, 8, 15, 16, 23, 42, 42]


@test(groups=["sorting", "quick_sort"])
class TestQuickSort(object):

    @test
    def empty_array(self):
        assert_that(quick_sort(EMPTY_ARRAY),
        is_(equal_to(EMPTY_ARRAY)))

    @test
    def unsorted_array(self):
        assert_that(quick_sort(UNSORTED_ARRAY),
        is_(equal_to(sorted(UNSORTED_ARRAY))))

    @test
    def sorted_array(self):
        assert_that(quick_sort(SORTED_ARRAY),
        is_(equal_to(SORTED_ARRAY)))
