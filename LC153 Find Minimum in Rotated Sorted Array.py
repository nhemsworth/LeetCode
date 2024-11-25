from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        m = len(nums) // 2

        while l < r:

            if nums[m] > nums[r]:
                l = m + 1
                m = (r - m) // 2 + m
            else:
                r = m
                m = l + (m - l) // 2
        return nums[l]
