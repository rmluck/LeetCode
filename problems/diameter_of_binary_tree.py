"""
Problem 543: Diameter of Binary Tree (https://leetcode.com/problems/diameter-of-binary-tree/)
- Difficulty: Easy
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS)

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    # Initialize the diameter to 0
    diameter = 0

    # If the root is None, return the diameter (which is 0)
    if not root:
        return diameter
    
    # Helper function to perform DFS and calculate the diameter
    def dfs(node: TreeNode) -> int:
        # If the left child exists, recursively calculate its depth
        left = dfs(node.left) if node.left else 0
        # If the right child exists, recursively calculate its depth
        right = dfs(node.right) if node.right else 0

        # Update the diameter using the maximum path length found so far
        nonlocal diameter
        diameter = max(diameter, left + right)

        # Return the depth of the current node
        return 1 + max(left, right)
    
    # Start the DFS from the root node
    dfs(root)
    # Return the calculated diameter
    return diameter

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
assert diameter_of_binary_tree(create_binary_tree_from_list([1, 2, 3, 4, 5])) == 3

# Example 2
assert diameter_of_binary_tree(create_binary_tree_from_list([1, 2])) == 1

# Additional Test Cases
assert diameter_of_binary_tree(create_binary_tree_from_list([1, 2, 3, 4, 5, None, None, 6, 7])) == 5
assert diameter_of_binary_tree(create_binary_tree_from_list([1, None, 2, None, 3, None, 4])) == 3
assert diameter_of_binary_tree(create_binary_tree_from_list([1, 2, None, 3, None, 4, None, 5])) == 4
assert diameter_of_binary_tree(create_binary_tree_from_list([1, 2, 3, None, None, 4, 5])) == 3

# Time Complexity: O(n)
# Space Complexity: O(h)
# Runtime: 3 ms, faster than 94.37% of Python3 online submissions
# Memory: 20.67 MB, less than 95.83% of Python3 online submissions