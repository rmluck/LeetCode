"""
Problem 15: 3Sum (https://leetcode.com/problems/3sum/)
- Difficulty: Medium
- Categories: Array, Sorting
- Technique: Two Pointers

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- 10^5 <= nums[i] <= 10^5
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    # Initialize the result list and sort the array
    triplets = []
    nums.sort()

    # Iterate through the array, using two pointers to find triplets that sum to zero
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize two pointers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            # Calculate the sum of the three numbers
            three_sum = nums[i] + nums[left] + nums[right]
            
            # Move the pointers based on the comparison with zero
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                # Found a triplet that sums to zero
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values for the second and third numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    # Return the list of triplets
    return triplets

# Example 1
assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

# Example 2
assert three_sum([0, 1, 1]) == []

# Example 3
assert three_sum([0, 0, 0]) == [[0, 0, 0]]

# Additional Test Cases
assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 1, 1], [-2, 0, 2]]
assert three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4]) == [[-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2], [-2, 1, 1]]
assert three_sum([3, 0, -4, -1, -2, 1, 2]) == [[-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([-1, 0, 1, 0]) == [[-1, 0, 1]]
assert three_sum([-1, -1, -1, 2]) == [[-1, -1, 2]]
assert three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
assert three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
assert three_sum([1, 2, -2, -1]) == []
assert three_sum([-2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Runtime: 573 ms, faster than 61.67% of Python3 online submissions
# Memory: 20.48 MB, less than 90.02% of Python3 online submissions