from hamcrest import assert_that, is_, equal_to, has_length, raises, calling
from src.graph import Graph, Vertex, Edge
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
        assert_that(graph.vertices, has_length(2))
        va, vb = graph.vertices["A"], graph.vertices["B"]
        assert_that(va.id, is_(equal_to("A")))
        assert_that(vb.id, is_(equal_to("B")))

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
        assert_that(va.is_connected_to(va), is_(False))
        assert_that(va.is_connected_to(vb), is_(True))
        assert_that(va.is_connected_to(vc), is_(True))
        assert_that(vb.is_connected_to(va), is_(True))
        assert_that(vb.is_connected_to(vb), is_(False))
        assert_that(vb.is_connected_to(vc), is_(False))
        assert_that(vc.is_connected_to(va), is_(False))
        assert_that(vc.is_connected_to(vb), is_(False))
        assert_that(vc.is_connected_to(vc), is_(False))

    def test_add_vertex_with_existing_id(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        assert_that(calling(graph.add_vertex).with_args(Vertex("A")),
                    raises(GraphError))

    def test_remove_existing_vertex(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        assert_that("A" in graph.vertices, is_(True))
        graph.remove_vertex(Vertex("A"))
        assert_that("A" in graph.vertices, is_(False))

    def test_remove_existing_edge(self):
        """
        Graph:
            (A)---(B)
        """
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert_that(graph.vertices["A"].is_connected_to(graph.vertices["B"]), is_(True))
        graph.remove_edge(Edge("A", "B"))
        assert_that(graph.vertices["A"].is_connected_to(graph.vertices["B"]), is_(False))


class TestVertex(object):
    """
    Tests Graph's component Vertex
    """
    def test_connect_to_new(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))

    def test_connect_to_already_connected(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))
        assert_that(calling(va.connect_to).with_args(vb),
                    raises(GraphError))

    def test_disconnect_connected(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))
        va.disconnect_from(vb)
        assert_that(va.is_connected_to(vb), is_(False))

    def test_disconnect_absent(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        assert_that(calling(va.disconnect_from).with_args(vb),
                    raises(GraphError))


class TestEdge(object):
    """
    Tests Graph's component Edge
    """
    def test_create(self):
        weight = 42
        edge = Edge("A", "B", weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(False)))
        assert_that(edge.weight, is_(equal_to(weight)))

    def test_create_directed(self):
        weight = 42
        edge = Edge("A", "B", directed=True, weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(True)))
        assert_that(edge.weight, is_(equal_to(weight)))
