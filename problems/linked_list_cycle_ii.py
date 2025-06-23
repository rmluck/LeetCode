"""
Problem 142: Linked List Cycle II (https://leetcode.com/problems/linked-list-cycle-ii/)
- Difficulty: Medium
- Categories: Linked List
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (0-indexed). Note that `pos` is not passed as a parameter.

Do not modify the linked list.

Constraints:
- The number of the nodes in the list is in the range `[0, 10^4]`.
- -10^5 <= Node.val <= 10^5
- `pos` is `-1` or a valid index in the linked-list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_cycle_ii(head: ListNode) -> ListNode:
    # Initialize the slow and fast pointers
    slow = head
    fast = head

    # First phase: Finding the intersection point in the cycle
    while True:
        # If there is no cycle
        if not fast or not fast.next:
            return None
        
        # To indicate if a cycle is found
        cycle = False
        # Slow pointer moves one step, fast pointer moves two steps
        slow = slow.next
        fast = fast.next.next

        # If they meet, there is a cycle
        if slow == fast:
            cycle = True
            break
    
    # Second phase: Finding the entrance to the cycle
    if cycle:
        # Reinitialize one pointer to the start
        fast = head
        # Move both pointers one step at a time until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # The meeting point is the start of the cycle
        return slow
    
    # If no cycle is found
    return None

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
head1.next.next.next.next = head1.next
assert linked_list_cycle_ii(head1) == head1.next

# Example 2
head2 = create_linked_list([1, 2])
head2.next.next = head2
assert linked_list_cycle_ii(head2) == head2

# Example 3
head3 = create_linked_list([1])
assert linked_list_cycle_ii(head3) == None

# Additional Test Cases
head4 = create_linked_list([])
assert linked_list_cycle_ii(head4) == None

head5 = create_linked_list([1])
assert linked_list_cycle_ii(head5) == None

head6 = create_linked_list([1])
head6.next = head6
assert linked_list_cycle_ii(head6) == head6

head7 = create_linked_list([1, 2, 3, 4, 5])
head7.next.next.next.next.next = head7.next.next
assert linked_list_cycle_ii(head7) == head7.next.next

head8 = create_linked_list([1, 2, 3, 4, 5])
assert linked_list_cycle_ii(head8) == None

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 42 ms, faster than 81.77% of Python3 online submissions
# Memory: 19.49 MB, less than 95.03% of Python3 online submissions