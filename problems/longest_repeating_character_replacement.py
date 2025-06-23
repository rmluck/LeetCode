"""
Problem 424: Longest Repeating Character Replacement (https://leetcode.com/problems/longest-repeating-character-replacement/)
- Difficulty: Medium
- Categories: String
- Technique: Sliding Window

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of only uppercase English letters.
- 0 <= k <= s.length
"""


def longest_repeating_character_replacement(s: str, k: int) -> int:
    # Initialize the left pointer, character count dictionary, and max length counter
    char_count = {}
    left = 0
    max_length = 0
    max_count = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # Add the current character to the count dictionary
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # Update the count of the most frequent character in the current window
        max_count = max(max_count, char_count[s[right]])

        # If the number of characters to change exceeds k, shrink the window from the left
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        # Update the maximum length of the substring found so far
        max_length = max(max_length, right - left + 1)

    # Return the maximum length of the substring after replacements
    return max_length

# Example 1
assert longest_repeating_character_replacement("ABAB", 2) == 4

# Example 2
assert longest_repeating_character_replacement("AABABBA", 1) == 4

# Additional Test Cases
assert longest_repeating_character_replacement("AAAA", 2) == 4
assert longest_repeating_character_replacement("ABCDE", 1) == 2
assert longest_repeating_character_replacement("AABBBCC", 2) == 5
assert longest_repeating_character_replacement("A", 0) == 1
assert longest_repeating_character_replacement("A", 1) == 1
assert longest_repeating_character_replacement("AB", 1) == 2
assert longest_repeating_character_replacement("AB", 0) == 1
assert longest_repeating_character_replacement("AAB", 1) == 3

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 129 ms, faster than 50.52% of Python3 online submissions
# Memory: 18.00 MB, less than 86.48% of Python3 online submissions