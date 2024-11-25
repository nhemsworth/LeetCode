"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Beats 41.35% on execution speed.
Beats 57.49% on memory usage.
"""

from typing import Optional, List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:



        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]

        for row in range(2, numRows):

            triangle_row = [1]

            for i in range(1, row):
                triangle_row.append(triangle[row -1][ i -1] + triangle[row -1][i])

            triangle_row.append(1)

            triangle.append(triangle_row)

        return triangle

sol = Solution()
out = sol.generate(4)

print(out)

