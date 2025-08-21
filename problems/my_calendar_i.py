"""
Problem 720: My Calendar I (https://leetcode.com/problems/my-calendar-i/)
- Difficulty: Medium
- Categories: Tree, Binary Tree
- Technique: Depth-First Search (DFS)

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events).

The event can be represented as a pair of integers `start_time` and `end_time` that represents a booking on the half-open interval `[start_time, end_time)`, the range of real numbers `x` such that `start_time <= x < end_time`.

Implement the `MyCalendar` class:
- `MyCalendar()` initializes the calendar object.
- `boolean book(int start_time, int end_time)` returns `true` if the event can be added to the calendar successfully without causing a double booking. Otherwise, return `false` and do not add the event to the calendar.

Constraints:
- `0 <= start_time < end_time <= 10^9`
- At most 1000 calls will be made to `book`.
"""


# Class for binary tree node
class TreeNode:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.left = None
        self.right = None

# Class for calendar management
class MyCalendar:
    def __init__(self):
        # Initialize the root of the binary search tree
        self.root = None

    # Method to book an event in the calendar
    def book(self, start_time: int, end_time: int) -> bool:
        # Attempt to insert the new event into the calendar
        if not self.root:
            # If the tree is empty, create the root node
            self.root = TreeNode(start_time, end_time)
            return True
        # Otherwise, insert the new event into the tree
        return self._insert(self.root, start_time, end_time)

    # Helper method to insert a new event into the binary search tree using DFS
    def _insert(self, node: TreeNode, start_time: int, end_time: int) -> bool:
        # Check if the current node's time range overlaps with the new event
        if node.end_time <= start_time:
            if node.right:
                return self._insert(node.right, start_time, end_time)
            else:
                node.right = TreeNode(start_time, end_time)
                return True
        elif node.start_time >= end_time:
            if node.left:
                return self._insert(node.left, start_time, end_time)
            else:
                node.left = TreeNode(start_time, end_time)
                return True
        else:
            return False
        
# Example 1
calendar1 = MyCalendar()
print(calendar1.book(10, 20))  # Returns True
print(calendar1.book(15, 25))  # Returns False
print(calendar1.book(20, 30))  # Returns True

# Example 2
calendar2 = MyCalendar()
print(calendar2.book(5, 10))   # Returns True
print(calendar2.book(10, 15))  # Returns True
print(calendar2.book(5, 10))   # Returns False
print(calendar2.book(0, 5))    # Returns True
print(calendar2.book(15, 20))  # Returns True

# Example 3
calendar3 = MyCalendar()
print(calendar3.book(1, 10))   # Returns True
print(calendar3.book(2, 3))    # Returns False
print(calendar3.book(4, 5))    # Returns False

# Example 4
calendar4 = MyCalendar()
print(calendar4.book(1, 2))    # Returns True
print(calendar4.book(2, 3))    # Returns True
print(calendar4.book(1, 3))    # Returns False

# Time Complexity: O(log n)
# Space Complexity: O(n)
# Runtime: 15 ms, faster than 99.42% of Python3 online submissions
# Memory: 18.58 MB, less than 93.82% of Python3 online submissions