"""
Problem 1004: Max Consecutive Ones III (https://leetcode.com/problems/max-consecutive-ones-iii/)
- Difficulty: Medium
- Categories: Array
- Technique: Sliding Window

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1's in the array if you can flip at most `k` 0's.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length
"""


def max_consecutive_ones_iii(nums: list[int], k: int) -> int:
    # Initialize the left pointer, zero count, and max length counter
    left = 0
    zero_count = 0
    max_length = 0

    # Iterate through the nums array with the right pointer
    for right in range(len(nums)):
        # If the current number is 0, increment the zero count
        if nums[right] == 0:
            zero_count += 1

        # If the number of zeros exceeds k, shrink the window from the left
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length of consecutive 1's found so far
        max_length = max(max_length, right - left + 1)

    # Return the maximum length of consecutive 1's after flipping at most k zeros
    return max_length

# Example 1
assert max_consecutive_ones_iii([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6

# Example 2
assert max_consecutive_ones_iii([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10

# Additional Test Cases
assert max_consecutive_ones_iii([1, 1, 1, 1, 1], 0) == 5
assert max_consecutive_ones_iii([0, 0, 0, 0, 0], 5) == 5
assert max_consecutive_ones_iii([0, 0, 0, 0, 0], 0) == 0
assert max_consecutive_ones_iii([1, 0, 1, 0, 1], 1) == 3
assert max_consecutive_ones_iii([1, 0, 1, 0, 1], 2) == 5
assert max_consecutive_ones_iii([1, 0, 1, 0, 1], 0) == 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 66 ms, faster than 58.45% of Python3 online submissions
# Memory: 18.24 MB, less than 80.74% of Python3 online submissions