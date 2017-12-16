from proboscis import test
from hamcrest import assert_that, is_, equal_to, has_length, raises, calling
from src.graph import Graph, Vertex, Edge
from src.exceptions import GraphError


@test(groups=["graph"], depends_on_groups=["graph-edge", "graph-vertex"])
class TestGraph(object):
    """
    Tests Graph data structure and its algorithms
    """
    @test
    def create_graph(self):
        """
        Graph:
            (A)---(B)
        """
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert_that(graph.vertices, has_length(2))
        va, vb = graph.vertices["A"], graph.vertices["B"]
        assert_that(va.id, is_(equal_to("A")))
        assert_that(vb.id, is_(equal_to("B")))

    @test
    def check_graph_connections(self):
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

    @test
    def add_vertex_with_existing_id(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        assert_that(calling(graph.add_vertex).with_args(Vertex("A")),
                    raises(GraphError))

    @test
    def remove_existing_vertex(self):
        """
        Graph:
            (A)
        """
        graph = Graph(["A"])
        assert_that("A" in graph.vertices, is_(True))
        graph.remove_vertex(Vertex("A"))
        assert_that("A" in graph.vertices, is_(False))

    @test
    def remove_existing_edge(self):
        """
        Graph:
            (A)---(B)
        """
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert_that(graph.vertices["A"].is_connected_to(graph.vertices["B"]), is_(True))
        graph.remove_edge(Edge("A", "B"))
        assert_that(graph.vertices["A"].is_connected_to(graph.vertices["B"]), is_(False))


@test(groups=["graph-vertex"], depends_on_groups=["graph-edge"])
class TestVertex(object):
    """
    Tests Graph's component Vertex
    """
    @test
    def connect_to_new_vertex(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))

    @test
    def connect_to_already_connected_vertex(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))
        assert_that(calling(va.connect_to).with_args(vb),
                    raises(GraphError))

    @test
    def disconnect_connected_vertex(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        va.connect_to(vb)
        assert_that(va.is_connected_to(vb), is_(True))
        va.disconnect_from(vb)
        assert_that(va.is_connected_to(vb), is_(False))

    @test
    def disconnect_absent_vertex(self):
        va, vb = Vertex("A"), Vertex("B")
        assert_that(va.is_connected_to(vb), is_(False))
        assert_that(calling(va.disconnect_from).with_args(vb),
                    raises(GraphError))


@test(groups=["graph-edge"])
class TestEdge(object):
    """
    Tests Graph's component Edge
    """
    @test
    def create_edge(self):
        weight = 42
        edge = Edge("A", "B", weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(False)))
        assert_that(edge.weight, is_(equal_to(weight)))

    @test
    def create_directed_edge(self):
        weight = 42
        edge = Edge("A", "B", directed=True, weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(True)))
        assert_that(edge.weight, is_(equal_to(weight)))
