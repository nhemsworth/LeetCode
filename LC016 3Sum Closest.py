"""
16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest
to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Beats 62.70% on execution time
Beats 59.55% on memory usage
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:

                temp_sum = nums[i] + nums[j] + nums[k]

                if abs(target - temp_sum) < abs(target - closest_sum):
                    closest_sum = temp_sum

                if temp_sum > target:
                    k -= 1
                elif temp_sum < target:
                    j += 1
                else:
                    return temp_sum

            i += 1

        return closest_sum
