from collections import deque


# TODO: Add Path class to save paths between vertices


def breadth_first_search(graph, src, dst):
    """
    https://en.wikipedia.org/wiki/Breadth-first_search
    """
    queue = deque([src])
    visited = set()
    while queue:
        cur_vertex = queue.popleft()
        if cur_vertex is dst:
            return True
        for vid in cur_vertex.edges:
            neighbor = graph.vertices[vid]
            if neighbor not in visited:
                queue.append(neighbor)
        visited.add(cur_vertex)
    return False


def depth_first_search(graph, src, dst, visited=None):
    """
    https://en.wikipedia.org/wiki/Depth-first_search
    """
    if src is dst:
        return True
    if visited is None:
        visited = set()
    visited.add(src)
    for vid in src.edges:
        neighbor = graph.vertices[vid]
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, dst, visited=visited):
                return True
    return False


def dijkstra(graph, src, dst):
    """
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    raise NotImplementedError
