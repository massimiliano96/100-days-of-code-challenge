from src.algo.jump_game_2 import Solution

def test1():
    nums = [2,3,1,1,4]
    sol = Solution()
    assert sol.canJump(nums) == 2

def test2():
    nums = [2,3,0,1,4]
    sol = Solution()
    assert sol.canJump(nums) == 2

def test3():
    nums = [4,1,1,2,3]
    sol = Solution()
    assert sol.canJump(nums) == 1