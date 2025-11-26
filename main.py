from collections import deque

def bfs_distances(graph, start):
    # If start not in graph, return empty result
    if start not in graph:
        return {}

    # Distance dictionary
    dist = {start: 0}

    # BFS queue
    queue = deque([start])

    while queue:
        current = queue.popleft()

        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in dist:  # Not visited yet
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    return dist


if __name__ == "__main__":
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
