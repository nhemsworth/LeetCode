"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

Beats 98.72% on execution speed.
Beats 17.25% on memory usage.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluatedDepth(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return True, 0

        else:
            left_bool, left_depth = self.evaluatedDepth(root.left)
            right_bool, right_depth = self.evaluatedDepth(root.right)

            root_bool = left_bool and right_bool and (abs(left_depth - right_depth) <= 1)
            max_depth = max(left_depth, right_depth) + 1
            return root_bool, max_depth


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.evaluatedDepth(root)
        return balanced


node0 = TreeNode(4)
node1 = TreeNode(4)
node2 = TreeNode(3, node0, node1)
node3 = TreeNode(3)
node4 = TreeNode(2, node2, node3)
node5 = TreeNode(2)
node6 = TreeNode(1, node4, node5)

sol = Solution()
out = sol.isBalanced(node6)

print(out)