from src.algo.course_schedule import Solution

def test1():
    courses = 2
    prereq = [[1,0]]
    solution = Solution()
    assert solution.canFinish(courses, prereq)
    
def test2():
    courses = 2
    prereq = [[1,0], [0,1]]
    solution = Solution()
    assert not solution.canFinish(courses, prereq)
    
def test3():
    courses = 3
    prereq = [[1,0], [0,2], [2, 1]]
    solution = Solution()
    assert not solution.canFinish(courses, prereq)
    
def test4():
    courses = 5
    prereq = [[1,0], [0,2], [2,3], [3,4]]
    solution = Solution()
    assert solution.canFinish(courses, prereq)