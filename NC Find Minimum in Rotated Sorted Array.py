class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums)

        m = len(nums) // 2
        r = len(nums) - 1

        if nums[m] < nums[r]:
            return self.findMin(nums[0:m + 1])
        else:
            return self.findMin(nums[m + 1:])
