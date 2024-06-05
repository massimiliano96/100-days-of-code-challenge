from src.algo.remove_element import Solution

def test1():
    nums = [3,2,2,3]
    val = 3
    solution = Solution()
    k = 2
    expected_nums = [2,2]
    assert solution.removeElement(nums, val) == k
    
    sort_nums = sorted(nums[:k])
    for i in range(0, k-1):
        assert sort_nums[i] == expected_nums[i]

def test2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    k = 5
    expected_nums = [0,1,4,0,3]
    assert solution.removeElement(nums, val) == k
    
    sort_nums = sorted(nums[:k])
    expected_nums_sorted = sorted(expected_nums)
    for i in range(0, k-1):
        assert sort_nums[i] == expected_nums_sorted[i]