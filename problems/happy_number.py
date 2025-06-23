"""
Problem 202: Happy Number (https://leetcode.com/problems/happy-number/)
- Difficulty: Easy
- Categories: Math
- Technique: Hash Table

Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

Constraints:
- 1 <= n <= 2^31 - 1
"""


def happy_number(n: int) -> bool:
    # Set to keep track of visited sums to detect cycles
    visited_sums = set()

    # Iterate until we find a happy number or detect a cycle
    while True:
        # Calculate the sum of the squares of the digits
        n = sum(int(digit) ** 2 for digit in str(n))
        # Check if we have reached 1 or detected a cycle
        if n == 1:
            return True
        elif n in visited_sums:
            return False
        else:
            # Add the current sum to the set of visited sums
            visited_sums.add(n)

# Example 1
assert happy_number(19) == True

# Example 2
assert happy_number(2) == False

# Additional Test Cases
assert happy_number(1) == True
assert happy_number(7) == True
assert happy_number(4) == False
assert happy_number(20) == True
assert happy_number(100) == True
assert happy_number(44) == False
assert happy_number(85) == True

# Time Complexity: O(log n)
# Space Complexity: O(log n)
# Runtime: 1 ms, faster than 54.94% of Python3 online submissions
# Memory: 17.64 MB, less than 86.38% of Python3 online submissions