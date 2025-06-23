"""
Problem 448: Find All Numbers Disappeared in an Array (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
- Difficulty: Easy
- Categories: Array
- Technique: Cyclic Sort

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
"""


def find_all_numbers_disappeared_in_an_array(nums: list[int]) -> list[int]:
    n = len(nums)
    # Place each number in its correct position
    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            # Swap nums[i] with the number at its correct position
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    # Collect all numbers that are not in their correct position
    missing_numbers = []
    for i in range(n):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
    
    # Return missing numbers
    return missing_numbers

# Example 1
assert find_all_numbers_disappeared_in_an_array([4,3,2,7,8,2,3,1]) == [5,6]

# Example 2
assert find_all_numbers_disappeared_in_an_array([1,1]) == [2]

# Additional Test Cases
assert find_all_numbers_disappeared_in_an_array([2,2]) == [1]
assert find_all_numbers_disappeared_in_an_array([1,2,3,4,5]) == []
assert find_all_numbers_disappeared_in_an_array([5,4,3,2,1]) == []
assert find_all_numbers_disappeared_in_an_array([2,3,4,5,6]) == [1]
assert find_all_numbers_disappeared_in_an_array([1,1,1,1,1]) == [2,3,4,5]
assert find_all_numbers_disappeared_in_an_array([3,3,3,3,3]) == [1,2,4,5]
assert find_all_numbers_disappeared_in_an_array([1,2,2,3,3,4,5,5]) == [6,7,8]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 51 ms, faster than 17.92% of Python3 online submissions
# Memory: :30.58 MB, less than 95.99% of Python3 online submissions