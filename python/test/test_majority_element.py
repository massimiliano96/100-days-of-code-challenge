from src.algo.majority_element import Solution

def test1():
    nums = [3,2,3]
    solution = Solution()
    assert solution.majorityElement(nums) == 3
    
def test2():
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    assert solution.majorityElement(nums) == 2