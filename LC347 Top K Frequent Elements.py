from typing import List
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}

        for i in range(len(nums)):
            if nums[i] in D:
                D[nums[i]] += 1
            else:
                D[nums[i]] = 1

        freq_list = []
        val_list = []

        for key in D:

            if len(val_list) < k:
                val_list.append(key)
                freq_list.append(D[key])
                freq_list, val_list = [list(x) for x in zip(*sorted(zip(freq_list, val_list), key=itemgetter(0), reverse=True))]
            else:
                if D[key] > freq_list[-1]:
                    freq_list.pop()
                    val_list.pop()
                    freq_list.append(D[key])
                    val_list.append(key)
                    freq_list, val_list = [list(x) for x in zip(*sorted(zip(freq_list, val_list), key=itemgetter(0), reverse=True))]

        return val_list

sol = Solution()

nums = [1, 1, 1, 2, 2, 3, 4, 4, 4]
k = 2

out = sol.topKFrequent(nums, k)

print(out)

# First attempt works but is a little slow

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}

        for i in range(len(nums)):
            if nums[i] in D:
                D[nums[i]] += 1
            else:
                D[nums[i]] = 1

        freq_list = [[] for _ in range(len(nums) + 1)]

        for key in D:
            freq_list[D[key]].append(key)

        output = []

        for i in range(len(freq_list) - 1, -1, -1):

            if len(freq_list[i]) > 0:
                output.extend(freq_list[i])

            if len(output) >= k:
                return output[:k]

# Beats 81.67% on execution speed
# Beats 14.18% on memory usage