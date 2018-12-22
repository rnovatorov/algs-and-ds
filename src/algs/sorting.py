from src.ds.bin_heap import MinBinHeap, MaxBinHeap


def insertion_sort(lst):
    """
    https://en.wikipedia.org/wiki/Insertion_sort
    """
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                lst.insert(j, lst.pop(i))
    return lst


def selection_sort(lst):
    """
    https://en.wikipedia.org/wiki/Selection_sort
    """
    for i in range(len(lst) - 1):
        m = min(range(i, len(lst)), key=lambda j: lst[j])
        lst[i], lst[m] = lst[m], lst[i]
    return lst


def merge_sort(lst):
    """
    https://en.wikipedia.org/wiki/Merge_sort
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left, right = lst[:mid], lst[mid:]

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


def min_heap_sort(lst):
    """
    https://en.wikipedia.org/wiki/Heapsort
    """
    h = MinBinHeap(lst)
    return [h.pop() for _ in lst]


def max_heap_sort(lst):
    """
    https://en.wikipedia.org/wiki/Heapsort
    """
    h = MaxBinHeap(lst)
    result = [h.pop() for _ in lst]
    result.reverse()
    return result


def quick_sort(lst):
    """
    https://en.wikipedia.org/wiki/Quicksort
    """
    if not lst:
        return lst

    pivot = lst.pop()

    left, right = [], []

    for item in lst:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_inplace(lst, i_first=0, i_last=None):
    """
    https://en.wikipedia.org/wiki/Quicksort
    """
    if i_last is None:
        i_last = len(lst) - 1

    if i_last <= i_first:
        return lst

    i_cur = i_large = i_first

    while i_cur != i_last:
        if lst[i_cur] < lst[i_last]:
            lst[i_cur], lst[i_large] = lst[i_large], lst[i_cur]
            i_large += 1
        i_cur += 1

    lst[i_last], lst[i_large] = lst[i_large], lst[i_last]

    quick_sort_inplace(lst, i_first, i_large - 1)
    quick_sort_inplace(lst, i_large + 1, i_last)

    return lst


def bubble_sort(lst):
    """
    https://en.wikipedia.org/wiki/Bubble_sort
    """
    while True:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        # not swapped -> sorted
        if not swapped:
            break
    return lst
