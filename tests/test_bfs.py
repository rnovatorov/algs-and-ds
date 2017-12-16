"""
Tests for breadth first search algorithm
"""

from src.graph import Graph, Vertex, Edge
from src.bfs import breadth_first_search


def test_empty_graph():
    """
    Graph:
        *empty*
    """
    graph = Graph()
    va, vb = Vertex("A"), Vertex("B")
    assert breadth_first_search(graph, va, vb) is False
    assert breadth_first_search(graph, vb, va) is False


def test_absent_node():
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
    assert breadth_first_search(graph, va, vx) is False
    assert breadth_first_search(graph, vx, va) is False


def test_acyclic_graph():
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
    assert breadth_first_search(graph, va, va)
    assert breadth_first_search(graph, va, vb)
    assert breadth_first_search(graph, va, vc)
    assert breadth_first_search(graph, vb, va)
    assert breadth_first_search(graph, vb, vb)
    assert breadth_first_search(graph, vb, vc)
    assert breadth_first_search(graph, vc, va) is False
    assert breadth_first_search(graph, vc, vb) is False
    assert breadth_first_search(graph, vc, vc)


def test_cyclic_graph():
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
    assert breadth_first_search(graph, vb, vg)
    assert breadth_first_search(graph, vg, vb) is False


def test_bidirectionally_cyclic_graph():
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
    assert breadth_first_search(graph, vb, vg)
    assert breadth_first_search(graph, vg, vb)
    assert breadth_first_search(graph, vd, ve)
    assert breadth_first_search(graph, ve, vd)
    assert breadth_first_search(graph, ve, vb)
    assert breadth_first_search(graph, ve, vg)
