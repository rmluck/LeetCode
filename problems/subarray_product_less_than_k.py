"""
Problem 713: Subarray Product Less Than K (https://leetcode.com/problems/subarray-product-less-than-k/)
- Difficulty: Medium
- Categories: Array
- Technique: Sliding Window

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6
"""


def subarray_product_less_than_k(nums: list[int], k: int) -> int:
    # Edge case: if k is less than or equal to 1, no products can be less than k
    if k <= 1:
        return 0

    # Initialize the product, count of subarrays, and left pointer
    product = 1
    count = 0
    left = 0

    # Use a sliding window approach to find valid subarrays
    for right in range(len(nums)):
        # Expand the window by including the right element
        product *= nums[right]

        # Shrink the window from the left if the product is not less than k
        while product >= k:
            product //= nums[left]
            left += 1

        # All subarrays ending at 'right' with start index from 'left' to 'right' are valid
        count += right - left + 1

    # Return the total count of valid subarrays
    return count

# Example 1
assert subarray_product_less_than_k([10, 5, 2, 6], 100) == 8

# Example 2
assert subarray_product_less_than_k([1, 2, 3], 0) == 0

# Additional Test Cases
assert subarray_product_less_than_k([1, 1, 1], 2) == 6
assert subarray_product_less_than_k([1, 2, 3], 7) == 5
assert subarray_product_less_than_k([10, 9, 8], 50) == 3
assert subarray_product_less_than_k([1, 2, 3, 4], 10) == 7
assert subarray_product_less_than_k([100, 200, 300], 1000) == 3
assert subarray_product_less_than_k([1, 2, 3, 4, 5], 20) == 10
assert subarray_product_less_than_k([1, 2, 3, 4, 5], 1) == 0
assert subarray_product_less_than_k([1], 1) == 0
assert subarray_product_less_than_k([1], 2) == 1
assert subarray_product_less_than_k([1000], 1001) == 1
assert subarray_product_less_than_k([1000], 1000) == 0

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 55 ms, faster than 62.23% of Python3 online submissions
# Memory: 19.78 MB, less than 48.26% of Python3 online submissions