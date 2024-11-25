from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    A = dict()

    for i in range(len(nums)):
        if nums[i] in A:
            A[nums[i]].append(i)
        else:
            A[nums[i]] = [i]

    for i in range(len(nums)):
        if (target - nums[i]) in A:
            if (target - nums[i]) == nums[i] and len(A[target - nums[i]]) >= 2:
                return A[nums[i]][:2]
            elif (target - nums[i]) != nums[i]:
                return [i, A[target - nums[i]][0]]


A = [2, 3, 3, 7]
target = 6

out = twoSum(A, target)

print(out)

# Beats 85.44% on runtime (54 ms)
# Performs poorly on memory though (beats 6.31%)
