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
        # self.vertices[vid] = Vertex(id=vid)

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
        self.conns = {}

    def __str__(self):
        return "<Vertex(id='%s')>" % self.id

    def connect_to(self, vertex, weight=None):
        if self.is_connected_to(vertex):
            raise ValueError("%s is already connected to %s" % (self, vertex))
        self.conns[vertex.id] = Connection(src=self, dst=vertex, weight=weight)

    def disconnect_from(self, vertex):
        if not self.is_connected_to(vertex):
            raise ValueError("%s is not connected to %s" % (self, vertex))
        del self.conns[vertex.id]

    def is_connected_to(self, vertex):
        return vertex.id in self.conns


class Edge(object):
    """
    Represents graph's edge
    """
    def __init__(self, src_id, dst_id, directed=False, weight=None):
        if src_id == dst_id:
            raise ValueError("srd_id and dst_id must differ")
        self.src_id = src_id
        self.dst_id = dst_id
        self.directed = directed
        self.weight = weight

    def __str__(self):
        return "<Edge(from='%s', to='%s', directed=%s, weight=%s)>" % (
            self.src_id, self.dst_id, self.directed, self.weight
        )


class Connection(object):
    """
    Represents directed connection between graph's vertices
    """
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return "<Connection(src=%s, dst=%s, weight=%s)>" % (
            self.src, self.dst, self.weight
        )
