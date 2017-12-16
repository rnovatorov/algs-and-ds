from collections import deque


def breadth_first_search(graph, src, dst):
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
