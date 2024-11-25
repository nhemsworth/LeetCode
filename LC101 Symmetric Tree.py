"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Beats 49.34% on execution time.
Beats 96.09% on memory usage.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        level_nodes = [root]

        while level_nodes:
            next_level_nodes = []
            level_vals = []

            for node in level_nodes:
                if node is not None:
                    level_vals.append(node.val)
                else:
                    level_vals.append(None)

                if node is not None:
                    if node.left:
                        next_level_nodes.append(node.left)
                    else:
                        next_level_nodes.append(None)
                    if node.right:
                        next_level_nodes.append(node.right)
                    else:
                        next_level_nodes.append(None)

            if level_vals != level_vals[::-1]:
                return False

            level_nodes = next_level_nodes

        return True


sol = Solution()
A = TreeNode(2)
B = TreeNode(2)
C = TreeNode(1, A, B)

out = sol.isSymmetric(C)

print(out)