# TODO: Add search, insert and delete


class RadixTree(object):
    """
    https://en.wikipedia.org/wiki/Radix_tree
    """
    def __init__(self, word_list):
        self.root = RadixTreeNode(word_list)

    def __getitem__(self, item):
        return self.root[item]


class RadixTreeNode(object):
    """
    Represent a node in a RadixTree.
    """
    def __init__(self, word_list, depth=0):
        self.children = {}
        self.depth = depth
        self._build(word_list)

    def __getitem__(self, item):
        return self.children.get(item)

    def _build(self, word_list):
        cur_fl = None  # Current first letter
        cropped_list = []

        for word in sorted(word_list):
            # If word is not empty (last level nodes)
            if word:
                new_fl_needed = cur_fl != word[0]
                if new_fl_needed:
                    # Excluding indexing error
                    if cropped_list:
                        self._make_child(cur_fl, cropped_list)
                        cropped_list = []
                    cur_fl = word[0]
                cropped_list.append(word[1:])

        # Taking care of last letter
        if cropped_list:
            self._make_child(cur_fl, cropped_list)

    def _make_child(self, key, word_list):
        child = RadixTreeNode(word_list, depth=self.depth + 1)
        self.children[key] = child
