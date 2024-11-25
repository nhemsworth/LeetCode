from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        output = []

        for i in range(len(candidates)):

            candidate = candidates[i]

            if candidate == target:
                output.append([candidate])
            elif candidate < target:
                out = self.combinationSum(candidates[i:], target - candidate)
                if len(out) > 0:
                    for entry in out:
                        output.append([candidate] + entry)

        return output

sol = Solution()

A = [2,3,6,7]

out = sol.combinationSum(A, 7)

print(out)

# Beats 90.66% on execution time
# Beats 42.99% on memory usage
