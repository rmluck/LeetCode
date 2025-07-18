"""
Problem 1: Two Sum (https://leetcode.com/problems/two-sum/)
- Difficulty: Easy
- Categories: Array
- Technique: Two Pointers, Hash Table

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such thatt hey add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # Create a hash map to store the numbers and their indices
    hash_map = {}

    # Iterate through the list of numbers
    for i in range(len(nums)):
        # Calculate the remainder needed to reach the target
        remainder = target - nums[i]
        # Check if the remainder is already in the hash map
        if remainder in hash_map:
            # If found, return the indices of the two numbers
            return [i, hash_map[remainder]]
        else:
            # If not found, add the current number and its index to the hash map
            hash_map[nums[i]] = i

# Example 1
assert two_sum([2,7,11,15], 9) == [0, 1] or [1, 0]

# Example 2
assert two_sum([3,2,4], 6) == [1, 2] or [2, 1]

# Example 3
assert two_sum([3,3], 6) == [0, 1] or [1, 0]

# Additional Test Cases
assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4] or [4, 3]
assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4] or [4, 2]
assert two_sum([0, 4, 3, 0], 0) == [0, 3] or [3, 0]
assert two_sum([1, 2], 3) == [0, 1] or [1, 0]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 19.06 MB, less than 24.11% of Python3 online submissions