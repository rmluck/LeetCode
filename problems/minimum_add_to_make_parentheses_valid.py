"""
Problem 921: Minimum Add to Make Parentheses Valid (https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
- Difficulty: Medium
- Categories: String
- Technique: Greedy Algorithm

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.
- For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be "())))"`.

Return the minimum number of moves required to make `s` valid.

Constraints:
- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.
"""


def minimum_add_to_make_parentheses_valid(s: str) -> int:
    # Count the number of unmatched left and right parentheses
    left_count = 0
    right_count = 0

    # Iterate through the string to count unmatched parentheses
    for char in s:
        # Check if the character is an opening parenthesis
        if char == '(':
            # Increment the count of unmatched left parentheses
            left_count += 1
        else:
            # If it's a closing parenthesis, check if there's an unmatched left parenthesis
            if left_count > 0:
                # If there is, match it with the closing parenthesis
                left_count -= 1
            else:
                # If not, increment the count of unmatched right parentheses
                right_count += 1

    # The total number of moves required is the sum of unmatched left and right parentheses
    return left_count + right_count

# Example 1
assert minimum_add_to_make_parentheses_valid("())") == 1

# Example 2
assert minimum_add_to_make_parentheses_valid("(((") == 3

# Additional Test Cases
assert minimum_add_to_make_parentheses_valid("()") == 0
assert minimum_add_to_make_parentheses_valid("()))((") == 4
assert minimum_add_to_make_parentheses_valid(")(") == 2
assert minimum_add_to_make_parentheses_valid("(()))") == 1
assert minimum_add_to_make_parentheses_valid(")(" * 500) == 1000
assert minimum_add_to_make_parentheses_valid("()()()") == 0
assert minimum_add_to_make_parentheses_valid("(()())") == 0
assert minimum_add_to_make_parentheses_valid("") == 0
assert minimum_add_to_make_parentheses_valid("(") == 1
assert minimum_add_to_make_parentheses_valid(")") == 1
assert minimum_add_to_make_parentheses_valid("(((((") == 5
assert minimum_add_to_make_parentheses_valid("))))))") == 6

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100% of Python3 online submissions
# Memory: 17.88 MB, less than 31.40% of Python3 online submissions