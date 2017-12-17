from src.heap import BinHeap, MinBinHeap, MaxBinHeap


class TestBinHeap(object):

    def create_fake_heap(self, items):
        heap = BinHeap()
        heap.items = items
        return heap

    def test_create_empty(self):
        assert not BinHeap()

    def test_has_left_child(self):
        heap = self.create_fake_heap(range(3))
        assert heap.has_left_child(0)
        assert not heap.has_left_child(1)
        assert not heap.has_left_child(2)

    def test_has_right_child(self):
        heap = self.create_fake_heap(range(3))
        assert heap.has_right_child(0)
        assert not heap.has_right_child(1)
        assert not heap.has_right_child(2)

    def test_has_parent(self):
        heap = self.create_fake_heap(range(3))
        assert not heap.has_parent(heap[0])
        assert heap.has_parent(heap[1])
        assert heap.has_parent(heap[2])

    def test_left_child_index(self):
        heap = self.create_fake_heap(range(42))
        assert heap.left_child_index(0) == heap[1]

    def test_right_child_index(self):
        heap = self.create_fake_heap(range(42))
        assert heap.right_child_index(0) == heap[2]

    def test_parent_index(self):
        heap = self.create_fake_heap(range(42))
        assert heap.parent_index(1) == heap[0]
        assert heap.parent_index(2) == heap[0]

    def test_peek(self):
        heap = self.create_fake_heap(range(42))
        assert heap.peek() == heap[0]


class TestMinBinHeap(object):

    def has_min_heap_property(self, min_heap):
        for n, item in enumerate(min_heap):
            if min_heap.has_left_child(n):
                if item > min_heap[min_heap.left_child_index(n)]:
                    return False
            if min_heap.has_right_child(n):
                if item > min_heap[min_heap.right_child_index(n)]:
                    return False
        return True

    def test_heap_property(self):
        min_heap = MinBinHeap([0, 4, -8, 15, -16, 23, -42, -42])
        assert self.has_min_heap_property(min_heap)

    def test_pop(self):
        min_heap = MinBinHeap([0, 4, -8, 15, -16, 23, -42, -42])
        for _ in range(len(min_heap)):
            min_heap.pop()
            assert self.has_min_heap_property(min_heap)


class TestMaxBinHeap(object):

    def has_max_heap_property(self, max_heap):
        for n, item in enumerate(max_heap):
            if max_heap.has_left_child(n):
                if item < max_heap[max_heap.left_child_index(n)]:
                    return False
            if max_heap.has_right_child(n):
                if item < max_heap[max_heap.right_child_index(n)]:
                    return False
        return True

    def test_heap_property(self):
        max_heap = MaxBinHeap([0, 4, -8, 15, -16, 23, -42, -42])
        assert self.has_max_heap_property(max_heap)

    def test_pop(self):
        max_heap = MaxBinHeap([0, 4, -8, 15, -16, 23, -42, -42])
        for _ in range(len(max_heap)):
            max_heap.pop()
            assert self.has_max_heap_property(max_heap)
