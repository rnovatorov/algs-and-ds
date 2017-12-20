from pytest import raises
from src.ds.graph import Graph, Vertex, Edge
from src.exceptions import GraphError


class TestGraph(object):
    """
    Tests for Graph data structure
    """
    def test_create(self):
        """
        Graph:
            (A)---(B)
        """
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert len(graph.vertices) == 2
        va, vb = graph.vertices["A"], graph.vertices["B"]
        assert (va.id, vb.id) == ("A", "B")

    def test_connections(self):
        """
        Graph:
            (B)<->(A)-->(C)
        """
        vids = ["A", "B", "C"]
        graph = Graph(vids=vids, edges={
            Edge("A", "B"),
            Edge("A", "C", directed=True)
        })
        va, vb, vc = graph.get_multiple_vertices(vids)
        assert va.is_connected_to(va) is False
        assert va.is_connected_to(vb)
        assert va.is_connected_to(vc)
        assert vb.is_connected_to(va)
        assert vb.is_connected_to(vb) is False
        assert vb.is_connected_to(vc) is False
        assert vc.is_connected_to(va) is False
        assert vc.is_connected_to(vb) is False
        assert vc.is_connected_to(vc) is False

    def test_add_vertex_with_existing_id(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        with raises(GraphError):
            graph.add_vertex(Vertex("A"))

    def test_remove_existing_vertex(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        assert "A" in graph.vertices
        graph.remove_vertex(Vertex("A"))
        assert "A" not in graph.vertices

    def test_remove_existing_edge(self):
        """
        Graph:
            (A)---(B)
        """
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert graph.vertices["A"].is_connected_to(graph.vertices["B"])
        graph.remove_edge(Edge("A", "B"))
        assert graph.vertices["A"].is_connected_to(graph.vertices["B"]) is False


class TestVertex(object):
    """
    Tests Graph's component Vertex
    """
    def test_connect_to_new(self):
        va, vb = Vertex("A"), Vertex("B")
        assert va.is_connected_to(vb) is False
        va.connect_to(vb)
        assert va.is_connected_to(vb)

    def test_connect_to_already_connected(self):
        va, vb = Vertex("A"), Vertex("B")
        assert va.is_connected_to(vb) is False
        va.connect_to(vb)
        assert va.is_connected_to(vb)
        with raises(GraphError):
            va.connect_to(vb)

    def test_disconnect_connected(self):
        va, vb = Vertex("A"), Vertex("B")
        assert va.is_connected_to(vb) is False
        va.connect_to(vb)
        assert va.is_connected_to(vb)
        va.disconnect_from(vb)
        assert va.is_connected_to(vb) is False

    def test_disconnect_absent(self):
        va, vb = Vertex("A"), Vertex("B")
        assert va.is_connected_to(vb) is False
        with raises(GraphError):
            va.disconnect_from(vb)


class TestEdge(object):
    """
    Tests Graph's component Edge
    """
    def test_create(self):
        weight = 42
        edge = Edge("A", "B", weight=weight)
        assert edge.src_id == "A"
        assert edge.dst_id == "B"
        assert edge.directed is False
        assert edge.weight == weight

    def test_create_directed(self):
        weight = 42
        edge = Edge("A", "B", directed=True, weight=weight)
        assert edge.src_id == "A"
        assert edge.dst_id == "B"
        assert edge.directed is True
        assert edge.weight == weight
