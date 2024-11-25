"""
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of
the nodes in the tree.

Beats 74.54% on execution time.
Beats 24.04% on memory usage.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        level_nodes = [root]
        vals = []

        while level_nodes:
            next_level_nodes = []

            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

                vals.append(node.val)

            level_nodes = next_level_nodes

        vals.sort()

        return vals[k - 1]
