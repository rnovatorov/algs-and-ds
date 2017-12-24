class BinHeap(object):
    """
    Represents heap data structure
    """
    def __init__(self, items=None):
        self.items = []
        if items:
            for item in items:
                self.push(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def has_parent(self, n):
        return n > 0

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

    def heapify_up(self):
        raise NotImplementedError

    def heapify_down(self):
        raise NotImplementedError


class MinBinHeap(BinHeap):

    def heapify_up(self):
        cur_item_index = len(self) - 1
        while self.has_parent(cur_item_index):
            cur_parent_index = self.parent_index(cur_item_index)

            # Must have a left child if has a right one
            if self.has_right_child(cur_parent_index):
                min_child_index = min(
                    self.left_child_index(cur_parent_index),
                    self.right_child_index(cur_parent_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                min_child_index = self.left_child_index(cur_parent_index)

            # If heap property is not violated
            if self[min_child_index] >= self[cur_parent_index]:
                return

            self.swap_by_indices(min_child_index, cur_parent_index)
            cur_item_index = cur_parent_index

    def heapify_down(self):
        cur_item_index = 0
        while self.has_children(cur_item_index):
            # Must have a left child if has a right one
            if self.has_right_child(cur_item_index):
                min_child_index = min(
                    self.left_child_index(cur_item_index),
                    self.right_child_index(cur_item_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                min_child_index = self.left_child_index(cur_item_index)

            # If heap property is not violated
            if self[min_child_index] >= self[cur_item_index]:
                return

            self.swap_by_indices(min_child_index, cur_item_index)
            cur_item_index = min_child_index


class MaxBinHeap(BinHeap):

    def heapify_up(self):
        cur_item_index = len(self) - 1
        while self.has_parent(cur_item_index):
            cur_parent_index = self.parent_index(cur_item_index)

            # Must have a left child if has a right one
            if self.has_right_child(cur_parent_index):
                max_child_index = max(
                    self.left_child_index(cur_parent_index),
                    self.right_child_index(cur_parent_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                max_child_index = self.left_child_index(cur_parent_index)

            # If heap property is not violated
            if self[max_child_index] <= self[cur_parent_index]:
                return

            self.swap_by_indices(max_child_index, cur_parent_index)
            cur_item_index = cur_parent_index

    def heapify_down(self):
        cur_item_index = 0
        while self.has_children(cur_item_index):
            # Must have a left child if has a right one
            if self.has_right_child(cur_item_index):
                max_child_index = max(
                    self.left_child_index(cur_item_index),
                    self.right_child_index(cur_item_index),
                    key=lambda i: self[i]  # By item value
                )
            else:
                max_child_index = self.left_child_index(cur_item_index)

            # If heap property is not violated
            if self[max_child_index] <= self[cur_item_index]:
                return

            self.swap_by_indices(max_child_index, cur_item_index)
            cur_item_index = max_child_index
