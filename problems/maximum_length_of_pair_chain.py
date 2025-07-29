"""
Problem 646: Maximum Length of Pair Chain (https://leetcode.com/problems/maximum-length-of-pair-chain/)
- Difficulty: Medium
- Categories: Array
- Technique: Greedy Algorithm

You are given an array of `n` pairs `pairs` where `pairs[i] = [left_i, right_i]` and `left_i < right_i`.

A pair `p2 = [c, d]` follows a pair `p1 = [a, b]` if `b < c`. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Constraints:
- `n == pairs.length`
- `1 <= n <= 1000`
- `-1000 <= left_i < right_i <= 1000`
"""


def maximum_length_of_pair_chain(pairs):
    # Sort pairs by their end times
    pairs.sort(key=lambda x: x[1])

    # Initialize the previous end time and the count of chains
    prev, num_chains = float('-inf'), 0
    # Iterate through the sorted pairs
    for left, right in pairs:
        # Check if the current pair's left is greater than the previous pair's right
        if prev < left:
            # If so, update the previous end and increment the count of chains
            prev = right
            num_chains += 1

    # Return the total number of chains formed
    return num_chains

# Example 1
assert maximum_length_of_pair_chain([[1, 2], [2, 3], [3, 4]]) == 2

# Example 2
assert maximum_length_of_pair_chain([[1, 2], [7, 8], [4, 5]]) == 3

# Additional Test Cases
assert maximum_length_of_pair_chain([[1, 3], [2, 4], [3, 5], [6, 7]]) == 3
assert maximum_length_of_pair_chain([[1, 10], [2, 3], [4, 5], [6, 8]]) == 3
assert maximum_length_of_pair_chain([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
assert maximum_length_of_pair_chain([[1, 5], [2, 3], [4, 6], [7, 8]]) == 3
assert maximum_length_of_pair_chain([[1, 2], [3, 4], [5, 6], [2, 3]]) == 4
assert maximum_length_of_pair_chain([[1, 3], [2, 5], [4, 6], [7, 8]]) == 3

# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100% of Python3 online submissions
# Memory: 18.03 MB, less than 80.32% of Python3 online submissions