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

    def remove_vertex(self, vid):
        del self.vertices[vid]

    def _get_vertices_pair(self, edge):
        return self.vertices[edge.src_id], self.vertices[edge.dst_id]

    def add_edge(self, edge):
        src, dst = self._get_vertices_pair(edge)
        src.connect_to(dst, weight=edge.weight)
        if not edge.directed:
            dst.connect_to(src, weight=edge.weight)

    def remove_edge(self, edge):
        src, dst = self._get_vertices_pair(edge)
        src.disconnect_from(dst)
        if not edge.directed:
            dst.disconnect_from(src)

    def depth_first_search(self, src, dst):
        raise NotImplementedError

    def breadth_first_search(self, src, dst):
        raise NotImplementedError

    def dijkstra(self, src, dst):
        raise NotImplementedError


class Vertex(object):
    """
    Represents graph's vertex
    """
    def __init__(self, id, graph=None):
        self.id = id
        self.graph = graph
        self.edges = {}

    def __str__(self):
        return "<Vertex(id='%s')>" % self.id

    def connect_to(self, vertex, weight=None):
        if self.is_connected_to(vertex):
            raise ValueError("%s is already connected to %s" % (self, vertex))
        self.edges[vertex.id] = DirectedEdge(
            src_id=self.id,
            dst_id=vertex.id,
            weight=weight
        )

    def disconnect_from(self, vertex):
        if not self.is_connected_to(vertex):
            raise ValueError("%s is not connected to %s" % (self, vertex))
        del self.edges[vertex.id]

    def is_connected_to(self, vertex):
        return vertex.id in self.edges

    def neighbors(self):
        return (self.graph.vertices[vid] for vid in self.edges)


class EdgeBase(object):
    """
    Serves as a base for edges classes to inherit from
    """
    def __init__(self, src_id, dst_id, weight=None):
        if src_id == dst_id:
            raise ValueError("srd_id and dst_id must differ")
        self.src_id = src_id
        self.dst_id = dst_id
        self.weight = weight

    def __str__(self):
        return "<%s(from='%s', to='%s', weight=%s)>" % (
            self.__class__.__name__,
            self.src_id,
            self.dst_id,
            self.weight
        )


class Edge(EdgeBase):
    """
    Represents graph's bidirectional edge
    """
    def __init__(self, *args, **kwargs):
        super(Edge, self).__init__(*args, **kwargs)
        self.directed = False


class DirectedEdge(EdgeBase):
    """
    Represents graph's directed edge
    """
    def __init__(self, *args, **kwargs):
        super(DirectedEdge, self).__init__(*args, **kwargs)
        self.directed = True
