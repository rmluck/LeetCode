"""
Problem 2363: Merge Similar Items (https://leetcode.com/problems/merge-similar-items/)
- Difficulty: Easy
- Topics: Array
- Techniques: Hash Table, Sorting

You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each array `items` has the following properties:
- `items[i] = [value_i, weight_i]` where `value_i` represents the value and `weight_i` represents the weight of the `ith` item.
- The value of each item in `items` is unique.

Return a 2D integer array `value_sums` where `value_sums[i] = [value_i, weight_i]`, with `weight_i` being the sum of weights of all items with value `value_i`.

The result should be returned in ascending order by value.

Constraints:
- `1 <= items1.length, items2.length <= 1000`
- `items1[i].length == items2[i].length == 2`
- `0 <= value_i, weight_i <= 1000`
- Each `value_i` in `items1`  is unique.
- Each `value_i` in items2 is unique.
"""


def merge_similar_items(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    # Combine the two lists and sum the weights for each unique value
    combined_weights = {}
    for value, weight in items1 + items2:
        combined_weights[value] = combined_weights.get(value, 0) + weight

    # Convert the dictionary to a list of value-weight pairs sorted by value
    return sorted(combined_weights.items())

# Example 1
assert merge_similar_items([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]) == [[1, 6], [3, 9], [4, 5]]

# Example 2
assert merge_similar_items([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]) == [[1, 4], [2, 4], [3, 4]]

# Example 3
assert merge_similar_items([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]) == [[1, 7], [2, 4], [7, 1]]

# Additional Test Cases
assert merge_similar_items([[5, 10], [2, 3]], [[2, 4], [5, 5]]) == [[2, 7], [5, 15]]
assert merge_similar_items([[10, 1]], [[10, 2], [20, 3]]) == [[10, 3], [20, 3]]
assert merge_similar_items([[1, 1]], [[2, 2], [3, 3]]) == [[1, 1], [2, 2], [3, 3]]
assert merge_similar_items([], []) == []

# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Runtime: 3 ms, faster than 79.26% of Python3 online submissions
# Memory: 18.45 MB, less than 79.26% of Python3 online submissions