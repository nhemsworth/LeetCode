"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.

Beats 85.08% on execution speed.
Beats 45.14% on memory usage.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 0:
            return None

        else:
            mid_idx = len(nums)//2
            mid_val = nums[mid_idx]
            left_branch = self.sortedArrayToBST(nums[:mid_idx])
            if len(nums) >= 2:
                right_branch = self.sortedArrayToBST(nums[mid_idx+1:])
            else:
                right_branch = None
            return TreeNode(mid_val, left_branch, right_branch)
