"""
Problem 33: Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array/)
- Difficulty: Medium
- Categories: Array
- Technique: Binary Search

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0, 1, 2, 4, 5, 6, 7]` might be rotated at pivot index `3` and become `[4, 5, 6, 7, 0, 1, 2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

Constraints:
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`
"""


def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    # Initialize the start and end pointers for binary search
    start, end = 0, len(nums) - 1

    # Perform binary search
    while start <= end:
        # Calculate the middle index
        middle = (start + end) // 2

        # Check if the middle element is the target
        if nums[middle] == target:
            return middle
        
        # Determine which side is sorted
        if nums[start] <= nums[middle]:
            # Check which side the target is on
            if nums[start] <= target < nums[middle]:
                # Target is in the left side
                end = middle - 1
            else:
                # Target is in the right side
                start = middle + 1
        else:
            # Check which side the target is on
            if nums[middle] < target <= nums[end]:
                # Target is in the right side
                start = middle + 1
            else:
                # Target is in the left side
                end = middle - 1

    # If we reach here, the target was not found
    return -1

# Example 1
assert search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4

# Example 2
assert search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1

# Example 3
assert search_in_rotated_sorted_array([1], 0) == -1

# Additional Test Cases
assert search_in_rotated_sorted_array([1, 3], 3) == 1
assert search_in_rotated_sorted_array([5, 1, 3], 5) == 0
assert search_in_rotated_sorted_array([1, 3, 5], 1) == 0
assert search_in_rotated_sorted_array([3, 1], 1) == 1
assert search_in_rotated_sorted_array([2, 3, 4, 5, 6, 7, 0, 1], 6) == 4
assert search_in_rotated_sorted_array([2, 3, 4, 5, 6, 7, 0, 1], 2) == 0
assert search_in_rotated_sorted_array([2, 3, 4, 5, 6, 7, 0, 1], 1) == 7
assert search_in_rotated_sorted_array([2, 3, 4, 5, 6, 7, 0, 1], 8) == -1
assert search_in_rotated_sorted_array([1, 2, 3, 4, 5, 6, 7], 4) == 3

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100% of Python3 online submissions
# Memory Usage: 17.97 MB, less than 91.13% of Python3 online submissions