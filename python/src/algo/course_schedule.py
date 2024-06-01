# LeetCode 207
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[preq].append(course)
        
        
        for course in range(0, numCourses):
            # 0 = not visisted, 1 = visited
            state = [0] * numCourses
            if self.hasCycle(graph, state, course):
                return False
        
        return True
    
    def hasCycle(self, graph, state, course):
        if state[course] == 1:
            return True
        
        state[course] = 1
        for child in graph[course]:
            if self.hasCycle(graph, state, child):
                return True
        
        return False