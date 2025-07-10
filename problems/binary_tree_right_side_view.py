"""
Problem 199: Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Breadth-First Search (BFS)

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: TreeNode) -> list[int]:
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Initialize the right side view list and a queue for BFS
    right_side_view = []
    queue = [root]

    # Perform BFS to traverse the tree level by level
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        # Iterate through all nodes at the current level
        for i in range(level_size):
            # Pop the first node from the queue
            node = queue.pop(0)
            # If this is the last node of the current level, add it to the right side view
            if i == level_size - 1:
                right_side_view.append(node.val)
            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Return the right side view of the binary tree
    return right_side_view

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
assert binary_tree_right_side_view(create_binary_tree_from_list([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]

# Example 2
assert binary_tree_right_side_view(create_binary_tree_from_list([1, 2, 3, 4, None, None, None, 5])) == [1, 3, 4, 5]

# Example 3
assert binary_tree_right_side_view (create_binary_tree_from_list([1, None, 3])) == [1, 3]

# Example 4
assert binary_tree_right_side_view(create_binary_tree_from_list([])) == []

# Additional Test Cases
assert binary_tree_right_side_view(create_binary_tree_from_list([1, 2, None, 3, None, None, 4])) == [1, 2, 3, 4]
assert binary_tree_right_side_view(create_binary_tree_from_list([1, None, 2, None, 3, None, 4])) == [1, 2, 3, 4]
assert binary_tree_right_side_view(create_binary_tree_from_list([1, 2, 3, None, None, 4, 5])) == [1, 3, 5]
assert binary_tree_right_side_view(create_binary_tree_from_list([1, 2, 3, 4, None, None, 5])) == [1, 2, 3, 5]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.74 MB, less than 60.28% of Python3 online submissions