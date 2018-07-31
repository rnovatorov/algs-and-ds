from collections import defaultdict


class Graph(object):
    """
    https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
    """
    DEFAULT_WEIGHT = 1

    def __init__(self):
        self._conns = defaultdict(dict)

    def __iter__(self):
        return iter(self._conns)

    def __getitem__(self, key):
        return self._conns[key]

    def connect(self, src, dst, weight=DEFAULT_WEIGHT, bidir=False):
        self[src][dst] = weight
        self[dst]

        if bidir:
            self.connect(dst, src, weight)

    def disconnect(self, src, dst, bidir=False):
        del self[src][dst]

        if bidir:
            self.disconnect(dst, src)

