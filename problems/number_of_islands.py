"""
Problem 200: Number of Islands (https://leetcode.com/problems/number-of-islands/)
- Difficulty: Medium
- Categories: Matrix
- Technique: Depth-First Search (DFS)

Given an `m x n` 2D binary grid `grid` which represents a map of `1`s (land) and `0`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""


def number_of_islands(grid: list[list[str]]) -> int:
    # Initialize the number of islands to 0
    num_islands = 0
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Define a helper function to traverse the island using DFS
    def traverse_island(x: int, y: int):
        # Check if the current position is out of bounds or is water
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == "0":
            return
        # Mark the current land as visited by changing it to '0'
        grid[x][y] = "0"
        # Recursively traverse the adjacent cells (up, down, left, right)
        traverse_island(x - 1, y)
        traverse_island(x + 1, y)
        traverse_island(x, y - 1)
        traverse_island(x, y + 1)

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is land ('1'), it indicates a new island
            if grid[i][j] == "1":
                num_islands += 1
                traverse_island(i, j)
    
    # Return the total number of islands found
    return num_islands

# Example 1
assert number_of_islands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1

# Example 2
assert number_of_islands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]) == 3

# Additional Test Cases
assert number_of_islands([["1", "0", "1", "0", "1"], ["0", "0", "0", "0", "0"], ["1", "0", "1", "0", "1"], ["0", "0", "0", "0", "0"]]) == 6
assert number_of_islands([["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]]) == 0
assert number_of_islands([["1", "1", "1"], ["0", "1", "0"], ["1", "0", "1"]]) == 3
assert number_of_islands([["1", "0", "1", "0"], ["0", "1", "0", "1"], ["1", "0", "1", "0"], ["0", "1", "0", "1"]]) == 8
assert number_of_islands([["1", "1", "1", "0"], ["1", "0", "0", "0"], ["1", "1", "0", "1"], ["0", "0", "0", "1"]]) == 2
assert number_of_islands([["1", "0", "0", "1"], ["0", "1", "1", "0"], ["0", "0", "0", "0"], ["1", "0", "1", "1"]]) == 5
assert number_of_islands([["1", "1", "1", "1", "1"], ["1", "0", "0", "0", "1"], ["1", "0", "1", "0", "1"], ["1", "0", "0", "0", "1"], ["1", "1", "1", "1", "1"]]) == 2
assert number_of_islands([["0", "0", "0", "0"], ["0", "1", "1", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "0"]]) == 1

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Runtime: 221 ms, faster than 97.85% of Python3 online submissions
# Memory: 20.12 MB, less than 68.19% of Python3 online submissions