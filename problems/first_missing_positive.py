"""
Problem 41: First Missing Positive (https://leetcode.com/problems/first-missing-positive/)
- Difficulty: Hard
- Categories: Array
- Technique: Cyclic Sort

Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

Constraints:
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
"""


def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    # Place each number in its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    # Find the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positions are correct, return n + 1
    return n + 1

# Example 1
assert first_missing_positive([1,2,0]) == 3

# Example 2
assert first_missing_positive([3,4,-1,1]) == 2

# Example 3
assert first_missing_positive([7,8,9,11,12]) == 1

# Additional Test Cases
assert first_missing_positive([1,1]) == 2
assert first_missing_positive([1,2,3,4,5]) == 6
assert first_missing_positive([-1,-2,-3]) == 1
assert first_missing_positive([2,3,4,5,6]) == 1
assert first_missing_positive([1,1,1,1,1]) == 2
assert first_missing_positive([3,3,3,3,3]) == 1
assert first_missing_positive([1,2,2,3,3,4,5,5]) == 6
assert first_missing_positive([1,2,3,4,5,6,7,8,9,10,11]) == 12
assert first_missing_positive([2,2]) == 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 39 ms, faster than 68.46% of Python3 online submissions
# Memory: 28.94 MB, less than 65.91% of Python3 online submissions