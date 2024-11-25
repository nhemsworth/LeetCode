# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        level_nodes = [root]
        next_level_nodes = []
        i = 0

        while len(level_nodes) != 0:
            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            level_nodes = next_level_nodes
            next_level_nodes = []
            i += 1

        return i