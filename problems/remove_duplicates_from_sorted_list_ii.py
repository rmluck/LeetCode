"""
Problem 82: Remove Duplicates from Sorted List II (https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
- Difficulty: Medium
- Categories: Linked List
- Technique: Two Pointers

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates_from_sorted_list_ii(head: list[ListNode]) -> list[ListNode]:
    # Edge case: if the list is empty or has only one node, return head
    if not head or not head.next:
        return head
    
    # Use a dummy node to handle edge cases where the head needs to be removed
    start = ListNode(0, head)

    # Initialize pointers
    current = head
    prev = start

    # Iterate through the list
    while current:
        # Flag to check if we found any duplicates
        duplicate = False

        # Move current pointer to the end of duplicates
        while current.next and current.val == current.next.val:
            duplicate = True
            current = current.next

        # If duplicates were found, skip all duplicates
        if duplicate:
            prev.next = current.next
        else:
            # No duplicates, move prev pointer
            prev = prev.next
        # Move current pointer
        current = current.next

    # Return the modified list, skipping the dummy node
    return start.next

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
head1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])
result1 = remove_duplicates_from_sorted_list_ii(head1)
assert linked_list_to_list(result1) == [1, 2, 5]

# Example 2
head2 = create_linked_list([1, 1, 1, 2, 3])
result2 = remove_duplicates_from_sorted_list_ii(head2)
assert linked_list_to_list(result2) == [2, 3]

# Additional Test Cases
head3 = create_linked_list([1, 1, 1, 1, 1])
result3 = remove_duplicates_from_sorted_list_ii(head3)
assert linked_list_to_list(result3) == []

head4 = create_linked_list([1, 2, 3, 4, 5])
result4 = remove_duplicates_from_sorted_list_ii(head4)
assert linked_list_to_list(result4) == [1, 2, 3, 4, 5]

head5 = create_linked_list([1, 1, 2, 3, 3, 4, 4, 5, 5])
result5 = remove_duplicates_from_sorted_list_ii(head5)
assert linked_list_to_list(result5) == [2]

head6 = create_linked_list([])
result6 = remove_duplicates_from_sorted_list_ii(head6)
assert linked_list_to_list(result6) == []

head7 = create_linked_list([1, 2, 2, 3, 4, 4, 5])
result7 = remove_duplicates_from_sorted_list_ii(head7)
assert linked_list_to_list(result7) == [1, 3, 5]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.02 MB, less than 24.70% of Python3 online submissions