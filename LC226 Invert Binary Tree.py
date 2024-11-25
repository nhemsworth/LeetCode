from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        level_nodes = [root]
        next_level_nodes = []

        while len(level_nodes) != 0:
            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
                node.left, node.right = node.right, node.left

            level_nodes = next_level_nodes
            next_level_nodes = []
        return root


A = TreeNode(3)
B = TreeNode(1)
C = TreeNode(2, left=B, right=A)

sol = Solution()
D = sol.invertTree(C)

print(D.left.val)

# Beats 73.31% on execution time
# Beats 34.37% on memory usage

