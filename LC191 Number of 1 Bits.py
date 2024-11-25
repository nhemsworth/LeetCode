"""
191. Number of 1 Bits
Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count

