"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Beats 64.49% on execution time.
Beats 11.40% on memory usage.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        carry = 0

        while a or b:

            if a and b:
                a_i = int(a[-1])
                a = a[:-1]
                b_i = int(b[-1])
                b = b[:-1]

                s_i = (a_i + b_i + carry)%2
                carry = (a_i + b_i + carry)//2

            elif a:
                a_i = int(a[-1])
                a = a[:-1]
                s_i = (a_i + carry)%2
                carry = (a_i + carry)//2
            else:
                b_i = int(b[-1])
                b = b[:-1]

                s_i = (b_i + carry)%2
                carry = (b_i + carry)//2

            sum = str(s_i) + sum

        if carry == 1:
            return "1" + sum
        else:
            return sum