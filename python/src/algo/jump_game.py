"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            if furthest >= len(nums) - 1:
                return True
        return False
    
    
    def canJumpRecursive(self, nums: List[int]) -> bool:
        def visitChild(curr):
            for j in range(1, nums[curr]):
                if curr + nums[j] >= (len(nums)-1):
                    return True
                elif visitChild(curr + j):
                        return True
            return False
        
        if visitChild(0):
            return True
        return False