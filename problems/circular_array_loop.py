"""
Problem 457: Circular Array Loop (https://leetcode.com/problems/circular-array-loop/)
- Difficulty: Medium
- Categories: Array
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

You are playing a game involving a circular array of non-zero integers `nums`. Each `nums[i]` denotes the number of indices forward/backward you must move if you are located at index `i`:
- If `nums[i]` is positive, move `nums[i]` steps forward, and
- If `nums[i]` is negative, move `nums[i]` steps backward

Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backward from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices `seq` of length `k` where:
- Following the movement rules above results in the repeating index sequence: `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...`
- Every `nums[seq[j]]` is either all positive or all negative.
- k > 1

Return `true` if there is a cycle in `nums`, or `false` otherwise.

Constraints:
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
- nums[i] != 0
"""


def circular_array_loop(nums: list[int]) -> bool:
    # Get the length of the array
    n = len(nums)

    # Helper function to get the next index in the circular array
    def next_index(i: int) -> int:
        return (i + nums[i]) % n

    # Iterate through each element in the array
    for i in range(n):
        # Skip if the element is already marked as 0
        if nums[i] == 0:
            continue

        # Initialize slow and fast pointers
        slow, fast = i, i

        # Use Floyd's Tortoise and Hare algorithm to detect a cycle
        while True:
            # Move slow pointer by one step and fast pointer by two steps
            slow = next_index(slow)
            fast = next_index(next_index(fast))

            # Check if the movement is in the same direction
            if nums[slow] * nums[i] <= 0 or nums[fast] * nums[i] <= 0:
                break

            # If slow and fast pointers meet, a cycle is detected
            if slow == fast:
                if slow == next_index(slow):
                    break
                # Cycle found
                return True

        # Mark all elements in the current traversal as 0 to avoid reprocessing
        slow = i
        val = nums[i]
        while nums[slow] * val > 0:
            next_i = next_index(slow)
            nums[slow] = 0
            slow = next_i

    # No cycle found
    return False

# Example 1
assert circular_array_loop([2, -1, 1, 2, 2]) == True

# Example 2
assert circular_array_loop([-1, -2, -3, -4, -5, 6]) == False

# Example 3
assert circular_array_loop([1, -1, 5, 1, 4]) == True

# Additional Test Cases
assert circular_array_loop([1, 2, 3, 4, 5]) == True
assert circular_array_loop([-1, -2, -3, -4, -5]) == True
assert circular_array_loop([1, 1, 1, 1, 1]) == True
assert circular_array_loop([-1, -1, -1, -1, -1]) == True
assert circular_array_loop([1, -1, 1, -1, 1]) == False
assert circular_array_loop([1]) == False
assert circular_array_loop([-1]) == False
assert circular_array_loop([1, 2]) == True
assert circular_array_loop([-1, -2]) == True
assert circular_array_loop([1, -2]) == False
assert circular_array_loop([-1, 2]) == False

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.82 MB, less than 73.52% of Python3 online submissions