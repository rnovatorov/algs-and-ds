import pytest
from src.ds.graph import Graph
from src.algs.path_finding import dijkstra


def wiki(algorithm):
    graph = Graph()
    edges = [
        ("A", "B", 7),
        ("A", "C", 9),
        ("A", "F", 14),
        ("B", "C", 10),
        ("B", "D", 15),
        ("C", "D", 11),
        ("C", "F", 2),
        ("D", "E", 6),
        ("E", "F", 9),
    ]
    for edge in edges:
        graph.connect(*edge, bidir=True)

    assert algorithm(graph, "A", "E") == ("A", "C", "F", "E")


@pytest.mark.parametrize("task", [
    wiki,
])
@pytest.mark.parametrize("algorithm", [
    dijkstra,
])
def test_path_finding(task, algorithm):
    task(algorithm)

