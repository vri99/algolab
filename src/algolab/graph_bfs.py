from collections import deque

graph: dict = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}



def init_q(graph_to_add: dict, start: str) -> deque:
    q: deque = deque()

    q += graph_to_add[start]

    return q

def bfs(graph_to_search: dict, start: str) -> list[list[str]] | None:
    q: deque = init_q(graph_to_search, start)
    searched: set = {start}
    order: list[str] = [start]

    while q:
        search: str = q.popleft()

        if search not in searched:
            searched.add(search)
            order.append(search)
        else:
            continue

        q += graph_to_search[search]

    print(searched)
    print(order)

    return None

if __name__ == "__main__":
    bfs(graph, "A")