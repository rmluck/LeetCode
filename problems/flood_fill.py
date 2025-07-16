"""
Problem 733: Flood Fill (https://leetcode.com/problems/flood-fill/)
- Difficulty: Easy
- Categories: Matrix
- Technique: Depth-First Search (DFS)

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a flood fill on the image starting from the pixel `image[sr][sc]`.

To perform a flood fill:
1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

Constraints:
- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 2^16`
- `0 <= sr < m`
- `0 <= sc < n`
"""


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # Check if the color is different from the original color
    original_color = image[sr][sc]
    if original_color == color:
        return image
    
    # Define a helper function to perform the flood fill using DFS
    def flood(x: int, y: int):
        # Check if the current pixel is out of bounds or does not match the original color
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != original_color:
            return
        # Change the color of the current pixel
        image[x][y] = color
        # Recursively flood the adjacent pixels
        flood(x - 1, y)
        flood(x + 1, y)
        flood(x, y - 1)
        flood(x, y + 1)

    # Start the flood fill from the given starting pixel
    flood(sr, sc)
    # Return the modified image
    return image

# Example 1
assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

# Example 2
assert flood_fill([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Additional Test Cases
assert flood_fill([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1, 1, 2) == [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
assert flood_fill([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1, 2) == [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
assert flood_fill([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0, 0) == [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
assert flood_fill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0, 2) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
assert flood_fill([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1, 10) == [[1, 2, 3], [4, 10, 6], [7, 8, 9]]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 17.96 MB, less than 70.10% of Python3 online submissions