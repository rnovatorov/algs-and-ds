from collections import deque


# TODO: Add Path class to save paths between vertices


def breadth_first_search(graph, src, dst):
    """
    https://en.wikipedia.org/wiki/Breadth-first_search
    """
    queue = deque([src])
    visited = set()

    while queue:
        vertex = queue.popleft()

        if vertex == dst:
            return True

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

        visited.add(vertex)

    return False


def depth_first_search(graph, src, dst, visited=None):
    """
    https://en.wikipedia.org/wiki/Depth-first_search
    """
    if visited is None:
        visited = set()

    if src == dst:
        return True

    if visited == set(graph):
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, dst, visited):
                return True

    return False


def dijkstra(graph, src, dst):
    """
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    raise NotImplementedError

