from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This solution works but it's not particularly elegant
        # Beats 16.33% on execution time
        # Beats 70.82% on memory consumption
        nums.sort()
        output = []
        i = 0
        while i < len(nums ) -2:
            j = i + 1
            k = len(nums ) -1
            while k> j:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    prev_k = k
                    while k > 0 and nums[k] == nums[prev_k]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    prev_k = k
                    while k > 0 and (nums[k] == nums[prev_k]):
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    prev_j = j
                    while j < len(nums) - 1 and (nums[j] == nums[prev_j]):
                        j += 1

            prev_i = i
            while i < len(nums) - 2 and (nums[i] == nums[prev_i]):
                i += 1

        return output