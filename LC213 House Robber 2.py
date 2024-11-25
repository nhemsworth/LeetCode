"""

213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of
each house, return the maximum amount of money you can rob tonight without alerting the police.

Beats 65.29% on execution time
Beats 11.66% on memory usage

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        cum_amount_0 = [nums[0], max(nums[0], nums[1]), max(nums[0] + nums[2], nums[1])]

        for i in range(3, len(nums) - 1):
            best_haul = max(cum_amount_0[i - 1], cum_amount_0[i - 2] + nums[i], cum_amount_0[i - 3] + nums[i])
            cum_amount_0.append(best_haul)

        cum_amount_1 = [nums[1], max(nums[1], nums[2]), max(nums[1] + nums[3], nums[2])]

        for i in range(4, len(nums)):
            best_haul = max(cum_amount_1[i - 2], cum_amount_1[i - 3] + nums[i], cum_amount_1[i - 4] + nums[i])
            cum_amount_1.append(best_haul)

        return max(cum_amount_0[-1], cum_amount_1[-1])
