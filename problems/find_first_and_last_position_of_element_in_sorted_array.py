"""
Problem 34: Find First and Last Position of Element in Sorted Array (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- Difficulty: Medium
- Categories: Array
- Technique: Binary Search
"""


def find_first_and_last_position_of_element_in_sorted_array(nums: list[int], target: int) -> list[int]:
    # Helper function to find the first or last position of the target
    def find_position(is_first: bool) -> int:
        # Initialize the start and end pointers for binary search
        start, end = 0, len(nums) - 1
        position = -1

        # Perform binary search
        while start <= end:
            # Calculate the middle index
            middle = (start + end) // 2

            # Check if the middle element is equal to target
            if nums[middle] == target:
                # If it is, update the position and adjust the search range
                position = middle
                if is_first:
                    end = middle - 1
                else:
                    start = middle + 1
            elif nums[middle] < target:
                # If the middle element is less than target, search in the right half
                start = middle + 1
            else:
                # If the middle element is greater than target, search in the left half
                end = middle - 1

        # Return the found position or -1 if not found
        return position
    
    # Find the first and last positions of the target
    first_position = find_position(True)
    last_position = find_position(False)

    # Return the results as a list
    return [first_position, last_position]

# Example 1
assert find_first_and_last_position_of_element_in_sorted_array([5, 7, 7, 8, 8, 10], 8) == [3, 4]

# Example 2
assert find_first_and_last_position_of_element_in_sorted_array([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

# Example 3
assert find_first_and_last_position_of_element_in_sorted_array([], 0) == [-1, -1]

# Additional Test Cases
assert find_first_and_last_position_of_element_in_sorted_array([1, 2, 3, 4, 5], 3) == [2, 2]
assert find_first_and_last_position_of_element_in_sorted_array([1, 2, 2, 2, 3, 4], 2) == [1, 3]
assert find_first_and_last_position_of_element_in_sorted_array([1, 1, 1, 1], 1) == [0, 3]
assert find_first_and_last_position_of_element_in_sorted_array([1, 2, 3, 4], 5) == [-1, -1]
assert find_first_and_last_position_of_element_in_sorted_array([1, 2, 3, 4, 5], 1) == [0, 0]
assert find_first_and_last_position_of_element_in_sorted_array([1, 2, 3, 4, 5], 5) == [4, 4]