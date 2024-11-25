from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        max_area = min(height[0], height[-1]) * j

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area

            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return max_area

# Beats 94.97% on execution time
# Beats 78.69% on memory usage