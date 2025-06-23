"""
Problem 904: Fruit Into Baskets (https://leetcode.com/problems/fruit-into-baskets/)
- Difficulty: Medium
- Categories: Array
- Technique: Sliding Window

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the maximum number of fruits you can pick.

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""


def fruit_into_baskets(fruits: list[int]) -> int:
    # Initialize the left pointer, fruit count dictionary, and max fruits counter
    fruit_count = {}
    left = 0
    max_fruits = 0

    # Iterate through the fruits array with the right pointer
    for right in range(len(fruits)):
        # Add the current fruit to the count dictionary
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        # If there are more than two types of fruits, shrink the window from the left
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, right - left + 1)

    # Return the maximum number of fruits that can be picked
    return max_fruits

# Example 1
assert fruit_into_baskets([1, 2, 1]) == 3

# Example 2
assert fruit_into_baskets([0, 1, 2, 2]) == 3

# Example 3
assert fruit_into_baskets([1, 2, 3, 2, 2]) == 4

# Additional Test Cases
assert fruit_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
assert fruit_into_baskets([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert fruit_into_baskets([1, 2, 1, 2, 1, 2, 1, 2]) == 8
assert fruit_into_baskets([1]) == 1
assert fruit_into_baskets([1, 2, 3, 4, 5]) == 2
assert fruit_into_baskets([1, 1, 1, 1, 1]) == 5
assert fruit_into_baskets([1, 2]) == 2
assert fruit_into_baskets([1, 2, 1, 3, 4, 2, 1]) == 4
assert fruit_into_baskets([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 2

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 178 ms, beats 70.45% of Python3 online submissions
# Memory: 23.41 MB, less than 88.72% of Python3 online submissions