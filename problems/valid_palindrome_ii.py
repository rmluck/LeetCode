"""
Problem 680: Valid Palindrome II (https://leetcode.com/problems/valid-palindrome-ii/)
- Difficulty: Easy
- Categories: String
- Technique: Two Pointers, Greedy Algorithm

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
"""


def valid_palindrome_ii(s: str) -> bool:
    # Helper function to check if a substring is a palindrome
    def is_palindrome(start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    # Initialize two pointers to check for mismatches
    left, right = 0, len(s) - 1
    # Iterate while the left pointer is less than the right pointer
    while left < right:
        # Check if characters at the pointers match
        if s[left] != s[right]:
            # If they don't match, try skipping either character and check for palindrome
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        # Move the pointers inward
        left += 1
        right -= 1
    # If we reach here, the string is already a palindrome or can be made one by deleting at most one character
    return True

# Example 1
assert valid_palindrome_ii("aba") == True

# Example 2
assert valid_palindrome_ii("abca") == True

# Example 3
assert valid_palindrome_ii("abc") == False

# Additional Test Cases
assert valid_palindrome_ii("a") == True
assert valid_palindrome_ii("aa") == True
assert valid_palindrome_ii("ab") == True
assert valid_palindrome_ii("racecar") == True
assert valid_palindrome_ii("raceecar") == True
assert valid_palindrome_ii("abcdefg") == False
assert valid_palindrome_ii("aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
assert valid_palindrome_ii("a" * 100000) == True
assert valid_palindrome_ii("a" * 99999 + "b") == True

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 56 ms, faster than 74.07% of Python3 online submissions
# Memory: 17.80 MB, less than 91.97% of Python3 online submissions