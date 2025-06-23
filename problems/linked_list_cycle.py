"""
Problem 141: Linked List Cycle (https://leetcode.com/problems/linked-list-cycle/)
- Difficulty: Easy
- Categories: Linked List
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

Constraints:
- The number of the nodes in the list is in the range `[0, 10^4]`.
- -10^5 <= Node.val <= 10^5
- `pos` is `-1` or a valid index in the linked-list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_cycle(head: ListNode) -> bool:
    # Initialize the slow and fast pointers
    slow = head
    fast = head

    # Traverse the linked list with two pointers
    while fast and fast.next:
        # Slow pointer moves one step, fast pointer moves two steps
        slow = slow.next
        fast = fast.next.next

        # If they meet, there is a cycle
        if slow == fast:
            return True
    
    # If we reach the end of the list, there is no cycle
    return False

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
head1 = create_linked_list([3, 2, 0, -4])
head1.next.next.next.next = head1.next  # Create a cycle
assert linked_list_cycle(head1) == True

# Example 2
head2 = create_linked_list([1, 2])
head2.next.next = head2  # Create a cycle
assert linked_list_cycle(head2) == True

# Example 3
head3 = create_linked_list([1])
assert linked_list_cycle(head3) == False

# Additional Test Cases
head4 = create_linked_list([])
assert linked_list_cycle(head4) == False

head5 = create_linked_list([1])
assert linked_list_cycle(head5) == False

head6 = create_linked_list([1])
head6.next = head6
assert linked_list_cycle(head6) == True

head7 = create_linked_list([1, 2])
assert linked_list_cycle(head7) == False

head8 = create_linked_list([1, 2])
head8.next.next = head8
assert linked_list_cycle(head8) == True

head9 = create_linked_list([1, 2, 3, 4, 5])
assert linked_list_cycle(head9) == False

head10 = create_linked_list([1, 2, 3, 4, 5])
head10.next.next.next.next.next = head10.next
assert linked_list_cycle(head10) == True

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 52 ms, beats 32.49% of Python3 online submissions
# Memory: 19.80 MB, beats 56.73% of submissions