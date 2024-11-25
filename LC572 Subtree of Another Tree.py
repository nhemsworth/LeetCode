from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkNodes(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False

        if root.val != subRoot.val:
            return False
        else:
            return self.checkNodes(root.left, subRoot.left) and self.checkNodes(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False

        if root.val == subRoot.val:
            return self.checkNodes(root.left, subRoot.left) and self.checkNodes(root.right,
                                                                                subRoot.right) or self.isSubtree(
                root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Beats 65.82% on execution time
# Beats 47.68% on memory usage
