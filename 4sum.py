"""
Problem 18: 4Sum (https://leetcode.com/problems/4sum/)
- Difficulty: Medium
- Categories: Array, Sorting
- Technique: Two Pointers

Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    quadruplets = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if four_sum < target:
                    left += 1
                elif four_sum > target:
                    right -= 1
                else:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    
    return quadruplets

# Example 1
assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Example 2
assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

# Additional Test Cases
assert four_sum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
assert four_sum([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4]]
assert four_sum([-1, 0, 1, 0, -1, 2], 0) == [[-1, -1, 0, 2], [-1, 0, 0, 1]]
assert four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0) == [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
assert four_sum([1000000000, 1000000000, 1000000000, 1000000000], 4000000000) == [[1000000000, 1000000000, 1000000000, 1000000000]]
assert four_sum([-5, -4, -3, -2, -1], -10) == [[-5, -4, -1, 0], [-5, -3, -2, 0], [-4, -3, -2, -1]]
assert four_sum([1, 1, 1, 1, 1], 4) == [[1, 1, 1, 1]]

# Time Complexity: O(n^3)
# Space Complexity: O(n)
# Runtime: 371 ms, faster than 72.22% of Python3 online submissions
# Memory: 17.84 MB, less than 56.58% of Python3 online submissions