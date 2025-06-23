"""
Problem 977: Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/)
- Difficulty: Easy
- Categories: Array, Sorting
- Technique: Two Pointers

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""


def squares_of_a_sorted_array(nums: list[int]) -> list[int]:
    # Square each element in the array
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    
    # Return the sorted array of squares
    return sorted(nums)

# Example 1
assert squares_of_a_sorted_array([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

# Example 2
assert squares_of_a_sorted_array([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

# Additional Test Cases
assert squares_of_a_sorted_array([-5, -3, -2, -1]) == [1, 4, 9, 25]
assert squares_of_a_sorted_array([1, 2, 3, 4]) == [1, 4, 9, 16]
assert squares_of_a_sorted_array([-2, 0, 2]) == [0, 4, 4]
assert squares_of_a_sorted_array([-1]) == [1]
assert squares_of_a_sorted_array([0]) == [0]

# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Runtime: 6 ms, faster than 83.87% of Python3 online submissions
# Memory: 19.45 MB, less than 62.37% of Python3 online submissions