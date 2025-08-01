"""
Problem 107: Binary Tree Level Order Traversal II (https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Breadth-First Search (BFS)

Given the `root` of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_level_order_traversal_ii(root: TreeNode) -> list[list[int]]:
    # Initialize the order list and the queue for BFS
    order = []
    queue = [root] if root else []

    # Perform BFS to traverse the tree level by level
    while queue:
        # Initialize a list to hold the current level's values
        level = []
        # Iterate through the current level's nodes
        for _ in range(len(queue)):
            # Pop the first node from the queue and add its value to the level list
            node = queue.pop(0)
            level.append(node.val)
            # Add the left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # Insert the current level's values at the beginning of the order list
        order.insert(0, level)

    # Return the complete bottom-up level order traversal
    return order

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

# Helper function to convert a binary tree to a list
def binary_tree_to_list(root: TreeNode) -> list[int]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

# Example 1
root1 = create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])
assert binary_tree_level_order_traversal_ii(root1) == [[15, 7], [9, 20], [3]]

# Example 2
root2 = create_binary_tree_from_list([1])
assert binary_tree_level_order_traversal_ii(root2) == [[1]]

# Example 3
root3 = create_binary_tree_from_list([])
assert binary_tree_level_order_traversal_ii(root3) == []

# Additional Test Cases
root4 = create_binary_tree_from_list([1, 2, 3, 4, 5, None, None])
assert binary_tree_level_order_traversal_ii(root4) == [[4, 5], [2, 3], [1]]

root5 = create_binary_tree_from_list([1, None, 2, None, 3])
assert binary_tree_level_order_traversal_ii(root5) == [[3], [2], [1]]

root6 = create_binary_tree_from_list([1, 2, 3, 4, None, None, 5])
assert binary_tree_level_order_traversal_ii(root6) == [[5], [4], [2, 3], [1]]

root7 = create_binary_tree_from_list([1, 2, None, 3, None, 4])
assert binary_tree_level_order_traversal_ii(root7) == [[4], [3], [2], [1]]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.11 MB, less than 38.13% of Python3 online submissions