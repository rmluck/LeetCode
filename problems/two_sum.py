"""
Problem 1: Two Sum
- Difficulty: Easy
- Categories: Array, Hash Table
- Technique: Two Pointers

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such thatt hey add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

def two_sum(self, nums: list[int], target: int) -> list[int]:
    hash_map = {}

    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in hash_map:
            return [i, hash_map[remainder]]
        else:
            hash_map[nums[i]] = i

# Example 1
assert two_sum(None, [2,7,11,15], 9) == [0, 1] or [1, 0]

# Example 2
assert two_sum(None, [3,2,4], 6) == [1, 2] or [2, 1]

# Example 3
assert two_sum(None, [3,3], 6) == [0, 1] or [1, 0]

# Additional Test Cases
assert two_sum(None, [1, 2, 3, 4, 5], 9) == [3, 4] or [4, 3]
assert two_sum(None, [-1, -2, -3, -4, -5], -8) == [2, 4] or [4, 2]
assert two_sum(None, [0, 4, 3, 0], 0) == [0, 3] or [3, 0]
assert two_sum(None, [1, 2], 3) == [0, 1] or [1, 0]