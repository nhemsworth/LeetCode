from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        def check_subset(nums, target):

            out_list = []
            for i in range(len(nums)):

                if nums[i] == target:
                    out_list.extend([[nums[i]]])
                elif nums[i] < target:
                    sub_list = check_subset(nums[i:], target - nums[i])
                    if len(sub_list) > 0:
                        for entry in sub_list:
                            entry.insert(0, nums[i])
                        out_list.extend(sub_list)
                else:
                    break

            return out_list

        return check_subset(nums, target)


sol = Solution()

nums = [2,5,6,9]
target = 9

result = sol.combinationSum(nums, target)

print(result)







