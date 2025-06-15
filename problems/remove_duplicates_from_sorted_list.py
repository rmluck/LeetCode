"""
Problem 83: Remove Duplicates from Sorted List (https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- Difficulty: Easy
- Categories: Linked List
- Technique: Two Pointers

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates_from_sorted_list(head: list[ListNode]) -> list[ListNode]:
    # Edge case: if the list is empty, return None
    current = head

    # Iterate through the list until the end
    while current and current.next:
        # If the current node's value is the same as the next node's value, skip the next node
        if current.val  == current.next.val:
            # Skip the next node by pointing the current node's next to the node after the next
            current.next = current.next.next
        else:
            # Move to the next node if no duplicate was found
            current = current.next
    
    # Return the modified list
    return head

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
head1 = create_linked_list([1, 1, 2])
result1 = remove_duplicates_from_sorted_list(head1)
assert linked_list_to_list(result1) == [1, 2]

# Example 2
head2 = create_linked_list([1, 1, 2, 3, 3])
result2 = remove_duplicates_from_sorted_list(head2)
assert linked_list_to_list(result2) == [1, 2, 3]

# Additional Test Cases
head3 = create_linked_list([1, 1, 1, 1, 1])
result3 = remove_duplicates_from_sorted_list(head3)
assert linked_list_to_list(result3) == [1]

head4 = create_linked_list([1, 2, 3, 4, 5])
result4 = remove_duplicates_from_sorted_list(head4)
assert linked_list_to_list(result4) == [1, 2, 3, 4, 5]

head5 = create_linked_list([])
result5 = remove_duplicates_from_sorted_list(head5)
assert linked_list_to_list(result5) == []

head6 = create_linked_list([1, 2, 2, 3, 4, 4, 5])
result6 = remove_duplicates_from_sorted_list(head6)
assert linked_list_to_list(result6) == [1, 2, 3, 4, 5]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.67 MB, less than 90.68% of Python3 online submissions