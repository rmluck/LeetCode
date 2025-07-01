"""
Problem 1209: Remove All Adjacent Duplicates In String II (https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)
- Difficulty: Medium
- Categories: String
- Technique: Stack

You are given a string `s` and an integer `k`, a `k` duplicate removal consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k` duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""


def remove_all_adjacent_duplicates_in_string_ii(s: str, k: int) -> str:
    # Initialize a stack to keep track of characters and their counts
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the stack is not empty and the top of the stack is the same as the current character
        if stack and stack[-1][0] == char:
            # Increment the count of the top character in the stack
            stack[-1][1] += 1
            # If the count reaches k, pop the character from the stack
            if stack[-1][1] == k:
                stack.pop()
        else:
            # If the stack is empty or the top character is different, push the current character onto the stack with count 1
            stack.append([char, 1])
    
    # Join the characters in the stack to form the final string
    return ''.join(char * count for char, count in stack)

# Example 1
assert remove_all_adjacent_duplicates_in_string_ii("abcd", 2) == "abcd"

# Example 2
assert remove_all_adjacent_duplicates_in_string_ii("deeedbbcccbdaa", 3) == "aa"

# Example 3
assert remove_all_adjacent_duplicates_in_string_ii("pbbcggttciiippooaannn", 2) == "ps"

# Additional Test Cases
assert remove_all_adjacent_duplicates_in_string_ii("aabbcc", 2) == ""
assert remove_all_adjacent_duplicates_in_string_ii("aabbccddeeff", 2) == ""
assert remove_all_adjacent_duplicates_in_string_ii("xyz", 3) == "xyz"
assert remove_all_adjacent_duplicates_in_string_ii("aaabbbccc", 3) == ""
assert remove_all_adjacent_duplicates_in_string_ii("aabbccddeeffgg", 2) == "g"

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 40 ms, faster than 76.11% of Python3 online submissions
# Memory: 22.35 MB, less than 70.19% of Python3 online submissions