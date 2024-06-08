from src.algo.remove_duplicates_from_sorted_array_2 import Solution

def test1():
    nums = [1,1,1,2,2,3]
    solution = Solution()
    k = 5
    expected_nums = [1,1,2,2,3]
    
    assert solution.removeDuplicates(nums) == k
    
    expected_nums_sorted = sorted(expected_nums)
    sort_nums = sorted(nums[:k])
    for i in range(0, k-1):
        assert sort_nums[i] == expected_nums_sorted[i]

def test2():
    nums = [0,0,1,1,1,1,2,3,3]
    solution = Solution()
    k = 7
    expected_nums = [0,0,1,1,2,3,3]
    assert solution.removeDuplicates(nums) == k
    
    sort_nums = sorted(nums[:k])
    expected_nums_sorted = sorted(expected_nums)
    for i in range(0, k-1):
        assert sort_nums[i] == expected_nums_sorted[i]
        
def test3():
    nums = []
    solution = Solution()
    k = 0
    assert solution.removeDuplicates(nums) == k