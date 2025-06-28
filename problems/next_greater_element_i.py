"""
Problem 496: Next Greater Element I (https://leetcode.com/problems/next-greater-element-i/)
- Difficulty: Easy
- Categories: Array
- Technique: Monotonic Stack, Hash Table

The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is -1.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[j] <= 10^4
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.
"""


def next_greater_element_i(nums1: list[int], nums2: list[int]) -> list[int]:
    # Create a dictionary to store the next greater element for each number in nums2 and a monotonic stack
    next_greater_elements = {}
    monotonic_stack = []

    # Iterate through nums2 to fill the next_greater_elements dictionary
    for num in nums2:
        # While the stack is not empty and the current number is greater than the top of the stack
        while monotonic_stack and num > monotonic_stack[-1]:
            # Pop from the stack and set the next greater element for that number
            next_greater_elements[monotonic_stack.pop()] = num
        # Push the current number onto the stack
        monotonic_stack.append(num)

    # For any remaining numbers in the stack, there is no next greater element
    while monotonic_stack:
        next_greater_elements[monotonic_stack.pop()] = -1

    # Return the next greater elements for each number in nums1 using the precomputed dictionary
    return [next_greater_elements[num] for num in nums1]

# Example 1
assert next_greater_element_i([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

# Example 2
assert next_greater_element_i([2, 4], [1, 2, 3, 4]) == [3, -1]

# Additional Test Cases
assert next_greater_element_i([1, 2, 3], [3, 2, 1]) == [-1, -1, -1]
assert next_greater_element_i([10, 20, 30], [30, 20, 10]) == [-1, -1, -1]
assert next_greater_element_i([5, 15, 25], [10, 5, 20, 15, 30, 25]) == [10, 20, 30]

# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.20 MB, less than 20.63% of Python3 online submissions