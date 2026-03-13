graph: dict = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}


def dfs(graph_to_search: dict, current_node: str, visited: set | None = None, order: list[str] | None = None) -> list[str] | None:
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if current_node in visited:
        return None

    visited.add(current_node)
    order.append(current_node)

    edges: list[str] = graph_to_search[current_node]

    for node in edges:
        if node not in visited:
            dfs(graph, node, visited, order)

    return order

if __name__ == "__main__":

    print(dfs(graph, "A"))