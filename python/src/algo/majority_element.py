"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

from typing import List
from math import floor


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[floor(len(nums)/2)]
    
    def majorityElementMoore(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num           
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate