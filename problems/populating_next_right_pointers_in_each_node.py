"""
Problem 116: Populating Next Right Pointers in Each Node (https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
- Difficulty: Medium
- Categories: Tree, Binary Tree, Linked List
- Technique: Breadth-First Search (BFS)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def populating_next_right_pointers_in_each_node(root: TreeNode) -> TreeNode:
    # If the tree is empty, return None
    if not root:
        return None
    
    # Initialize the queue for BFS
    queue = [root]
    
    # Perform BFS to populate next right pointers
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        
        # Iterate through the nodes at the current level
        for i in range(level_size):
            # Pop the first node from the queue
            node = queue.pop(0)
            
            # If this is not the last node in the level, set its next pointer
            if i < level_size - 1:
                node.next = queue[0]
            
            # Add the left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return root

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
root = create_binary_tree_from_list([1, 2, 3, 4, 5, None, 7])
assert populating_next_right_pointers_in_each_node(root) == root

# Example 2
root = create_binary_tree_from_list([1, None, 2, None, 3])
assert populating_next_right_pointers_in_each_node(root) == root

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 54 ms, faster than 38.95% of Python3 online submissions
# Memory: 19.29 MB, less than 34.41% of Python3 online submissions