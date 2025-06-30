"""
Problem 739: Daily Temperatures (https://leetcode.com/problems/daily-temperatures/)
- Difficulty: Medium
- Categories: Array
- Technique: Monotonic Stack

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    # Initialize a monotonic stack and an array to store the days waiting for a warmer temperature
    monotonic_stack = []
    days_waiting = [0] * n

    # Iterate through the temperatures
    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack
        while monotonic_stack and temperatures[i] > temperatures[monotonic_stack[-1]]:
            # Pop the index from the stack
            prev_index = monotonic_stack.pop()
            # Calculate the number of days waiting for a warmer temperature
            days_waiting[prev_index] = i - prev_index
        # Push the current index onto the stack
        monotonic_stack.append(i)

    # Return the days waiting for a warmer temperature for each day
    return days_waiting

# Example 1
assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

# Example 2
assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

# Example 3
assert daily_temperatures([30, 60, 90]) == [1, 1, 0]

# Additional Test Cases
assert daily_temperatures([100, 90, 80, 70]) == [0, 0, 0, 0]
assert daily_temperatures([75, 75, 75, 75]) == [0, 0, 0, 0]
assert daily_temperatures([70, 71, 72, 73, 74, 75]) == [1, 1, 1, 1, 1, 0]
assert daily_temperatures([70, 75, 70, 75, 70, 75]) == [1, 0, 1, 0, 1, 0]
assert daily_temperatures([80]) == [0]
assert daily_temperatures([80, 90]) == [1, 0]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 75 ms, faster than 97.61% of Python3 online submissions
# Memory: 27.45 MB, less than 67.30% of Python3 online submissions