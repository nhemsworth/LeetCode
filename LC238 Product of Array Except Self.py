"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must
write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initialize lists for cumulative products
        l_cum_prod = [nums[0]]
        r_cum_prod = [nums[-1]]

        # Iterate from left to right, populating the cumulative product list
        for i in range(1, len(nums)):
            l_cum_prod.append(nums[i] * l_cum_prod[i - 1])
            r_cum_prod.append(nums[-i - 1] * r_cum_prod[i - 1])

        r_cum_prod = r_cum_prod[::-1]

        output = [r_cum_prod[1]]

        for i in range(1, len(nums) - 1):
            prod = l_cum_prod[i - 1] * r_cum_prod[i + 1]
            output.append(prod)

        output.append(l_cum_prod[-2])

        return output

sol = Solution()
nums = [1, 2, 3, 4]
output = sol.productExceptSelf(nums)

print(output)