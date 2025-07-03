"""
Problem 409: Longest Palindrome (https://leetcode.com/problems/longest-palindrome/)
- Difficulty: Easy
- Categories: String
- Technique: Hash Table

Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.
"""


def longest_palindrome(s: str) -> int:
    # Count occurrences of each character and determine the number of characters with odd counts
    char_count = {}
    odd_count = 0

    # Iterate through each character in the string
    for char in s:
        # Count the occurrences of each character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # Update the odd count based on the current character's count
        if char_count[char] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1

    # If there are odd counts, we can use one odd character in the center of the palindrome
    if odd_count > 1:
        return len(s) - odd_count + 1
    
    # If all characters have even counts, the entire string can be a palindrome
    return len(s)

# Example 1
assert longest_palindrome("abccccd") == 7

# Example 2
assert longest_palindrome("a") == 1

# Additional Test Cases
assert longest_palindrome("aaaa") == 4
assert longest_palindrome("abcde") == 1
assert longest_palindrome("aabbcc") == 6
assert longest_palindrome("aaabbb") == 5
assert longest_palindrome("") == 0
assert longest_palindrome("xyz") == 1

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 1 ms, faster than 57.45% of Pytohn3 online submissions
# Memory: 18.00 MB, less than 27.44% of Python3 online submissions