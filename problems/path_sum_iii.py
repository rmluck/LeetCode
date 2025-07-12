"""
Problem 437: Path Sum III (https://leetcode.com/problems/path-sum-iii/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS), Prefix Sum

Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum_iii(root: TreeNode, target_sum: int) -> int:
    from collections import defaultdict

    # Base case: if the tree is empty, return 0
    if not root:
        return 0

    # Recursive DFS function to count paths with the given sum
    def dfs(node: TreeNode, current_sum: int) -> int:
        if not node:
            return 0
        
        # Initialize the number of paths found and the current sum
        num_paths = 0
        current_sum += node.val

        # Check if the current sum minus target sum exists in the prefix map
        if current_sum - target_sum in prefix_map:
            # If it exists, add the number of times it has been seen to num_paths
            num_paths += prefix_map[current_sum - target_sum]
        # Update the prefix map with the current sum
        prefix_map[current_sum] += 1

        # Continue the search in left and right subtrees
        num_paths += dfs(node.left, current_sum)
        num_paths += dfs(node.right, current_sum)
        # Backtrack by decrementing the count of the current sum in the prefix map
        prefix_map[current_sum] -= 1

        # Return the total number of paths found
        return num_paths
    
    # Initialize a prefix map to store the count of prefix sums with an initial sum of 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1
    # Start the DFS from the root with an initial sum of 0, return the count of paths
    return dfs(root, 0)

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
assert path_sum_iii(create_binary_tree_from_list([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3

# Example 2
assert path_sum_iii(create_binary_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == 3

# Additional Test Cases
assert path_sum_iii(create_binary_tree_from_list([1, 2, 3]), 3) == 1
assert path_sum_iii(create_binary_tree_from_list([1, -1, 1]), 0) == 1
assert path_sum_iii(create_binary_tree_from_list([1, 2, 3, 4, 5]), 5) == 2
assert path_sum_iii(create_binary_tree_from_list([1, 2, 3, None, 4]), 4) == 1
assert path_sum_iii(create_binary_tree_from_list([1, None, 2, None, 3]), 3) == 1
assert path_sum_iii(create_binary_tree_from_list([1, 2, 3]), 6) == 1
assert path_sum_iii(create_binary_tree_from_list([1, 2, 3]), 7) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)