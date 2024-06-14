from src.algo.jump_game import Solution

def test1():
    nums = [2,3,1,1,4]
    sol = Solution()
    assert sol.canJump(nums)

def test2():
    nums = [3,2,1,0,4]
    sol = Solution()
    assert not sol.canJump(nums)