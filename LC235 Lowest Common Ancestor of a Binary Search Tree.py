"""
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Beats 93.72% on execution time.
Beats 85.14% on memory usage.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val or root.val == q.val:
            return root
        elif (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root
        elif root.left and (root.val > p.val) and (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.right and (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)