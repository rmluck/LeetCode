"""
Problem 207: Course Schedule (https://leetcode.com/problems/course-schedule/)
- Difficulty: Medium
- Categories: Graph
- Technique: Topological Sort, Breadth-First Search (BFS)

There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.
- For example, the pair `[0, 1]` indicates that to take course `0` yyou have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Constraints:
- `1 <= num_courses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < num_courses`
- All the pairs `prerequisites[i]` are unique.
"""


def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> bool:
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
        course_schedule.append(current_course)

        # Decrease the in-degree of each adjacent course
        for next_course in adjacent_courses[current_course]:
            prereq_counts[next_course] -= 1
            # If the in-degree becomes zero, add it to the queue
            if prereq_counts[next_course] == 0:
                queue.append(next_course)

    # If the number of courses in the schedule matches the total number of courses, return True
    return len(course_schedule) == num_courses

# Example 1
assert course_schedule(2, [1, 0]) == True

# Example 2
assert course_schedule(2, [[1, 0], [0, 1]]) == False

# Additional Test Cases
assert course_schedule(3, [[0, 1], [1, 2]]) == True
assert course_schedule(4, [[1, 0], [2, 1], [3, 2]]) == True
assert course_schedule(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == True
assert course_schedule(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == False
assert course_schedule(1, []) == True
assert course_schedule(0, []) == True

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Runtime: 3 ms, faster than 87.95% of Python3 online submissions
# Memory: 18.90 MB, less than 93.31% of Python3 online submissions