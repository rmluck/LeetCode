"""
Problem 210: Course Schedule II (https://leetcode.com/problems/course-schedule-ii/)
- Difficulty: Medium
- Topics: Graph
- Techniques: Topological Sort, Breadth-First Search (BFS)

There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.
- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Constraints:
- `1 <= num_courses <= 2000`
- `0 <= prerequisites.length <= num_courses * (num_courses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < num_courses`
- `a_i != b_i`
- All the pairs `[a_i, b_i]` are distinct.
"""


def course_schedule_ii(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # Initialize a list to hold the final order of courses
    course_schedule = []

    # Initialize an adjacency list to represent the graph and a list to track in-degrees
    adjacent_courses = {i: [] for i in range(num_courses)}
    prereq_counts = [0] * num_courses

    # Build the graph and count in-degrees for each course
    for course, prereq in prerequisites:
        adjacent_courses[course].append(prereq)
        prereq_counts[prereq] += 1

    # Initialize a queue for courses with no prerequisites
    queue = [i for i in range(num_courses) if prereq_counts[i] == 0]

    # Process the courses in the queue using BFS
    while queue:
        # Pop a course from the queue and add it to the schedule
        current_course = queue.pop(0)
        course_schedule.insert(0, current_course)

        # Decrease the in-degree of each adjacent course
        for next_course in adjacent_courses[current_course]:
            prereq_counts[next_course] -= 1
            # If the in-degree becomes zero, add it to the queue
            if prereq_counts[next_course] == 0:
                queue.append(next_course)

    # If the number of courses in the schedule matches the total number of courses, return the ordered schedule
    return course_schedule if len(course_schedule) == num_courses else []

# Example 1
assert course_schedule_ii(2, [[1, 0]]) == [0, 1]

# Example 2
assert course_schedule_ii(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]

# Example 3
assert course_schedule_ii(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]

# Additional Test Cases
assert course_schedule_ii(3, [[0, 1], [1, 2]]) == [0, 1, 2]
assert course_schedule_ii(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3, 4]
assert course_schedule_ii(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == []
assert course_schedule_ii(1, []) == [0]
assert course_schedule_ii(0, []) == []

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions
# Memory: 18.92 MB, less than 85.61% of Python3 online submissions