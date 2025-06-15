"""
Problem 1089: Duplicate Zeros (https://leetcode.com/problems/duplicate-zeros/)
- Difficulty: Easy
- Categories: Array
- Technique: Two Pointers

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 9
"""


def duplicate_zeros(arr: list[int]) -> None:
    n = len(arr)
    zeros = 0

    # Count the number of zeros in the original array
    for i in range(n):
        if arr[i] == 0:
            zeros += 1

    # Set two pointers: one for the original array and one for the new position
    i = n - 1
    j = n + zeros - 1

    # Move backwards through the array, duplicating zeros as needed
    while i < j:
        # Only write to the array if the new position is within bounds
        if j < n:
            # Set the value at the new position
            arr[j] = arr[i]
        # If the current element is zero, we need to duplicate it
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
        # Move both pointers to the left
        i -= 1
        j -= 1

# Example 1
arr1 = [1,0,2,3,0,4,5,0]
duplicate_zeros(arr1)
assert arr1 == [1,0,0,2,3,0,0,4]

# Example 2
arr2 = [1,2,3]
duplicate_zeros(arr2)
assert arr2 == [1,2,3]

# Additional Test Cases
arr3 = [0,0,0]
duplicate_zeros(arr3)
assert arr3 == [0,0,0]

arr4 = [1,0,0,2,3]
duplicate_zeros(arr4)
assert arr4 == [1,0,0,0,0]

arr5 = [1,2,3,0,4,5]
duplicate_zeros(arr5)
assert arr5 == [1,2,3,0,0,4]

arr6 = [9,8,0,7,6]
duplicate_zeros(arr6)
assert arr6 == [9,8,0,0,7]

arr7 = [1]
duplicate_zeros(arr7)
assert arr7 == [1]

arr8 = [0]
duplicate_zeros(arr8)
assert arr8 == [0]

arr9 = [1,0,2,0,3,0]
duplicate_zeros(arr9)
assert arr9 == [1,0,0,2,0,0]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.16 MB, less than 38.98% of Python3 online submissions