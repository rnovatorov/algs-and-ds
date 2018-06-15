class BinHeap(object):
    """
    https://en.wikipedia.org/wiki/Binary_heap
    """
    def __init__(self, items=None):
        self.items = []
        if items:
            for item in items:
                self.push(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def is_root(self, n):
        return n == 0

    def has_children(self, n):
        return self.has_left_child(n) or self.has_right_child(n)

    def has_left_child(self, n):
        return self.left_child_index(n) < len(self)

    def has_right_child(self, n):
        return self.right_child_index(n) < len(self)

    def parent_index(self, n):
        return (n - 1) // 2

    def left_child_index(self, n):
        return (2 * n) + 1

    def right_child_index(self, n):
        return (2 * n) + 2

    def swap_by_indices(self, n, m):
        self[n], self[m] = self[m], self[n]

    def peek(self):
        return self[0]

    def push(self, item):
        self.items.append(item)
        self.heapify_up()

    def pop(self):
        if len(self) <= 1:
            return self.items.pop()

        # Swap first and last items
        self.swap_by_indices(0, -1)

        # Pop last item and restore heap property
        item = self.items.pop()
        self.heapify_down()
        return item

    def choose_child(self, func, parent_index):
        left_child_index = self.left_child_index(parent_index)
        right_child_index = self.right_child_index(parent_index)
        if self.has_right_child(parent_index):
            return func(
                left_child_index,
                right_child_index,
                key=lambda i: self[i]  # By value
            )
        else:
            return left_child_index  # The only child

    def heapify_up(self):
        raise NotImplementedError

    def heapify_down(self):
        raise NotImplementedError


class MinBinHeap(BinHeap):

    def heapify_up(self):
        item_index = len(self) - 1
        while not self.is_root(item_index):
            parent_index = self.parent_index(item_index)

            # Must have a left child if has a right one
            if self.has_right_child(parent_index):
                min_child_index = min(
                    self.left_child_index(parent_index),
                    self.right_child_index(parent_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                min_child_index = item_index

            # If heap property is not violated
            if self[min_child_index] >= self[parent_index]:
                return

            self.swap_by_indices(min_child_index, parent_index)
            item_index = parent_index

    def heapify_down(self):
        item_index = 0
        while self.has_children(item_index):
            # Must have a left child if has a right one
            if self.has_right_child(item_index):
                min_child_index = min(
                    self.left_child_index(item_index),
                    self.right_child_index(item_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                min_child_index = self.left_child_index(item_index)

            # If heap property is not violated
            if self[min_child_index] >= self[item_index]:
                return

            self.swap_by_indices(min_child_index, item_index)
            item_index = min_child_index


class MaxBinHeap(BinHeap):

    def heapify_up(self):
        item_index = len(self) - 1
        while not self.is_root(item_index):
            parent_index = self.parent_index(item_index)

            # Must have a left child if has a right one
            if self.has_right_child(parent_index):
                max_child_index = max(
                    self.left_child_index(parent_index),
                    self.right_child_index(parent_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                max_child_index = item_index

            # If heap property is not violated
            if self[max_child_index] <= self[parent_index]:
                return

            self.swap_by_indices(max_child_index, parent_index)
            item_index = parent_index

    def heapify_down(self):
        item_index = 0
        while self.has_children(item_index):
            # Must have a left child if has a right one
            if self.has_right_child(item_index):
                max_child_index = max(
                    self.left_child_index(item_index),
                    self.right_child_index(item_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                max_child_index = self.left_child_index(item_index)

            # If heap property is not violated
            if self[max_child_index] <= self[item_index]:
                return

            self.swap_by_indices(max_child_index, item_index)
            item_index = max_child_index
