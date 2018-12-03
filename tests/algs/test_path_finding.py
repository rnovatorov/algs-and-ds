import pytest

from src.ds.graph import Graph
from src.algs.path_finding import dijkstra


def empty_graph(algorithm):
    """
    Graph:
        *empty*
    """
    graph = Graph()

    assert algorithm(graph, 'X', 'Y') is None


def src_is_dst(algorithm):
    """
    Graph:
        (A)---(B)
    """
    graph = Graph()
    graph.connect('A', 'B', bidir=True)

    assert list(algorithm(graph, 'A', 'A')) == ['A']


def nonexistent_src(algorithm):
    """
    Graph:
        (A)---(B)
    """
    graph = Graph()
    graph.connect('A', 'B', bidir=True)

    assert algorithm(graph, 'X', 'A') is None


def nonexistent_dst(algorithm):
    """
    Graph:
        (A)---(B)
    """
    graph = Graph()
    graph.connect('A', 'B', bidir=True)

    assert algorithm(graph, 'A', 'X') is None


def undirected_graph(algorithm):
    """
    Graph:
        https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
    """
    graph = Graph()
    edges = [
        ('A', 'B', 7),
        ('A', 'C', 9),
        ('A', 'F', 14),
        ('B', 'C', 10),
        ('B', 'D', 15),
        ('C', 'D', 11),
        ('C', 'F', 2),
        ('D', 'E', 6),
        ('E', 'F', 9),
    ]
    for edge in edges:
        graph.connect(*edge, bidir=True)

    assert list(algorithm(graph, 'A', 'E')) == ['A', 'C', 'F', 'E']


@pytest.mark.parametrize('task', [
    undirected_graph,
    empty_graph,
    src_is_dst,
    nonexistent_src,
    nonexistent_dst,
])
@pytest.mark.parametrize('algorithm', [
    dijkstra,
])
def test_path_finding(task, algorithm):
    task(algorithm)
