from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        m = len(nums) // 2

        if nums[m] == target:
            return m
        elif nums[m] > target and nums[0] <= target and nums[m] > nums[0]:
            return self.search(nums[0:m], target)
        elif nums[m] < target and nums[-1] >= target and nums[-1] > nums[m]:
            idx = self.search(nums[m:], target)
            if idx == -1:
                return -1
            else:
                return m + idx
        elif nums[-1] > nums[m]:
            return self.search(nums[0:m], target)
        else:
            idx = self.search(nums[m:], target)
            if idx == -1:
                return -1
            else:
                return m + idx


if __name__ == "__main__":

    sol = Solution()
    nums = [1, 3, 5]
    target = 5
    idx = sol.search(nums, target)
    print(idx)

