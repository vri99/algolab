from collections import deque

type node = tuple[str, str | None]

# Create a new queue FIFO data structure
def init_q(start: str) -> deque:
    # put the first element into the queue
    q: deque = deque([start])

    return q

"""
Breadth-first search.

Time complexity: O(V + E)
Space complexity: O(V)
"""
def bfs(graph_to_search: dict, start: str, target: str) -> list[list[str]] | None:
    q: deque = init_q(start)

    searched: set = {start}
    parents: dict = {start: None}
    order: list[str] = []
    path_to_target: list[str] = []

    while q:
        search: str = q.popleft() # get first element (FIFO)
        neighbors: set = graph_to_search[search] # get all neighbors for specific node

        # if target's parent has been found -> build path to the target
        if parents.get(target) is not None:
            path_to_target += target
            key: str | None = parents[target]

            # loop while key is not None (start of the path)
            while key:
                path_to_target.append(key)
                key = parents[key]

            # reverse end:start -> start:end
            path_to_target.reverse()
            # target found -> end the while
            break

        # if neighbors has not been processed:
        # 1. define its parent
        # 2. marked as searched now
        # 3. put it in the queue for further process
        for neighbor in neighbors:
            if neighbor not in searched:
                parents[neighbor] = search
                searched.add(neighbor)
                q.append(neighbor)

        # add node to the process order
        order.append(search)

    print(f'algorithm process order: {" -> ".join(order)}')
    print(f'path to target: {" -> ".join(path_to_target)}')

    return None