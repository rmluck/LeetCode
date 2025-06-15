"""
Problem 287: Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/)
- Difficulty: Medium
- Categories: Array
- Technique: Floyd's Tortoise and Hare (Cycle Detection)

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and uses only constant extra space.

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""


def find_the_duplicate_number(nums: list[int]) -> int:
    # Initialize the slow and fast pointers
    slow = nums[0]
    fast = nums[0]

    # First phase: Finding the intersection point in the cycle
    while True:
        # Slow pointer moves one step, fast pointer moves two steps
        slow = nums[slow]
        fast = nums[nums[fast]]

        # If they meet, there is a cycle
        if slow == fast:
            break
    
    # Second phase: Finding the entrance to the cycle
    # Reinitialize one pointer to the start
    fast = nums[0]
    # Move both pointers one step at a time until they meet
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    # The meeting point is the duplicate number
    return slow

# Example 1
assert find_the_duplicate_number([1,3,4,2,2]) == 2

# Example 2
assert find_the_duplicate_number([3,1,3,4,2]) == 3

# Example 3
assert find_the_duplicate_number([3, 3, 3, 3, 3]) == 3

# Additional Test Cases
assert find_the_duplicate_number([1, 1]) == 1
assert find_the_duplicate_number([1, 2, 3, 4, 5, 5]) == 5
assert find_the_duplicate_number([2, 2, 2, 2, 2]) == 2
assert find_the_duplicate_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == 10
assert find_the_duplicate_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
assert find_the_duplicate_number([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
assert find_the_duplicate_number([1, 4, 6, 3, 2, 5, 4]) == 4

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 25 ms, faster than 70.43% of Python3 online submissions
# Memory: 29.11 MB, less than 90.52% of Python3 online submissions