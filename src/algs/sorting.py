from src.ds.bin_heap import MinBinHeap, MaxBinHeap


def insertion_sort(array):
    """
    https://en.wikipedia.org/wiki/Insertion_sort
    """
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
    return array


def selection_sort(array):
    """
    https://en.wikipedia.org/wiki/Selection_sort
    """
    for i in range(len(array) - 1):
        m = min(range(i, len(array)), key=lambda j: array[j])
        array[i], array[m] = array[m], array[i]
    return array


def merge_sort(array):
    """
    https://en.wikipedia.org/wiki/Merge_sort
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = array[:mid], array[mid:]

    return _merge(merge_sort(left), merge_sort(right))


def _merge(left, right):
    """
    "Merge" part of merge sort.
    """
    merged = []
    i_left = i_right = 0
    while True:
        if i_left == len(left):
            return merged + right[i_right:]
        if i_right == len(right):
            return merged + left[i_left:]
        if left[i_left] < right[i_right]:
            merged.append(left[i_left])
            i_left += 1
        else:
            merged.append(right[i_right])
            i_right += 1


def min_heap_sort(array):
    """
    https://en.wikipedia.org/wiki/Heapsort
    """
    h = MinBinHeap(array)
    return [h.pop() for _ in array]


def max_heap_sort(array):
    """
    https://en.wikipedia.org/wiki/Heapsort
    """
    h = MaxBinHeap(array)
    result = [h.pop() for _ in array]
    result.reverse()
    return result


def quick_sort(array):
    """
    https://en.wikipedia.org/wiki/Quicksort
    """
    if not array:
        return array

    pivot = array.pop()

    left, right = [], []

    for item in array:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_inplace(array, i_first=0, i_last=None):
    """
    https://en.wikipedia.org/wiki/Quicksort
    """
    if i_last is None:
        i_last = len(array) - 1

    if i_last <= i_first:
        return array

    i_cur = i_large = i_first

    while i_cur != i_last:
        if array[i_cur] < array[i_last]:
            array[i_cur], array[i_large] = array[i_large], array[i_cur]
            i_large += 1
        i_cur += 1

    array[i_last], array[i_large] = array[i_large], array[i_last]

    quick_sort_inplace(array, i_first, i_large - 1)
    quick_sort_inplace(array, i_large + 1, i_last)

    return array


def bubble_sort(array):
    """
    https://en.wikipedia.org/wiki/Bubble_sort
    """
    while True:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # not swapped -> sorted
        if not swapped:
            break
    return array
