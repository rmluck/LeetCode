"""
Problem 61: Rotate List (https://leetcode.com/problems/rotate-list/)
- Difficulty: Medium
- Categories: Linked List
- Technique: Linked List Manipulation

Given the `head` of a linked list, rotate the list to the right by `k` places.

Constraints:
- The number of nodes in the list is in the range `[0, 500]`.
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10^9
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_list(head: ListNode, k: int) -> ListNode:
    # Edge case: if the list is empty or k is 0, no rotation needed
    if not head or k == 0:
        return head

    # First, determine the length of the list and get the tail node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Compute the effective number of rotations needed
    k = k % length
    if k == 0:
        return head

    # Find the new tail: (length - k - 1)th node
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # The new head is the next node after the new tail
    new_head = new_tail.next

    # Break the link to form the new list
    new_tail.next = None
    tail.next = head

    # Return the new head of the rotated list
    return new_head

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
head1 = create_linked_list([1,2,3,4,5])
rotated_head1 = rotate_list(head1, 2)
assert linked_list_to_list(rotated_head1) == [4,5,1,2,3]

# Example 2
head2 = create_linked_list([0,1,2])
rotated_head2 = rotate_list(head2, 4)
assert linked_list_to_list(rotated_head2) == [2,0,1]

# Additional Test Cases
head3 = create_linked_list([])
rotated_head3 = rotate_list(head3, 1)
assert linked_list_to_list(rotated_head3) == []

head4 = create_linked_list([1])
rotated_head4 = rotate_list(head4, 0)
assert linked_list_to_list(rotated_head4) == [1]

head5 = create_linked_list([1])
rotated_head5 = rotate_list(head5, 1)
assert linked_list_to_list(rotated_head5) == [1]

head6 = create_linked_list([1,2])
rotated_head6 = rotate_list(head6, 1)
assert linked_list_to_list(rotated_head6) == [2,1]

head7 = create_linked_list([1,2])
rotated_head7 = rotate_list(head7, 2)
assert linked_list_to_list(rotated_head7) == [1,2]

head8 = create_linked_list([1,2,3])
rotated_head8 = rotate_list(head8, 3)
assert linked_list_to_list(rotated_head8) == [1,2,3]

head9 = create_linked_list([1,2,3,4])
rotated_head9 = rotate_list(head9, 5)
assert linked_list_to_list(rotated_head9) == [4,1,2,3]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.89 MB, less than 57.00% of Python3 online submissions