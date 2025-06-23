"""
Problem 438: Find All Anagrams in a String (https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- Difficulty: Medium
- Categories: String
- Technique: Sliding Window, Hash Table

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.
"""


def find_all_anagrams_in_a_string(s: str, p: str) -> list[int]:
    # Import Counter from collections module
    from collections import Counter

    # Get the lengths of both strings
    len_s = len(s)
    len_p = len(p)

    # If p is longer than s, return an empty list
    if len_p > len_s:
        return []

    # Create frequency counters for p and the first window of s
    count_p = Counter(p)
    count_s = Counter(s[:len_p])

    result = []
    # If the frequency counters are equal, add the starting index to the result
    if count_p == count_s:
        result.append(0)

    # Slide the window over s and update the frequency counter
    for i in range(len_p, len_s):
        count_s[s[i]] += 1
        count_s[s[i - len_p]] -= 1

        # Remove the character count if it drops to zero
        if count_s[s[i - len_p]] == 0:
            del count_s[s[i - len_p]]

        # If the frequency counters are equal, add the starting index to the result
        if count_p == count_s:
            result.append(i - len_p + 1)

    # Return the list of starting indices of anagrams
    return result

# Example 1
assert find_all_anagrams_in_a_string("cbaebabacd", "abc") == [0, 6]

# Example 2
assert find_all_anagrams_in_a_string("abab", "ab") == [0, 1, 2]

# Additional Test Cases
assert find_all_anagrams_in_a_string("afdgzyxksldfm", "xyz") == [4]
assert find_all_anagrams_in_a_string("aa", "bb") == []
assert find_all_anagrams_in_a_string("a", "a") == [0]
assert find_all_anagrams_in_a_string("a", "b") == []
assert find_all_anagrams_in_a_string("abc", "cba") == [0]
assert find_all_anagrams_in_a_string("ababab", "ab") == [0, 1, 2, 3, 4]
assert find_all_anagrams_in_a_string("abcd", "dcba") == [0]
assert find_all_anagrams_in_a_string("abcd", "abce") == []
assert find_all_anagrams_in_a_string("abc", "defghijkl") == []
assert find_all_anagrams_in_a_string("aa", "a") == [0, 1]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 85 ms, beats 46.62% of Python3 online submissions
# Memory: 18.23 MB, less than 79.32% of Python3 online submissions