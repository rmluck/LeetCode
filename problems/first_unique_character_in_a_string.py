"""
Problem 387: First Unique Character in a String (https://leetcode.com/problems/first-unique-character-in-a-string/)
- Difficulty: Easy
- Categories: String
- Techniques: Hash Table, Queue

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""


def first_unique_character_in_a_string(s: str) -> int:
    char_count = {}
    first_appearances = []

    for i in range(len(s)):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            first_appearances.append((char, i))
    
    for char, index in first_appearances:
        if char_count[char] == 1:
            return index
        
    return -1

# Example 1
assert first_unique_character_in_a_string("leetcode") == 0

# Example 2
assert first_unique_character_in_a_string("loveleetcode") == 2

# Example 3
assert first_unique_character_in_a_string("aabb") == -1

# Additional Test Cases
assert first_unique_character_in_a_string("abcdefg") == 0
assert first_unique_character_in_a_string("aabbcc") == -1
assert first_unique_character_in_a_string("z") == 0
assert first_unique_character_in_a_string("abacabad") == 1

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 73 ms, faster than 31.95% of Python3 online submissions
# Memory: 17.94 MB, less than 82.89% of Python3 online submissions