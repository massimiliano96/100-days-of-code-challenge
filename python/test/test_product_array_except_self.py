from src.algo.product_array_except_self import Solution

def test1():
    nums = [1,2,3,4]
    sol = Solution()
    expected = [24,12,8,6]
    assert sol.productExceptSelf(nums) == expected