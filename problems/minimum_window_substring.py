"""
Problem 76: Minimum Window Substring (https://leetcode.com/problems/minimum-window-substring/)
- Difficulty: Hard
- Categories: String
- Technique: Sliding Window, Hash Table

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The answer is guaranteed to be unique.

Constraints:
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.
"""


def minimum_window_substring(s: str, t: str) -> str:
    # Import Counter from collections module
    from collections import Counter

    # Get the lengths of both strings
    len_s = len(s)
    len_t = len(t)

    # If t is longer than s, return an empty string
    if len_t > len_s:
        return ""

    # Create frequency counters for t and the current window in s
    count_t = Counter(t)
    count_window = Counter()

    # Initialize the two pointers, have and need counters, and the result variables
    have, need = 0, len(count_t)
    left = 0
    min_length = float("inf")
    result = ""

    # Expand the window with the right pointer
    for right in range(len_s):
        char_right = s[right]
        count_window[char_right] += 1

        # If the current character's count matches the required count in t, increment have
        if char_right in count_t and count_window[char_right] == count_t[char_right]:
            have += 1

        # When we have all required characters, try to shrink the window from the left
        while have == need:
            window_length = right - left + 1
            if window_length < min_length:
                min_length = window_length
                result = s[left:right + 1]

            char_left = s[left]
            count_window[char_left] -= 1

            if char_left in count_t and count_window[char_left] < count_t[char_left]:
                have -= 1
            left += 1


    # Return the minimum window substring found
    return result