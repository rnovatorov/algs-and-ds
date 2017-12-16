def depth_first_search(graph, src, dst, visited=None):
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
