"""
Problem 1189: Maximum Number of Balloons (https://leetcode.com/problems/maximum-number-of-balloons/)
- Difficulty: Easy
- Categories: String
- Techniques: Counting

Given a string `text`, you want to use the characters of `text` to form as many instances of the word "balloon" as possible.

You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

Constraints:
- 1 <= text.length <= 10^4
- text consists of lowercase English letters only.
"""


def maximum_number_of_balloons(text: str) -> int:
    from collections import Counter

    # Count the occurrences of each character in the text
    char_count = Counter(text)

    # Calculate the maximum number of "balloon" instances
    # 'b' -> 1, 'a' -> 1, 'l' -> 2, 'o' -> 2, 'n' -> 1
    return min(
        char_count['b'],
        char_count['a'],
        char_count['l'] // 2,
        char_count['o'] // 2,
        char_count['n']
    )

# Example 1
assert maximum_number_of_balloons("nlaebolko") == 1

# Example 2
assert maximum_number_of_balloons("loonbalxballpoon") == 2

# Example 3
assert maximum_number_of_balloons("leetcode") == 0

# Additional Test Cases
assert maximum_number_of_balloons("balloonballoon") == 2
assert maximum_number_of_balloons("balloon") == 1
assert maximum_number_of_balloons("bbaallooonn") == 1
assert maximum_number_of_balloons("aabblloonn") == 0

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.69 MB, less than 94.47% of Python3 online submissions