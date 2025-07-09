"""
Problem 111: Minimum Depth of Binary Tree (https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- Difficulty: Easy
- Categories: Tree, Binary Tree
- Technique: Breadth-First Search (BFS)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Constraints:
- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimum_depth_of_binary_tree(root: TreeNode) -> int:
    # If the tree is empty, return 0
    if not root:
        return 0
    
    # Initialize the depth and the queue for BFS
    depth = 1
    queue = [root]

    # Perform BFS to find the minimum depth
    while queue:
        # Iterate through the current level's nodes
        for _ in range(len(queue)):
            # Pop the first node from the queue
            node = queue.pop(0)
            # If the node is a leaf node, return the current depth
            if not node.left and not node.right:
                return depth
            # Add the left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # Increment the depth after processing the current level
        depth += 1

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
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])) == 2

# Example 2
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([2, None, 3, None, 4, None, 5, None, 6])) == 5

# Additional Test Cases
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([1, 2, 3, 4, 5])) == 2
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([1, None, 2, None, 3, None, 4])) == 4
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([1, 2, 3, None, None, 4, 5])) == 2
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([])) == 0
assert minimum_depth_of_binary_tree(create_binary_tree_from_list([1])) == 1

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 50.38 MB, less than 45.90% of Python3 online submissions