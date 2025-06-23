"""
Problem 581: Shortest Unsorted Continuous Subarray (https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
- Difficulty: Medium
- Categories: Array, Sorting
- Technique: Two Pointers

Given an integer array `nums`, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
"""


def shortest_unsorted_continuous_subarray(nums: list[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1

    # Find the first element which is out of sorting order from the left
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1

    # If the array is already sorted
    if left == n - 1:
        return 0

    # Find the first element which is out of sorting order from the right
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    # Find the maximum and minimum values in the unsorted subarray
    subarray_max = max(nums[left:right + 1])
    subarray_min = min(nums[left:right + 1])

    # Extend the left boundary to include any numbers greater than subarray_min
    while left > 0 and nums[left - 1] > subarray_min:
        left -= 1

    # Extend the right boundary to include any numbers less than subarray_max
    while right < n - 1 and nums[right + 1] < subarray_max:
        right += 1

    # Return the length of the unsorted subarray
    return right - left + 1

# Example 1
assert shortest_unsorted_continuous_subarray([2, 6, 4, 8, 10, 9, 15]) == 5

# Example 2
assert shortest_unsorted_continuous_subarray([1, 2, 3, 4]) == 0

# Example 3
assert shortest_unsorted_continuous_subarray([1]) == 0

# Additional Test Cases
assert shortest_unsorted_continuous_subarray([1, 3, 2, 4, 5]) == 2
assert shortest_unsorted_continuous_subarray([5, 4, 3, 2, 1]) == 5
assert shortest_unsorted_continuous_subarray([1, 2, 3, 5, 4]) == 2
assert shortest_unsorted_continuous_subarray([1, 2, 3, 3, 3]) == 0
assert shortest_unsorted_continuous_subarray([1, 2, 3, 3, 2]) == 2
assert shortest_unsorted_continuous_subarray([1, 2, 3, 3, 4, 5, 0]) == 7
assert shortest_unsorted_continuous_subarray([1, 2, 3, 4, 5, 0]) == 6
assert shortest_unsorted_continuous_subarray([1, 1, 1, 1]) == 0
assert shortest_unsorted_continuous_subarray([1, 2, 3, 4, 5]) == 0
assert shortest_unsorted_continuous_subarray([2, 1]) == 2
assert shortest_unsorted_continuous_subarray([1, 2]) == 0

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 4 ms, faster than 91.32% of Python3 online submissions
# Memory: 18.59 MB, less than 93.97% of Python3 online submissions