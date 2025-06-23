"""
Problem 16: 3Sum Closest (https://leetcode.com/problems/3sum-closest/)
- Difficulty: Medium
- Categories: Array, Sorting
- Technique: Two Pointers

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Constraints:
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""


def three_sum_closest(nums: list[int], target: int) -> int:
    # Initialize the closest sum to None, sort the array
    closest = None
    nums.sort()

    # Iterate through the array, using two pointers to find the closest sum
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first number
        left = i + 1
        right = len(nums) - 1

        while left < right:
            # Calculate the sum of the three numbers
            three_sum = nums[i] + nums[left] + nums[right]

            # Update the closest sum if it's closer to the target
            if closest is None or abs(three_sum - target) < abs(closest - target):
                closest = three_sum

            # Move the pointers based on the comparison with the target
            if three_sum < target:
                left += 1
            elif three_sum > target:
                right -= 1
            else:
                return three_sum
    
    # Return the closest sum found
    return closest

# Example 1
assert three_sum_closest([-1, 2, 1, -4], 1) == 2

# Example 2
assert three_sum_closest([0, 0, 0], 1) == 0

# Additional Test Cases
assert three_sum_closest([1, 1, 1, 0], -100) == 2
assert three_sum_closest([1, 2, 5, 10, 11], 12) == 13
assert three_sum_closest([-1, 0, 1, 1, 55], 3) == 2
assert three_sum_closest([0, 2, 1, -3], 1) == 0
assert three_sum_closest([1, 6, 9, 14, 16, 70], 81) == 80
assert three_sum_closest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2) == -2
assert three_sum_closest([0, 1, 2], 3) == 3
assert three_sum_closest([-3, -2, -5, 3, -4], -1) == -2
assert three_sum_closest([1, 1, 1, 1], 0) == 3
assert three_sum_closest([1, 2, 3, 4, 5], 10) == 10
assert three_sum_closest([-1, 0, 1, 2, -1, -4], 0) == 0
assert three_sum_closest([0, 0, 0], 0) == 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Runtime: 387 ms, beats 21.90% of Python3 online submissions
# Memory: 17.71 MB, beats 78.31% of Python3 online submissions