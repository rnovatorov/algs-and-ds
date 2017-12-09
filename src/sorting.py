import random
from heapq import heappush, heappop


def quick_sort(array):
    # Recursion base case
    if len(array) == 0 or len(array) == 1:
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


def heap_sort(array):
    heap = []
    for item in array:
        heappush(heap, item)
    return [heappop(heap) for _ in range(len(array))]
