"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Beats 57.30% on execution time
Beats 14.51% on memory usage
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for _ in range(32):
            output <<= 1
            output += n & 1
            n >>= 1

        return output
