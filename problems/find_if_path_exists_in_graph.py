"""
Problem 1971: Find if Path Exists in Graph (https://leetcode.com/problems/find-if-path-exists-in-graph/)
- Difficulty: Easy
- Categories: Graph
- Technique: Union Find

There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.

Constraints:
- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.
"""


def find_if_path_exists_in_graph(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Initialize the parent array for Union-Find
    parents = list(range(n))

    # Find the root parent of a vertex
    def find(vertex: int) -> int:
        # If the vertex is its own parent, return it
        if parents[vertex] == vertex:
            return vertex
        # Otherwise, recursively find the root parent and apply path compression
        parents[vertex] = find(parents[vertex])
        # Return the root parent
        return parents[vertex]
    
    # Union two vertices by connecting their root parents
    def union(vertex1: int, vertex2: int) -> None:
        # Find the root parents of both vertices
        vertex1_parent = find(vertex1)
        vertex2_parent = find(vertex2)

        # If they are not already connected, connect them by updating the parent of one root to the other
        if vertex1_parent != vertex2_parent:
            parents[vertex1_parent] = vertex2_parent
    
    # Iterate through each edge and union the vertices
    for u, v in edges:
        union(u, v)
    
    # Check if the source and destination vertices have the same root parent
    return find(source) == find(destination)

# Example 1
assert find_if_path_exists_in_graph(3, [[0, 1], [1, 2]], 0, 2) == True

# Example 2
assert find_if_path_exists_in_graph(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False

# Additional Test Cases
assert find_if_path_exists_in_graph(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4) == True
assert find_if_path_exists_in_graph(4, [[0, 1], [1, 2], [2, 3]], 0, 3) == True
assert find_if_path_exists_in_graph(4, [[0, 1], [1, 2]], 0, 3) == False
assert find_if_path_exists_in_graph(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4) == True
assert find_if_path_exists_in_graph(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1, 4) == True
assert find_if_path_exists_in_graph(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 2, 4) == True

# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Runtime: 228 ms, faster than 97.29% of Python3 online submissions
# Memory: 83.96 MB, less than 93.77% of Python3 online submissions