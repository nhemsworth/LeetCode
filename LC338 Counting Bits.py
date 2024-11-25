"""
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0 for _ in range(n+1)]

        for i in range(len(count)):
            count[i] = count[i >> 1] + (i & 1)

        return count
