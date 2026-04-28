"""
Depth-first search.

Time complexity: O(V + E)
Space complexity: O(V)
"""
def dfs(graph_to_search: dict, current_node: str, visited: set | None = None, order: list[str] | None = None) -> tuple[list[str], set]:
    if visited is None:
        visited = set()
    if order is None:
        order = []

    # Base case for recursion
    if current_node in visited:
        return order, visited

    # On each step add current node as visited
    visited.add(current_node)

    # get node's edges
    edges: list[str] = graph_to_search[current_node]

    for node in edges:
        if node not in visited:
            # go deeply into edges for the current node until it ends
            # then return and go to the other edges of the node
            # else return back until new node with edges exists
            dfs(graph_to_search, node, visited, order)

    # and save the order
    order.append(current_node)

    return order, visited

"""
Topological sort.
Time complexity: O(V + E)
"""
def topological_sort(grap, visited, order):
    for node in grap:
        if node not in visited:
            dfs(grap, node, visited, order)

    order.reverse()

    return order