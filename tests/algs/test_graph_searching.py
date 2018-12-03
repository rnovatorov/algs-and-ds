import pytest

from src.ds.graph import Graph
from src.algs.graph_searching import breadth_first_search, depth_first_search


def search_in_empty_graph(algorithm):
    """
    Graph:
        *empty*
    """
    graph = Graph()

    assert not algorithm(graph, 'A', 'B')


def search_for_absent_node(algorithm):
    """
    Graph:
        (B)<->(A)-->(C)
    """
    graph = Graph()
    graph.connect('B', 'A')
    graph.connect('A', 'B')
    graph.connect('A', 'C')

    for vertex in 'A', 'B', 'C':
        assert not algorithm(graph, vertex, 'X')
        assert not algorithm(graph, 'X', vertex)


def search_in_acyclic_graph(algorithm):
    """
    Graph:
        (B)<->(A)-->(C)
    """
    graph = Graph()
    graph.connect('A', 'B', bidir=True)
    graph.connect('A', 'C')

    assert algorithm(graph, 'A', 'A')
    assert algorithm(graph, 'A', 'B')
    assert algorithm(graph, 'A', 'C')
    assert algorithm(graph, 'B', 'A')
    assert algorithm(graph, 'B', 'B')
    assert algorithm(graph, 'B', 'C')
    assert not algorithm(graph, 'C', 'A')
    assert not algorithm(graph, 'C', 'B')
    assert algorithm(graph, 'C', 'C')


def search_in_cyclic_graph(algorithm):
    """
    Graph:
                     .---(D)<--.
                     v         |
        (A)<--(B)-->(C)       (F)-->(G)
                     |         ^
                     '-->(E)---'
    """
    graph = Graph()
    graph.connect('B', 'A')
    graph.connect('B', 'C')
    graph.connect('C', 'E')
    graph.connect('E', 'F')
    graph.connect('F', 'D')
    graph.connect('D', 'C')
    graph.connect('F', 'G')

    assert algorithm(graph, 'B', 'G')
    assert algorithm(graph, 'C', 'D')
    assert not algorithm(graph, 'G', 'B')


def search_in_bidirectionally_cyclic_graph(algorithm):
    """
    Graph:
                     .---(D)---.
                     |         |
        (A)---(B)---(C)       (F)---(G)
                     |         |
                     '---(E)---'
    """
    graph = Graph()
    graph.connect('A', 'B', bidir=True)
    graph.connect('B', 'C', bidir=True)
    graph.connect('C', 'E', bidir=True)
    graph.connect('E', 'F', bidir=True)
    graph.connect('F', 'D', bidir=True)
    graph.connect('D', 'C', bidir=True)
    graph.connect('F', 'G', bidir=True)

    assert algorithm(graph, 'B', 'G')
    assert algorithm(graph, 'G', 'B')
    assert algorithm(graph, 'D', 'E')
    assert algorithm(graph, 'E', 'D')
    assert algorithm(graph, 'E', 'B')
    assert algorithm(graph, 'E', 'G')


@pytest.mark.parametrize('task', [
    search_in_empty_graph,
    search_for_absent_node,
    search_in_acyclic_graph,
    search_in_cyclic_graph,
    search_in_bidirectionally_cyclic_graph,
])
@pytest.mark.parametrize('algorithm', [
    breadth_first_search,
    depth_first_search,
])
def test_graph_searching(task, algorithm):
    task(algorithm)
