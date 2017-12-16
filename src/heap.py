class Heap(object):
    """
    Represents heap data structure
    """
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []
        if len(self) > 1:
            self.heapify()

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other

    def __getitem__(self, item):
        return self.items[item]

    def has_parent(self, n):
        return n > 0

    def has_left_child(self, n):
        return (2 * n) + 1 < len(self)

    def has_right_child(self, n):
        return (2 * n) + 2 < len(self)

    def parent(self, n):
        return self[(n - 1) // 2]

    def left_child(self, n):
        return self[(2 * n) + 1]

    def right_child(self, n):
        return self[(2 * n) + 2]

    def peek(self):
        return self[0]

    def push(self, item):
        self.items.append(item)
        self.heapify()

    def pop(self):
        item = self.items.pop()
        if len(self) > 1:
            self.heapify()
        return item

    def heapify(self):
        raise NotImplementedError


# TODO: Implement
class MinHeap(Heap):

    def heapify(self):
        raise NotImplementedError


# TODO: Implement
class MaxHeap(Heap):

    def heapify(self):
        raise NotImplementedError
