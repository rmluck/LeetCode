"""
Problem 503: Next Greater Element II (https://leetcode.com/problems/next-greater-element-ii/)
- Difficulty: Medium
- Categories: Array
- Technique: Monotonic Stack

Given a circular array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the next greater number for every element in `nums`.

The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""


def next_greater_element_ii(nums: list[int]) -> list[int]:
    # Initialize the result array with -1 and a monotonic stack
    n = len(nums)
    next_greater_elements = [-1] * n
    monotonic_stack = []

    # Iterate through the array twice to handle the circular nature
    for i in range(2 * n):
        # Calculate the current index in the circular array
        current_index = i % n
        current_value = nums[current_index]

        # While the stack is not empty and the current value is greater than the value at the index on top of the stack
        while monotonic_stack and nums[monotonic_stack[-1]] < current_value:
            # Pop from the stack and set the next greater element for that index
            index = monotonic_stack.pop()
            next_greater_elements[index] = current_value

        # Only push indices from the first pass (0 to n-1)
        if i < n:
            monotonic_stack.append(current_index)

    return next_greater_elements

# Example 1
assert next_greater_element_ii([1, 2, 1]) == [2, -1, 2]

# Example 2
assert next_greater_element_ii([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]

# Additional Test Cases
assert next_greater_element_ii([5, 4, 3, 2, 1]) == [-1, 5, 5, 5, 5]
assert next_greater_element_ii([10, 20, 30, 20, 10]) == [20, 30, -1, 30, 20]
assert next_greater_element_ii([1, 3, 2, 4]) == [3, 4, 4, -1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 25 ms, faster than 54.98% of Python3 online submissions
# Memory: 19.50 MB, less than 60.67% of Python3 online submissions