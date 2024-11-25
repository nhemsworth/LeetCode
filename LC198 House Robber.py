from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[2] + nums[0], nums[1])

        total_haul = [nums[0], max(nums[0], nums[1])]
        total_haul.append(nums[0] + nums[2])

        for i in range(3, len(nums)):
            haul_i = max(total_haul[i - 2] + nums[i], total_haul[i - 3] + nums[i])
            total_haul.append(haul_i)

        return max(total_haul[-1], total_haul[-2])

# Beats 54.42% on execution time
# Beats 44.37% on memory usage
