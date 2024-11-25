"""
66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

Beats 89.18% on execution time
Beats 40.55% on memory usage
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1
        carry = 1

        while i >= 0 and carry != 0:

            if digits[i] + carry < 10:
                digits[i] += carry
                return digits
            else:
                digits[i] = digits[i] + carry - 10
                carry = 1

            i -= 1

        if i == -1:
            digits.insert(0, 1)

        return digits