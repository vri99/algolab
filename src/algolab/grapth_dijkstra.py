import heapq

"""
Dijkstra's search.

Time complexity: O((V + E) log V)
"""
def dijkstra(graph_, start, end):
    heap = []
    # initiate first iteration with start entity
    heapq.heappush(heap, (0, start, None))
    visited = dict()
    parents = dict()

    while heap:
        cost, vertex, parent = heapq.heappop(heap)

        if vertex not in visited:
            # update vertex's cost
            visited[vertex] = cost
            # save vertex's parent to restore the path
            parents[vertex] = parent

            # for each child_node of a vertex
            for child_node, weight in graph_[vertex]:
                if child_node not in visited:
                    # add another element to the priority queue and update it's cost
                    # of parent's node + weight of the current node
                    heapq.heappush(heap, (cost + weight, child_node, vertex))

    #restore the shortest path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()

    return path