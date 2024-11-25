"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum. A leaf is a node with no children.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        # Leaf node found, verify if the targetSum can be attained
        elif not root.left and not root.right:
            return root.val == targetSum
        # Only the right branch is present, search right
        elif not root.left:
            return self.hasPathSum(root.right, targetSum - root.val)
        # Only the left branch is present, search left
        elif not root.right:
            return self.hasPathSum(root.left, targetSum - root.val)
        # Both branches are present, search both
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
