class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        out = []
        curr_range_start = None
        curr_range_last = None

        for i in range(len(nums)):

            if curr_range_start == None:
                curr_range_start = nums[i]
                curr_range_last = nums[i]
            elif nums[i] == curr_range_last + 1:
                curr_range_last = nums[i]
            else:
                if curr_range_start == curr_range_last:
                    out.append("{}".format(curr_range_start))
                else:
                    out.append("{}->{}".format(curr_range_start, curr_range_last))
                curr_range_start = nums[i]
                curr_range_last = nums[i]

        if curr_range_last == nums[-1]:
            if curr_range_start == curr_range_last:
                out.append("{}".format(curr_range_start))
            else:
                out.append("{}->{}".format(curr_range_start, curr_range_last))

        return out
