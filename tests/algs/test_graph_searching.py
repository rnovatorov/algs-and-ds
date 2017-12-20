"""
Tests for graph searching algorithms
"""

from src.ds.graph import Graph, Vertex, Edge
from src.algs.graph_searching import breadth_first_search, depth_first_search


def test_breadth_first_search():
    for task in [
        search_in_empty_graph,
        search_for_absent_node,
        search_in_acyclic_graph,
        search_in_cyclic_graph,
        search_in_bidirectionally_cyclic_graph
    ]:
        task(breadth_first_search)


def test_depth_first_search():
    for task in [
        search_in_empty_graph,
        search_for_absent_node,
        search_in_acyclic_graph,
        search_in_cyclic_graph,
        search_in_bidirectionally_cyclic_graph
    ]:
        task(depth_first_search)


def search_in_empty_graph(searching_algorithm):
    """
    Graph:
        *empty*
    """
    graph = Graph()
    va, vb = Vertex("A"), Vertex("B")
    assert searching_algorithm(graph, va, vb) is False
    assert searching_algorithm(graph, vb, va) is False


def search_for_absent_node(searching_algorithm):
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
    assert searching_algorithm(graph, va, vx) is False
    assert searching_algorithm(graph, vx, va) is False


def search_in_acyclic_graph(searching_algorithm):
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
    assert searching_algorithm(graph, va, va)
    assert searching_algorithm(graph, va, vb)
    assert searching_algorithm(graph, va, vc)
    assert searching_algorithm(graph, vb, va)
    assert searching_algorithm(graph, vb, vb)
    assert searching_algorithm(graph, vb, vc)
    assert searching_algorithm(graph, vc, va) is False
    assert searching_algorithm(graph, vc, vb) is False
    assert searching_algorithm(graph, vc, vc)


def search_in_cyclic_graph(searching_algorithm):
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
    assert searching_algorithm(graph, vb, vg)
    assert searching_algorithm(graph, vg, vb) is False


def search_in_bidirectionally_cyclic_graph(searching_algorithm):
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
    assert searching_algorithm(graph, vb, vg)
    assert searching_algorithm(graph, vg, vb)
    assert searching_algorithm(graph, vd, ve)
    assert searching_algorithm(graph, ve, vd)
    assert searching_algorithm(graph, ve, vb)
    assert searching_algorithm(graph, ve, vg)
