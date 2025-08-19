"""
Problem 456: 132 Pattern (https://leetcode.com/problems/132-pattern/)
- Difficulty: Medium
- Categories: Array
- Technique: Monotonic Stack

Given an array of `n` integers `nums`, a 132 pattern is a subsequence of three integers `nums[i]`, `nums[j]`, and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` if there is a 132 pattern in `nums`, otherwise, return `false`.

Constraints:
- `n == nums.length`
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`
"""


def find_132_pattern(nums: list[int]) -> bool:
    # Initialize stack to keep track of potential '3' values in the 132 pattern
    stack = []

    # Initialize a variable to keep track of the current minimum value which can be '1' in the 132 pattern
    min_value = nums[0]

    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Maintain the monotonicity of the stack
        while stack and stack[-1][0] <= num:
            stack.pop()
        
        # If the current number is greater than the minimum value and there is a valid '3' in the stack, then a 132 pattern exists
        if stack and stack[-1][1] < num:
            return True
        
        # Push the current number and the current minimum value onto the stack, then update the minimum value
        stack.append((num, min_value))
        min_value = min(min_value, num)

    # If no 132 pattern was found, return False
    return False

# Example 1
assert find_132_pattern([1, 2, 3, 4]) == False

# Example 2
assert find_132_pattern([3, 1, 4, 2]) == True

# Example 3
assert find_132_pattern([-1, 3, 2, 0]) == True

# Additional Test Cases
assert find_132_pattern([1, 0, 1, -4, -3]) == False
assert find_132_pattern([1, 2, 3, 4, 5]) == False
assert find_132_pattern([3, 5, 0, 3, 4]) == True
assert find_132_pattern([5, 4, 3, 2, 1]) == False
assert find_132_pattern([1, 3, 2, 4]) == True
assert find_132_pattern([2, 1, 3, 4]) == True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 103 ms, faster than 38.64% of Python3 online submissions
# Memory Usage: 35.04 MB, less than 86.64% of Python3 online submissions