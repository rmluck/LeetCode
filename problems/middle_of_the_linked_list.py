"""
Problem 876: Middle of the Linked List (https://leetcode.com/problems/middle-of-the-linked-list/)
- Difficulty: Easy
- Categories: Linked List
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:
- The number of nodes in the list is in the range `[1, 100]`.
- 1 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_the_linked_list(head: ListNode) -> ListNode:
    # Initialize the slow and fast pointers
    slow = head
    fast = head

    # Traverse the linked list with two pointers
    while fast and fast.next:
        # Slow pointer moves one step, fast pointer moves two steps
        slow = slow.next
        fast = fast.next.next

    # When the fast pointer reaches the end, the slow pointer is at the middle
    return slow

# Helper function to create a linked list from a list
def create_linked_list(lst: list[int]) -> ListNode:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head: ListNode) -> list[int]:
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Example 1
head = create_linked_list([1,2,3,4,5])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [3,4,5]

# Example 2
head = create_linked_list([1,2,3,4,5,6])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [4,5,6]

# Additional Test Cases
head = create_linked_list([1])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [1]

head = create_linked_list([1,2])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [2]

head = create_linked_list([1,2,3])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [2,3]

head = create_linked_list([1,2,3,4])
middle_node = middle_of_the_linked_list(head)
assert linked_list_to_list(middle_node) == [3,4]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.61 MB, less than 79.32% of Python3 online submissions