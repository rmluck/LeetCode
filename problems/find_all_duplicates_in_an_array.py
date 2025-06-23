"""
Problem 442: Find All Duplicates in an Array (https://leetcode.com/problems/find-all-duplicates-in-an-array/)
- Difficulty: Medium
- Categories: Array
- Technique: Cyclic Sort

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appear twice.

You must write an algorithm that runs in `O(n)` time and uses only constant extra space, excluding the space needed to store the output.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
"""


def find_all_duplicates_in_an_array(nums: list[int]) -> list[int]:
    # Get the length of the input array and initialize the result list
    n = len(nums)
    duplicates = []

    # Place each number in its correct position
    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            # Swap nums[i] with the number at its correct position
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # Collect all numbers that are in their correct position and appear twice
    for i in range(n):
        if nums[i] != i + 1 and nums[nums[i] - 1] == nums[i]:
            duplicates.append(nums[i])

    # Return the list of duplicates
    return list(set(duplicates))

# Example 1
assert find_all_duplicates_in_an_array([4,3,2,7,8,2,3,1]) == [2,3]

# Example 2
assert find_all_duplicates_in_an_array([1,1,2]) == [1]

# Example 3
assert find_all_duplicates_in_an_array([1]) == []

# Additional Test Cases
assert find_all_duplicates_in_an_array([2,2]) == [2]
assert find_all_duplicates_in_an_array([1,2,3,4,5]) == []
assert find_all_duplicates_in_an_array([5,4,3,2,1]) == []
assert find_all_duplicates_in_an_array([2,3,4,5,6]) == []
assert find_all_duplicates_in_an_array([1,1,1,1,1]) == [1]
assert find_all_duplicates_in_an_array([3,3,3,3,3]) == [3]
assert find_all_duplicates_in_an_array([1,2,2,3,3,4,5,5]) == [2,3,5]
assert find_all_duplicates_in_an_array([1,2,3,4,5,6,7,8,9,10,10]) == [10]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 41 ms, faster than 41.03% of Python3 online submissions
# Memory: 26.84 MB, less than 93.59% of Python3 online submissions