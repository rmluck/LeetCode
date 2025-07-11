"""
Problem 113: Path Sum II (https://leetcode.com/problems/path-sum-ii/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS), Backtracking

Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum_ii(root: TreeNode, target_sum: int) -> list[list[int]]:
    # Initialize a list to store all paths that meet the criteria
    all_paths = []

    # Helper function to perform DFS and find all paths
    def dfs(root: TreeNode, path: list[int], remaining_sum: int):
        # Base case: if there is no node, return
        if not root:
            return
        
        # Include the current node in the path
        path.append(root.val)
        remaining_sum -= root.val
        
        # If we reach a leaf node and the current sum equals target_sum, add the path to the result
        if not root.left and not root.right:
            if remaining_sum == 0:
                all_paths.append(list(path))
        
        # Continue the search in left and right subtrees
        dfs(root.left, path, remaining_sum)
        dfs(root.right, path, remaining_sum)
        
        # Backtrack by removing the last node from the path
        path.pop()

    # Start DFS from the root with an initial sum of 0 and an empty path
    dfs(root, [], target_sum)
    return all_paths

# Helper function to create a binary tree from a list
def create_binary_tree_from_list(values: list[int]) -> TreeNode:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        node = queue.pop(0)
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

# Example 1
assert path_sum_ii(create_binary_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == [[5, 4, 11, 7], [5, 8, 4, 5]]

# Example 2
assert path_sum_ii(create_binary_tree_from_list([1, 2, 3]), 5) == []

# Example 3
assert path_sum_ii(create_binary_tree_from_list([]), 0) == []

# Additional Test Cases
assert path_sum_ii(create_binary_tree_from_list([1, 2, 3, 4, 5, None, None]), 6) == [[1, 2, 3]]
assert path_sum_ii(create_binary_tree_from_list([1, 2, 3, None, 4]), 5) == [[1, 2, 4]]
assert path_sum_ii(create_binary_tree_from_list([1, 2, None, 3]), 3) == [[1, 2, 3]]
assert path_sum_ii(create_binary_tree_from_list([1, None, 2, None, 3]), 6) == [[1, 2, 3]]
assert path_sum_ii(create_binary_tree_from_list([1, 2, 3]), 4) == []
assert path_sum_ii(create_binary_tree_from_list([1, 2, 3]), 3) == [[1, 2]]

# Time Complexity: O(n)
# Space Complexity: O(n)
