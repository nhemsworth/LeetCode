"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Beats 62.22% on execution time
Beats 80.45 on memory usage
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_length = 0

        while num_set:

            low = high = num_set.pop()

            while low - 1 in num_set or high + 1 in num_set:

                if low - 1 in num_set:
                    num_set.remove(low - 1)
                    low = low - 1

                if high + 1 in num_set:
                    num_set.remove(high + 1)
                    high = high + 1

            max_length = max(high - low + 1, max_length)

        return max_length