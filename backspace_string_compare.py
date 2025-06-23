"""
Problem 844: Backspace String Compare (https://leetcode.com/problems/backspace-string-compare/)
- Difficulty: Easy
- Categories: String
- Technique: Stack, Two Pointers

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `#` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and `#` characters.
"""


def backspace_string_compare(s: str, t: str) -> bool:
    s_stack = []
    t_stack = []

    for char in s:
        if char == '#':
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(char)

    for char in t:
        if char == '#':
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(char)

    return s_stack == t_stack

# Example 1
assert backspace_string_compare("ab#c", "ad#c") == True

# Example 2
assert backspace_string_compare("ab##", "c#d#") == True

# Example 3
assert backspace_string_compare("a#c", "b") == False

# Additional Test Cases
assert backspace_string_compare("a##c", "#a#c") == True
assert backspace_string_compare("a#b#c#", "###") == True
assert backspace_string_compare("a#b#c", "c") == True
assert backspace_string_compare("abc###", "###") == True
assert backspace_string_compare("abc#d", "abzz##d") == True
assert backspace_string_compare("", "") == True
assert backspace_string_compare("a", "a") == True
assert backspace_string_compare("a", "b") == False
assert backspace_string_compare("a#", "") == True

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Runtime: 0 ms, beats 100% of Python3 online submissions
# Memory: 17.73 MB, beats 57.94% of Python3 online submissions