from src.algo.rotate_array import Solution

def test1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol = Solution()
    sol.rotate(nums,k)
    expected = [5,6,7,1,2,3,4]
    assert nums == expected
    
def test2():
    nums = [-1,-100,3,99]
    k = 2
    sol = Solution()
    sol.rotate(nums,k)
    expected = [3,99,-1,-100]
    assert nums == expected