from proboscis import test
from hamcrest import assert_that, is_, is_not, equal_to, has_length, same_instance, raises, calling
from src.graph import Graph, Vertex, Edge, DirectedEdge


@test(groups=["graph"],
      depends_on_groups=["graph-edge", "graph-vertex"])
class GraphTest(object):
    """
    Tests Graph data structure and its algorithms
    """
    @test
    def graph_creation_sanity(self):
        graph = Graph(["A", "B"], {Edge("A", "B")})
        assert_that(graph.vertices, has_length(2))
        va, vb = graph.vertices["A"], graph.vertices["B"]
        assert_that(va.id, is_(equal_to("A")))
        assert_that(vb.id, is_(equal_to("B")))
        assert_that(va.graph, is_(same_instance(graph)))
        assert_that(vb.graph, is_(same_instance(graph)))

    @test
    def graph_connections_sanity(self):
        graph = Graph(
            vids=["A", "B", "C"],
            edges={
                Edge("A", "B"),
                DirectedEdge("A", "C")
            }
        )
        va, vb, vc = graph.vertices["A"], graph.vertices["B"], graph.vertices["C"]
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
    def depth_first_search(self):
        pass

    @test
    def breadth_first_search(self):
        pass


@test(groups=["graph", "graph-vertex"],
      depends_on_groups=["graph-edge"])
class VertexTest(object):
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
                    raises(ValueError))

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
                    raises(ValueError))


@test(groups=["graph", "graph-edge"])
class EdgeTest(object):
    """
    Tests Graph's component Edge
    """
    @test
    def edge_creation_sanity(self):
        weight = 42
        edge = Edge("A", "B", weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(False)))
        assert_that(edge.weight, is_(equal_to(weight)))

    @test
    def directed_edge_creation_sanity(self):
        weight = 42
        edge = DirectedEdge("A", "B", weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(True)))
        assert_that(edge.weight, is_(equal_to(weight)))

    @test
    def same_src_and_dst_ids(self):
        assert_that(calling(Edge).with_args("A", "A"),
                    raises(ValueError))
