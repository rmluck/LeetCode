"""
Problem 74: Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
- Difficulty: Medium
- Categories: Matrix
- Technique: Binary Search

You are given an `m x n` integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false` otherwise.
"""


def search_a_2D_matrix(matrix: list[list[int]], target: int) -> bool:
    # Check if the matrix is empty or has no columns
    if not matrix or not matrix[0]:
        return False
    
    # Get the number of rows and columns
    num_rows, num_cols = len(matrix), len(matrix[0])

    # Initialize binary search bounds
    start, end = 0, num_rows * num_cols - 1
    # Perform binary search
    while start <= end:
        # Calculate the middle index
        middle = (start + end) // 2
        # Convert the middle index to row and column
        middle_value = matrix[middle // num_cols][middle % num_cols]

        # Compare the middle value with the target
        if target < middle_value:
            # If target is less than middle value, search in the left half
            end = middle - 1
        elif target > middle_value:
            # If target is greater than middle value, search in the right half
            start = middle + 1
        else:
            # If target is equal to middle value, we found the target
            return True
        
    # If we exit the loop, the target was not found
    return False

# Example 1
assert search_a_2D_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True

# Example 2
assert search_a_2D_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False

# Additional Test Cases
assert search_a_2D_matrix([[1]], 1) == True
assert search_a_2D_matrix([[1, 2], [3, 4]], 2) == True
assert search_a_2D_matrix([[1, 2], [3, 4]], 5) == False
assert search_a_2D_matrix([], 1) == False
assert search_a_2D_matrix([[1, 2, 3], [4, 5, 6]], 4) == True
assert search_a_2D_matrix([[1, 2, 3], [4, 5, 6]], 7) == False

# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100% of Python3 online submissions
# Memory: 18.26 MB, less than 44.88% of Python3 online submissions