"""
Problem 234: Palindrome Linked List (https://leetcode.com/problems/palindrome-linked-list/)
- Difficulty: Easy
- Categories: Linked List
- Technique: Floyd's Tortoise and Hare (Cycle Detection), Stack

Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

Constraints:
- The number of nodes in the list is in the range `[1, 10^5]`.
- 0 <= Node.val <= 9
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def palindrome_linked_list(head: ListNode) -> bool:
    # Initialize the slow and fast pointers
    slow = head
    fast = head
    stack = []

    # Traverse the linked list with two pointers to find the middle
    while fast and fast.next:
        # Push the value of the slow pointer onto the stack
        stack.append(slow.val)
        # Slow pointer moves one step, fast pointer moves two steps
        slow = slow.next
        fast = fast.next.next

    # If the number of nodes is odd, skip the middle node
    if fast:
        slow = slow.next

    # Compare the second half of the list with the values in the stack
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next

    return True

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
head1 = create_linked_list([1,2,2,1])
assert palindrome_linked_list(head1) == True

# Example 2
head2 = create_linked_list([1,2])
assert palindrome_linked_list(head2) == False

# Additional Test Cases
head3 = create_linked_list([1])
assert palindrome_linked_list(head3) == True

head4 = create_linked_list([1, 2, 3, 2, 1])
assert palindrome_linked_list(head4) == True

head5 = create_linked_list([1, 2, 3, 4, 5])
assert palindrome_linked_list(head5) == False

head6 = create_linked_list([1, 2, 3, 4, 3, 2, 1])
assert palindrome_linked_list(head6) == True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 19 ms, faster than 90.42% of Python3 online submissions
# Memory: 39.36 MB, less than 36.98% of Python3 online submissions