"""
Problem 567: Permutation in String (https://leetcode.com/problems/permutation-in-string/)
- Difficulty: Medium
- Categories: String
- Technique: Sliding Window, Hash Table
"""


def permutation_in_string(s1: str, s2: str) -> bool:
    # Import Counter from collections module
    from collections import Counter

    # Get the lengths of both strings
    len_s1 = len(s1)
    len_s2 = len(s2)

    # If s1 is longer than s2, return False
    if len_s1 > len_s2:
        return False

    # Create frequency counters for s1 and the first window of s2
    count_s1 = Counter(s1)
    count_s2 = Counter(s2[:len_s1])

    # If the frequency counters are equal, return True
    if count_s1 == count_s2:
        return True

    # Slide the window over s2 and update the frequency counter
    for i in range(len_s1, len_s2):
        count_s2[s2[i]] += 1
        count_s2[s2[i - len_s1]] -= 1

        # Remove the character count if it drops to zero
        if count_s2[s2[i - len_s1]] == 0:
            del count_s2[s2[i - len_s1]]

        # If the frequency counters are equal, return True
        if count_s1 == count_s2:
            return True

    # If no permutation is found, return False
    return False

# Example 1
assert permutation_in_string("ab", "eidbaooo") == True

# Example 2
assert permutation_in_string("ab", "eidboaoo") == False

# Additional Test Cases
assert permutation_in_string("adc", "dcda") == True
assert permutation_in_string("hello", "ooolleoooleh") == False
assert permutation_in_string("a", "a") == True
assert permutation_in_string("a", "b") == False
assert permutation_in_string("abc", "bbbca") == True
assert permutation_in_string("xyz", "afdgzyxksldfm") == True
assert permutation_in_string("abcd", "dcba") == True
assert permutation_in_string("abcd", "abce") == False
assert permutation_in_string("abc", "defghijkl") == False
assert permutation_in_string("aa", "a") == False
assert permutation_in_string("aa", "aaa") == True
assert permutation_in_string("abc", "cbaebabacd") == True
assert permutation_in_string("abcd", "abcde") == True
assert permutation_in_string("abcd", "abcfed") == False

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 27 ms, faster than 47.97% of Python3 online submissions
# Memory: 17.98 MB, less than 38.96% of Python3 online submissions