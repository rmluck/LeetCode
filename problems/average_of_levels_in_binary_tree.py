"""
Problem 637: Average of Levels in Binary Tree (https://leetcode.com/problems/average-of-levels-in-binary-tree/)
- Difficulty: Easy
- Categories: Tree, Binary Tree
- Technique: Breadth-First Search (BFS)

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10^-5 of the actual answer will be accepted.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels_in_binary_tree(root: TreeNode) -> list[float]:
    # Initialize the list to hold averages and the queue for BFS
    averages = []
    queue = [root] if root else []

    # Perform BFS to traverse the tree level by level
    while queue:
        # Initialize the sum for the current level and count of nodes at this level
        level_sum = 0
        level_count = len(queue)
        # Iterate through the current level's nodes
        for _ in range(level_count):
            # Pop the first node from the queue and add its value to the level sum
            node = queue.pop(0)
            level_sum += node.val
            # Add the left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate the average for the current level and append it to the averages list
        averages.append(level_sum / level_count)

    # Return the list of averages for each level
    return averages

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
assert average_of_levels_in_binary_tree(create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])) == [3.0, 14.5, 11.0]

# Example 2
assert average_of_levels_in_binary_tree(create_binary_tree_from_list([3, 9, 20, 15, 7, None, None])) == [3.0, 14.5, 11.0]

# Additional Test Cases
assert average_of_levels_in_binary_tree(create_binary_tree_from_list([1])) == [1.0]
assert average_of_levels_in_binary_tree(create_binary_tree_from_list([1, 2, 3, 4, 5, None, None])) == [1.0, 2.5, 4.0]
assert average_of_levels_in_binary_tree(create_binary_tree_from_list([1, 2, None, 3, None, 4, None])) == [1.0, 2.0, 3.0, 4.0]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 19.88 MB, less than 79.85% of Python3 online submissions