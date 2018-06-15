# TODO: Add delete


class BinSearchTree(object):
    """
    https://en.wikipedia.org/wiki/Binary_search_tree
    """
    def __init__(self, items=None):
        self.root = None
        if items is not None:
            for item in items:
                self.insert(item)

    def insert(self, item):
        node = BinTreeNode(key=item)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def search(self, item):
        self.root.search(key=item)


class BinTreeNode(object):

    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child

    def insert(self, node):
        if node.key < self.key:
            if self.left_child is not None:
                self.left_child.insert(node)
            else:
                self.left_child = node
        else:
            if self.right_child is not None:
                self.right_child.insert(node)
            else:
                self.right_child = node

    def search(self, key):
        if self.key == key:
            return self
        elif self.key < key:
            if self.left_child:
                return self.left_child.search(key)
        else:
            if self.right_child:
                return self.right_child.search(key)
