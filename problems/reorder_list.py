"""
Problem 143: Reorder List (https://leetcode.com/problems/reorder-list/)
- Difficulty: Medium
- Categories: Linked List
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode) -> None:
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list using slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Merge the two halves
    first = head
    second = prev  # This is the head of the reversed second half
    while second.next:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

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
head1 = create_linked_list([1,2,3,4])
reorder_list(head1)
assert linked_list_to_list(head1) == [1,4,2,3]

# Example 2
head2 = create_linked_list([1,2,3,4,5])
reorder_list(head2)
assert linked_list_to_list(head2) == [1,5,2,4,3]

# Additional Test Cases
head3 = create_linked_list([1])
reorder_list(head3)
assert linked_list_to_list(head3) == [1]

head4 = create_linked_list([1, 2])
reorder_list(head4)
assert linked_list_to_list(head4) == [1, 2]

head5 = create_linked_list([1, 2, 3])
reorder_list(head5)
assert linked_list_to_list(head5) == [1, 3, 2]

head6 = create_linked_list([1, 2, 3, 4, 5, 6])
reorder_list(head6)
assert linked_list_to_list(head6) == [1, 6, 2, 5, 3, 4]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 7 ms, faster than 21.82% of Python3 online submissions
# Memory: 23.39 MB, less than 38.13% of Python3 online submissions