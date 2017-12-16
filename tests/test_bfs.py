from hamcrest import assert_that, is_
from src.graph import Graph, Vertex, Edge
from src.bfs import breadth_first_search


class TestBFS(object):
    """
    Tests for breadth first search algorithm
    """
    def test_bfs_in_empty_graph(self):
        """
        Graph:
            *empty*
        """
        graph = Graph()
        va, vb = Vertex("A"), Vertex("B")
        assert_that(breadth_first_search(graph, va, vb), is_(False))
        assert_that(breadth_first_search(graph, vb, va), is_(False))

    def test_bfs_for_absent_node(self):
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
        assert_that(breadth_first_search(graph, va, vx), is_(False))
        assert_that(breadth_first_search(graph, vx, va), is_(False))

    def test_bfs_in_acyclic_graph(self):
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
        assert_that(breadth_first_search(graph, va, va), is_(True))
        assert_that(breadth_first_search(graph, va, vb), is_(True))
        assert_that(breadth_first_search(graph, va, vc), is_(True))
        assert_that(breadth_first_search(graph, vb, va), is_(True))
        assert_that(breadth_first_search(graph, vb, vb), is_(True))
        assert_that(breadth_first_search(graph, vb, vc), is_(True))
        assert_that(breadth_first_search(graph, vc, va), is_(False))
        assert_that(breadth_first_search(graph, vc, vb), is_(False))
        assert_that(breadth_first_search(graph, vc, vc), is_(True))

    def test_bfs_in_graph_with_bidirectional_cycle(self):
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
        assert_that(breadth_first_search(graph, vb, vg), is_(True))
        assert_that(breadth_first_search(graph, vg, vb), is_(True))
        assert_that(breadth_first_search(graph, vd, ve), is_(True))
        assert_that(breadth_first_search(graph, ve, vd), is_(True))
        assert_that(breadth_first_search(graph, ve, vb), is_(True))
        assert_that(breadth_first_search(graph, ve, vg), is_(True))

    def test_bfs_in_graph_with_directed_cycle(self):
        """
        Graph:
                         .---(D)<--.
                         v         |
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
        assert_that(breadth_first_search(graph, vb, vg), is_(True))
        assert_that(breadth_first_search(graph, vg, vb), is_(False))
