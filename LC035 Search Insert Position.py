"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

Beats 52.78% on execution time
Beats 17.36% on memory usage
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums)==1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        else:
            mid_idx = len(nums)//2

            if target == nums[mid_idx]:
                return mid_idx
            elif target > nums[mid_idx]:
                return mid_idx + self.searchInsert(nums[mid_idx:], target)
            else:
                return self.searchInsert(nums[0:mid_idx], target)
