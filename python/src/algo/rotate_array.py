
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        def revert(left, right):
            while left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                right-=1
                left+=1
        
        revert(0,n-1)
        revert(0,k-1)
        revert(k,n-1)