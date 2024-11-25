"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Beats 53.18% on execution time.
Beats 48.46% on memory usage.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBranch(self, root: Optional[TreeNode], upper_bound: Optional[int], lower_bound: Optional[int]):

        if not root:
            return True

        elif upper_bound == None and lower_bound == None:
            return self.isValidBranch(root.left, root.val, None) and self.isValidBranch(root.right, None, root.val)
        elif upper_bound == None:
            if root.val <= lower_bound:
                return False
            else:
                return self.isValidBranch(root.left, root.val, lower_bound) and self.isValidBranch(root.right, None, root.val)
        elif lower_bound == None:
            if root.val >= upper_bound:
                return False
            else:
                return self.isValidBranch(root.left, root.val, None) and self.isValidBranch(root.right, upper_bound, root.val)


        elif root.val >= upper_bound or root.val <= lower_bound:
            return False
        else:
            return self.isValidBranch(root.left, root.val, lower_bound) and self.isValidBranch(root.right, upper_bound, root.val)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBranch(root, None, None)


sol = Solution()
B = TreeNode(-1)
A = TreeNode(0, None, B)
out = sol.isValidBST(A)
print(out)
