from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        num_zeros = 0
        product = 1

        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                product *= num

        if num_zeros >= 2:
            for i in range(len(nums)):
                output.append(0)
        elif num_zeros == 1:
            for num in nums:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
        else:
            for num in nums:
                output.append(int(product/num))

        return output