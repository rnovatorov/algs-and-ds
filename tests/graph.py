from proboscis import test
from hamcrest import assert_that, is_, is_not, equal_to, has_length, same_instance, raises, calling
from src.graph import Graph, Vertex, Edge


@test(groups=["graph"],
      depends_on_groups=["graph-edge", "graph-vertex"])
class GraphTest(object):
    """
    Tests that Graph data structure functions properly
    """
    @test
    def sanity(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, directed=True)}
        graph = Graph(vids, edges)

        assert_that(graph.vertices, has_length(len(vids)))

        assert_that(graph.vertices[va_id].id, is_(equal_to(va_id)))
        assert_that(graph.vertices[vb_id].id, is_(equal_to(vb_id)))

        assert_that(graph.vertices[va_id].graph, is_(same_instance(graph)))
        assert_that(graph.vertices[vb_id].graph, is_(same_instance(graph)))

    @test
    def adjacency(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, bidir=False)}
        graph = Graph(vids, edges)

        va, vb = graph.vertices[va_id], graph.vertices[vb_id]

        assert_that(va.is_adjacent_to(vb), is_(True))
        assert_that(vb.is_adjacent_to(va), is_(False))

    @test
    def adjacency_bidirectional(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, bidir=True)}
        graph = Graph(vids, edges)

        va, vb = graph.vertices[va_id], graph.vertices[vb_id]

        assert_that(va.is_adjacent_to(vb), is_(True))
        assert_that(vb.is_adjacent_to(va), is_(True))

    @test
    def depth_first_search(self):
        vids = ["Z", "A", "S", "X", "D", "C", "F", "V"]
        edges = {
            Edge("Z", "A", directed=True),
            Edge("A", "S"),
            Edge("S", "X"),
            Edge("X", "D"),
            Edge("X", "C"),
            Edge("D", "C"),
            Edge("C", "F"),
            Edge("C", "V"),
            Edge("F", "V")
        }
        graph = Graph(vids, edges)

        # src = graph.vertices["S"]
        # not_s_vids = [vid for vid in vids if vid != "S"]
        # dsts = [graph.vertices[vid] for vid in not_s_vids]

        src = graph.vertices["S"]
        dst = graph.vertices["Z"]

        assert_that(src.has_path_to(dst, algorithm="dfs"), is_(True))

        # for dst in dsts:
        #     assert_that(src.has_path_to(dst, algorithm="dfs"), is_(True))

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
    def valid_edge(self):
        src_id, dst_id = "A", "B"
        directed = True
        weight = 42
        edge = Edge(src_id, dst_id, directed=directed, weight=weight)

        assert_that(edge.src_id, is_(equal_to(src_id)))
        assert_that(edge.dst_id, is_(equal_to(dst_id)))
        assert_that(edge.directed, is_(equal_to(directed)))
        assert_that(edge.weight, is_(equal_to(weight)))

    @test
    def same_src_and_dst_ids(self):
        src_id = "A"
        assert_that(calling(Edge).with_args(src_id, src_id),
                    raises(ValueError))
