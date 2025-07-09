"""
Problem 104: Maximum Depth of Binary Tree (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- Difficulty: Easy
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS)

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximum_depth_of_binary_tree(root: TreeNode) -> int:
    # If the tree is empty, return 0
    if not root:
        return 0

    # Recursively calculate the maximum depth of the left and right subtrees and return the maximum of the two subtrees plus one for the current node
    return 1 + max(maximum_depth_of_binary_tree(root.left), maximum_depth_of_binary_tree(root.right))

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
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])) == 3

# Example 2
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([1, None, 2])) == 2

# Additional Test Cases
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([])) == 0
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([1, 2, 3, 4, 5])) == 3
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([1, None, 2, None, 3])) == 3
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([1, 2, None, 3, None, 4])) == 4
assert maximum_depth_of_binary_tree(create_binary_tree_from_list([1, 2, 3, None, None, 4, 5])) == 3

# Time Complexity: O(n)
# Space Complexity: O(h)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 19.11 MB, less than 29.80% of Python3 online submissions