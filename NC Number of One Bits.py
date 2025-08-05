class Solution:
    def hammingWeight(self, n: int) -> int:
        total_sum = 0

        while n > 0:
            total_sum += n & 1
            n = n >> 1
        return total_sum
