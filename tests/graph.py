from proboscis import test
from hamcrest import assert_that, is_, equal_to, has_length, raises, calling
from src.graph import Graph, Vertex, Edge


@test(groups=["graph"], depends_on_groups=["graph-edge", "graph-vertex"])
class GraphTest(object):
    """
    Tests Graph data structure and its algorithms
    """
    @test
    def graph_creation_sanity(self):
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
    def graph_connections_sanity(self):
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

    @test(groups=["dfs"])
    def dfs_in_empty_graph(self):
        """
        Graph:
            *empty*
        """
        graph = Graph()
        va, vb = Vertex("A"), Vertex("B")
        assert_that(graph.depth_first_search(va, vb), is_(False))
        assert_that(graph.depth_first_search(vb, va), is_(False))

    @test(groups=["dfs"])
    def dfs_for_absent_node(self):
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
        vx = Vertex("X")
        assert_that(graph.depth_first_search(va, vx), is_(False))
        assert_that(graph.depth_first_search(vx, va), is_(False))

    @test(groups=["dfs"])
    def dfs_with_no_cycles(self):
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
        assert_that(graph.depth_first_search(va, va), is_(True))
        assert_that(graph.depth_first_search(va, vb), is_(True))
        assert_that(graph.depth_first_search(va, vc), is_(True))
        assert_that(graph.depth_first_search(vb, va), is_(True))
        assert_that(graph.depth_first_search(vb, vb), is_(True))
        assert_that(graph.depth_first_search(vb, vc), is_(True))
        assert_that(graph.depth_first_search(vc, va), is_(False))
        assert_that(graph.depth_first_search(vc, vb), is_(False))
        assert_that(graph.depth_first_search(vc, vc), is_(True))

    @test(groups=["dfs"])
    def dfs_with_bidirectional_cycle(self):
        """
        Graph:
                         .---(D)---.
                         |         |
            (A)---(B)---(C)       (F)---(G)
                         |         |
                         '---(E)---'
        """
        vids = ["A", "B", "C", "D", "E", "F", "G"]
        graph = Graph(vids=vids, edges={
            Edge("B", "A"),
            Edge("B", "C"),
            Edge("C", "D"),
            Edge("C", "E"),
            Edge("D", "F"),
            Edge("E", "F"),
            Edge("F", "G"),
        })
        vb, vd, ve, vg = graph.get_multiple_vertices(["B", "D", "E", "G"])
        assert_that(graph.depth_first_search(vb, vg), is_(True))
        assert_that(graph.depth_first_search(vg, vb), is_(True))
        assert_that(graph.depth_first_search(vd, ve), is_(True))
        assert_that(graph.depth_first_search(ve, vd), is_(True))
        assert_that(graph.depth_first_search(ve, vb), is_(True))
        assert_that(graph.depth_first_search(ve, vg), is_(True))

    @test(groups=["dfs"])
    def dfs_with_directed_cycle(self):
        """
        Graph:
                         .---(D)<--.
                         V         |
            (A)<--(B)-->(C)       (F)-->(G)
                         |         ^
                         '-->(E)---'
        """
        vids = ["A", "B", "C", "D", "E", "F", "G"]
        graph = Graph(vids=vids, edges={
            Edge("B", "A", directed=True),
            Edge("B", "C", directed=True),
            Edge("C", "E", directed=True),
            Edge("E", "F", directed=True),
            Edge("F", "D", directed=True),
            Edge("D", "C", directed=True),
            Edge("F", "G", directed=True),
        })
        vb, vg = graph.get_multiple_vertices(["B", "G"])
        assert_that(graph.depth_first_search(vb, vg), is_(True))
        assert_that(graph.depth_first_search(vg, vb), is_(False))

    @test(groups=["bfs"])
    def bfs_in_empty_graph(self):
        """
        Graph:
            *empty*
        """
        graph = Graph()
        va, vb = Vertex("A"), Vertex("B")
        assert_that(graph.breadth_first_search(va, vb), is_(False))
        assert_that(graph.breadth_first_search(vb, va), is_(False))

    @test(groups=["bfs"])
    def bfs_for_absent_node(self):
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
        vx = Vertex("X")
        assert_that(graph.breadth_first_search(va, vx), is_(False))
        assert_that(graph.breadth_first_search(vx, va), is_(False))

    @test(groups=["bfs"])
    def bfs_with_no_cycles(self):
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
        assert_that(graph.breadth_first_search(va, va), is_(True))
        assert_that(graph.breadth_first_search(va, vb), is_(True))
        assert_that(graph.breadth_first_search(va, vc), is_(True))
        assert_that(graph.breadth_first_search(vb, va), is_(True))
        assert_that(graph.breadth_first_search(vb, vb), is_(True))
        assert_that(graph.breadth_first_search(vb, vc), is_(True))
        assert_that(graph.breadth_first_search(vc, va), is_(False))
        assert_that(graph.breadth_first_search(vc, vb), is_(False))
        assert_that(graph.breadth_first_search(vc, vc), is_(True))

    @test(groups=["bfs"])
    def bfs_with_bidirectional_cycle(self):
        """
        Graph:
                         .---(D)---.
                         |         |
            (A)---(B)---(C)       (F)---(G)
                         |         |
                         '---(E)---'
        """
        vids = ["A", "B", "C", "D", "E", "F", "G"]
        graph = Graph(vids=vids, edges={
            Edge("B", "A"),
            Edge("B", "C"),
            Edge("C", "D"),
            Edge("C", "E"),
            Edge("D", "F"),
            Edge("E", "F"),
            Edge("F", "G"),
        })
        vb, vd, ve, vg = graph.get_multiple_vertices(["B", "D", "E", "G"])
        assert_that(graph.breadth_first_search(vb, vg), is_(True))
        assert_that(graph.breadth_first_search(vg, vb), is_(True))
        assert_that(graph.breadth_first_search(vd, ve), is_(True))
        assert_that(graph.breadth_first_search(ve, vd), is_(True))
        assert_that(graph.breadth_first_search(ve, vb), is_(True))
        assert_that(graph.breadth_first_search(ve, vg), is_(True))

    @test(groups=["bfs"])
    def bfs_with_directed_cycle(self):
        """
        Graph:
                         .---(D)<--.
                         V         |
            (A)<--(B)-->(C)       (F)-->(G)
                         |         ^
                         '-->(E)---'
        """
        vids = ["A", "B", "C", "D", "E", "F", "G"]
        graph = Graph(vids=vids, edges={
            Edge("B", "A", directed=True),
            Edge("B", "C", directed=True),
            Edge("C", "E", directed=True),
            Edge("E", "F", directed=True),
            Edge("F", "D", directed=True),
            Edge("D", "C", directed=True),
            Edge("F", "G", directed=True),
        })
        vb, vg = graph.get_multiple_vertices(["B", "G"])
        assert_that(graph.breadth_first_search(vb, vg), is_(True))
        assert_that(graph.breadth_first_search(vg, vb), is_(False))


@test(groups=["graph-vertex"], depends_on_groups=["graph-edge"])
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


@test(groups=["graph-edge"])
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
        edge = Edge("A", "B", directed=True, weight=weight)
        assert_that(edge.src_id, is_(equal_to("A")))
        assert_that(edge.dst_id, is_(equal_to("B")))
        assert_that(edge.directed, is_(equal_to(True)))
        assert_that(edge.weight, is_(equal_to(weight)))

    @test
    def same_src_and_dst_ids(self):
        assert_that(calling(Edge).with_args("A", "A"),
                    raises(ValueError))
