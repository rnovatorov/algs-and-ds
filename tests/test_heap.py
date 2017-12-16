import pytest
from src.heap import Heap, MinHeap, MaxHeap


@pytest.fixture()
def disable_heapify(monkeypatch):
    monkeypatch.setattr(Heap, "heapify", lambda self: None)


@pytest.mark.usefixtures("disable_heapify")
class TestHeap(object):

    def test_create(self):
        array = range(3)
        assert Heap(array) == list(array)

    def test_create_empty(self):
        assert not Heap()

    def test_has_left_child(self):
        heap = Heap(range(3))
        assert heap.has_left_child(0)
        assert not heap.has_left_child(1)
        assert not heap.has_left_child(2)

    def test_has_right_child(self):
        heap = Heap(range(3))
        assert heap.has_right_child(0)
        assert not heap.has_right_child(1)
        assert not heap.has_right_child(2)

    def test_has_parent(self):
        heap = Heap(range(3))
        assert not heap.has_parent(heap[0])
        assert heap.has_parent(heap[1])
        assert heap.has_parent(heap[2])

    def test_left_child(self):
        heap = Heap(range(3))
        assert heap.left_child(0) == heap[1]

    def test_right_child(self):
        heap = Heap(range(3))
        assert heap.right_child(0) == heap[2]

    def test_parent_index(self):
        heap = Heap(range(3))
        assert heap.parent(1) == heap[0]
        assert heap.parent(2) == heap[0]

    def test_peek(self):
        heap = Heap(range(3))
        assert heap.peek() == heap[0]

    def test_push(self):
        heap = Heap(range(3))
        heap.push(42)
        assert 42 in heap

    def test_pop(self):
        array = range(3)
        heap = Heap(array)
        assert heap.pop() == array[-1]
        assert len(heap) == len(array) - 1


def test_min_heapify():
    min_heap = MinHeap([0, 4, -8, 15, -16, 23, -42, -42])
    for n, item in enumerate(min_heap):
        if min_heap.has_left_child(n):
            assert item < min_heap.left_child(n)
        if min_heap.has_right_child(n):
            assert item < min_heap.right_child(n)


def test_max_heapify():
    max_heap = MaxHeap([0, 4, -8, 15, -16, 23, -42, -42])
    for n, item in enumerate(max_heap):
        if max_heap.has_left_child(n):
            assert item > max_heap.left_child(n)
        if max_heap.has_right_child(n):
            assert item > max_heap.right_child(n)
