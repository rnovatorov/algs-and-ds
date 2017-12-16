import random
from .heap import MinHeap


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
    return array


def selection_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array)):
        m = array[i]  # Min
        for j in range(i + 1, len(array)):
            if array[j] < m:
                m = array[j]
        array[i] = m
    return array


def merge_sort(array):
    # Recursion base case
    if len(array) <= 1:
        return array

    # Divide
    mid = int(len(array) / 2)
    left, right = array[:mid], array[mid:]

    # Conquer
    return _merge(merge_sort(left), merge_sort(right))


# TODO: Find a way to avoid list.pop(0)... deque?
def _merge(left, right):
    merged = []
    while True:
        if not left:
            merged.extend(right)
            return merged
        if not right:
            merged.extend(left)
            return merged
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))


# TODO: Add max_heap_sort as well
def heap_sort(array):
    h = MinHeap(array)
    return [h.pop() for _ in range(len(array))]


def quick_sort(array):
    # Recursion base case
    if len(array) <= 1:
        return array

    # Choose pivot
    pivot = random.choice(array)

    # Divide
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            center.append(item)
        else:
            right.append(item)

    # Conquer
    return quick_sort(left) + center + quick_sort(right)


def bubble_sort(array):
    while True:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # not swapped => sorted
        if not swapped:
            break
    return array
