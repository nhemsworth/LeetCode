"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).

Beats 63.65% on execution time.
Beats 92.36% on memory usage.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        output = []

        node = root
        level_nodes = [node]

        while level_nodes:

            next_level_nodes = []
            curr_level_values = []

            for node in level_nodes:

                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

                curr_level_values.append(node.val)

            output.append(curr_level_values)
            level_nodes = next_level_nodes

        return output
