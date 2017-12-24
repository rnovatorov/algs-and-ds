class Graph(object):
    """
    Represents graph data structure
    """
    def __init__(self, vids=None, edges=None):
        self.vertices = {}
        if vids is not None:
            for vid in vids:
                self.add_vertex(Vertex(id=vid))
        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def __str__(self):
        return "<Graph(vertices=%s)>" % self.vertices

    def get_multiple_vertices(self, vids):
        return [self.vertices[vid] for vid in vids]

    def add_vertex(self, vertex):
        if vertex.id in self.vertices:
            raise ValueError("%s is already in %s" % (vertex, self))
        self.vertices[vertex.id] = vertex

    def remove_vertex(self, vertex):
        del self.vertices[vertex.id]

    def add_edge(self, edge):
        src, dst = self.get_multiple_vertices(edge.src_dst_pair)
        src.connect_to(dst, weight=edge.weight)
        if not edge.directed:
            dst.connect_to(src, weight=edge.weight)

    def remove_edge(self, edge):
        src, dst = self.get_multiple_vertices(edge.src_dst_pair)
        src.disconnect_from(dst)
        if not edge.directed:
            dst.disconnect_from(src)


class Vertex(object):
    """
    Represents graph's vertex
    """
    def __init__(self, id):
        self.id = id
        self.edges = {}

    def __str__(self):
        return "<Vertex(id='%s')>" % self.id

    def connect_to(self, vertex, weight=None):
        if not self.is_connected_to(vertex):
            self.edges[vertex.id] = weight
        else:
            raise ValueError("%s is already connected to %s" % (self, vertex))

    def disconnect_from(self, vertex):
        if self.is_connected_to(vertex):
            del self.edges[vertex.id]
        else:
            raise ValueError("%s is not connected to %s" % (self, vertex))

    def is_connected_to(self, vertex):
        return vertex.id in self.edges


class Edge(object):
    """
    Represents graph's edge
    """
    def __init__(self, src_id, dst_id, directed=False, weight=None):
        self.src_id = src_id
        self.dst_id = dst_id
        self.directed = directed
        self.weight = weight

    def __str__(self):
        return "<%s(src_id='%s', dst_id='%s', directed=%s, weight=%s)>" % (
            self.__class__.__name__,
            self.src_id,
            self.dst_id,
            self.directed,
            self.weight
        )

    @property
    def src_dst_pair(self):
        return self.src_id, self.dst_id
