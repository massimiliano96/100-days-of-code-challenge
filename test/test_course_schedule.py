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