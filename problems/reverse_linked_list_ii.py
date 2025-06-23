"""
Problem 92: Reverse Linked List II (https://leetcode.com/problems/reverse-linked-list-ii/)
- Difficulty: Medium
- Categories: Linked List
- Technique: In-Place Linked List Manipulation

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

Constraints:
- The number of nodes in the list is the range `[1, 500]`.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_ii(head: ListNode, left: int, right: int) -> ListNode:
    # Edge case: if left == right, no need to reverse
    if left == right:
        return head

    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node just before the left position
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing the sublist from left to right
    reverse_start = prev.next
    curr = reverse_start.next

    # Reverse the sublist
    for _ in range(right - left):
        reverse_start.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = reverse_start.next

    # Return the new head of the modified list
    return dummy.next

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
reversed_head = reverse_linked_list_ii(head, 2, 4)
assert linked_list_to_list(reversed_head) == [1,4,3,2,5]

# Example 2
head = create_linked_list([5])
reversed_head = reverse_linked_list_ii(head, 1, 1)
assert linked_list_to_list(reversed_head) == [5]

# Additional Test Cases
head = create_linked_list([1,2,3])
reversed_head = reverse_linked_list_ii(head, 1, 3)
assert linked_list_to_list(reversed_head) == [3,2,1]

head = create_linked_list([1,2,3,4])
reversed_head = reverse_linked_list_ii(head, 1, 2)
assert linked_list_to_list(reversed_head) == [2,1,3,4]

head = create_linked_list([1,2,3,4])
reversed_head = reverse_linked_list_ii(head, 3, 4)
assert linked_list_to_list(reversed_head) == [1,2,4,3]

head = create_linked_list([1,2,3,4,5])
reversed_head = reverse_linked_list_ii(head, 2, 5)
assert linked_list_to_list(reversed_head) == [1,5,4,3,
2]

head = create_linked_list([1,2,3,4,5])
reversed_head = reverse_linked_list_ii(head, 1, 5)
assert linked_list_to_list(reversed_head) == [5,4,3,2,1]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.02 MB, less than 13.52% of Python3 online submissions