"""
Problem 383: Ransom Note (https://leetcode.com/problems/ransom-note/)
- Difficulty: Easy
- Categories: String
- Technique: Hash Table

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed from the letters in `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.
"""


def ransom_note(note: str, magazine: str) -> bool:
    # Count occurrences of each character in magazine
    char_count = {}

    # Iterate through each character in magazine
    for char in magazine:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check if each character in note can be formed from magazine
    for char in note:
        # If the character is not in magazine or its count is zero, return False
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    # If all characters in note can be formed, return True
    return True

# Example 1
assert ransom_note("a", "b") == False

# Example 2
assert ransom_note("aa", "ab") == False

# Example 3
assert ransom_note("aa", "aab") == True

# Additional Test Cases
assert ransom_note("hello", "oellh") == True
assert ransom_note("abc", "def") == False
assert ransom_note("xyz", "zyxwvu") == True
assert ransom_note("aabbcc", "abcabc") == True
assert ransom_note("a", "a") == True
assert ransom_note("abc", "cba") == True

# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Runtime: 19 ms, faster than 58.36% of Python3 online submissions
# Memory: 17.80 MB, less than 96.49% of Python3 online submissions