"""
Problem 744: Find Smallest Letter Greater Than Target (https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
- Difficulty: Easy
- Categories: Array
- Technique: Binary Search

You are given an array of characters `letters` that is sorted in non-decreasing order, and a character `target`. There are at least two different characters in `letters`.

Return the smallest character in `letters` that is lexicographically greater than `target`. If such a character does not exist, return the first character in `letters`.
"""


def next_greatest_letter(letters: list[str], target: str) -> str:
    # Initialize the start and end pointers for binary search
    n = len(letters)
    start, end = 0, n - 1

    # If target is less than first character, return the first character
    if target < letters[start]:
        return letters[start]
    
    # Binary search to find the smallest character greater than target
    while start <= end:
        # Calculate the middle index
        middle = (start + end) // 2
        # Check if the middle character is less than or equal to target
        if target < letters[middle]:
            # If it is, search in the left half
            end = middle - 1
        else:
            # If it is not, search in the right half
            start = middle + 1

    # If we reach here, start is the index of the smallest character greater than target
    return letters[start % n]

# Example 1
assert next_greatest_letter(["c", "f", "j"], "a") == "c"

# Example 2
assert next_greatest_letter(["c", "f", "j"], "c") == "f"

# Example 3
assert next_greatest_letter(["x", "x", "y", "y"], "z") == "x"

# Additional Test Cases
assert next_greatest_letter(["a", "b", "c", "d"], "a") == "b"
assert next_greatest_letter(["a", "b", "c", "d"], "d") == "a"
assert next_greatest_letter(["a", "b", "c", "d"], "c") == "d"
assert next_greatest_letter(["a", "b", "c", "d"], "e") == "a"
assert next_greatest_letter(["a", "b", "c", "d"], "b") == "c"

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 19.02 MB, less than 73.84% of Python3 online submissions