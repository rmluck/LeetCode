"""
Problem 129: Sum Root to Leaf Numbers (https://leetcode.com/problems/sum-root-to-leaf-numbers/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS)

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.
- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:
- The number of nodes in the tree is in the range `[1, 1000]`
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_root_to_leaf_numbers(root: TreeNode) -> int:
    # Initialize a list to store all root-to-leaf paths
    paths = []

    # If the root is None, return 0
    if not root:
        return 0
    
    # Helper function to perform DFS and find all root-to-leaf paths
    def dfs(node: TreeNode, current_path: str):
        # If the current node is None, return
        if not node:
            return
        
        # Append the current node's value to the path
        current_path += str(node.val)
        
        # If the current node is a leaf node, add the path to the paths list
        if not node.left and not node.right:
            nonlocal paths
            paths.append(current_path)
        
        # Continue DFS on the left and right children
        dfs(node.left, current_path)
        dfs(node.right, current_path)
    
    # Start DFS from the root node with an empty path
    dfs(root, "")

    # Convert all paths to integers and return their sum
    return sum(int(path) for path in paths)

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
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([1, 2, 3])) == 25

# Example 2
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([4, 9, 0, 5, 1])) == 1026

# Additional Test Cases
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([1, 2, 3, 4, 5])) == 262
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([1, None, 2, None, 3])) == 123
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([0, 1, 2, 3, 4, 5, 6])) == 123456
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([9, 1, 0, 5, 2, None, None, 3])) == 9135
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([1, 2, None, 3, None, 4])) == 1234
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([5, 6, 7, 8, 9, None, None, None, 1])) == 56781
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([3, 1, 4, 1, 5, None, None, 9, 2])) == 3141592
assert sum_root_to_leaf_numbers(create_binary_tree_from_list([2, 3, 4, 5, 6, 7, 8, 9, 0])) == 234567890

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.64 MB, less than 86.76% of Python3 online submissions