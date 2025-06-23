"""
Problem 3: Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- Difficulty: Medium
- Categories: String
- Technique: Sliding Window

Given a string `s`, find the length of the longest substring without duplicate characters.

Constraints:
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces.
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    # Initialize the left pointer, character index dictionary, and max length counter
    char_index = {}
    left = 0
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the dictionary and its index is within the current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to the right of the last occurrence of the character
            left = char_index[s[right]] + 1

        # Update the character's index in the dictionary
        char_index[s[right]] = right

        # Update the maximum length of the substring found so far
        max_length = max(max_length, right - left + 1)

    # Return the maximum length of the substring without repeating characters
    return max_length

# Example 1
assert longest_substring_without_repeating_characters("abcabcbb") == 3

# Example 2
assert longest_substring_without_repeating_characters("bbbbb") == 1

# Example 3
assert longest_substring_without_repeating_characters("pwwkew") == 3

# Additional Test Cases
assert longest_substring_without_repeating_characters("") == 0
assert longest_substring_without_repeating_characters("a") == 1
assert longest_substring_without_repeating_characters("au") == 2
assert longest_substring_without_repeating_characters("dvdf") == 3
assert longest_substring_without_repeating_characters("anviaj") == 5
assert longest_substring_without_repeating_characters("tmmzuxt") == 5
assert longest_substring_without_repeating_characters("ohvhjdml") == 6
assert longest_substring_without_repeating_characters("abba") == 2
assert longest_substring_without_repeating_characters("abcdeafghij") == 10
assert longest_substring_without_repeating_characters("aab") == 2
assert longest_substring_without_repeating_characters("aabbcc") == 2
assert longest_substring_without_repeating_characters("abcdefg") == 7
assert longest_substring_without_repeating_characters("abcabcbbxyz") == 6
assert longest_substring_without_repeating_characters(" ") == 1
assert longest_substring_without_repeating_characters("  ") == 1
assert longest_substring_without_repeating_characters("a b c") == 5
assert longest_substring_without_repeating_characters("!@#$%^&*()") == 10
assert longest_substring_without_repeating_characters("a!b@c#d$") == 8

# Time Complexity: O(n)
# Space Complexity: O(min(m, n))
# Runtime: 23 ms, beats 32.01% of Python3 online submissions
# Memory: 17.79 MB, less than 81.89% of Python3 online submissions