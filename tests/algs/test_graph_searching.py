from src.ds.graph import Graph
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

    assert searching_algorithm(graph, "A", "B") is False


def search_for_absent_node(searching_algorithm):
    """
    Graph:
        (B)<->(A)-->(C)
    """
    graph = Graph()
    graph.connect("B", "A")
    graph.connect("A", "B")
    graph.connect("A", "C")

    for vertex in "A", "B", "C":
        assert searching_algorithm(graph, vertex, "X") is False
        assert searching_algorithm(graph, "X", vertex) is False


def search_in_acyclic_graph(searching_algorithm):
    """
    Graph:
        (B)<->(A)-->(C)
    """
    graph = Graph()
    graph.connect("A", "B", bidir=True)
    graph.connect("A", "C")

    assert searching_algorithm(graph, "A", "A")
    assert searching_algorithm(graph, "A", "B")
    assert searching_algorithm(graph, "A", "C")
    assert searching_algorithm(graph, "B", "A")
    assert searching_algorithm(graph, "B", "B")
    assert searching_algorithm(graph, "B", "C")
    assert searching_algorithm(graph, "C", "A") is False
    assert searching_algorithm(graph, "C", "B") is False
    assert searching_algorithm(graph, "C", "C")


def search_in_cyclic_graph(searching_algorithm):
    """
    Graph:
                     .---(D)<--.
                     v         |
        (A)<--(B)-->(C)       (F)-->(G)
                     |         ^
                     '-->(E)---'
    """
    graph = Graph()
    graph.connect("B", "A")
    graph.connect("B", "C")
    graph.connect("C", "E")
    graph.connect("E", "F")
    graph.connect("F", "D")
    graph.connect("D", "C")
    graph.connect("F", "G")

    assert searching_algorithm(graph, "B", "G")
    assert searching_algorithm(graph, "C", "D")
    assert searching_algorithm(graph, "G", "B") is False


def search_in_bidirectionally_cyclic_graph(searching_algorithm):
    """
    Graph:
                     .---(D)---.
                     |         |
        (A)---(B)---(C)       (F)---(G)
                     |         |
                     '---(E)---'
    """
    graph = Graph()
    graph.connect("A", "B", bidir=True)
    graph.connect("B", "C", bidir=True)
    graph.connect("C", "E", bidir=True)
    graph.connect("E", "F", bidir=True)
    graph.connect("F", "D", bidir=True)
    graph.connect("D", "C", bidir=True)
    graph.connect("F", "G", bidir=True)

    assert searching_algorithm(graph, "B", "G")
    assert searching_algorithm(graph, "G", "B")
    assert searching_algorithm(graph, "D", "E")
    assert searching_algorithm(graph, "E", "D")
    assert searching_algorithm(graph, "E", "B")
    assert searching_algorithm(graph, "E", "G")

