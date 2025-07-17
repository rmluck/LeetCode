"""
295: Find Median from Data Stream (https://leetcode.com/problems/find-median-from-data-stream/)
- Difficulty: Hard
- Categories: Sorting
- Technique: Two Heaps (Priority Queues)

The median is in the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
- For example, for `arr = [2, 3, 4]`, the median is `3`.
- For example, for `arr = [2, 3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void add_num(int num)` adds the integer `num` from the data stream to the data structure.
- `double find_median()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

Constraints:
- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `find_median`.
- At most `5 * 10^4` calls will be made to `add_num` and `find_median`.
"""


from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        # Two heaps: max_heap for the lower half (inverted to use min-heap properties), min_heap for the upper half
        self.max_heap = []
        self.min_heap = []

    # Adds a number to the data structure
    def add_num(self, num: int) -> None:
        # Check which heap to add the number to
        if not self.max_heap or num <= -self.max_heap[0]:
            # Add to max_heap (inverted to maintain max-heap property) if it's less than or equal to the max of max_heap
            heappush(self.max_heap, -num)
        else:
            # Add to min_heap if it's greater than the max of max_heap
            heappush(self.min_heap, num)
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            # If max_heap has more than one extra element, move the largest from max_heap to min_heap
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            # If min_heap has more elements, move the smallest from min_heap to max_heap
            heappush(self.max_heap, -heappop(self.min_heap))

    # Finds the median of the current data stream
    def find_median(self) -> float:
        # If both heaps are of equal size, the median is the average of the two middle elements
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # If max_heap has one more element, the median is the top of max_heap
        return -self.max_heap[0] / 1.0
    
# Example 1
medianFinder = MedianFinder()
medianFinder.add_num(1)
medianFinder.add_num(2)
assert medianFinder.find_median() == 1.5
medianFinder.add_num(3)
assert medianFinder.find_median() == 2.0

# Time Complexity:
# - add_num: O(log n) for adding to the heap and balancing
# - find_median: O(1) for retrieving the median
# Space Complexity: O(n)
# Runtime: 121 ms, faster than 82.64% of Python3 online submissions
# Memory: 39.50 MB, less than 62.05% of Python3 online submissions