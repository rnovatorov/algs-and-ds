INF = float('inf')


def dijkstra(graph, src, dst):
    """
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    unvisited = set(graph)
    prev = {}

    distances = {vertex: INF for vertex in graph}
    distances[src] = 0

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])

        # If path does not exist.
        if distances[current] == INF:
            return None

        # If path is found.
        if current == dst:
            path = [dst]
            while current != src:
                next = prev[current]
                path.append(next)
                current = next                
            return reversed(path)

        unvisited.remove(current)

        unvisited_neighbors = [
            neighbor
            for neighbor in graph[current]
            if neighbor in unvisited
        ]

        for neighbor in unvisited_neighbors:
            distance = distances[current] + graph[current][neighbor]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current

    # No dst in graph.
    return None
