"""
Problem 206: Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)
- Difficulty: Easy
- Categories: Linked List
- Technique: In-Place Linked List Manipulation

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

Constraints:
- The number of nodes in the list is the range `[0, 5000]`.
- -5000 <= Node.val <= 5000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    # Initialize pointers
    prev = None
    current = head

    # Traverse the list and reverse the links
    while current:
        next_node = current.next # Store the next node
        current.next = prev # Reverse the link
        prev = current # Move prev to current
        current = next_node # Move to the next node

    # At the end, prev will be the new head of the reversed list
    return prev

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
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [5,4,3,2,1]

# Example 2
head = create_linked_list([1,2])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [2,1]

# Example 3
head = create_linked_list([])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == []

# Additional Test Cases
head = create_linked_list([1])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [1]

head = create_linked_list([1,2,3])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [3,2,1]

head = create_linked_list([1,2,3,4])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [4,3,2,1]

head = create_linked_list([5,4,3,2,1])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [1,2,3,4,5]

head = create_linked_list([0,-1,-2,-3])
reversed_head = reverse_linked_list(head)
assert linked_list_to_list(reversed_head) == [-3,-2,-1,0]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.86 MB, less than 14.66% of Python3 online submissions