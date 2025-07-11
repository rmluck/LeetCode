"""
Problem 112: Path Sum (https://leetcode.com/problems/path-sum/)
- Difficulty: Easy
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS)

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

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

def path_sum(root: TreeNode, target_sum: int) -> bool:
    # Base case: if the tree is empty, return False
    if not root:
        return False
    
    # If we reach a leaf node, check if the current value equals target_sum
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recursively check left and right subtrees with updated target_sum
    target_sum -= root.val
    return path_sum(root.left, target_sum) or path_sum(root.right, target_sum)

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
assert path_sum(create_binary_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True

# Example 2
assert path_sum(create_binary_tree_from_list([1, 2, 3]), 5) == False

# Example 3
assert path_sum(create_binary_tree_from_list([]), 0) == False

# Additional Test Cases
assert path_sum(create_binary_tree_from_list([1, 2, 3, 4, 5, None, None]), 6) == True
assert path_sum(create_binary_tree_from_list([1, 2, 3, None, 4]), 5) == True
assert path_sum(create_binary_tree_from_list([1, 2, None, 3]), 3) == True
assert path_sum(create_binary_tree_from_list([1, None, 2, None, 3]), 6) == True
assert path_sum(create_binary_tree_from_list([1, 2, 3]), 4) == False
assert path_sum(create_binary_tree_from_list([1, 2, 3]), 3) == True

# Time Complexity: O(n)
# Space Complexity: O(h)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.77 MB, less than 91.27% of Python3 online submissions