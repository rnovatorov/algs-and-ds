class Graph(object):
    """
    Represents graph data structure
    """
    def __init__(self, vids=None, edges=None):
        self.vertices = {}
        if vids:
            for vid in vids:
                self.add_vertex(vid)
        if edges:
            for edge in edges:
                self.add_edge(edge)

    def __str__(self):
        return "<Graph(vertices=%s)>" % self.vertices

    def add_vertex(self, vid):
        self.vertices[vid] = Vertex(id=vid, graph=self)

    def add_edge(self, edge):
        va, vb = self.vertices[edge.va_id], self.vertices[edge.vb_id]
        va.connect_to(vb, weight=edge.weight)
        if edge.bidir:
            vb.connect_to(va, weight=edge.weight)

    def depth_first_search(self, src, dst):
        pass

    def breadth_first_search(self, src, dst):
        pass

    def dijkstra(self, src, dst):
        pass


class Vertex(object):
    """
    Graph's vertex
    """
    def __init__(self, id, graph):
        self.id = id
        self.graph = graph
        self._conns = {}

    def __str__(self):
        return "<Vertex(id='%s', neighbors=%s)>" % (self.id, self.neighbors)

    def connect_to(self, vertex, weight=None):
        self._conns[vertex.id] = weight

    def disconnect_from(self, vertex):
        del self._conns[vertex.id]

    @property
    def neighbors(self):
        return [self.graph.vertices[vid] for vid in self._conns]

    def is_adjacent_to(self, vertex):
        return vertex.id in self._conns


class Edge(object):
    """
    Graph's edge
    """
    def __init__(self, va_id, vb_id, bidir, weight=None):
        self.va_id = va_id
        self.vb_id = vb_id
        self.bidir = bidir
        self.weight = weight
