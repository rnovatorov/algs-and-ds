# TODO: Add tests.


class SinglyLinkedList:

    def __init__(self, first):
        self.first = first

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self):
        return f'<{type(self).__name__}(first={self.first})'

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def insert_left(self, node):
        node.next = self.first
        self.first = node

    def remove_after(self, node):
        if node.next is None:
            raise ValueError('Cannot remove after last node')
        node.next = node.next.next

    def remove_left(self):
        self.first = self.first.next


class SinglyLinkedListNode:

    def __init__(self, value, next=None):
        assert next is None or isinstance(next, type(self))
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{type(self).__name__}(value={self.value}, next={self.next})'
