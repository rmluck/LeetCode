"""
Problem 1047: Remove All Adjacent Duplicates In String (https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
- Difficulty: Easy
- Categories: String
- Technique: Stack

You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
"""


def remove_all_adjacent_duplicates_in_string(string: str) -> str:
    stack = []

    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

# Example 1
assert remove_all_adjacent_duplicates_in_string("abbaca") == "ca"

# Example 2
assert remove_all_adjacent_duplicates_in_string("azxxzy") == "ay"

# Additional Test Cases
assert remove_all_adjacent_duplicates_in_string("abcdef") == "abcdef"
assert remove_all_adjacent_duplicates_in_string("aaaaaa") == ""
assert remove_all_adjacent_duplicates_in_string("abababab") == "abababab"
assert remove_all_adjacent_duplicates_in_string("aabbccddeeff") == ""

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 15 ms, faster than 97.76% of Python3 submissions
# Memory: 18.88 MB, less than 20.06% of Python3 submissions