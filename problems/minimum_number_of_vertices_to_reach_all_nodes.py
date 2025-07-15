"""
Problem 1557: Minimum Number of Vertices to Reach All Nodes (https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)
- Difficulty: Medium
- Categories: Graph
- Technique: Graph
"""


def minimum_number_of_vertices_to_reach_all_nodes(n: int, edges: list[list[int]]) -> list[int]:
    # Create a set to track all nodes that are reachable from any other node
    reachable = set([j for _, j in edges])

    # The vertices that cannot be reached from any other vertex are those not in the reachable set
    return [i for i in range(n) if i not in reachable]

# Example 1
assert minimum_number_of_vertices_to_reach_all_nodes(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]

# Example 2
assert minimum_number_of_vertices_to_reach_all_nodes(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]

# Additional Test Cases
assert minimum_number_of_vertices_to_reach_all_nodes(3, [[0, 1], [1, 2]]) == [0]
assert minimum_number_of_vertices_to_reach_all_nodes(4, [[1, 0], [2, 1], [3, 2]]) == [3]
assert minimum_number_of_vertices_to_reach_all_nodes(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0]
assert minimum_number_of_vertices_to_reach_all_nodes(1, []) == [0]

# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Runtime: 15 ms, faster than 81.67% of Python3 online submissions
# Memory: 45.18 MB, less than 42.53% of Python3 online submissions